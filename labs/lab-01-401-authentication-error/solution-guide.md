# Solution Guide 

## Root cause

The server expects the `Authorization` header to equal only the raw API key:

```python3 
if auth_header != API_KEY:
```

But the client sends:

```text
Bearer dev-secret-key
```

Those strings do not match so the server always returns `401 Unauthorized`.

## Fix

Update the authentication check to expect the full bearer token format.

```python3
expected_header = f"Bearer {API_KEY}"

if auth_header != expected_header:
    return jsonify({"error": "Unauthorized. Missing or invalid API key."}), 401
```

## Test again

```bash
curl -H "Authorization: Bearer dev-secret-key" http://localhost:5001/profile
```

## Expected response

```json
{
    "id": 1,
    "name": "API Learner",
    "role": "Developer"
}
```

## Extension

Add better error messages for:

- Missing `Authorization` header
- Incorrect token format
- Invalid API key
