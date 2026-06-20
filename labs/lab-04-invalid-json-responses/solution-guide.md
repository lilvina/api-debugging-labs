# Solution Guide

## Root cause

The endpoint returns a plain string instead of a real JSON response. It also uses single quotes, which are not valid JSON syntax.

Broken response:

```python3
return "{'products': ['keyboard', 'mouse', 'monitor']}"
```

## Fix

Use Flask's `jsonify()` helper.

```python3
from flask import Flask, jsonify

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({
        "products": ["keyboard", "mouse", "monitor"]
    })
```

## Test again

```bash
curl -i http://localhost:5004/products
```

## Expected response header

```text
Content-Type: application/json
```

## Extension

Add a frontend `fetch()` example that calls this endpoint and renders the product list.
