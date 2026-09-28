import re
email_text = "Срочно! Ваш аккаунт заблокирован. Перейдите по ссылке http://fake-bank.com/login и подтвердите данные. Введите пароль и номер карты."
phishing_words = ["срочно", "заблокирован", "пароль", "карта", "подтвердите"]
score = 0
urls = re.findall(r'http[s]?://\S+', email_text)
print(urls)
for my_email in phishing_words:
    if my_email in email_text.lower():
        score += 1
if "http://" in email_text:
    score += 1
if score >= 2:
    print("Phishing")
else:
    print("Save")
