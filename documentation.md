# Packet Sniffer Documentation

## Introduction
This Python program is a simple network packet sniffer that captures and analyzes network traffic. It uses the `scapy` library for packet manipulation and provides insights into the structure and content of captured packets, including source/destination IPs, protocols, and payloads.

## Features
- Captures network packets in real-time.
- Parses Ethernet, IP, TCP, UDP, ICMP, and ARP layers.
- Displays source and destination MAC addresses for Ethernet frames.
- Displays source and destination IP addresses and protocol names for IP packets.
- Extracts and displays source/destination ports and flags for TCP packets.
- Extracts and displays source/destination ports for UDP packets.
- Displays ICMP type and code for ICMP packets.
- Displays ARP operation, sender IP, and target IP for ARP packets.
- Attempts to decode payloads as UTF-8, falling back to hexadecimal representation if decoding fails.
- Command-line arguments for specifying the number of packets to capture and applying BPF filters.

## Requirements
- Python 3.x
- `scapy` library
- `libpcap-dev` (or equivalent for your OS) for packet filtering functionality.

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install `scapy` using pip:
   ```bash
   pip install scapy
   ```
3. Install `libpcap-dev` (or equivalent) on your system. For Debian/Ubuntu-based systems:
   ```bash
   sudo apt-get update
   sudo apt-get install libpcap-dev
   ```
   For Fedora/RHEL-based systems:
   ```bash
   sudo dnf install libpcap-devel
   ```
   For macOS (using Homebrew):
   ```bash
   brew install libpcap
   ```

## Usage
To run the packet sniffer, navigate to the directory containing `packet_sniffer.py` in your terminal and execute the script. Since packet capturing often requires elevated privileges, you might need to run it with `sudo` (on Linux/macOS) or as an administrator (on Windows).

```bash
sudo python3 packet_sniffer.py [options]
```

### Command-line Options
- `-c` or `--count`: Number of packets to capture. If set to `0` (default), it will capture packets indefinitely until manually stopped (e.g., by pressing `Ctrl+C`).
  Example: `sudo python3 packet_sniffer.py -c 10` (captures 10 packets)

- `-f` or `--filter`: A BPF (Berkeley Packet Filter) string to filter captured packets. This allows you to capture only specific types of traffic.
  Example: `sudo python3 packet_sniffer.py -f "tcp port 80"` (captures only TCP traffic on port 80)
  Example: `sudo python3 packet_sniffer.py -f "host 192.168.1.1 and icmp"` (captures ICMP traffic to/from 192.168.1.1)

## Example Output
```
--- New Packet ---
Ethernet - Source MAC: 02:fc:00:00:00:05, Destination MAC: f2:3a:e1:16:8a:54
IP - Source: 169.254.0.21, Destination: 10.238.218.1, Protocol: TCP
  TCP - Source Port: 8330, Destination Port: 49674, Flags: PA
    Payload (Hex): c17e00e94490414b03311085ffca10a417eb76d7bded492982208a227b6a256493b48d269390cc4017d1df6ec4058f33df9be1bdf729684e560c82935164c55a90cdc1a1f2759794feb024b54ac4f997294d2ea274a6428ad173b1f2b1eb1edeb3b91fdd8821be3cdda9ee763c5671e149ea188242231d1a7b1643bb16d916f6240664efd7223225aed34eecb96dbb69d75f079e18896f4abd9be279f8868b85b501b481cd2906bbf913c16a05854d8434d329620f8be382ee70b0b949335c69e8f7f84a2a93c3e322802552d334f05c1d15d852f6975ba00885626ac4db7f11b290222e357266c4fa447cfd00
--- New Packet ---
Ethernet - Source MAC: 02:fc:00:00:00:05, Destination MAC: f2:3a:e1:16:8a:54
IP - Source: 169.254.0.21, Destination: 169.254.169.254, Protocol: TCP
  TCP - Source Port: 58042, Destination Port: 80, Flags: PA
    Payload (UTF-8): PUT /latest/api/token HTTP/1.1
Host: 169.254.169.254
User-Agent: Go-http-client/1.1
Content-Length: 0
X-metadata-token-ttl-seconds: 60
Accept-Encoding: gzip
--- New Packet ---
Ethernet - Source MAC: 06:01:23:45:67:01, Destination MAC: 02:fc:00:00:00:05
IP - Source: 169.254.169.254, Destination: 169.254.0.21, Protocol: TCP
  TCP - Source Port: 80, Destination Port: 58042, Flags: A
    Payload (UTF-8): HTTP/1.1 200 
Server: Firecracker API
Connection: keep-alive
Content-Type: text/plain
Content-Length: 48
0v788GAO91FJq4jELAtzX9FOVCPNITyh3p3KaVUrk+4e+sWh
Packet capture finished.
```

## Understanding the Code
- `PROTOCOL_NAMES`: A dictionary mapping common IP protocol numbers to their names for better readability.
- `get_protocol_name(proto_id)`: A helper function to retrieve the protocol name based on its ID.
- `packet_callback(packet)`: This function is called for every captured packet. It dissects the packet layer by layer:
    - **Ethernet Layer**: Checks for `Ether` in the packet and prints source/destination MAC addresses.
    - **IP Layer**: Checks for `IP` in the packet and prints source/destination IP addresses and the protocol name.
    - **TCP/UDP Layers**: If the packet contains TCP or UDP, it prints source/destination ports and TCP flags. It also attempts to decode the payload.
    - **ICMP Layer**: If the packet contains ICMP, it prints the ICMP type and code.
    - **ARP Layer**: Checks for `ARP` in the packet and prints the operation, sender IP, and target IP.
- `main()`: This function handles command-line arguments using `argparse` to allow users to specify the number of packets to capture (`-c`) and a BPF filter (`-f`).
- `sniff()`: The core `scapy` function used for packet capturing. `prn` specifies the callback function to be executed for each packet, `count` limits the number of packets, and `filter` applies the BPF filter.

## Troubleshooting
- **`PermissionError: [Errno 1] Operation not permitted`**: This error indicates that the script does not have the necessary permissions to capture network traffic. Run the script with `sudo` (on Linux/macOS) or as an administrator (on Windows).
- **`OSError: Cannot find libpcap.so library` or `ImportError: libpcap is not available. Cannot compile filter !`**: This means the `libpcap` development library is not installed on your system. Refer to the "Installation" section for instructions on how to install it.

## Conclusion
This packet sniffer provides a foundational understanding of network traffic analysis using Python and Scapy. It can be extended further to include more advanced features like saving captured packets to a file (PCAP format), real-time visualization, or deeper protocol analysis.

