import hashlib
users = {}
def register(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed
def login(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed:
        return True
    else:
        return False
    
username, password = input("Tolko bukvi: "), input("Tolko tsifri: ")
regist = register(username, password)
login_user, login_pass = input("Tolko bukvi: "), input("Tolko tsifri: ")
log = login(login_user, login_pass)
if log == True:
    print("Вход успешен")
else:
    print("Неверный логин или пароль")
    

