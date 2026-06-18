# Solution Guide

## Root cause

The app keeps adding request timestamps but never removes old ones. This means the request list grows forever.

## Fix

Filter out old requests before appending the current request.

```python3
requests_by_ip[client_ip] = [
    timestamp for timestamp in requests_by_ip[client_ip]
    if current_time - timestamp < WINDOW_SECONDS
]

requests_by_ip[client_ip].append(current_time)
```

## Improved route

```python3
@app.route("/search", methods=["GET"])
def search():
    client_ip = request.remote_addr
    current_time = time()

    if client_ip not in requests_by_ip:
        requests_by_ip[client_ip] = []

    requests_by_ip[client_ip] = [
        timestamp for timestamp in requests_by_ip[client_ip]
        if current_time - timestamp < WINDOW_SECONDS
    ]

    if len(requests_by_ip[client_ip]) >= RATE_LIMIT:
        return jsonify({"error": "Too many requests. Try again later."}), 429

    requests_by_ip[client_ip].append(current_time)

    return jsonify({"results": ["api", "debugging", "flask"]})
```

## Extension

Return rate limit headers such as:

- `X-RateLimit-Limit`
- `X-RateLimit-Remaining`
- `Retry-After`
