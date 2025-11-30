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
