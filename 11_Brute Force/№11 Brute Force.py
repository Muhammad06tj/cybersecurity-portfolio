def load_password(file_path):
    password = []
    with open(file_path, 'r') as file:
        for line in file:
            clean = line.strip()
            password.append(clean)
    return password
def login(username, password):
    if username == "admin" and password == "letmein":
        return True
    else:
        return False
loaded_list = load_password(r"C:/Users/Мухаммад/Desktop/Практика/password.txt")
target_user = "admin"
for pass_try in loaded_list:
    check = login(target_user, pass_try)
    if check == True:
        print(f"[+] Пароль найден: {pass_try}")
        break          
    else:
        print(f"[-] Неверный пароль: {pass_try}")

        
            
    
