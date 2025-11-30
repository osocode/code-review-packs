# Windsurf Cascade Instructions: Build Code Review Packs Repository

## Project Overview

Build a GitHub repository called `code-review-packs` that provides versioned, AI-tool-agnostic code review frameworks. The first pack targets Python AI agent solutions built on Azure AI Foundry using the Microsoft Agent Framework.

## Key Design Decisions

1. **Windsurf workflows are Markdown files**, not YAML
2. **Single consolidated overlay per pack** - no stacking/composition
3. **Profile-based pack structure** - each pack is self-contained for a specific tech stack
4. **Claude Opus 4.5** is the AI provider for code reviews
5. **No risk classification** in v0.0.1 - all reviews are comprehensive
6. **No PR blocking** in v0.0.1 - reviews are advisory only
7. **Review all changed files** - no file filtering in initial release

## Repository Structure

Create this exact structure:

```
code-review-packs/
├── README.md
├── LICENSE
├── .gitignore
├── setup.py
├── pyproject.toml
├── src/
│   └── code_review_pack/
│       ├── __init__.py
│       ├── cli.py
│       ├── reviewer.py
│       └── templates/
│           └── (copies of pack files for CLI distribution)
├── packs/
│   └── python-azure-ai-agent/
│       ├── pack.yaml
│       ├── framework/
│       │   ├── dimensions.md
│       │   ├── process.md
│       │   └── output-format.md
│       ├── overlay.md
│       ├── checklists/
│       │   ├── correctness.md
│       │   ├── readability.md
│       │   ├── architecture.md
│       │   ├── python-patterns.md
│       │   ├── security.md
│       │   ├── ai-security.md
│       │   ├── azure-ai-foundry.md
│       │   ├── agent-framework.md
│       │   ├── dependencies.md
│       │   ├── performance.md
│       │   ├── operations.md
│       │   └── tests.md
│       ├── windsurf/
│       │   ├── rules/
│       │   │   └── code-review.md
│       │   └── workflows/
│       │       ├── review-full.md
│       │       ├── review-security.md
│       │       └── review-ai-agent.md
│       ├── cursor/
│       │   ├── cursorrules
│       │   └── AGENTS.md
│       ├── claude/
│       │   ├── CLAUDE.md
│       │   └── settings.json
│       ├── github/
│       │   └── workflows/
│       │       └── ai-code-review.yml
│       └── examples/
│           ├── example-review-input.md
│           └── example-review-output.md
└── docs/
    ├── getting-started.md
    ├── pack-structure.md
    ├── creating-custom-packs.md
    └── ai-tool-setup.md
```

---

## File Contents

### Root Files

#### README.md

```markdown
# Code Review Packs

Versioned, AI-tool-agnostic code review frameworks for development teams.

## What is a Code Review Pack?

A Code Review Pack is a self-contained set of review guidelines, checklists, and AI tool configurations for a specific technology stack. Packs enable consistent, thorough code reviews whether performed by humans, AI assistants in IDEs, or automated CI pipelines.

## Available Packs

| Pack | Description | Status |
|------|-------------|--------|
| `python-azure-ai-agent` | Python AI agents on Azure AI Foundry with Microsoft Agent Framework | v0.0.1 |

## Quick Start

### Option 1: CLI Installation

```bash
pip install code-review-pack

# Initialize a pack in your project
code-review-pack init --pack python-azure-ai-agent

# Or run interactively
code-review-pack init
```

### Option 2: Manual Installation

1. Copy the desired pack from `packs/<pack-name>/` to your repository
2. Copy AI tool configurations to appropriate locations:
   - Windsurf: `.windsurf/rules/` and `.windsurf/workflows/`
   - Cursor: `.cursorrules` and `AGENTS.md` to repo root
   - Claude Code: `CLAUDE.md` to repo root
3. Copy GitHub Action to `.github/workflows/` for CI reviews

## Supported AI Tools

- **Windsurf**: Rules and Cascade Workflows
- **Cursor**: Rules and Agent definitions
- **Claude Code**: CLAUDE.md project instructions
- **Claude Desktop/Web**: System prompts and checklists
- **GitHub Actions**: Automated PR reviews via Claude API

## Review Dimensions

Each pack reviews code across these dimensions:

1. **Correctness** - Logic, edge cases, error handling
2. **Readability** - Clarity, naming, documentation
3. **Architecture** - Structure, boundaries, patterns
4. **Language Patterns** - Idiomatic usage, anti-patterns
5. **Security** - Traditional AppSec concerns
6. **AI Security** - Prompt injection, tool safety, data leakage
7. **Dependencies** - Necessity, versions, supply chain
8. **Performance** - Efficiency, scalability, resource usage
9. **Operations** - Observability, deployment, configuration
10. **Tests** - Coverage, quality, maintainability

## Documentation

- [Getting Started](docs/getting-started.md)
- [Pack Structure](docs/pack-structure.md)
- [Creating Custom Packs](docs/creating-custom-packs.md)
- [AI Tool Setup](docs/ai-tool-setup.md)

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE)
```

#### .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.env
.venv
env/
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/

