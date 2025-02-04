# Simple Port Scanner

## Description
A simple Python-based port scanner that scans specified ports on a given target IP address to detect open services. This script allows scanning a range of ports or individual ports for a target machine.

## Features
- Scan a range of ports (e.g., 1-1024)
- Supports individual ports (e.g., 22, 80, 21)
- Simple and efficient
- Written in Python

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Nelushi04/simple-port-scanner.git
    cd Simple-Port-Scanner
    ```
2. Run the scanner:
    ```bash
    python3 port_scanner.py <target_ip> -p <port_range>
    ```

   Example:
    ```bash
    python3 port_scanner.py 192.168.1.100 -p 22,80,443
    python3 port_scanner.py 192.168.1.100 -p 1-1024
    ```

3. The script will print which ports are open.

## Requirements
- Python 3.x
- No additional dependencies required

## Disclaimer
This tool is intended for educational purposes only. Always have explicit permission before scanning any network or system.
