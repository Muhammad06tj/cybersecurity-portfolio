def check_url(url):
    danger = 0
    if url.startswith('http://'):
        danger += 1
    domain = url.split('//')[1]
    domain = domain.split('/')[0]
    if domain[0].isdigit():
        danger += 1
    point = url.count('.')
    if point > 3:
        danger += 1
    dwords = ['free', 'winner', 'click', 'hack', 'login', 'secure']    
    for word in dwords:
        if word in url:
            danger += 1
    long = len(url)
    if long > 75:
        danger += 1
    return danger    
ui = input("Вводите подозрительный URL: ")
result = check_url(ui)
if result > 3:
    print("Опасный URL")
elif result > 1:
    print("Подозрительный URL")
else:
    print("Безопасный URL")
