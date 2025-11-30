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
