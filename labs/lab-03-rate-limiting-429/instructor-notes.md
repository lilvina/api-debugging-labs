# Instructor Notes

## Teaching goal

Teach learners that `429` errors are not always client mistakes. The server-side rate limiter can be implemented incorrectly.

## Discussion prompts

- Why do APIs use rate limits?
- What should a helpful `429` response include?
- How can rate limits improve reliability?

## Common learner mistake

Learners may increase the rate limit instead of fixing the expiration logic.

## Production connection

Production systems often use Redis or API gateways for rate limiting instead of in-memory dictionaries.
