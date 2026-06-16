# Solution Guide

## Root cause

The app reads the environment variable before calling `load_dotenv()`.

Broken order:

```python3
API_KEY = os.getenv("WEATHER_API_KEY")
load_dotenv()
```

At the time `os.getenv()` runs, the `.env` values have not been loaded yet.

## Fix

Move `load_dotenv()` above the environment variable lookup.

```python3
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
```

## Test again

```bash
curl http://localhost:5002/weather
```

## Expected response

```json
{
    "api_key_loaded": true,
    "city": "Oakland",
    "forecast": "Sunny"
}
```

## Extension

Add a startup validation function that checks all required environment variables before the server starts.