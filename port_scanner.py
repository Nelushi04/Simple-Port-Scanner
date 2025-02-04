import socket
import threading
import argparse

def scan_port(target, port, verbose=False):
    """Scans a specific port on the target and identifies services."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            service = get_service(port)
            print(f"[+] Port {port} is open ({service})")
            return f"Port {port} is open ({service})"
        sock.close()
    except socket.error:
        pass
    return None

def get_service(port):
    """Attempts to identify the service running on a given port."""
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

def scan_ports(target, ports, verbose=False):
    """Scans a range of ports on a target using threading."""
    print(f"Scanning {target}...")
    threads = []
    results = []

    for port in ports:
        thread = threading.Thread(target=lambda p: results.append(scan_port(target, p, verbose)), args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    return [res for res in results if res]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--ports", type=str, default="1-1024", help="Port range to scan (e.g., 20-80)")
    parser.add_argument("-o", "--output", type=str, help="Save results to a file")
    args = parser.parse_args()

    # Parse port range
    start_port, end_port = map(int, args.ports.split("-"))
    ports_to_scan = range(start_port, end_port + 1)

    # Run scan
    scan_results = scan_ports(args.target, ports_to_scan)

    # Save to file if specified
    if args.output:
        with open(args.output, "w") as file:
            file.write("\n".join(scan_results))
        print(f"Results saved to {args.output}")

