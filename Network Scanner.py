import nmap

scanner = nmap.PortScanner()
target = "192.168.1.1"  # Replace with authorized target
scanner.scan(target, '1-1024')  # Scan common ports

for host in scanner.all_hosts():
    print(f"Open ports for {host}:")
    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in ports:
            print(f"Port {port}: {scanner[host][proto][port]['state']}")
