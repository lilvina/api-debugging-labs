# Solution Guide

## Root cause

The Flask app does not send CORS headers. Browser requests from another origin are blocked.

## Fix

Install and use `Flask-Cors`.

```python3
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

## Safer production-style option

Instead of allowing every origin, allow only the frontend origin.

```python3
CORS(app, resources={
    r"/*": {"origins": "http://localhost:3000"}
})
```

## Test again

```bash
curl -i http://localhost:5005/message
```

Look for:

```text
Access-Control-Allow-Origin
```

## Extension

Create a small `index.html` file that uses `fetch()` to call this endpoint from the browser.
