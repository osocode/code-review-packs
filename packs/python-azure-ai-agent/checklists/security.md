# Security Checklist

## Input Validation
- [ ] Is all external input validated before use?
- [ ] Are input size limits enforced?
- [ ] Is input type checking performed?
- [ ] Are injection attacks prevented (SQL, command, etc.)?

## Authentication & Authorization
- [ ] Is authentication required for protected endpoints?
- [ ] Is authorization checked for each operation?
- [ ] Are authentication tokens validated properly?
- [ ] Is the principle of least privilege followed?

## Secrets Management
- [ ] Are secrets stored in secure vaults (not code/config)?
- [ ] Are secrets accessed via environment variables or secret managers?
- [ ] Are secrets excluded from logs and error messages?
- [ ] Is secret rotation supported?

## Data Protection
- [ ] Is sensitive data encrypted at rest?
- [ ] Is TLS used for data in transit?
- [ ] Is PII handled according to data protection requirements?
- [ ] Is data sanitized before logging?

## Configuration Security
- [ ] Are debug features disabled in production?
- [ ] Are secure defaults used?
- [ ] Is configuration validated at startup?
- [ ] Are configuration changes audited?
