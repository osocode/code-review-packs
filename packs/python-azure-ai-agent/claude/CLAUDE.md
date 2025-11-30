# Code Review Framework

This project uses a standardized code review framework for Python AI agents on Azure AI Foundry.

## Quick Reference

### Review Dimensions
1. Correctness, Readability, Architecture
2. Python Patterns (type hints, async, idioms)
3. Security (traditional AppSec)
4. AI Security (prompt injection, tool safety, data leakage)
5. Azure AI Foundry (auth, config, connections)
6. Agent Framework (agents, tools, threads)
7. Dependencies, Performance, Operations, Tests
8. Documentation (docs in sync, examples accurate, changelog updated)

### Severity Levels
- **Critical**: Block merge (security vulns, data loss)
- **Major**: Should fix (bugs, error handling)
- **Minor**: Worth addressing (style, optimization)
- **Info**: Suggestions

### AI Security Focus Areas
- Prompt injection: Is user input separated from system prompts?
- Tool safety: Are tool permissions minimal? Parameters validated?
- Data leakage: Can the agent reveal system prompts or other users' data?
- Agent bounds: Are there loop limits? Human-in-the-loop for sensitive ops?

### Output Format
```
## Summary
[1-3 sentences]

## Findings
### Critical
[findings]

### Major
[findings]

## Recommendation
**[Approve / Request Changes]**
[explanation]
```

## Project Structure

```
src/
├── agents/      # Agent definitions
├── tools/       # Tool implementations
├── api/         # API endpoints
├── services/    # Business logic
├── models/      # Data models
└── config/      # Configuration
```

## Key Patterns

### Managed Identity Auth
```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
```

### Agent Creation
```python
from agent_framework.azure import AzureOpenAIResponsesClient

agent = AzureOpenAIResponsesClient(
    credential=credential
).create_agent(
    name="MyAgent",
    instructions="...",
)
```

### Tool Definition
```python
from agent_framework import tool

@tool
async def my_tool(param: str) -> str:
    """Tool description for the model."""
    # Validate param before use
    return result
```
