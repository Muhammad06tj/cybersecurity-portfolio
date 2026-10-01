import email
raw_email = """From: support@fake-bank.com
Subject: Ваш аккаунт заблокирован"""
msg = email.message_from_string(raw_email)
if 'fake' in msg['From']:
    print("Подозрительный отправитель")
if 'заблокирован' in msg['Subject']:
    print("Подозрительная тема")

      
