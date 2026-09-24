import jwt
secret = "mysecretkey"
payload = {"user": "muhammad", "role": "admin"}
token = jwt.encode(payload, secret, algorithm="HS256")
print(token)
decoded = jwt.decode(token, secret, algorithms=["HS256"])
print(decoded)
try:
    fake_token = jwt.decode(token, "wrongkey", algorithms=["HS256"])

except:
    print("Invalid token - access denied")
