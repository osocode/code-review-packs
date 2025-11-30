# Microsoft Agent Framework Checklist

## Agent Definition
- [ ] Is the agent's `instructions` (system prompt) clear and bounded?
- [ ] Is the agent name meaningful for debugging/observability?
- [ ] Are agent capabilities appropriately scoped?
- [ ] Is the model selection appropriate for the task?

## Tool Registration
- [ ] Are tools properly typed with clear parameter descriptions?
- [ ] Do tool descriptions accurately reflect their behavior?
- [ ] Are tools testable in isolation?
- [ ] Is tool error handling implemented?

## Thread & State Management
- [ ] Is conversation state managed through framework thread abstraction?
- [ ] Are long-running conversations checkpointed?
- [ ] Is thread cleanup handled for completed/abandoned conversations?
- [ ] Is state serialization safe and complete?

## Middleware
- [ ] Is middleware used for cross-cutting concerns?
- [ ] Are request/response filters applied consistently?
- [ ] Is there circuit breaker middleware for failures?
- [ ] Are sensitive data filters in place?

## Workflow Patterns (if applicable)
- [ ] Is the workflow graph explicitly defined?
- [ ] Are all edges typed correctly for data flow?
- [ ] Is there a clear termination condition?
- [ ] Are checkpoints used for long-running workflows?

## Error Handling
- [ ] Are model API errors handled gracefully?
- [ ] Is retry logic implemented for transient failures?
- [ ] Are timeout limits configured?
- [ ] Is fallback behavior defined for failures?
