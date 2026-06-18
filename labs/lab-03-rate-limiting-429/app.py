from flask import Flask, jsonify, request
from time import time

app = Flask(__name__)

requests_by_ip = {}
RATE_LIMIT = 3
WINDOW_SECONDS = 60

@app.route("/search", methods=["GET"])
def search():
    client_ip = request.remote_addr
    current_time = time()

    if client_ip not in requests_by_ip:
        requests_by_ip[client_ip] = []

    #BUG: Old requests are never removed, so users stay rate-limited forever.
    requests_by_ip[client_ip].append(current_time)

    if len(requests_by_ip[client_ip]) > RATE_LIMIT:
        return jsonify({"error": "Too many requests. Try again later."}), 429
    
    return jsonify({"results": ["api", "debugging", "flask"]})

if __name__=="__main__":
    app.run(debug=True, port=5003)