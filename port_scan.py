import socket
import threading

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{port}/tcp")
    except Exception:
        pass

def main():
    ip = input("Enter the IP address you want to scan: ")

    threads = []
    for port in range(1, 65536):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nPort scan complete.")

if __name__ == "__main__":
    main()
