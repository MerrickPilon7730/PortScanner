import psutil
import nmap

nm = nmap.PortScanner()
nm.executable = r"A:\Nmap\nmap.exe"  # Adjust if needed


# Function to list ports and services using psutil
def list_ports_with_services_psutil():
    connections = psutil.net_connections(kind='inet')
    ports_with_services = []

    for conn in connections:
        if conn.status in ['ESTABLISHED', 'TIME_WAIT', 'SYN_RECV', 'FIN_WAIT1']:
            pid = conn.pid
            try:
                process = psutil.Process(pid)
                process_name = process.name()
                ports_with_services.append((conn.laddr.port, process_name))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                ports_with_services.append((conn.laddr.port, "Unknown/Access Denied"))

    ports_with_services = sorted(ports_with_services, key=lambda x: x[0])
    return ports_with_services


# Function to list services for open ports using Nmap
def list_ports_with_services_nmap():
    nm.scan(hosts='127.0.0.1', arguments='-p-')

    ports_with_services = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                service = nm[host][proto][port].get('name', 'Unknown Service')
                ports_with_services.append((port, service))

    ports_with_services = sorted(ports_with_services, key=lambda x: x[0])
    return ports_with_services


# Print out the ports with their corresponding services (psutil)
print("Ports and their corresponding services (using psutil):")
ports_with_services_psutil = list_ports_with_services_psutil()
for port, service in ports_with_services_psutil:
    print(f"Port: {port}, Service: {service}")

# Print out the ports with their corresponding services (using nmap)
print("\nPorts and their corresponding services (using Nmap):")
ports_with_services_nmap = list_ports_with_services_nmap()
for port, service in ports_with_services_nmap:
    print(f"Port: {port}, Service: {service}")
