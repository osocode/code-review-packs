# Azure AI Foundry Checklist

## Authentication & Identity
- [ ] Is Managed Identity used instead of API keys?
- [ ] Are RBAC roles scoped appropriately (Hub vs Project)?
- [ ] Is `DefaultAzureCredential` or `AzureCliCredential` used correctly?
- [ ] Are cross-resource permissions configured correctly?

## Resource Configuration
- [ ] Are model deployments configured with content safety filters?
- [ ] Is the deployment type appropriate (serverless vs provisioned)?
- [ ] Are quotas and rate limits understood and handled?
- [ ] Is the correct API version specified?

## Connection Management
- [ ] Are connections defined in AI Foundry (not hardcoded)?
- [ ] Are connection secrets stored in Key Vault?
- [ ] Is connection configuration environment-specific?
- [ ] Are connections tested at application startup?

## Cost & Quota Awareness
- [ ] Are token usage patterns understood and optimized?
- [ ] Is there handling for quota exceeded errors?
- [ ] Are cost monitoring and alerts configured?
- [ ] Is caching considered for repeated queries?

## Environment Configuration
- [ ] Are Hub/Project IDs configurable per environment?
- [ ] Are deployment names environment-specific?
- [ ] Is there a clear dev/staging/prod separation?
- [ ] Are feature flags used for gradual rollout?
