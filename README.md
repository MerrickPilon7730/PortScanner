# Port Scanner Using psutil and Nmap

This project provides a script to list open network ports and their corresponding services on a local machine using two different methods:
1. **psutil** - A Python library that provides an interface for retrieving information on running processes and system utilization.
2. **Nmap** - A powerful network scanning tool to discover hosts and services on a computer network.

## Features:
- List open network ports along with the corresponding processes using **psutil**.
- List open network ports and the associated services using **Nmap**.
- Outputs port-service mappings from both methods to the console.

## Requirements:
- **Python 3.x** installed on your machine.
- **psutil** Python library to interact with system processes and network connections.
- **Nmap** tool installed on your machine.
- **Nmap executable path** (adjust the path in the script based on your system).

### Installation:
1. **Install Python**:  
   Download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Install psutil**:  
   Install the `psutil` library using pip:
   ```bash
   pip install psutil

3. **Install Nmap**:

    You should also install `Nmap` if you haven't already. You can download it from [here](https://nmap.org/download.html) or use a package manager depending on your operating system.
4. **Set Nmap Executable Path**:
    
    Make sure you set the path to your Nmap executable in the script correctly:

    ```python
    nm.executable = r"A:\Nmap\nmap.exe"  # Change A:\Nmap\nmap.exe to the correct path where nmap.exe is located on your system.
### Script Overview

The script performs the following tasks:

- **psutil Network Connections**: It lists network connections that are in specific states (ESTABLISHED, TIME_WAIT, SYN_RECV, FIN_WAIT1). For each connection, it fetches the associated process name using the process ID (PID).

- **Nmap Port Scanning**: It performs a full port scan (`-p-`) on the localhost (`127.0.0.1`) to discover open ports and identify the services running on those ports using Nmap's service detection (`-sV`).

### Output Format

The script will print the following information:

- **Ports and their corresponding services (using psutil)**: This lists the ports that have active connections and the associated services (processes).

- **Ports and their corresponding services (using Nmap)**: This lists all open ports detected on the local machine and the services detected by Nmap.

### Script Structure

### `list_ports_with_services_psutil`

This function uses `psutil` to list all the network connections that are in specific states (ESTABLISHED, TIME_WAIT, SYN_RECV, FIN_WAIT1). For each connection, it attempts to get the associated process and its name.

### `list_ports_with_services_nmap`

This function uses `nmap` to scan the localhost (`127.0.0.1`) for open ports and identifies the services running on those ports using Nmap's `-sV` argument.

### Notes

- `psutil` will list connections that are in specific states (e.g., ESTABLISHED), which means it may not show all ports that are open.
- `Nmap` will show all open ports on the machine. The `-p-` option scans all ports (1-65535) and `-sV` attempts to determine the version of the service running on each port.
- Both `psutil` and `Nmap` might show slightly different results, especially when it comes to dynamic ports or services that are not actively used.

### Troubleshooting

- **Nmap not working**: Ensure that the path to `nmap.exe` is correctly set in the script and that `Nmap` is properly installed. You can verify if `nmap` is installed by running `nmap` from the command line.
  
- **Permission errors**: Make sure you have the necessary permissions to access network connections and the processes associated with them. Running the script as an administrator may be required on some systems.

