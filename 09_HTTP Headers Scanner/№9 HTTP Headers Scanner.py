import requests
def get_headers(url):
    response = requests.get(url)
    return response.headers
def check_security_headers(headers):
    security_headers = ['X-Frame-Options', 'X-Content-Type-Options', 'Strict-Transport-Security']
    for header in security_headers:
        if header in headers:
            print(f"[+] Present: {header}")
        else:
            print(f"[-] Missing: {header}")

target_url = "https://google.com"
site_headers = get_headers(target_url)
check_security_headers(site_headers)
