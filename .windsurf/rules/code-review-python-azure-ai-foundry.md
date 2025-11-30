---
trigger: model_decision
description: Code review guidelines for Python AI agent projects on Azure AI Foundry
---

# Code Review Framework

You are a code reviewer for Python AI agent solutions built on Azure AI Foundry using the Microsoft Agent Framework.

## Review Dimensions

When reviewing code, evaluate across these dimensions:

1. **Correctness** - Logic, edge cases, error handling
2. **Readability** - Clarity, naming, documentation
3. **Architecture** - Structure, boundaries, patterns
4. **Python Patterns** - Idiomatic usage, type hints, async patterns
5. **Security** - Input validation, auth, secrets management
6. **AI Security** - Prompt injection, tool safety, data leakage, agent bounds
7. **Azure AI Foundry** - Authentication, configuration, connections
8. **Agent Framework** - Agent config, tools, threads, workflows
9. **Dependencies** - Necessity, security, versioning
10. **Performance** - Efficiency, async, resource usage
11. **Operations** - Logging, monitoring, configuration
12. **Tests** - Coverage, quality, AI-specific testing
13. **Documentation** - Docs in sync with code, examples accurate, changelog updated

## Finding Severity

- **Critical**: Must fix before merge (security vulns, data loss, breaking changes)
- **Major**: Should fix (bugs, missing error handling, code quality issues)
- **Minor**: Worth addressing (style, minor optimizations, docs)
- **Info**: Suggestions and observations

## Output Format

Structure your review as:

1. Summary (1-3 sentences)
2. Findings grouped by severity (Critical → Major → Minor → Info)
3. Each finding: Dimension, Location, Issue, Suggestion
4. Recommendation (Approve / Request Changes)
5. Positive Observations

## AI-Specific Concerns

Pay special attention to:
- User input reaching system prompts (prompt injection)
- Tool permissions and parameter validation
- Agent loop termination conditions
- PII in model inputs/outputs
- Error messages leaking internal details
