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
