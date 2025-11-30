#!/usr/bin/env python3
"""AI Code Review script for GitHub Actions."""

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

from anthropic import Anthropic

# Maximum diff size to send to the API (characters)
# Note: Intentionally duplicated from reviewer.py since this script runs standalone in GitHub Actions
MAX_DIFF_SIZE = 100_000

# Timeout for API calls (seconds)
API_TIMEOUT = 120.0


def get_diff() -> str:
    """Get the diff for the PR."""
    base_ref = os.environ.get("GITHUB_BASE_REF", "main")
    result = subprocess.run(
        ["git", "diff", f"origin/{base_ref}...HEAD"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Warning: git diff failed: {result.stderr}")
        return ""
    return result.stdout


def get_changed_files() -> list[str]:
    """Get list of changed files."""
    base_ref = os.environ.get("GITHUB_BASE_REF", "main")
    result = subprocess.run(
        ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Warning: git diff --name-only failed: {result.stderr}")
        return []
    return [f for f in result.stdout.strip().split("\n") if f]


def build_review_prompt(diff: str, files: list[str]) -> str:
    """Build the review prompt."""
    files_list = "\n".join(f"- {f}" for f in files)
    return f"""You are an expert code reviewer for Python AI agent solutions built on Azure AI Foundry using the Microsoft Agent Framework.

Review the following code changes across these dimensions:
1. Correctness - Logic, edge cases, error handling
2. Readability - Clarity, naming, documentation
3. Architecture - Structure, boundaries, patterns
4. Python Patterns - Type hints, async, idioms
5. Security - Input validation, auth, secrets
6. AI Security - Prompt injection, tool safety, data leakage, agent bounds
7. Azure AI Foundry - Managed Identity, configuration, connections
8. Agent Framework - Agent config, tools, threads, workflows
9. Dependencies - Necessity, security, versioning
10. Performance - Efficiency, async, resources
11. Operations - Logging, monitoring, configuration
12. Tests - Coverage, quality, AI testing
13. Documentation - Docs in sync with code, examples accurate, changelog updated

Severity levels:
- Critical: Must fix (security vulns, data loss)
- Major: Should fix (bugs, error handling)
- Minor: Worth addressing (style, optimization)
- Info: Suggestions

Changed files:
{files_list}

Diff:
```
{diff}
```

Provide your review in this format:

## Summary
[1-3 sentence assessment]

## Findings

### Critical
[List findings or "None"]

### Major
[List findings or "None"]

### Minor
[List findings or "None"]

### Info
[List findings or "None"]

## Recommendation
**[Approve / Request Changes]**
[Brief explanation]

## Positive Observations
[What was done well]

For each finding, use this format:
**[Dimension]** - `path/to/file.py:L##`
[Issue description]
**Suggestion:** [Specific recommendation]
"""


def run_review() -> None:
    """Run the AI code review."""
    client = Anthropic()

    diff = get_diff()
    files = get_changed_files()

    if not diff.strip():
        print("No changes to review")
        return

    if len(diff) > MAX_DIFF_SIZE:
        print(f"Diff too large ({len(diff):,} characters, max {MAX_DIFF_SIZE:,}). Skipping AI review.")
        print("Consider breaking the PR into smaller changes.")
        return

    prompt = build_review_prompt(diff, files)

    message = client.messages.create(
        model="claude-opus-4-5-20250514",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}],
        timeout=API_TIMEOUT,
    )

    review = message.content[0].text

    # Post as PR comment
    pr_number = os.environ.get("PR_NUMBER")
    if pr_number:
        post_pr_comment(review, pr_number)
    else:
        print(review)


def post_pr_comment(body: str, pr_number: str) -> None:
    """Post review as PR comment."""
    repo = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN")

    if not repo or not token:
        print("Error: Missing GITHUB_REPOSITORY or GITHUB_TOKEN environment variables")
        sys.exit(1)

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    data = json.dumps({"body": f"## 🤖 AI Code Review\n\n{body}"}).encode()

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as response:
            print(f"Posted review comment: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"Failed to post PR comment: {e.code} - {e.reason}")
        if e.code == 403:
            print("Hint: Check that GITHUB_TOKEN has 'pull-requests: write' permission")
        elif e.code == 404:
            print(f"Hint: Repository '{repo}' or PR #{pr_number} not found")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error posting PR comment: {e.reason}")
        sys.exit(1)


if __name__ == "__main__":
    run_review()
