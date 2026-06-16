from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEY = "dev-secret-key"

@app.route("/profile", methods=["GET"])
def get_profile():
    auth_header = request.headers.get("Authorization")

    #BUG: This bug checks for the raw API key, but the client sends "Bearer <key>".
    if auth_header != API_KEY:
        return jsonify({"error": "Unauthorized. Missing or invalid API key."}), 401
    return jsonify({
        "id": 1,
        "name": "API Learner",
        "role": "Developer"
    })

if __name__=="__main__":
    app.run(debug=True, port=5001)