# Build
*.log
```

#### pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "code-review-pack"
version = "0.0.1"
description = "AI-tool-agnostic code review frameworks"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.10"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
dependencies = [
    "click>=8.0.0",
    "pyyaml>=6.0",
    "rich>=13.0.0",
    "anthropic>=0.40.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]

[project.scripts]
code-review-pack = "code_review_pack.cli:main"

[project.urls]
Homepage = "https://github.com/your-org/code-review-packs"
Documentation = "https://github.com/your-org/code-review-packs/docs"
Repository = "https://github.com/your-org/code-review-packs"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
code_review_pack = ["templates/**/*"]

[tool.black]
line-length = 100
target-version = ["py310", "py311", "py312"]

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "W", "UP"]
ignore = ["E501"]
```

---

### Pack Definition

#### packs/python-azure-ai-agent/pack.yaml

```yaml
pack:
  name: python-azure-ai-agent
  description: "Code review pack for Python AI agents on Azure AI Foundry using Microsoft Agent Framework"
  version: 0.0.1

  profile:
    primary_language: python
    python_version: ">=3.10"
    ai_platform: azure-ai-foundry
    agent_framework: microsoft-agent-framework
    web_frameworks:
      - fastapi
      - flask
    iac_options:
      - terraform
      - bicep
    cloud_provider: azure

  supported_tools:
    - windsurf
    - cursor
    - claude-code
    - claude-desktop
    - github-actions

  dimensions:
    - correctness
    - readability
    - architecture
    - python-patterns
    - security
    - ai-security
    - azure-ai-foundry
    - agent-framework
    - dependencies
    - performance
    - operations
    - tests

  review_settings:
    ai_provider: anthropic
    model: claude-opus-4-5-20250514
    max_tokens: 8192
    temperature: 0.2
```

---

### Framework Documents

#### packs/python-azure-ai-agent/framework/dimensions.md

```markdown
# Code Review Dimensions

This document defines the review dimensions used to systematically evaluate code changes.

## Core Dimensions

### 1. Correctness
Does the code do what it's supposed to do?
- Logic accuracy and completeness
- Edge case handling
- Error handling and recovery
- State management correctness
- Concurrency safety (if applicable)

### 2. Readability
Can other developers understand this code?
- Clear naming conventions
- Appropriate comments and documentation
- Logical code organization
- Consistent formatting
- Self-documenting patterns

### 3. Architecture
Does this fit well into the system?
- Appropriate abstraction levels
- Clear boundaries and responsibilities
- Dependency direction (dependencies point inward)
- Interface design
- Separation of concerns

### 4. Python Patterns
Does this follow Python idioms and best practices?
- Pythonic code style (PEP 8, PEP 20)
- Appropriate use of language features
- Type hints and annotations
- Standard library usage
- Framework-specific patterns

### 5. Security
Is this code secure from traditional threats?
- Input validation and sanitization
- Authentication and authorization
- Secrets management
- Secure communications
- Logging without sensitive data

### 6. AI Security
Is this code secure from AI-specific threats?
- Prompt injection prevention
- Tool/function calling safety
- Data leakage prevention
- Agent autonomy bounds
- Content filtering configuration

### 7. Azure AI Foundry
Does this follow Azure AI Foundry best practices?
- Authentication patterns (Managed Identity preferred)
- Resource configuration
- Connection management
- Content safety settings
- Cost and quota awareness

### 8. Agent Framework
Does this follow Microsoft Agent Framework patterns?
- Agent definition and configuration
- Tool registration and validation
- Thread and state management
- Middleware usage
- Workflow structure (if applicable)

### 9. Dependencies
Are dependencies appropriate and secure?
- Necessity of new dependencies
- Version selection (avoiding known vulnerabilities)
- License compatibility
- Maintenance status
- Pinning strategy

### 10. Performance
Is this code efficient and scalable?
- Algorithmic efficiency
- Resource utilization
- Async/await patterns
- Caching strategies
- Database query efficiency

### 11. Operations
Is this code production-ready?
- Logging and observability
- Configuration management
- Health checks and monitoring
- Graceful degradation
- Deployment considerations

### 12. Tests
Is this code adequately tested?
- Test coverage for new code
- Test quality and maintainability
- Edge case coverage
- Mock/stub appropriateness
- Integration test considerations
```

#### packs/python-azure-ai-agent/framework/process.md

```markdown
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
```

#### packs/python-azure-ai-agent/framework/output-format.md

```markdown
# Review Output Format

This document defines the standard output format for code reviews.

## Structured Output

Reviews should follow this structure:

```
## Summary

[1-3 sentence summary of the change and overall assessment]

## Findings

### Critical

[List critical findings, or "None" if none exist]

### Major

[List major findings, or "None" if none exist]

### Minor

[List minor findings, or "None" if none exist]

### Info

[List informational findings, or "None" if none exist]

## Recommendation

**[Approve / Request Changes]**

[Brief explanation of the recommendation]

## Positive Observations

[Things done well worth acknowledging]
```

## Finding Format

Each finding should follow this format:

```
**[Dimension]** - `path/to/file.py:L42-L50`

[Description of the issue]

**Suggestion:** [Specific recommendation]

**Rationale:** [Why this matters - optional if obvious]
```

## Example Output

```
## Summary

This PR adds a new chat endpoint to the FastAPI application that interacts with the AI agent. The implementation is functional but has security concerns around input validation and a missing error handler for rate limit responses.

## Findings

### Critical

None

### Major

**AI Security** - `src/api/chat.py:L23-L28`

User input is passed directly to the agent without sanitization. This could allow prompt injection attacks where malicious input manipulates agent behavior.

**Suggestion:** Add input validation and consider a sanitization layer that strips or escapes potential injection patterns before passing to the agent.

