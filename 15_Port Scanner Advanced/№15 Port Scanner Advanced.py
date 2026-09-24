import socket
from concurrent.futures import ThreadPoolExecutor
def scan_port(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    connect = s.connect_ex((host, port))
    if connect == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "unknown"
        print(f"Port {port} is OPEN | Service: {service}")    
    s.close()

host = input("Enter host: ")
start_port = int(input("Start port: "))
end_port = int(input("Enter port: "))
    
with ThreadPoolExecutor(max_workers=100) as executor:
    results = list(executor.map(lambda port: scan_port(port, host), range(start_port, end_port + 1)))
    
