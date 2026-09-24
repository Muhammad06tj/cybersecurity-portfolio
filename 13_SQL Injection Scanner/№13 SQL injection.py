import requests
def load_payloads(path_file):
    password = []
    with open(path_file, 'r') as scan:
        for weaknees in scan:
            clean = weaknees.strip()
            password.append(clean)
    return password

def scan_url(url, payload):
    target_url = (url + payload)
    r = requests.get(target_url)
    return r

def check_response(response):
    special_words = ["sql syntax", "mysql", "unclosed quotation"]
    for words in special_words:
        if words in response.text :
            return True
        
    return False
payloads = load_payloads(r"C:\Users\Мухаммад\Desktop\Практика\payloads.txt")
print(payloads)
url = "http://testphp.vulnweb.com/listproducts.php?cat="
for i in payloads:
    print(f"Testing: {url + i}")
    scan = scan_url(url, i)
    check = check_response(scan)
    if check == True:
        print(f'[+] Уязвимость найдена:, {i}')
    else:
        print(f'[-] Не уязвимо:, {i}')

    



    
