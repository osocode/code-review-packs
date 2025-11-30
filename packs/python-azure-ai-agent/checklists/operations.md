# Operations Checklist

## Observability
- [ ] Are key operations logged with appropriate context?
- [ ] Are log levels used correctly (DEBUG, INFO, WARNING, ERROR)?
- [ ] Is structured logging used for machine parsing?
- [ ] Are correlation IDs propagated for tracing?

## Metrics & Monitoring
- [ ] Are business-relevant metrics exposed?
- [ ] Are technical health metrics available?
- [ ] Is there monitoring for error rates and latency?
- [ ] Are AI-specific metrics tracked (token usage, latency)?

## Configuration
- [ ] Is configuration externalized (environment variables, config files)?
- [ ] Are configuration changes possible without redeployment?
- [ ] Is configuration validated at startup?
- [ ] Are sensible defaults provided?

## Health & Readiness
- [ ] Are health check endpoints implemented?
- [ ] Do health checks verify critical dependencies?
- [ ] Are readiness checks separate from liveness checks?
- [ ] Is graceful shutdown implemented?

## Deployment
- [ ] Is the deployment process documented?
- [ ] Are deployment artifacts versioned?
- [ ] Is rollback possible and tested?
- [ ] Are feature flags used for risky changes?
