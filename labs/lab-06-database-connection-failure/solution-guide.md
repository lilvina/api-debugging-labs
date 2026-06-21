# Solution Guide

## Root cause

The app assumes the database file, folder and table already exist. If they do not exist, the connection or query fails.

## Fix

Create the data directory and initialize the database before the app starts.

```python3
import os
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
DATABASE = "data/app.db"

def init_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany(
            "INSERT INTO users (name) VALUES (?)",
            [("Amina",), ("Jordan",), ("Kai",)]
        )

    conn.commit()
    conn.close()

init_db()
```

## Test again

```bash
curl http://localhost:5006/users
```

## Expected response

```json
{
    "users": [
        {"id": 1, "name": "Amina"},
        {"id": 2, "name": "Jordan"},
        {"id": 3, "name": "Kai"}
    ]
}
```

## Extension

Add a `/health` endpoint that checks whether the database connection is working.
