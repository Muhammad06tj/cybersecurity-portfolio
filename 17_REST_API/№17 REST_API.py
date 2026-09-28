from flask import Flask, jsonify, request
app = Flask(__name__)
API_KEY = "secret123"
@app.route("/users")
def get_users():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"users": ["muhammad", "admin", "guest"]})

if __name__ == "__main__":
    app.run(debug=True)
