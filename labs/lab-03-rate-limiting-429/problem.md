# Lab 3: Rate Limiting 429

## Scenario

A search endpoint allows only a few requests per minute. After a few requests, it returns `429 Too Many Requests`.

The issue: even after waiting, the user still appears to be blocked.

## Your task

Fix the rate limiter so old requests expire after the time window.

## Run the app

```bash
python3 app.py
```

## Reproduce the issue

Run this command several times:

```bash
curl http://localhost:5003/search
```

## Expected behavior

After the time window passes, users should be allowed to make requests again.

## Actual behavior

Once the limit is reached, the request count never resets.