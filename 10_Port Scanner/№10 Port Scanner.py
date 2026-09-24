import socket
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    s.close()
    if result == 0:
        return True
    else:
        return False
target_ip = 'scanme.nmap.org'
for port in range(20, 85):
    a = scan_port(target_ip, port)
    if a == True:
        print(f"[+] Port {port} is OPEN")
        
