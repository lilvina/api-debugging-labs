import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

DATABASE = "data/app.db"

@app.route("/users", methods=["GET"])
def get_users():
    #BUG: The data directory and database may not exist before this connection/query runs
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    users = cursor.fetchall()
    conn.close()

    return jsonify({
        "users": [
            {"id": user[0], "name": user[1]}
            for user in users
        ]
    })

if __name__=="__main__":
    app.run(debug=True, port=5006)