import socket 

def scan_ports(host, porta, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host,porta))
        return True 
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

def scan_range (host, inicio, fim):
    print(f"\n Escanenado {host} de {inicio} a {fim} \n")
    portas_abertas = []

    for porta in range(inicio, fim +1):
        if scan_ports(host, porta):
            print(f"[+] Porta {porta} aberta")
            portas_abertas.append(porta)

    print("PORTAS ABERTAS:", portas_abertas)

if __name__ == "__main__":
    scan_range("scanme.nmap.org",1,1024)