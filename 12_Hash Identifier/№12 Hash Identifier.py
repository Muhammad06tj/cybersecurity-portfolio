def identify_hash(hash_input):
    if hash_input.startswith('$2b$') or hash_input.startswith('$2a$'):
        return('bcrypt')
    elif len(hash_input) == 32:
        return('MD5')
    elif len(hash_input) == 40:
        return('SHA-1')
    elif len(hash_input) == 64:
        return('SHA-256')
    elif len(hash_input) == 128:
        return('SHA-512')
    else:
        return('Unknown')
check_hash = identify_hash(input())
print(check_hash)

    
