# Lab 6: Database Connection Failure

## Scenario

A `/users` endpoint should read users from a SQLite database. Instead, the app crashes because the database path or table is missing.

## Your task

Fix the database setup so the endpoint can connect to the database and return users.

## Run the app

```bash
python3 app.py
```

## Reproduce the issue

```bash
curl http://localhost:5006/users
```

## Expected behavior

The endpoint should return a list of users.

## Actual behavior

The API may fail with an error related to opening the database file or missing the `users` table.
