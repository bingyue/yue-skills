#!/usr/bin/env python3
"""Submit a new Capsule as a GitHub Issue to openclaw-pitfalls repo."""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

REPO = "BENZEMA216/openclaw-pitfalls"
API_URL = f"https://api.github.com/repos/{REPO}/issues"
TOKEN_PATH = "/root/.openclaw-claw2/credentials/github_token"

def load_token():
    if os.path.exists(TOKEN_PATH):
        return open(TOKEN_PATH).read().strip()
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    print("Error: No GitHub token found.", file=sys.stderr)
    print(f"  Set GITHUB_TOKEN env or write token to {TOKEN_PATH}", file=sys.stderr)
    sys.exit(1)

def submit_issue(title, body, labels, token):
    data = json.dumps({"title": title, "body": body, "labels": labels}).encode()
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Authorization": f"token {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            return result
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"GitHub API error {e.code}: {body}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Submit Capsule as GitHub Issue")
    parser.add_argument("--id", required=True, help="Capsule ID (e.g. PIT-015)")
    parser.add_argument("--title", required=True, help="Short problem description")
    parser.add_argument("--severity", default="medium", choices=["critical","high","medium","low"])
    parser.add_argument("--category", default="config", choices=["repair","config","env"])
    parser.add_argument("--yaml-file", required=True, help="Path to capsule YAML file")
    args = parser.parse_args()

    token = load_token()

    with open(args.yaml_file) as f:
        yaml_content = f.read()

    issue_title = f"{args.id}: {args.title}"
    issue_body = f"""## New Capsule: {args.id}

### Source
- Instance: claw2 (profile)
- Gateway port: 18890
- Auto-submitted by pitfall-experience skill

### Capsule YAML



### Severity & Category
- Severity: {args.severity}
- Category: {args.category}
"""

    labels = ["capsule", "auto-submitted", f"severity:{args.severity}", f"category:{args.category}"]
    result = submit_issue(issue_title, issue_body, labels, token)

    print(f"Issue created successfully!")
    print(f"URL: {result['html_url']}")
    print(f"Number: #{result['number']}")

if __name__ == "__main__":
    main()
