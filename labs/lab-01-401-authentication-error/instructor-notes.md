# Instructor Notes

## Teaching goal

Help learners understand that authentication bugs are often caused by header formatting issues, not just incorrect credentials.

## Discussion prompts

- What is the difference between authentication and authorization?
- Why do APIs often use the `Bearer` token format?
- How could unclear documentation cause this bug?

## Common learner mistake

Many learners will assume the key itself is wrong instead of checking the full header value. Encourage them to inspect the exact request.

## Production connection

In production APIs, `401` errors often come from missing headers, expired tokens, incorrect token prefixes, or environment mismatch between development and production keys.
