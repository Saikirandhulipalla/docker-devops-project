from flask import Flask, jsonify
import os

app = Flask(__name__)

name = os.getenv("NAME", "Guest")

@app.route("/")
def home():
    return f"""
    <h1>🚀 Docker DevOps Project</h1>
    <p>Hello, {name}!</p>
    <p>Your container is running successfully.</p>
    <a href="/api">Check API Status</a>
    """

@app.route("/api")
def api():
    return jsonify({
        "status": "running",
        "user": name,
        "project": "Docker DevOps Project"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

