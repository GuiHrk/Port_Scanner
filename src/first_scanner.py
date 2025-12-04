import socket

host = "scanme.nmap.org"
porta = 99

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

try:
    sock.connect((host, porta))
    print(f"[+] Porta {porta} aberta!")
except socket.timeout:
    print(f"[!] Porta {porta} filtrada (timeout)")
except ConnectionRefusedError:
    print(f"[-] Porta {porta} fechada!")
except Exception as e:
    print(f"[?] Erro desconhecido: {e}")
finally:
    sock.close()