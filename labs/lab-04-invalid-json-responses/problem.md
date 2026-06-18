# Lab 4: Invalid JSON Responses

## Scenario

A frontend app calls `/products` and tries to parse the response as JSON. The request succeeds but the JSON parsing is failing.

## Your task

Fix the API so it returns valid JSON with the correct content type.

## Run the app

```bash
python3 app.py
```

## Reproduce the issue

```bash
curl -i http://localhost:5004/products
```

## Expected behavior

The API should return valid JSON.

## Actual behavior

The API returns a string that looks like JSON but is not valid JSON.