**Security** - `src/api/chat.py:L45`

The error response includes the full exception message which may leak internal details.

**Suggestion:** Return a generic error message to users and log the full exception server-side.

### Minor

**Readability** - `src/api/chat.py:L15-L20`

The function `process_msg` could be renamed to better describe its purpose.

**Suggestion:** Consider `handle_chat_request` or `process_chat_message`.

**Tests** - `tests/test_chat.py`

No tests for the rate limit error handling path.

**Suggestion:** Add a test that mocks a 429 response from the agent service.

### Info

**Performance** - `src/api/chat.py:L30`

Consider adding response streaming for better UX on longer agent responses. Not required for this PR but worth considering.

## Recommendation

**Request Changes**

The prompt injection vulnerability should be addressed before merge. The error message leakage is also important but could be a fast follow-up if needed.

## Positive Observations

- Good use of async/await patterns
- Clean separation between API layer and agent interaction
- Comprehensive logging for debugging
```
```

---

### Overlay Document

#### packs/python-azure-ai-agent/overlay.md

```markdown
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
```

---

### Checklists

#### packs/python-azure-ai-agent/checklists/correctness.md

```markdown
# Correctness Checklist

## Logic & Behavior
- [ ] Does the code implement the intended functionality completely?
- [ ] Are all code paths reachable and tested?
- [ ] Are edge cases handled appropriately?
- [ ] Are boundary conditions correct (off-by-one, empty inputs, etc.)?

## Error Handling
- [ ] Are errors caught at appropriate levels?
- [ ] Are error messages informative without leaking sensitive info?
- [ ] Is there appropriate cleanup/rollback on failure?
- [ ] Are async errors properly propagated?

## State Management
- [ ] Is state modified consistently and atomically where needed?
- [ ] Are race conditions prevented in concurrent code?
- [ ] Is state properly initialized before use?
- [ ] Is cleanup performed when state is no longer needed?

## Data Integrity
- [ ] Are data transformations preserving required properties?
- [ ] Are nulls/None values handled explicitly?
- [ ] Are type conversions safe and validated?
```

#### packs/python-azure-ai-agent/checklists/readability.md

```markdown
# Readability Checklist

## Naming
- [ ] Do names clearly convey purpose and intent?
- [ ] Are naming conventions consistent throughout?
- [ ] Are abbreviations avoided or well-established?
- [ ] Do boolean names read as yes/no questions (is_, has_, can_)?

## Structure
- [ ] Are functions/methods appropriately sized (single responsibility)?
- [ ] Is nesting depth reasonable (≤3 levels preferred)?
- [ ] Is related code grouped together?
- [ ] Are imports organized (standard lib, third-party, local)?

## Documentation
- [ ] Do public functions/classes have docstrings?
- [ ] Are complex algorithms or business logic explained?
- [ ] Are non-obvious decisions documented with rationale?
- [ ] Is the module/file purpose clear from its name or header?

## Code Clarity
- [ ] Is clever code avoided in favor of clear code?
- [ ] Are magic numbers replaced with named constants?
- [ ] Are complex conditions extracted to well-named functions?
- [ ] Is control flow straightforward and predictable?
```

#### packs/python-azure-ai-agent/checklists/architecture.md

```markdown
# Architecture Checklist

## Boundaries & Responsibilities
- [ ] Are component boundaries clear and well-defined?
- [ ] Does each module have a single, clear responsibility?
- [ ] Are dependencies between components explicit and minimal?
- [ ] Is the dependency direction correct (dependencies point inward)?

## Abstraction
- [ ] Are abstractions at appropriate levels (not too leaky, not too opaque)?
- [ ] Are interfaces stable and implementation details hidden?
- [ ] Is there unnecessary abstraction adding complexity?
- [ ] Are extension points identified for likely future changes?

## Patterns & Consistency
- [ ] Does this follow established patterns in the codebase?
- [ ] If introducing a new pattern, is it justified and documented?
- [ ] Are similar problems solved consistently?
- [ ] Is the architecture decision aligned with system constraints?

## Integration
- [ ] Does this integrate cleanly with existing components?
- [ ] Are integration points well-defined and documented?
- [ ] Is there appropriate error handling at boundaries?
- [ ] Are contracts between components explicit?
```

#### packs/python-azure-ai-agent/checklists/python-patterns.md

```markdown
# Python Patterns Checklist

## Type Safety
- [ ] Are type hints provided for public function signatures?
- [ ] Are complex types defined clearly (TypedDict, dataclass, Pydantic)?
- [ ] Is `Any` avoided except where truly necessary?
- [ ] Are Optional types used correctly with None checks?

## Pythonic Patterns
- [ ] Are list/dict/set comprehensions used where appropriate?
- [ ] Are context managers used for resource management?
- [ ] Are generators used for large sequences?
- [ ] Is `enumerate()` used instead of manual indexing?

## Async Patterns
- [ ] Are async functions used for I/O-bound operations?
- [ ] Is `asyncio.gather()` used for concurrent operations?
- [ ] Are blocking calls avoided in async contexts?
- [ ] Is async context properly propagated through call chains?

## Error Handling
- [ ] Are specific exceptions caught rather than bare `except`?
- [ ] Are custom exceptions used for domain-specific errors?
- [ ] Is exception chaining used (`raise ... from ...`)?
- [ ] Are exceptions logged with appropriate context?

## Standard Library Usage
- [ ] Is `pathlib` used instead of string path manipulation?
- [ ] Is `dataclasses` or Pydantic used for data structures?
- [ ] Is `logging` used instead of print statements?
- [ ] Are appropriate collections types used (defaultdict, Counter, etc.)?
```

