# AI Security Checklist

## Prompt Injection Prevention
- [ ] Is user input separated from system prompts?
- [ ] Are prompt templates protected from user modification?
- [ ] Is indirect injection considered (RAG sources, tool outputs)?
- [ ] Are output instructions in prompts resistant to override?

## Tool & Function Calling Safety
- [ ] Are tool permissions scoped to minimum necessary?
- [ ] Are tool parameters validated before execution?
- [ ] Is the blast radius of tool misuse bounded?
- [ ] Are destructive operations gated (confirmation, human approval)?

## Data Leakage Prevention
- [ ] Can the agent be manipulated to reveal system prompts?
- [ ] Is cross-user data isolation enforced?
- [ ] Are RAG retrieval results filtered for authorization?
- [ ] Is PII filtered before model input and after output?

## Agent Autonomy & Oversight
- [ ] Is the agent's action scope bounded and documented?
- [ ] Are there termination conditions for agent loops?
- [ ] Is there human-in-the-loop for high-risk operations?
- [ ] Are autonomous operations logged with sufficient context?

## Content Safety
- [ ] Are content safety filters configured appropriately?
- [ ] Is harmful content filtered from outputs?
- [ ] Are model outputs validated before use in downstream operations?
- [ ] Is there monitoring for adversarial inputs?

## Model Configuration
- [ ] Are model endpoints authenticated securely?
- [ ] Are rate limits configured to prevent abuse?
- [ ] Is token usage tracked and bounded?
- [ ] Are model responses validated for expected format?
