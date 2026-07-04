import socket
from IPy import IP
from colorama import init, Fore, Style

init(autoreset=True)




print(Fore.CYAN + r"""
▓▓▓▓   ▓▓▓  ▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓  ▓▓▓   ▓▓▓  ▓   ▓ ▓   ▓ 
▓   ▓ ▓   ▓ ▓   ▓   ▓   ▓     ▓     ▓   ▓ ▓▓  ▓  ▓ ▓  
▓▓▓▓  ▓   ▓ ▓▓▓▓    ▓    ▓▓▓  ▓     ▓▓▓▓▓ ▓ ▓ ▓   ▓   
▓     ▓   ▓ ▓  ▓    ▓       ▓ ▓     ▓   ▓ ▓  ▓▓  ▓ ▓  
▓      ▓▓▓  ▓   ▓   ▓   ▓▓▓▓   ▓▓▓  ▓   ▓ ▓   ▓ ▓   ▓
""")
print(Fore.MAGENTA + "\nCopyright © 2026 Sriram. All Rights Reserved.")


def scan(target):
    conv_ip = checkIp(target)
   
    try:
        for port in range(1,1025):
            scanPort(conv_ip,port)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan Stopped by User.")
        exit()

def checkIp(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)
def scanPort(ipaddr,port):
    
    try: 
        x = socket.socket()
        x.settimeout(0.1)
        x.connect((ipaddr,port))
        print(Fore.GREEN + f"[+] Port {port} is Open")

    except:
        pass

    finally : 
        x.close()

targets = input(Fore.CYAN + "\n[+] Enter Target/s to Scan (Split Multiple targets with ',') : ")

if ',' in targets:
    for ip_addr in targets.split(','):
        scan(ip_addr.strip())
else:
    scan(targets)

print(Fore.BLUE + "\n[✓] Scan Completed.")