#### packs/python-azure-ai-agent/checklists/security.md

```markdown
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
```

#### packs/python-azure-ai-agent/checklists/ai-security.md

```markdown
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
```

#### packs/python-azure-ai-agent/checklists/azure-ai-foundry.md

```markdown
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
```

#### packs/python-azure-ai-agent/checklists/agent-framework.md

```markdown
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
```

#### packs/python-azure-ai-agent/checklists/dependencies.md

```markdown
# Dependencies Checklist

## Necessity
- [ ] Is each new dependency truly necessary?
- [ ] Could standard library functionality be used instead?
- [ ] Is the dependency actively maintained?
- [ ] Is the dependency's scope appropriate (not bloated)?

## Security
- [ ] Are there known vulnerabilities in selected versions?
- [ ] Is the package source trusted (PyPI, not arbitrary URLs)?
- [ ] Are dependency hashes verified (if high security)?
- [ ] Is the dependency's security track record acceptable?

## Versioning
- [ ] Are version constraints appropriate (not too loose, not too tight)?
- [ ] Are breaking change risks understood?
- [ ] Is there a strategy for security updates?
- [ ] Are transitive dependencies considered?

## License Compliance
- [ ] Is the license compatible with project requirements?
- [ ] Are license obligations understood and met?
- [ ] Is license information documented?

## Operational Impact
- [ ] Does the dependency have reasonable performance?
- [ ] Are there deployment size implications?
- [ ] Is the dependency's error behavior understood?
- [ ] Are there platform compatibility concerns?
```

#### packs/python-azure-ai-agent/checklists/performance.md

```markdown
# Performance Checklist

## Algorithmic Efficiency
- [ ] Is the algorithm appropriate for expected data sizes?
- [ ] Are there obvious O(n²) or worse patterns that could be improved?
- [ ] Is unnecessary computation avoided?
- [ ] Are results cached where beneficial?

## Async & Concurrency
- [ ] Are I/O operations async where possible?
- [ ] Is `asyncio.gather()` used for concurrent operations?
- [ ] Are blocking operations offloaded to thread pools?
- [ ] Is concurrency limited to prevent resource exhaustion?

## Resource Usage
- [ ] Are resources (connections, files) properly pooled and reused?
- [ ] Is memory usage bounded for large operations?
- [ ] Are database queries efficient (proper indexes, no N+1)?
- [ ] Is streaming used for large payloads?

## AI-Specific Performance
- [ ] Is token usage optimized (prompt length, model selection)?
- [ ] Are AI responses cached where appropriate?
- [ ] Is streaming used for long AI responses?
- [ ] Are rate limits handled with backoff?

## Scalability
- [ ] Can this code handle 10x the expected load?
- [ ] Are there stateful bottlenecks that prevent scaling?
- [ ] Is horizontal scaling supported?
- [ ] Are external dependencies scalable?
```

#### packs/python-azure-ai-agent/checklists/operations.md

```markdown
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
```

#### packs/python-azure-ai-agent/checklists/tests.md

```markdown
# Tests Checklist

## Coverage
- [ ] Are new code paths covered by tests?
- [ ] Are error handling paths tested?
- [ ] Are edge cases explicitly tested?
- [ ] Is the happy path fully exercised?

## Quality
- [ ] Do tests have clear, descriptive names?
- [ ] Is each test focused on one behavior?
- [ ] Are assertions meaningful and complete?
- [ ] Are tests independent (no shared mutable state)?

## Maintainability
- [ ] Are test fixtures reusable and well-organized?
- [ ] Is test setup minimal and clear?
- [ ] Are magic values replaced with named constants?
- [ ] Is test code as readable as production code?

## AI Testing
- [ ] Are AI responses mocked for unit tests?
- [ ] Is there integration testing with real AI services?
- [ ] Are prompt changes regression tested?
- [ ] Is tool calling tested in isolation?

## Test Types
- [ ] Are unit tests fast and isolated?
- [ ] Are integration tests focused on boundaries?
- [ ] Are there smoke tests for critical paths?
- [ ] Is there consideration for contract tests?
```

---

### Windsurf Configuration

#### packs/python-azure-ai-agent/windsurf/rules/code-review.md

```markdown
---
trigger: model_decision
description: Code review guidelines for Python AI agent projects on Azure AI Foundry
---

# Code Review Framework

You are a code reviewer for Python AI agent solutions built on Azure AI Foundry using the Microsoft Agent Framework.

## Review Dimensions

When reviewing code, evaluate across these dimensions:

1. **Correctness** - Logic, edge cases, error handling
2. **Readability** - Clarity, naming, documentation
3. **Architecture** - Structure, boundaries, patterns
4. **Python Patterns** - Idiomatic usage, type hints, async patterns
5. **Security** - Input validation, auth, secrets management
6. **AI Security** - Prompt injection, tool safety, data leakage, agent bounds
7. **Azure AI Foundry** - Authentication, configuration, connections
8. **Agent Framework** - Agent config, tools, threads, workflows
9. **Dependencies** - Necessity, security, versioning
10. **Performance** - Efficiency, async, resource usage
11. **Operations** - Logging, monitoring, configuration
12. **Tests** - Coverage, quality, AI-specific testing

## Finding Severity

- **Critical**: Must fix before merge (security vulns, data loss, breaking changes)
- **Major**: Should fix (bugs, missing error handling, code quality issues)
- **Minor**: Worth addressing (style, minor optimizations, docs)
- **Info**: Suggestions and observations

## Output Format

Structure your review as:

1. Summary (1-3 sentences)
2. Findings grouped by severity (Critical → Major → Minor → Info)
3. Each finding: Dimension, Location, Issue, Suggestion
4. Recommendation (Approve / Request Changes)
5. Positive Observations

## AI-Specific Concerns

Pay special attention to:
- User input reaching system prompts (prompt injection)
- Tool permissions and parameter validation
- Agent loop termination conditions
- PII in model inputs/outputs
- Error messages leaking internal details
```

