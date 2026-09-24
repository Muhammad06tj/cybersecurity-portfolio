import string
user_input = input("Вводите свой пароль следую критериям: ")
symbols = len(user_input)
score = 0
if symbols >= 8:
    score += 1
if any(char in string.ascii_uppercase for char in user_input):
    score += 1
if any(char in string.ascii_lowercase for char in user_input):
    score += 1
if any(char in string.digits for char in user_input):
    score += 1
if any(char in string.punctuation for char in user_input):
    score += 1
if score == 1 or score == 2:
    print("Пароль слабый")
if score == 3 or score == 4:
    print("Пароль средний")
if score == 5:
    print("Пароль надежный")
    
