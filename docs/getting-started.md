# Getting Started

## Installation

```bash
pip install code-review-pack
```

## Quick Start

### 1. Initialize a pack in your project

```bash
cd your-project
code-review-pack init
```

Follow the prompts to select a pack and choose which components to install.

### 2. Configure your AI tools

The CLI installs configuration for:
- **Windsurf**: `.windsurf/rules/` and `.windsurf/workflows/`
- **Cursor**: `.cursorrules` and `AGENTS.md`
- **Claude Code**: `CLAUDE.md` and `.claude/settings.json`

### 3. Set up GitHub Actions (optional)

If you installed the GitHub Action:

1. Go to your repository Settings → Secrets and variables → Actions
2. Add `ANTHROPIC_API_KEY` with your Claude API key
3. PRs will now receive automated code reviews

## Using the Review Framework

### Local CLI Review

Run a code review directly from the command line:

```bash
# Review all uncommitted changes
code-review-pack review

# Review only staged changes (useful before committing)
code-review-pack review --staged

# Use a specific pack for context
code-review-pack review --pack python-azure-ai-agent
```

This requires the `ANTHROPIC_API_KEY` environment variable to be set.

### In Windsurf

1. Type `/` in Cascade to see available workflows
2. Select `/review-full` for comprehensive review
3. Or `/review-security` for security-focused review

### In Cursor

1. The rules are automatically applied
2. Ask for a "code review" to invoke the review agent

### In Claude Code

1. Reference CLAUDE.md for review guidelines
2. Ask Claude to review your changes

### Manual Review

Use the checklists in the pack as a guide for manual code reviews.
