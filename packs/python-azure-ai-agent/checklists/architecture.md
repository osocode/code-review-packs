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
