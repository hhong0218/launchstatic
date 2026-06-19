# Migrate LaunchStatic Cloudflare Pages project to GitHub auto-deploy
# Prerequisite: Cloudflare Pages GitHub App installed
# https://github.com/apps/cloudflare-pages

param(
  [string]$AccountId = "75c4898a1b8e3213936e24322485e741",
  [string]$ProjectName = "launchstatic",
  [string]$Owner = "hhong0218",
  [string]$RepoName = "launchstatic",
  [string]$RepoId = "1274422510",
  [string]$Branch = "main"
)

$wranglerConfig = "$env:USERPROFILE\.wrangler\config\default.toml"
if (-not (Test-Path $wranglerConfig)) {
  Write-Error "Wrangler config not found. Run: npx wrangler login"
  exit 1
}

$token = (Get-Content $wranglerConfig -Raw | Select-String 'oauth_token = "(.+)"').Matches.Groups[1].Value
$headers = @{
  Authorization = "Bearer $token"
  "Content-Type" = "application/json"
}

function Invoke-CfApi($Method, $Uri, $Body = $null) {
  try {
    if ($Body) {
      return Invoke-RestMethod -Method $Method -Uri $Uri -Headers $headers -Body $Body
    }
    return Invoke-RestMethod -Method $Method -Uri $Uri -Headers $headers
  } catch {
    $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
    throw $reader.ReadToEnd()
  }
}

$createBody = @{
  name = $ProjectName
  production_branch = $Branch
  source = @{
    type = "github"
    config = @{
      owner = $Owner
      owner_id = "270345484"
      repo_name = $RepoName
      repo_id = $RepoId
      production_branch = $Branch
      deployments_enabled = $true
      production_deployments_enabled = $true
      preview_deployment_setting = "all"
      pr_comments_enabled = $false
    }
  }
  build_config = @{
    build_command = ""
    destination_dir = ""
    root_dir = ""
  }
} | ConvertTo-Json -Depth 6

Write-Host "Testing GitHub integration..."
$testName = "$ProjectName-git-test-$(Get-Date -Format 'HHmmss')"
$testBody = $createBody.Replace("`"$ProjectName`"", "`"$testName`"")
try {
  Invoke-CfApi Post "https://api.cloudflare.com/client/v4/accounts/$AccountId/pages/projects" $testBody | Out-Null
  Invoke-CfApi Delete "https://api.cloudflare.com/client/v4/accounts/$AccountId/pages/projects/$testName" | Out-Null
  Write-Host "GitHub integration OK"
} catch {
  Write-Host "GitHub app not connected. Install: https://github.com/apps/cloudflare-pages/installations/new"
  Write-Host $_
  exit 1
}

$existing = $null
try {
  $existing = Invoke-CfApi Get "https://api.cloudflare.com/client/v4/accounts/$AccountId/pages/projects/$ProjectName"
} catch {}

if ($existing -and -not $existing.result.source.type) {
  Write-Host "Removing direct-upload project..."
  Invoke-CfApi Delete "https://api.cloudflare.com/client/v4/accounts/$AccountId/pages/projects/$ProjectName" | Out-Null
  Start-Sleep -Seconds 2
}

Write-Host "Creating Git-connected project..."
$result = Invoke-CfApi Post "https://api.cloudflare.com/client/v4/accounts/$AccountId/pages/projects" $createBody
Write-Host "Done: https://$($result.result.subdomain)"