# Instructor Notes

## Teaching goal

Help learners understand that a successful `200 OK` response can still be broken if the response body or headers are wrong.

## Discussion prompts

- What makes JSON valid?
- Why does `Content-Type` matter?
- Why might Postman appear to work while browser Javascript fails?

## Common learner mistake

Learners may focus only on status code and miss that the response body is invalid.

## Production connection

Invalid JSON responses can break SDKs, frontend apps, mobile apps, and integrations even when the API status code is `200`.
