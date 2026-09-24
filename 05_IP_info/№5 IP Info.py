import requests
def ip_lookup(ip):
    response = requests.get("http://ip-api.com/json/" + ip)
    data = response.json()
    print(data["country"])
    print(data["city"])
    print(data["isp"])
users_ip = input("Vvedite svoy ip: ")
finder = ip_lookup(users_ip)
