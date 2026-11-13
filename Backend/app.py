from flask import Flask, jsonify, request
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status":"ok","project":"ForestWatch AI"})

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    return jsonify({
        "region": data.get("region","Western Ghats"),
        "uncertainty_percent": round(random.uniform(10,28),1),
        "vegetation_change_percent": round(random.uniform(2,14),1),
        "priority_areas": random.randint(5,18),
        "recommendation": "Ground verification required"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)