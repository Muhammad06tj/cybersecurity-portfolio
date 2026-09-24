import secrets, time

def generate_otp():
    random_numbers = secrets.randbelow(999999)
    created_at = time.time()
    return random_numbers, created_at
otp, code_time  = generate_otp()
print(otp)
print(code_time)
def check_otp(code_time):
    now_time = time.time()
    minus = now_time - code_time
    if minus >= 30:
        print("код истёк")
    else:
        print("код не истек")
time.sleep(31)        
check = check_otp(code_time)        
