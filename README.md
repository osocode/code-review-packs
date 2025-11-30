# Code Review Packs

Versioned, AI-tool-agnostic code review frameworks for development teams.

## What is a Code Review Pack?

A Code Review Pack is a self-contained set of review guidelines, checklists, and AI tool configurations for a specific technology stack. Packs enable consistent, thorough code reviews whether performed by humans, AI assistants in IDEs, or automated CI pipelines.

## Available Packs

| Pack | Description | Status |
|------|-------------|--------|
| `python-azure-ai-agent` | Python AI agents on Azure AI Foundry with Microsoft Agent Framework | v0.0.1 |

## Quick Start

### Option 1: CLI Installation

```bash
pip install code-review-pack

# Initialize a pack in your project
code-review-pack init --pack python-azure-ai-agent

# Or run interactively
code-review-pack init

# Run a local code review on your changes
code-review-pack review

# Review only staged changes
code-review-pack review --staged
```

### Option 2: Manual Installation

1. Copy the desired pack from `packs/<pack-name>/` to your repository
2. Copy AI tool configurations to appropriate locations:
   - Windsurf: `.windsurf/rules/` and `.windsurf/workflows/`
   - Cursor: `.cursorrules` and `AGENTS.md` to repo root
   - Claude Code: `CLAUDE.md` to repo root
3. Copy GitHub Action to `.github/workflows/` for CI reviews

## Supported AI Tools

- **Windsurf**: Rules and Cascade Workflows
- **Cursor**: Rules and Agent definitions
- **Claude Code**: CLAUDE.md project instructions
- **Claude Desktop/Web**: System prompts and checklists
- **GitHub Actions**: Automated PR reviews via Claude API

## Review Dimensions

Each pack reviews code across these dimensions:

1. **Correctness** - Logic, edge cases, error handling
2. **Readability** - Clarity, naming, documentation
3. **Architecture** - Structure, boundaries, patterns
4. **Language Patterns** - Idiomatic usage, anti-patterns
5. **Security** - Traditional AppSec concerns
6. **AI Security** - Prompt injection, tool safety, data leakage
7. **Dependencies** - Necessity, versions, supply chain
8. **Performance** - Efficiency, scalability, resource usage
9. **Operations** - Observability, deployment, configuration
10. **Tests** - Coverage, quality, maintainability

## Documentation

- [Getting Started](docs/getting-started.md)
- [Pack Structure](docs/pack-structure.md)
- [Creating Custom Packs](docs/creating-custom-packs.md)
- [AI Tool Setup](docs/ai-tool-setup.md)

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

Apache License 2.0 - see [LICENSE](LICENSE)
