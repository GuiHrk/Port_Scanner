import socket 
from concurrent.futures import ThreadPoolExecutor

socket.setdefaulttimeout(1)


def scan_port(host, porta, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:
       result = sock.connect_ex((host, porta))

       if result == 0:
          return porta, "OPEN"
       else:
        return porta, "CLOSED"
    
    except socket.timeout:
         return porta, "FILTERED"

    except Exception as e:
            return porta, f"ERROR: ({e})"

    finally:
         sock.close()

def grab_banner(host,porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host,porta))
        banner = sock.recv(1024)
        sock.close()
        return banner.decode(errors="ignore").strip()
    except:
         return None


def main():
   host = "scanme.nmap.org"
   start_port = 1
   end_port = 1024

   print(f"Escanenando{host} de portas {start_port} a {end_port}")

   with ThreadPoolExecutor(max_workers=100) as executor:
      futures = []
      for port in range(start_port, end_port +1):
          futures.append(executor.submit(scan_port, host, port))

      for future in futures:
          porta, status = future.result()
          if status == "OPEN":
             banner = grab_banner(host, porta)
             if banner:
              print(f"[+] Porta {porta} OPEN | {banner} ")
             else:  
               print(f"[+] Porta {porta} OPEN | Banner não identificado")

if __name__ == "__main__":
   main()