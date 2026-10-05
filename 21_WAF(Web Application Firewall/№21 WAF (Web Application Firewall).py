from flask import Flask, request
app = Flask(__name__)
blocked_patterns = ["<script>", "SELECT", "DROP TABLE", "../"]
@app.route('/')
def check_requests():
    user_input = request.args.get('input', '')
    for blocked_pattern in blocked_patterns:
        if blocked_pattern in user_input:
            return "BLOCKED"
    return "OK"
if __name__ == '__main__':
    app.run(debug=True)
