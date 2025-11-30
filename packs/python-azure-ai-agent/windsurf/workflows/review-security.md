---
description: Security-focused code review for Python AI agent solutions
---

# Security Review

Perform a security-focused code review of the current changes.

## Instructions

1. **Identify the scope**: Determine which files have changed or are selected for review.

2. **Review for traditional security concerns**:
   - Input validation and sanitization
   - Authentication and authorization
   - Secrets management (no hardcoded secrets)
   - Data protection (encryption, PII handling)
   - Secure configuration
   - Dependency vulnerabilities

3. **Review for AI-specific security concerns**:
   - Prompt injection vulnerabilities
   - Tool/function calling safety
   - Data leakage through AI interactions
   - Agent autonomy bounds
   - Content safety configuration

4. **Review for Azure security concerns**:
   - Managed Identity usage (vs API keys)
   - RBAC configuration
   - Connection security
   - Network isolation

5. **Document findings** with severity levels:
   - **Critical**: Exploitable vulnerabilities
   - **Major**: Security weaknesses
   - **Minor**: Security improvements
   - **Info**: Security suggestions

## Output Structure

```markdown
## Security Review Summary

[Assessment of overall security posture]

## Traditional Security Findings

[Findings related to AppSec]

## AI Security Findings

[Findings related to AI/agent security]

## Azure Security Findings

[Findings related to Azure configuration]

## Recommendation

**[Approve / Request Changes]**

[Security-specific recommendations]
```
