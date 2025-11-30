# Cascade Execution Checklist

Use this alongside `cascade-instructions.md` for the detailed content of each file.

## Phase 1: Repository Setup

```bash
mkdir code-review-packs
cd code-review-packs
git init
```

- [ ] Create `README.md`
- [ ] Create `LICENSE` (MIT)
- [ ] Create `.gitignore`
- [ ] Create `pyproject.toml`

## Phase 2: Pack Structure

```bash
mkdir -p packs/python-azure-ai-agent/{framework,checklists,windsurf/{rules,workflows},cursor,claude,github/workflows,examples}
mkdir -p src/code_review_pack
mkdir -p docs
```

- [ ] Create `packs/python-azure-ai-agent/pack.yaml`

## Phase 3: Framework Documents

- [ ] Create `packs/python-azure-ai-agent/framework/dimensions.md`
- [ ] Create `packs/python-azure-ai-agent/framework/process.md`
- [ ] Create `packs/python-azure-ai-agent/framework/output-format.md`
- [ ] Create `packs/python-azure-ai-agent/overlay.md`

## Phase 4: Checklists (12 files)

- [ ] `checklists/correctness.md`
- [ ] `checklists/readability.md`
- [ ] `checklists/architecture.md`
- [ ] `checklists/python-patterns.md`
- [ ] `checklists/security.md`
- [ ] `checklists/ai-security.md` ← NEW, critical for AI agents
- [ ] `checklists/azure-ai-foundry.md`
- [ ] `checklists/agent-framework.md`
- [ ] `checklists/dependencies.md`
- [ ] `checklists/performance.md`
- [ ] `checklists/operations.md`
- [ ] `checklists/tests.md`

## Phase 5: Windsurf Config (Markdown, NOT YAML)

- [ ] `windsurf/rules/code-review.md`
- [ ] `windsurf/workflows/review-full.md`
- [ ] `windsurf/workflows/review-security.md`
- [ ] `windsurf/workflows/review-ai-agent.md`

## Phase 6: Cursor Config

- [ ] `cursor/cursorrules`
- [ ] `cursor/AGENTS.md`

## Phase 7: Claude Config

- [ ] `claude/CLAUDE.md`
- [ ] `claude/settings.json`

## Phase 8: GitHub Action

- [ ] `github/workflows/ai-code-review.yml`
- [ ] Create `.github/scripts/ai_review.py` in the pack examples (users copy this)

## Phase 9: CLI

- [ ] `src/code_review_pack/__init__.py`
- [ ] `src/code_review_pack/cli.py`
- [ ] `src/code_review_pack/reviewer.py`

## Phase 10: Documentation

- [ ] `docs/getting-started.md`
- [ ] `docs/pack-structure.md`
- [ ] `docs/creating-custom-packs.md`
- [ ] `docs/ai-tool-setup.md`

## Phase 11: Examples

- [ ] `examples/example-review-output.md`

## Phase 12: Verification

```bash
# Verify Python syntax
python -m py_compile src/code_review_pack/*.py

# Test CLI
pip install -e .
code-review-pack --help
code-review-pack list-packs

# Verify YAML validity
python -c "import yaml; yaml.safe_load(open('packs/python-azure-ai-agent/pack.yaml'))"
```

## Critical Reminders

1. **Windsurf workflows are MARKDOWN files** with frontmatter, not YAML
2. **Claude model is `claude-opus-4-5-20250514`** (Opus 4.5)
3. **No risk classification** in v0.0.1 - all reviews are comprehensive
4. **No PR blocking** in v0.0.1 - reviews are advisory
5. **AI Security checklist is critical** - covers prompt injection, tool safety, data leakage

## File Naming Conventions

- Windsurf rules: `.windsurf/rules/*.md`
- Windsurf workflows: `.windsurf/workflows/*.md`
- Cursor rules: `.cursorrules` (no extension)
- Claude: `CLAUDE.md`, `.claude/settings.json`
