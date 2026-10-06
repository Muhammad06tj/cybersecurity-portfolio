from flask import Flask, request
import time
secret_password = "secret123"
failed_attempts = {}
app = Flask(__name__)
@app.route('/login', methods=['POST'])
def password_cheker():
    username = request.form.get("username")
    password = request.form.get("password")
    real_ip = request.remote_addr
    key = real_ip + ':' + username
    print(key)
    
    if key in failed_attempts and failed_attempts[key]['count'] >= 900:
        if time.time() - failed_attempts[key]['first_time'] > 20:
            del failed_attempts[key]
        else:    
            return "Too many attempts. Try later"
    
    if password == secret_password:
        return "Access granted"
    else:
        if key in failed_attempts:
            failed_attempts[key]['count']+= 1
        else:
            failed_attempts[key]={'count': 1, 'first_time': time.time()}
        print(failed_attempts)
        return "Wrong password"

        
if __name__ == "__main__":
    app.run()
