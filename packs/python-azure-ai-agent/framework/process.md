# Code Review Process

This document describes how to conduct a code review using this pack.

## Review Workflow

### Step 1: Understand the Change
Before diving into details:
- Read the PR description or commit messages
- Understand the purpose and scope of the change
- Identify which dimensions are most relevant

### Step 2: Systematic Review
Work through each applicable dimension:
1. Review the code against the dimension's checklist
2. Note any findings with specific file/line references
3. Categorize findings by severity
4. Formulate actionable suggestions

### Step 3: Document Findings
For each finding, document:
- **Dimension**: Which review dimension this relates to
- **Severity**: Critical, Major, Minor, or Info
- **Location**: File path and line number(s)
- **Issue**: Clear description of the problem
- **Suggestion**: Specific recommendation to address it
- **Rationale**: Why this matters (if not obvious)

### Step 4: Final Assessment
Provide an overall assessment:
- Summary of the change
- Key findings grouped by severity
- Recommendation (Approve / Request Changes)
- Positive observations (what was done well)

## Severity Definitions

### Critical
Issues that must be fixed before merge:
- Security vulnerabilities
- Data loss or corruption risks
- Breaking changes to public interfaces
- Severe performance regressions

### Major
Issues that should be fixed, can be follow-up if justified:
- Bugs that affect functionality
- Missing error handling for likely scenarios
- Significant code quality issues
- Missing tests for critical paths

### Minor
Issues worth addressing but lower priority:
- Style inconsistencies
- Minor optimization opportunities
- Documentation improvements
- Test coverage gaps for edge cases

### Info
Observations and suggestions:
- Alternative approaches to consider
- Future improvement opportunities
- Positive patterns to recognize
- Educational notes

## Review Etiquette

- Be specific and constructive
- Explain the "why" behind suggestions
- Acknowledge good work
- Ask questions when intent is unclear
- Suggest, don't demand (unless it's a blocker)