#### packs/python-azure-ai-agent/windsurf/workflows/review-full.md

```markdown
---
description: Perform a comprehensive code review across all dimensions
---

# Full Code Review

Perform a comprehensive code review of the current changes.

## Instructions

1. **Identify the scope**: Determine which files have changed or are selected for review.

2. **Review each file** against all applicable dimensions:
   - Correctness
   - Readability
   - Architecture
   - Python Patterns
   - Security
   - AI Security
   - Azure AI Foundry
   - Agent Framework
   - Dependencies
   - Performance
   - Operations
   - Tests

3. **Document findings** using this format for each issue:
   ```
   **[Dimension]** - `path/to/file.py:L##`
   
   [Description of the issue]
   
   **Suggestion:** [Specific recommendation]
   ```

4. **Categorize findings** by severity:
   - **Critical**: Must fix before merge
   - **Major**: Should fix
   - **Minor**: Worth addressing
   - **Info**: Suggestions

5. **Provide summary** including:
   - Overall assessment
   - Key concerns
   - Positive observations
   - Recommendation (Approve / Request Changes)

## Output Structure

Format your review as:

```markdown
## Summary

[1-3 sentence summary]

## Findings

### Critical
[Findings or "None"]

### Major
[Findings or "None"]

### Minor
[Findings or "None"]

### Info
[Findings or "None"]

## Recommendation

**[Approve / Request Changes]**

[Brief explanation]

## Positive Observations

[Things done well]
```
```

#### packs/python-azure-ai-agent/windsurf/workflows/review-security.md

```markdown
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
```

#### packs/python-azure-ai-agent/windsurf/workflows/review-ai-agent.md

```markdown
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
```

---

### Cursor Configuration

#### packs/python-azure-ai-agent/cursor/cursorrules

```markdown
# Code Review Framework for Python AI Agents

## Context

This project builds Python AI agents on Azure AI Foundry using the Microsoft Agent Framework.

## Code Review Guidelines

When reviewing code or assisting with code changes, apply these review dimensions:

### Security (Highest Priority)
- Validate all user input before use
- Never pass user input directly to system prompts
- Use Managed Identity, not API keys
- Keep secrets in Key Vault
- Sanitize logs and error messages

### AI Safety
- Bound agent capabilities and loop iterations
- Validate tool parameters before execution
- Filter PII from model inputs/outputs
- Configure content safety filters
- Test for prompt injection resistance

### Python Best Practices
- Use type hints for public interfaces
- Prefer async for I/O operations
- Use Pydantic for data validation
- Follow PEP 8 style guidelines
- Handle errors with specific exceptions

### Architecture
- Clear separation of concerns
- Dependencies point inward
- Explicit interfaces between components
- Configuration externalized

### Testing
- Unit tests with mocked AI responses
- Integration tests for critical paths
- Edge case coverage
- Async test patterns

## Finding Format

When identifying issues, use:

```
**[Dimension]** - `file:line`
Issue description.
**Suggestion:** Specific fix.
```

## Severity Levels

- **Critical**: Security vulnerabilities, data loss risks
- **Major**: Bugs, missing error handling
- **Minor**: Style, minor improvements
- **Info**: Suggestions
```

#### packs/python-azure-ai-agent/cursor/AGENTS.md

```markdown
# Agent Definitions

## Code Review Agent

### Purpose
Perform comprehensive code reviews for Python AI agent solutions.

### Capabilities
- Analyze code changes across all review dimensions
- Identify security vulnerabilities including AI-specific threats
- Suggest improvements with specific code examples
- Evaluate architecture and design patterns

### Activation
Invoke when:
- User asks for a code review
- User asks to check code quality
- User asks about security concerns
- User asks about best practices

### Behavior
1. Identify scope of code to review
2. Analyze against all applicable dimensions
3. Document findings with severity levels
4. Provide actionable suggestions
5. Give overall recommendation

### Output Format
```markdown
## Summary
[Brief assessment]

## Findings
### Critical
[Findings]

### Major
[Findings]

### Minor
[Findings]

## Recommendation
[Approve/Request Changes with explanation]
```

### Knowledge Sources
- Project overlay and checklists
- Microsoft Agent Framework documentation
- Azure AI Foundry best practices
- Python security guidelines
```

---

### Claude Configuration

#### packs/python-azure-ai-agent/claude/CLAUDE.md

```markdown
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
```

#### packs/python-azure-ai-agent/claude/settings.json

