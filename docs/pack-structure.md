# Pack Structure

Each pack contains:

```
pack-name/
├── pack.yaml              # Pack metadata and configuration
├── framework/
│   ├── dimensions.md      # Review dimension definitions
│   ├── process.md         # Review process guide
│   └── output-format.md   # Standard output format
├── overlay.md             # Stack-specific guidance
├── checklists/            # Per-dimension checklists
├── windsurf/              # Windsurf configuration
│   ├── rules/
│   └── workflows/
├── cursor/                # Cursor configuration
├── claude/                # Claude Code configuration
├── github/                # GitHub Actions
│   └── workflows/
└── examples/              # Example reviews
```

## pack.yaml

Defines the pack identity, supported tools, and review configuration.

```yaml
pack:
  name: pack-name
  description: "Pack description"
  version: 0.0.1

  profile:
    primary_language: python
    # ... other profile settings

  supported_tools:
    - windsurf
    - cursor
    - claude-code

  dimensions:
    - correctness
    - readability
    # ... other dimensions

  review_settings:
    ai_provider: anthropic
    model: claude-opus-4-5-20250514
```

## overlay.md

Contains stack-specific guidance including:
- Architecture patterns
- Common anti-patterns
- Security considerations
- Testing patterns

## checklists/

One file per dimension with 3-7 key questions to evaluate.

## AI Tool Configurations

Each tool gets its own directory with appropriate configuration files:

### Windsurf
- `rules/code-review.md` - Always-on review guidelines
- `workflows/review-*.md` - On-demand review workflows

### Cursor
- `cursorrules` - Project rules file
- `AGENTS.md` - Agent definitions

### Claude
- `CLAUDE.md` - Project instructions
- `settings.json` - Configuration settings

### GitHub
- `workflows/ai-code-review.yml` - PR review action
- `scripts/ai_review.py` - Review script
