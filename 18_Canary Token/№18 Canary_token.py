from flask import Flask, request, jsonify
import datetime
app = Flask(__name__)
logs = []
@app.route("/token")
def token_triggered():
    IP = request.remote_addr
    timetamp = datetime.datetime.now()
    browser = request.headers.get("User-Agent")
    logs.append({"ip": IP, "time": timetamp, "browser": browser})
    return jsonify({"status": "logged"})            
    
@app.route("/logs")
def get_logs():
    return jsonify(logs)
if __name__ == "__main__":
    app.run(debug=True)
