# Lab 5: CORS Issues

## Scenario

A frontend running on a different origin tries to call the Flask API. The API works in curl but the browser blocks the request because of a CORS error.

## Your task

Enable CORS so browser-based frontend apps can access the API.

## Run the app

```bash
python3 app.py
```

## Reproduce the API response

```bash
curl -i http://localhost:5005/message
```

## Expected behavior

The API should include CORS headers that allow frontend requests.

## Actual behavior

The API response does not include an `Access-Control-Allow-Origin` header.

## Browser symptom

The browser console may show an error like:

```text
Access to fetch at "http://localhost:5005/message" from origin "http://localhost:3000" has been blocked by CORS policy.
```
