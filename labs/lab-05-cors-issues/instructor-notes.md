# Instructor Notes

## Teaching goal

Help learners distinguish between server errors and browser security errors.

## Discussion prompts

- Why does curl work when the browser fails?
- What is an origin?
- Why should production apps avoid allowing all origins?

## Common learner mistake

Learners may think the API is down because the browser request fails. Show them how to compare browser behavior with curl or Postman.

## Production connection

CORS misconfiguration is common when frontend and backend apps are deployed on separate domains.
