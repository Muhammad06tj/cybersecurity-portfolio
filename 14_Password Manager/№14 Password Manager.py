from cryptography.fernet import Fernet

def load_key():
    with open('key.key', 'rb') as f:
        read_key = f.read()
        return read_key

def save_key(key):
    with open('key.key', 'wb') as q:
        q.write(key)
        
def generate_key():
    kkey = Fernet.generate_key()
    save_key(kkey)

def encrypt_password(password, key):
    f = Fernet(key)
    shifr = f.encrypt(password.encode())
    return shifr

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    shifr = f.decrypt(encrypted_password).decode()
    return shifr

def save_password(site, encrypted_password):
    with open('password.txt', 'a') as w:
        w.write(site + ':' + encrypted_password.decode() + '\n')

def get_password(site, key):
    with open('password.txt', 'r') as t:
        for line in t:
            split = line.split(':')
            if split[0] == site:
                res = decrypt_password(split[1], key)
                return res
        

generate_key()
key = load_key()
shifr = encrypt_password('mypassword123', key)
save = save_password('gmail', shifr)
get = get_password('gmail', key)
print(get)
    
