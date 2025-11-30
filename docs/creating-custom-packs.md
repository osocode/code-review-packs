# Creating Custom Packs

This guide explains how to create a custom code review pack for your technology stack.

## Step 1: Create the Pack Directory

```bash
mkdir -p packs/my-custom-pack/{framework,checklists,windsurf/{rules,workflows},cursor,claude,github/{workflows,scripts},examples}
```

## Step 2: Define pack.yaml

Create `packs/my-custom-pack/pack.yaml`:

```yaml
pack:
  name: my-custom-pack
  description: "Code review pack for [your stack]"
  version: 0.0.1

  profile:
    primary_language: [language]
    # Add relevant profile settings

  supported_tools:
    - windsurf
    - cursor
    - claude-code
    - github-actions

  dimensions:
    - correctness
    - readability
    - architecture
    # Add your dimensions

  review_settings:
    ai_provider: anthropic
    model: claude-opus-4-5-20250514
    max_tokens: 8192
    temperature: 0.2
```

## Step 3: Create Framework Documents

### dimensions.md

Define what each review dimension means for your stack:

```markdown
# Code Review Dimensions

## 1. Correctness
[What correctness means for your stack]

## 2. Readability
[What readability means for your stack]

# ... etc
```

### process.md

Document your review workflow and severity definitions.

### output-format.md

Define the standard output format for reviews.

## Step 4: Create the Overlay

The overlay (`overlay.md`) provides stack-specific context:

- Technology stack details
- Architecture patterns
- Common anti-patterns
- Security considerations
- Testing patterns

## Step 5: Create Checklists

Create one checklist per dimension in `checklists/`:

```markdown
# [Dimension] Checklist

## [Category]
- [ ] Question 1?
- [ ] Question 2?
- [ ] Question 3?
```

Keep checklists focused with 3-7 items per category.

## Step 6: Configure AI Tools

### Windsurf

Create `windsurf/rules/code-review.md` with frontmatter:

```markdown
---
trigger: model_decision
description: Code review guidelines for [your stack]
---

# Code Review Framework
[Your review guidelines]
```

Create workflows in `windsurf/workflows/`:
- `review-full.md` - Comprehensive review
- `review-security.md` - Security-focused review
- Add domain-specific workflows as needed

### Cursor

Create `cursor/cursorrules` and `cursor/AGENTS.md`.

### Claude

Create `claude/CLAUDE.md` and `claude/settings.json`.

### GitHub Action

Copy and customize the GitHub Action from an existing pack.

## Step 7: Add Examples

Create example review outputs in `examples/` to show expected format.

## Step 8: Test Your Pack

```bash
# Install the CLI
pip install -e .

# List packs to verify yours appears
code-review-pack list-packs

# Test initialization
cd /tmp && mkdir test-project && cd test-project
code-review-pack init --pack my-custom-pack
```

## Best Practices

1. **Keep checklists actionable** - Each item should be a clear yes/no question
2. **Be specific in the overlay** - Include code examples for patterns and anti-patterns
3. **Test with real code** - Validate your pack produces useful reviews
4. **Version your pack** - Update version when making changes
5. **Document assumptions** - Be clear about what technology versions you support
