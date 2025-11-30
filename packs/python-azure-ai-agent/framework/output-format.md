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