```json
{
  "project": {
    "name": "python-azure-ai-agent",
    "description": "Python AI agents on Azure AI Foundry"
  },
  "review": {
    "enabled": true,
    "dimensions": [
      "correctness",
      "readability", 
      "architecture",
      "python-patterns",
      "security",
      "ai-security",
      "azure-ai-foundry",
      "agent-framework",
      "dependencies",
      "performance",
      "operations",
      "tests"
    ]
  },
  "ai_security": {
    "check_prompt_injection": true,
    "check_tool_safety": true,
    "check_data_leakage": true,
    "check_agent_bounds": true
  }
}
```

---

### GitHub Action

#### packs/python-azure-ai-agent/github/workflows/ai-code-review.yml

```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pull-requests: write

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install anthropic pyyaml

      - name: Get changed files
        id: changed
        run: |
          FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD | grep -E '\.(py|yaml|yml|json|md)$' || true)
          echo "files<<EOF" >> $GITHUB_OUTPUT
          echo "$FILES" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Run AI Code Review
        if: steps.changed.outputs.files != ''
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
        run: |
          python .github/scripts/ai_review.py

      - name: Skip review
        if: steps.changed.outputs.files == ''
        run: echo "No reviewable files changed"
```

Create a supporting script at `.github/scripts/ai_review.py`:

