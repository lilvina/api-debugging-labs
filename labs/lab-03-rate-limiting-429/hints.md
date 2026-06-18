# Hints

## Hint 1

The app stores timestamps for each request. Are old timestamps ever removed?

## Hint 2

A rate limiter needs both a request count and a time window.

## Hint 3

Before counting requests. filter out timestamps older than `WINDOW_SECONDS`.
