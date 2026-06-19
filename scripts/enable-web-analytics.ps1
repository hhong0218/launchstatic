# Enable Cloudflare Web Analytics for the LaunchStatic Pages project.
# Tries API first; if RUM access is missing, opens the dashboard Metrics tab and polls until enabled.

param(
  [string]$AccountId = "75c4898a1b8e3213936e24322485e741",
  [string]$ProjectName = "launchstatic",
  [int]$PollSeconds = 120
)

$ErrorActionPreference = "Stop"
$wranglerConfig = "$env:USERPROFILE\.wrangler\config\default.toml"
if (-not (Test-Path $wranglerConfig)) {
  Write-Error "Wrangler config not found. Run: npx wrangler login"
}

$token = (Get-Content $wranglerConfig -Raw | Select-String 'oauth_token = "(.+)"').Matches.Groups[1].Value
$headers = @{
  Authorization = "Bearer $token"
  "Content-Type" = "application/json"
}

function Get-ProjectAnalytics {
  $uri = "https://api.cloudflare.com/client/v4/accounts/$AccountId/pages/projects/$ProjectName"
  $project = Invoke-RestMethod -Method Get -Uri $uri -Headers $headers
  return $project.result.build_config
}

function Enable-RumSite([string]$HostName) {
  $uri = "https://api.cloudflare.com/client/v4/accounts/$AccountId/rum/site_info"
  $body = @{ host = $HostName } | ConvertTo-Json
  return Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -Body $body
}

function Patch-ProjectAnalytics([string]$SiteTag, [string]$SiteToken) {
  $uri = "https://api.cloudflare.com/client/v4/accounts/$AccountId/pages/projects/$ProjectName"
  $body = @{
    build_config = @{
      web_analytics_tag = $SiteTag
      web_analytics_token = $SiteToken
    }
  } | ConvertTo-Json -Depth 4
  return Invoke-RestMethod -Method Patch -Uri $uri -Headers $headers -Body $body
}

Write-Host "Checking Pages Web Analytics status..."
$build = Get-ProjectAnalytics
if ($build.web_analytics_token -and $build.web_analytics_token -ne "enable") {
  Write-Host "Already enabled. Token starts with: $($build.web_analytics_token.Substring(0, [Math]::Min(8, $build.web_analytics_token.Length)))..."
  exit 0
}

Write-Host "Trying RUM API..."
try {
  foreach ($hostName in @("launchstatic.pages.dev", "launchstatic.dev")) {
    try {
      $rum = Enable-RumSite $hostName
      if ($rum.success) {
        $tag = $rum.result.site_tag
        $siteToken = $rum.result.site_token
        Patch-ProjectAnalytics $tag $siteToken | Out-Null
        Write-Host "Web Analytics enabled via API for $hostName"
        exit 0
      }
    } catch {
      Write-Host "RUM create failed for ${hostName}: $($_.Exception.Message)"
    }
  }
} catch {
  Write-Host "RUM API unavailable: $($_.Exception.Message)"
}

$metricsUrl = "https://dash.cloudflare.com/$AccountId/pages/view/$ProjectName/metrics"
Write-Host "Opening dashboard Metrics tab (one click: Enable under Web Analytics)..."
Write-Host $metricsUrl
Start-Process $metricsUrl

$deadline = (Get-Date).AddSeconds($PollSeconds)
while ((Get-Date) -lt $deadline) {
  Start-Sleep -Seconds 5
  $build = Get-ProjectAnalytics
  if ($build.web_analytics_token -and $build.web_analytics_token -ne "enable") {
    Write-Host "Web Analytics enabled from dashboard."
    exit 0
  }
  Write-Host "Waiting for Enable click in dashboard..."
}

Write-Error "Timed out. Open Metrics and click Enable, then redeploy: npx wrangler pages deploy . --project-name=launchstatic --branch=main"