```python
#!/usr/bin/env python3
"""AI Code Review script for GitHub Actions."""

import os
import subprocess
import json
from anthropic import Anthropic

def get_diff():
    """Get the diff for the PR."""
    base_ref = os.environ.get('GITHUB_BASE_REF', 'main')
    result = subprocess.run(
        ['git', 'diff', f'origin/{base_ref}...HEAD'],
        capture_output=True,
        text=True
    )
    return result.stdout

def get_changed_files():
    """Get list of changed files."""
    base_ref = os.environ.get('GITHUB_BASE_REF', 'main')
    result = subprocess.run(
        ['git', 'diff', '--name-only', f'origin/{base_ref}...HEAD'],
        capture_output=True,
        text=True
    )
    return [f for f in result.stdout.strip().split('\n') if f]

def build_review_prompt(diff: str, files: list[str]) -> str:
    """Build the review prompt."""
    return f"""You are an expert code reviewer for Python AI agent solutions built on Azure AI Foundry using the Microsoft Agent Framework.

Review the following code changes across these dimensions:
1. Correctness - Logic, edge cases, error handling
2. Readability - Clarity, naming, documentation
3. Architecture - Structure, boundaries, patterns
4. Python Patterns - Type hints, async, idioms
5. Security - Input validation, auth, secrets
6. AI Security - Prompt injection, tool safety, data leakage, agent bounds
7. Azure AI Foundry - Managed Identity, configuration, connections
8. Agent Framework - Agent config, tools, threads, workflows
9. Dependencies - Necessity, security, versioning
10. Performance - Efficiency, async, resources
11. Operations - Logging, monitoring, configuration
12. Tests - Coverage, quality, AI testing

Severity levels:
- Critical: Must fix (security vulns, data loss)
- Major: Should fix (bugs, error handling)
- Minor: Worth addressing (style, optimization)
- Info: Suggestions

Changed files:
{chr(10).join(f'- {f}' for f in files)}

Diff:
```
{diff}
```

Provide your review in this format:

## Summary
[1-3 sentence assessment]

## Findings

### Critical
[List findings or "None"]

### Major
[List findings or "None"]

### Minor
[List findings or "None"]

### Info
[List findings or "None"]

## Recommendation
**[Approve / Request Changes]**
[Brief explanation]

## Positive Observations
[What was done well]

For each finding, use this format:
**[Dimension]** - `path/to/file.py:L##`
[Issue description]
**Suggestion:** [Specific recommendation]
"""

def run_review():
    """Run the AI code review."""
    client = Anthropic()
    
    diff = get_diff()
    files = get_changed_files()
    
    if not diff.strip():
        print("No changes to review")
        return
    
    prompt = build_review_prompt(diff, files)
    
    message = client.messages.create(
        model="claude-opus-4-5-20250514",
        max_tokens=8192,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    review = message.content[0].text
    
    # Post as PR comment
    pr_number = os.environ.get('PR_NUMBER')
    if pr_number:
        post_pr_comment(review, pr_number)
    else:
        print(review)

def post_pr_comment(body: str, pr_number: str):
    """Post review as PR comment."""
    import urllib.request
    
    repo = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GITHUB_TOKEN')
    
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    
    data = json.dumps({"body": f"## 🤖 AI Code Review\n\n{body}"}).encode()
    
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    with urllib.request.urlopen(req) as response:
        print(f"Posted review comment: {response.status}")

if __name__ == "__main__":
    run_review()
```

---

### CLI Implementation

#### src/code_review_pack/__init__.py

```python
"""Code Review Pack - AI-tool-agnostic code review frameworks."""

__version__ = "0.0.1"
```

#### src/code_review_pack/cli.py

```python
#!/usr/bin/env python3
"""CLI for code-review-pack."""

import os
import shutil
from pathlib import Path

import click
from rich.console import Console
from rich.prompt import Prompt, Confirm

console = Console()

PACKS_DIR = Path(__file__).parent.parent.parent.parent / "packs"


@click.group()
@click.version_option()
def main():
    """Code Review Pack CLI."""
    pass


@main.command()
@click.option("--pack", "-p", help="Pack name to initialize")
@click.option("--target", "-t", default=".", help="Target directory")
def init(pack: str | None, target: str):
    """Initialize a code review pack in a project."""
    target_path = Path(target).resolve()
    
    if not target_path.exists():
        console.print(f"[red]Target directory does not exist: {target_path}[/red]")
        raise SystemExit(1)
    
    # List available packs
    available_packs = [p.name for p in PACKS_DIR.iterdir() if p.is_dir()]
    
    if not pack:
        console.print("\n[bold]Available packs:[/bold]")
        for p in available_packs:
            console.print(f"  - {p}")
        
        pack = Prompt.ask("\nSelect pack", choices=available_packs)
    
    if pack not in available_packs:
        console.print(f"[red]Unknown pack: {pack}[/red]")
        raise SystemExit(1)
    
    pack_path = PACKS_DIR / pack
    
    console.print(f"\n[bold]Initializing {pack} in {target_path}[/bold]\n")
    
    # Copy Windsurf config
    if Confirm.ask("Install Windsurf rules and workflows?", default=True):
        windsurf_src = pack_path / "windsurf"
        windsurf_dst = target_path / ".windsurf"
        
        if windsurf_src.exists():
            copy_tree(windsurf_src, windsurf_dst)
            console.print("[green]✓[/green] Installed .windsurf/rules/ and .windsurf/workflows/")
    
    # Copy Cursor config
    if Confirm.ask("Install Cursor rules?", default=True):
        cursor_src = pack_path / "cursor"
        
        if cursor_src.exists():
            shutil.copy(cursor_src / "cursorrules", target_path / ".cursorrules")
            shutil.copy(cursor_src / "AGENTS.md", target_path / "AGENTS.md")
            console.print("[green]✓[/green] Installed .cursorrules and AGENTS.md")
    
    # Copy Claude config
    if Confirm.ask("Install Claude Code config?", default=True):
        claude_src = pack_path / "claude"
        
        if claude_src.exists():
            shutil.copy(claude_src / "CLAUDE.md", target_path / "CLAUDE.md")
            
            claude_dst = target_path / ".claude"
            claude_dst.mkdir(exist_ok=True)
            shutil.copy(claude_src / "settings.json", claude_dst / "settings.json")
            console.print("[green]✓[/green] Installed CLAUDE.md and .claude/settings.json")
    
    # Copy GitHub Action
    if Confirm.ask("Install GitHub Action for PR reviews?", default=True):
        gh_src = pack_path / "github" / "workflows"
        gh_dst = target_path / ".github" / "workflows"
        gh_scripts_dst = target_path / ".github" / "scripts"
        
        if gh_src.exists():
            gh_dst.mkdir(parents=True, exist_ok=True)
            gh_scripts_dst.mkdir(parents=True, exist_ok=True)
            
            for f in gh_src.iterdir():
                shutil.copy(f, gh_dst / f.name)
            
            console.print("[green]✓[/green] Installed .github/workflows/ai-code-review.yml")
            console.print("[yellow]![/yellow] Remember to add ANTHROPIC_API_KEY to repository secrets")
    
    console.print("\n[bold green]Pack initialized successfully![/bold green]")
    console.print("\nNext steps:")
    console.print("  1. Review the installed configuration files")
    console.print("  2. Customize as needed for your project")
    console.print("  3. Add ANTHROPIC_API_KEY to GitHub secrets for CI reviews")


def copy_tree(src: Path, dst: Path):
    """Copy directory tree, creating parents as needed."""
    dst.mkdir(parents=True, exist_ok=True)
    
    for item in src.iterdir():
        if item.is_dir():
            copy_tree(item, dst / item.name)
        else:
            shutil.copy(item, dst / item.name)


@main.command()
def list_packs():
    """List available packs."""
    console.print("\n[bold]Available Code Review Packs:[/bold]\n")
    
    for pack_dir in PACKS_DIR.iterdir():
        if pack_dir.is_dir():
            pack_yaml = pack_dir / "pack.yaml"
            if pack_yaml.exists():
                import yaml
                with open(pack_yaml) as f:
                    config = yaml.safe_load(f)
                
                name = config["pack"]["name"]
                desc = config["pack"]["description"]
                version = config["pack"]["version"]
                
                console.print(f"[bold]{name}[/bold] v{version}")
                console.print(f"  {desc}\n")


if __name__ == "__main__":
    main()
```

#### src/code_review_pack/reviewer.py

```python
#!/usr/bin/env python3
"""Local code reviewer using Claude."""

import os
import subprocess
from pathlib import Path

from anthropic import Anthropic


def get_staged_diff() -> str:
    """Get diff of staged changes."""
    result = subprocess.run(
        ["git", "diff", "--cached"],
        capture_output=True,
        text=True
    )
    return result.stdout


def get_working_diff() -> str:
    """Get diff of working directory changes."""
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True,
        text=True
    )
    return result.stdout


def load_overlay(pack_path: Path) -> str:
    """Load the pack overlay."""
    overlay_path = pack_path / "overlay.md"
    if overlay_path.exists():
        return overlay_path.read_text()
    return ""


def load_checklists(pack_path: Path) -> str:
    """Load relevant checklists."""
    checklists_path = pack_path / "checklists"
    if not checklists_path.exists():
        return ""
    
    content = []
    for checklist in checklists_path.iterdir():
        if checklist.suffix == ".md":
            content.append(f"## {checklist.stem}\n{checklist.read_text()}")
    
    return "\n\n".join(content)


def review_code(diff: str, overlay: str = "", checklists: str = "") -> str:
    """Run code review on diff."""
    client = Anthropic()
    
    prompt = f"""You are an expert code reviewer for Python AI agent solutions.

