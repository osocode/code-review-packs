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
