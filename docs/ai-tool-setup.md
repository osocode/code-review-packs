# AI Tool Setup

This guide covers how to configure each supported AI tool for code reviews.

## Local CLI

The CLI includes a built-in `review` command that uses Claude to review your changes.

### Setup

Set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY=your-key
```

### Usage

```bash
# Review all uncommitted changes
code-review-pack review

# Review only staged changes
code-review-pack review --staged

# Use a specific pack
code-review-pack review --pack python-azure-ai-agent
```

### Troubleshooting

- **"No changes to review"**: Ensure you have uncommitted changes in your git repository
- **API errors**: Verify `ANTHROPIC_API_KEY` is set correctly
- **Pack not found**: Run `code-review-pack list-packs` to see available packs

## Windsurf

### Installation

After running `code-review-pack init`, Windsurf configuration is installed to:
- `.windsurf/rules/code-review.md` - Always-active review guidelines
- `.windsurf/workflows/` - On-demand review workflows

### Usage

1. **Rules** are automatically applied when Cascade analyzes your code
2. **Workflows** can be invoked by typing `/` in Cascade:
   - `/review-full` - Comprehensive review
   - `/review-security` - Security-focused review
   - `/review-ai-agent` - AI agent-specific review

### Customization

Edit the markdown files to customize:
- Add project-specific patterns
- Adjust severity definitions
- Add custom workflows

## Cursor

### Installation

Configuration is installed to:
- `.cursorrules` - Project rules
- `AGENTS.md` - Agent definitions

### Usage

1. Rules are automatically applied to all interactions
2. Ask for a "code review" to invoke the review agent
3. Reference specific dimensions: "Review this for security"

### Customization

Edit `.cursorrules` to add:
- Project-specific conventions
- Additional review criteria
- Custom patterns to watch for

## Claude Code

### Installation

Configuration is installed to:
- `CLAUDE.md` - Project instructions (repo root)
- `.claude/settings.json` - Settings

### Usage

1. Claude automatically reads `CLAUDE.md` for context
2. Ask Claude to review code changes
3. Reference specific dimensions as needed

### Customization

Edit `CLAUDE.md` to include:
- Project-specific architecture
- Team conventions
- Domain-specific security concerns

## GitHub Actions

### Installation

The action is installed to:
- `.github/workflows/ai-code-review.yml`
- `.github/scripts/ai_review.py`

### Setup

1. Go to repository Settings → Secrets and variables → Actions
2. Add secret: `ANTHROPIC_API_KEY` with your Claude API key
3. PRs will automatically receive AI code reviews

### Customization

Edit `ai-code-review.yml` to:
- Change which file types trigger reviews
- Adjust the review prompt
- Modify when reviews run

Edit `ai_review.py` to:
- Customize the review prompt
- Add project-specific context
- Change output formatting

## API Keys

### Anthropic (Claude)

1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Create an API key
3. Set as environment variable or GitHub secret:
   - Local: `export ANTHROPIC_API_KEY=your-key`
   - GitHub: Add as repository secret

### Security Best Practices

- Never commit API keys to version control
- Use environment variables or secret managers
- Rotate keys periodically
- Use separate keys for development and production
- Monitor API usage for anomalies

## Troubleshooting

### Windsurf workflows not appearing

- Ensure files are in `.windsurf/workflows/`
- Check frontmatter format (YAML between `---` markers)
- Restart Windsurf

### Cursor rules not applying

- Verify `.cursorrules` is in repo root
- Check for syntax errors in the file
- Restart Cursor

### GitHub Action failing

- Verify `ANTHROPIC_API_KEY` secret is set
- Check action logs for specific errors
- Ensure Python dependencies install correctly

### Claude not seeing CLAUDE.md

- Ensure file is in repo root
- Check file permissions
- Verify Claude Code has access to the repository
