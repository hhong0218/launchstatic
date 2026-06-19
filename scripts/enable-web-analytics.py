#!/usr/bin/env python3
"""Enable Cloudflare Web Analytics for LaunchStatic Pages project."""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ACCOUNT_ID = "75c4898a1b8e3213936e24322485e741"
PROJECT_NAME = "launchstatic"
HOSTS = ["launchstatic.pages.dev", "launchstatic.dev"]
WRANGLER_CONFIG = Path.home() / ".wrangler" / "config" / "default.toml"


def load_token() -> str:
    text = WRANGLER_CONFIG.read_text(encoding="utf-8")
    match = re.search(r'oauth_token = "(.+)"', text)
    if not match:
        raise SystemExit("Wrangler oauth token not found. Run: npx wrangler login")
    return match.group(1)


def api(method: str, url: str, token: str, body: dict | None = None) -> dict:
    data = None
    headers = {"Authorization": f"Bearer {token}"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8")
        raise SystemExit(f"{method} {url} failed ({exc.code}): {payload}") from exc


def list_rum_sites(token: str) -> list[dict]:
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/rum/site_info/list"
    payload = api("GET", url, token)
    if not payload.get("success"):
        raise SystemExit(f"List RUM failed: {payload}")
    return payload.get("result") or []


def create_rum_site(token: str, host: str) -> dict:
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/rum/site_info"
    payload = api("POST", url, token, {"host": host})
    if not payload.get("success"):
        raise SystemExit(f"Create RUM for {host} failed: {payload}")
    return payload["result"]


def patch_pages_project(token: str, site_tag: str, site_token: str) -> dict:
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT_NAME}"
    body = {
        "build_config": {
            "web_analytics_tag": site_tag,
            "web_analytics_token": site_token,
        }
    }
    payload = api("PATCH", url, token, body)
    if not payload.get("success"):
        raise SystemExit(f"Patch Pages project failed: {payload}")
    return payload["result"]


def find_site(sites: list[dict]) -> dict | None:
    for site in sites:
        for rule in site.get("rules") or []:
            host = (rule.get("host") or "").lower()
            if host in HOSTS:
                return site
    return None


def main() -> None:
    token = load_token()
    sites = list_rum_sites(token)
    site = find_site(sites)

    if not site:
        last_error = None
        for host in HOSTS:
            try:
                site = create_rum_site(token, host)
                print(f"Created Web Analytics site for {host}")
                break
            except SystemExit as exc:
                last_error = exc
        if not site:
            raise last_error or SystemExit("Could not create Web Analytics site")

    site_tag = site.get("site_tag") or ""
    site_token = site.get("site_token") or ""
    if not site_tag or not site_token:
        raise SystemExit(f"Missing site_tag/site_token in RUM response: {site}")

    result = patch_pages_project(token, site_tag, site_token)
    build = (result.get("build_config") or {})
    print("Pages Web Analytics enabled.")
    print(f"  tag:   {build.get('web_analytics_tag')}")
    print(f"  token: {build.get('web_analytics_token')}")
    print("Redeploy the project for auto-injection on HTML pages.")


if __name__ == "__main__":
    main()