from flask import Flask

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    # BUG: This looks like JSON but it is return as plain text and it contains invalid JSON.
    return "{'products': ['keyboard', 'mouse', 'monitor']}"

if __name__=="__main__":
    app.run(debug=True, port=5004)