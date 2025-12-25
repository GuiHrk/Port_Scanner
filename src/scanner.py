import socket 
from concurrent.futures import ThreadPoolExecutor

socket.setdefaulttimeout(1)


def scan_port(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, porta))

    if result == 0:
        print(f"[+] Porta {porta} aberta")
    sock.close()


def main():
   host = "scanme.nmap.org"
   start_port = 1
   end_port = 1024

   print(f"Escanenando{host} de portas {start_port} a {end_port}")

   with ThreadPoolExecutor(max_workers=100) as executor:
      for port in range(start_port, end_port +1):
          executor.submit(scan_port, host, port)


if __name__ == "__main__":
   main()