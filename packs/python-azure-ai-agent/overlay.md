# Python Azure AI Agent - Consolidated Overlay

This overlay provides stack-specific guidance for reviewing Python AI agent solutions built on Azure AI Foundry using the Microsoft Agent Framework.

## Technology Stack Context

### Python
- Version: 3.10+
- Style: PEP 8, type hints required for public interfaces
- Async: Preferred for I/O operations, especially AI calls
- Package management: pip with requirements.txt or pyproject.toml

### Azure AI Foundry
- Hub/Project model for resource organization
- Model deployments (serverless or provisioned throughput)
- Connections for external resources (Key Vault, Storage, AI Search)
- Content safety filters on deployments

### Microsoft Agent Framework
- Successor to Semantic Kernel and AutoGen
- Core concepts: Agents, Tools, Threads, Workflows
- Python package: `agent-framework`
- Azure integration via `AzureOpenAIResponsesClient`

### Common Web Frameworks
- FastAPI: Preferred for new APIs
- Flask: Legacy or simpler use cases

## Architecture Patterns

### Recommended Structure
```
src/
├── agents/           # Agent definitions and configurations
├── tools/            # Tool implementations for agents
├── api/              # FastAPI/Flask endpoints
├── services/         # Business logic
├── models/           # Data models (Pydantic)
├── config/           # Configuration management
└── utils/            # Shared utilities
```

### Agent Architecture
```
User Request → API Layer → Agent Orchestration → Agent(s) → Tool Calls → Response
                              ↓
                         Thread State
```

## Common Anti-Patterns

### Python Anti-Patterns
- Using `Any` type instead of proper typing
- Catching bare `Exception` without re-raising or specific handling
- Mutable default arguments
- Global state for request-scoped data
- Synchronous I/O in async contexts

### AI Agent Anti-Patterns
- Passing user input directly to system prompts
- Unbounded agent loops without termination conditions
- Tools with excessive permissions
- Storing conversation state in memory only (no persistence)
- Missing error handling for model API failures

### Azure Anti-Patterns
- Hardcoded API keys instead of Managed Identity
- Missing content safety configuration
- No rate limit handling
- Inline connection strings instead of Key Vault references

## Security Considerations

### Authentication Flow
1. User authenticates to your application
2. Application uses Managed Identity to call Azure AI services
3. Azure RBAC controls access at Hub/Project level
4. Tools authenticate to downstream services via Managed Identity

### Data Flow Security
1. Validate and sanitize user input at API boundary
2. Filter PII before sending to AI models
3. Audit log AI interactions (without PII)
4. Filter/validate model responses before returning to users

### Tool Security
1. Define tools with minimum required permissions
2. Validate tool parameters before execution
3. Implement timeouts and circuit breakers
4. Log tool invocations for audit trail

## Testing Patterns

### Unit Testing Agents
```python
# Mock the model client for deterministic testing
@pytest.fixture
def mock_agent():
    with patch('agent_framework.azure.AzureOpenAIResponsesClient') as mock:
        mock.return_value.create_agent.return_value.run.return_value = "Expected response"
        yield mock

async def test_agent_responds(mock_agent):
    result = await my_agent_function("test input")
    assert "Expected" in result
```

### Integration Testing
- Use Azure AI Foundry test deployments
- Test with representative prompts
- Verify content safety filter behavior
- Test rate limit handling

### Evaluation
- Consider prompt regression testing for critical agent behaviors
- Track response quality metrics over time
- Test for prompt injection resistance
