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

### 13. Documentation
Is documentation kept in sync with code?
- README/docs updated for API changes
- New features documented
- Examples and instructions accurate
- Changelog updated for user-facing changes
