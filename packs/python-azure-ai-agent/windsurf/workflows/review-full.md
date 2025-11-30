---
description: Perform a comprehensive code review across all dimensions
---

# Full Code Review

Perform a comprehensive code review of the current changes.

## Instructions

1. **Identify the scope**: Determine which files have changed or are selected for review.

2. **Review each file** against all applicable dimensions:
   - Correctness
   - Readability
   - Architecture
   - Python Patterns
   - Security
   - AI Security
   - Azure AI Foundry
   - Agent Framework
   - Dependencies
   - Performance
   - Operations
   - Tests
   - Documentation

3. **Document findings** using this format for each issue:
   ```
   **[Dimension]** - `path/to/file.py:L##`
   
   [Description of the issue]
   
   **Suggestion:** [Specific recommendation]
   ```

4. **Categorize findings** by severity:
   - **Critical**: Must fix before merge
   - **Major**: Should fix
   - **Minor**: Worth addressing
   - **Info**: Suggestions

5. **Provide summary** including:
   - Overall assessment
   - Key concerns
   - Positive observations
   - Recommendation (Approve / Request Changes)

## Output Structure

Format your review as:

```markdown
## Summary

[1-3 sentence summary]

## Findings

### Critical
[Findings or "None"]

### Major
[Findings or "None"]

### Minor
[Findings or "None"]

### Info
[Findings or "None"]

## Recommendation

**[Approve / Request Changes]**

[Brief explanation]

## Positive Observations

[Things done well]
```
