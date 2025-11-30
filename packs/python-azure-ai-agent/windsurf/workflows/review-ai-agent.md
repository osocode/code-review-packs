---
description: AI agent-specific code review focusing on agent patterns and safety
---

# AI Agent Review

Perform a focused review on AI agent implementation patterns and safety.

## Instructions

1. **Identify agent-related code**: Find agent definitions, tool implementations, and orchestration logic.

2. **Review agent configuration**:
   - Are system prompts/instructions clear and bounded?
   - Is the model selection appropriate?
   - Are agent capabilities appropriately scoped?

3. **Review tool implementations**:
   - Are tools properly typed with descriptions?
   - Are tool permissions minimal?
   - Is parameter validation implemented?
   - Are destructive operations gated?

4. **Review safety measures**:
   - Prompt injection prevention
   - Agent loop termination conditions
   - Human-in-the-loop for sensitive operations
   - Output validation before use

5. **Review state management**:
   - Thread/conversation state handling
   - Checkpointing for long operations
   - State cleanup

6. **Review error handling**:
   - Model API error handling
   - Retry logic for transient failures
   - Fallback behavior
   - Timeout configuration

## Output Structure

```markdown
## AI Agent Review Summary

[Assessment of agent implementation quality and safety]

## Agent Configuration

[Findings about agent setup and instructions]

## Tool Safety

[Findings about tool implementations]

## Safety Measures

[Findings about prompt injection, bounds, oversight]

## State Management

[Findings about thread/state handling]

## Error Handling

[Findings about failure modes]

## Recommendation

**[Approve / Request Changes]**

[Agent-specific recommendations]
```