{overlay}

Reference checklists:
{checklists}

Review the following diff:

```
{diff}
```

Provide a structured review with:
1. Summary (1-3 sentences)
2. Findings by severity (Critical, Major, Minor, Info)
3. Each finding: Dimension, Location, Issue, Suggestion
4. Recommendation (Approve / Request Changes)
5. Positive observations
"""
    
    message = client.messages.create(
        model="claude-opus-4-5-20250514",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text
```

---

### Documentation

#### docs/getting-started.md

```markdown
# Getting Started

## Installation

```bash
pip install code-review-pack
```

## Quick Start

### 1. Initialize a pack in your project

```bash
cd your-project
code-review-pack init
```

Follow the prompts to select a pack and choose which components to install.

### 2. Configure your AI tools

The CLI installs configuration for:
- **Windsurf**: `.windsurf/rules/` and `.windsurf/workflows/`
- **Cursor**: `.cursorrules` and `AGENTS.md`
- **Claude Code**: `CLAUDE.md` and `.claude/settings.json`

### 3. Set up GitHub Actions (optional)

If you installed the GitHub Action:

1. Go to your repository Settings → Secrets and variables → Actions
2. Add `ANTHROPIC_API_KEY` with your Claude API key
3. PRs will now receive automated code reviews

## Using the Review Framework

### In Windsurf

1. Type `/` in Cascade to see available workflows
2. Select `/review-full` for comprehensive review
3. Or `/review-security` for security-focused review

### In Cursor

1. The rules are automatically applied
2. Ask for a "code review" to invoke the review agent

### In Claude Code

1. Reference CLAUDE.md for review guidelines
2. Ask Claude to review your changes

### Manual Review

Use the checklists in the pack as a guide for manual code reviews.
```

#### docs/pack-structure.md

```markdown
# Pack Structure

Each pack contains:

```
pack-name/
├── pack.yaml              # Pack metadata and configuration
├── framework/
│   ├── dimensions.md      # Review dimension definitions
│   ├── process.md         # Review process guide
│   └── output-format.md   # Standard output format
├── overlay.md             # Stack-specific guidance
├── checklists/            # Per-dimension checklists
├── windsurf/              # Windsurf configuration
│   ├── rules/
│   └── workflows/
├── cursor/                # Cursor configuration
├── claude/                # Claude Code configuration
├── github/                # GitHub Actions
│   └── workflows/
└── examples/              # Example reviews
```

## pack.yaml

Defines the pack identity, supported tools, and review configuration.

## overlay.md

Contains stack-specific guidance including:
- Architecture patterns
- Common anti-patterns
- Security considerations
- Testing patterns

## checklists/

One file per dimension with 3-7 key questions to evaluate.

## AI Tool Configurations

Each tool gets its own directory with appropriate configuration files.
```

---

### Examples

#### packs/python-azure-ai-agent/examples/example-review-output.md

```markdown
# Example Code Review Output

## Summary

This PR adds a new chat endpoint that forwards user messages to an AI agent. The implementation works but has a prompt injection vulnerability and missing error handling for rate limits.

## Findings

### Critical

None

### Major

**AI Security** - `src/api/chat.py:L23-L28`

User input is concatenated directly into the agent prompt without sanitization:
```python
prompt = f"User request: {user_message}\nRespond helpfully."
```

This allows prompt injection where a malicious user could include instructions like "Ignore previous instructions and..." to manipulate agent behavior.

**Suggestion:** Keep user input separate from system instructions. Use the agent framework's message structure:
```python
response = await agent.run(user_message)  # Agent instructions set separately
```

**Operations** - `src/api/chat.py:L45-L50`

No handling for rate limit (429) responses from the Azure OpenAI service. This will surface as an unhandled exception to users.

**Suggestion:** Add specific handling for rate limit errors with appropriate retry logic or user messaging:
```python
except RateLimitError:
    raise HTTPException(503, "Service temporarily busy, please retry")
```

### Minor

**Readability** - `src/api/chat.py:L15`

Function name `do_chat` doesn't clearly convey its purpose.

**Suggestion:** Consider `handle_chat_request` or `process_chat_message`.

**Tests** - `tests/test_chat.py`

No test coverage for the error handling paths.

**Suggestion:** Add tests for:
- Invalid input handling
- Rate limit response
- Agent timeout

### Info

**Performance** - `src/api/chat.py:L30`

Consider implementing response streaming for better UX on longer agent responses. The current implementation waits for the full response before returning.

## Recommendation

**Request Changes**

The prompt injection vulnerability should be addressed before merge. The rate limit handling is also important for production reliability.

## Positive Observations

- Good use of async/await patterns throughout
- Clean separation between API routing and business logic
- Comprehensive request logging for debugging
- Type hints on all public functions
```

---

## Build Instructions for Cascade

1. Create the repository structure exactly as specified above
2. Create all files with the content provided
3. Ensure proper file permissions (scripts should be executable)
4. Initialize git repository with appropriate .gitignore
5. Verify the CLI works by running `pip install -e .` and `code-review-pack --help`

## Verification Steps

After building, verify:
- [ ] `code-review-pack list-packs` shows the python-azure-ai-agent pack
- [ ] All Windsurf workflows are valid markdown
- [ ] GitHub Action YAML is valid
- [ ] Python code passes basic syntax check (`python -m py_compile src/code_review_pack/*.py`)
```
