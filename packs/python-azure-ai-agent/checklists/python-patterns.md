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
