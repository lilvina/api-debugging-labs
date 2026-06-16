# Lab 2: Missing Environment Variables

## Scenario

A weather API endpoint depends on a `WEATHER_API_KEY` stored in a `.env` file. The `.env` file exists, but the app still behaves as if the key is missing.

## Your task

Find out why the environment variable is not being loaded correctly.

## Setup

Create a `.env` file in this lab folder:

```bash
WEATHER_API_KEY=fake-weather-key
```

## Run the app

```bash
python3 app.py
```

## Reproduce the issue

```bash
curl http://localhost:5002/weather
```

## Expected behavior

The endpoint should confirm that the API key was loaded.

## Actual behavior

The API returns a missing environment variable error.
