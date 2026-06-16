from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv

#BUG: .env is not loaded before reading the environment variable.
API_KEY = os.getenv("WEATHER_API_KEY")

load_dotenv()

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def get_weather():
    if not API_KEY:
        return jsonify({"error": "Missing WEATHER_API_KEY environment variable."}), 500
    
    return jsonify({
        "city": "Oakland",
        "forecast": "Sunny",
        "api_key_loaded": True
    })

if __name__=="__main__":
    app.run(debug=True, port=5002)