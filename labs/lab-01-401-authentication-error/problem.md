# Lab 1: 401 Authentication Error

## Scenario

You are working on a profile API that requires an API key. The developer documentation says clients should send the key using an `Authorization` header.

The endpoint keeps returning `401 Unauthorized` even when the client sends the correct key.

## Your task

Debug the authenication logic so a valid request works correctly.

## Run the app

```bash 
python3 app.py
```

## Reproduce the issue

```bash
curl -H "Authorization: Bearer dev-secret-key" http://localhost:5001/profile
```

## Expected behavior

A successful request should return a user profile.

## Actual behavior

The API returns:

```json
{
    "error": "Unauthorized. Missing or invalid API key."
}
```
