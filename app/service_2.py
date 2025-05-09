from flask import Flask, request
from logger import log_info, generate_alert

app = Flask(__name__)

@app.route("/receive", methods=["POST"])
def receive():
    data = request.get_json()
    log_info(f"Received: {data}")
    
    if not data or "message" not in data:
        generate_alert("InvalidInput", "Missing 'message' field in payload")
        return "Invalid input", 400

    return f"Service B received: {data['message']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
