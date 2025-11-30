#!/usr/bin/env python3
"""Local code reviewer using Claude."""

import subprocess
from pathlib import Path

from anthropic import Anthropic

# Maximum diff size to send to the API (characters)
# ~100k chars is roughly 25k tokens, well within Claude's context window
MAX_DIFF_SIZE = 100_000

# Timeout for API calls (seconds)
API_TIMEOUT = 120.0


class GitError(Exception):
    """Raised when a git command fails."""

    pass


def get_staged_diff() -> str:
    """Get diff of staged changes.

    Raises:
        GitError: If the git command fails.
    """
    result = subprocess.run(
        ["git", "diff", "--cached"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise GitError(f"git diff --cached failed: {result.stderr}")
    return result.stdout


def get_working_diff() -> str:
    """Get diff of working directory changes.

    Raises:
        GitError: If the git command fails.
    """
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise GitError(f"git diff failed: {result.stderr}")
    return result.stdout


def load_overlay(pack_path: Path) -> str:
    """Load the pack overlay."""
    overlay_path = pack_path / "overlay.md"
    if overlay_path.exists():
        return overlay_path.read_text(encoding="utf-8")
    return ""


def load_checklists(pack_path: Path) -> str:
    """Load relevant checklists."""
    checklists_path = pack_path / "checklists"
    if not checklists_path.exists():
        return ""

    content = []
    for checklist in checklists_path.iterdir():
        if checklist.suffix == ".md":
            content.append(f"## {checklist.stem}\n{checklist.read_text(encoding='utf-8')}")

    return "\n\n".join(content)


def review_code(diff: str, overlay: str = "", checklists: str = "") -> str:
    """Run code review on diff.

    Args:
        diff: The git diff to review.
        overlay: Optional pack overlay content.
        checklists: Optional checklist content.

    Returns:
        The review text from Claude.

    Raises:
        ValueError: If the diff exceeds MAX_DIFF_SIZE.
    """
    if len(diff) > MAX_DIFF_SIZE:
        raise ValueError(
            f"Diff too large ({len(diff):,} characters). "
            f"Maximum size is {MAX_DIFF_SIZE:,} characters. "
            "Consider reviewing smaller changesets."
        )

    client = Anthropic()

    prompt = f"""You are an expert code reviewer for Python AI agent solutions.

{overlay}

Reference checklists:
{checklists}

Review the following diff:

```
{diff}
```

Provide a structured review with:
1. Summary (1-3 sentences)
2. Findings by severity (Critical, Major, Minor, Info)
3. Each finding: Dimension, Location, Issue, Suggestion
4. Recommendation (Approve / Request Changes)
5. Positive observations
"""

    message = client.messages.create(
        model="claude-opus-4-5-20250514",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}],
        timeout=API_TIMEOUT,
    )

    return message.content[0].text
