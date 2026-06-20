from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/message", methods=["GET"])
def get_message():
    return jsonify({"message": "Hello fron the API"})

if __name__=="__main__":
    app.run(debug=True, port=5005)