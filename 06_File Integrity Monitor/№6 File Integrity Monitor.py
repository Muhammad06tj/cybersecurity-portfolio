import hashlib
hashes = {}
def get_hash(filename):
    with open(filename, "rb") as f:
        content = f.read()
        return hashlib.sha256(content).hexdigest()
def save_hash(filename):
    h = get_hash(filename)
    with open("hashes.txt", "w") as f:
        f.write(h)
def check_file(filename):
    current  = get_hash(filename)
    with open("hashes.txt", "r") as f:
        saved = f.read()
        if saved == current:
            return True
        else:
            return False

#work_hash = save_hash("C:/Users/Мухаммад/Desktop/Text Document.txt")
work_hash1 = check_file("C:/Users/Мухаммад/Desktop/Text Document.txt")
print(work_hash1)
        
        
    
    
    
    
