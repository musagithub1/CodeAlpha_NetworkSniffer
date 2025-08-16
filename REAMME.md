# Network Packet Sniffer 🔍

**CodeAlpha Cybersecurity Internship - Task 1**

A comprehensive Python-based network packet sniffer that captures and analyzes network traffic in real-time. This tool helps understand network protocols, data flow, and packet structure for educational and security analysis purposes.

## 🎯 Features

- **Multi-Protocol Support**: Analyzes Ethernet, IP, TCP, UDP, ICMP, ARP, and DNS packets
- **Real-time Analysis**: Captures and displays packet information instantly
- **Detailed Information**: Shows source/destination IPs, ports, protocols, and payloads
- **Service Recognition**: Identifies common services (HTTP, HTTPS, SSH, DNS, etc.)
- **Flexible Filtering**: Uses Berkeley Packet Filter (BPF) syntax for targeted capture
- **Data Export**: Save captured packets to JSON format for later analysis
- **User-friendly Interface**: Clean, organized output with emojis and formatting

## 🛠️ Requirements

- Python 3.6+
- Scapy library
- Root/Administrator privileges (required for packet capture)
- Network interface access

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/musagithub1/CodeAlpha_NetworkSniffer.git
cd CodeAlpha_NetworkSniffer
```

2. **Install dependencies:**
```bash
make install
# or manually:
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Usage
```bash
# Capture all packets (requires sudo)
sudo python3 packet_sniffer.py

# Capture specific number of packets
sudo python3 packet_sniffer.py -c 10

# Apply filter for specific traffic
sudo python3 packet_sniffer.py -f "tcp port 80"
```

### Advanced Usage
```bash
# Capture HTTP traffic and save to file
sudo python3 packet_sniffer.py -f "tcp port 80" --save

# Capture on specific interface with timeout
sudo python3 packet_sniffer.py -i eth0 --timeout 30

# Capture DNS queries
sudo python3 packet_sniffer.py -f "port 53"

# Capture packets from specific host
sudo python3 packet_sniffer.py -f "host google.com"
```

### Using Makefile Commands
```bash
make install          # Install dependencies
make run             # Run with default settings
make run-count       # Run with packet count limit
make run-filter      # Run with HTTP filter
make clean           # Clean temporary files
```

## 📋 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `-c, --count` | Number of packets to capture (0 = infinite) | `-c 50` |
| `-f, --filter` | BPF filter string | `-f "tcp port 443"` |
| `--save` | Save packets to JSON file | `--save` |
| `-i, --interface` | Network interface to use | `-i eth0` |
| `--timeout` | Stop after specified seconds | `--timeout 60` |

## 🔍 Supported Protocols

- **Ethernet**: MAC addresses and frame types
- **IP**: Source/destination IPs, protocol identification, TTL
- **TCP**: Port numbers, flags, sequence numbers, payloads
- **UDP**: Port numbers, length, payloads
- **ICMP**: Type and code analysis
- **ARP**: Address resolution requests/replies
- **DNS**: Query and response analysis

## 📊 Sample Output

```
🚀 Enhanced Network Packet Sniffer
📡 CodeAlpha Cybersecurity Internship Project
==================================================

============================================================
Packet #1 - 2024-01-15 14:30:25
============================================================
🔗 Ethernet Frame:
   Source MAC:      aa:bb:cc:dd:ee:ff
   Destination MAC: 11:22:33:44:55:66
   Type:           0x800

🌐 IP Packet:
   Source IP:      192.168.1.100
   Destination IP: 8.8.8.8
   Protocol:       UDP
   TTL:           64
   Total Length:   76 bytes

📦 UDP Datagram:
   Source Port:    12345 (12345)
   Dest Port:      53 (DNS)
   Length:         56 bytes
   DNS Query:      Query for www.google.com
============================================================
```

## 🔐 Security Considerations

- **Ethical Use Only**: This tool is for educational and authorized security testing
- **Privacy Respect**: Only capture traffic on networks you own or have permission to monitor
- **Legal Compliance**: Ensure compliance with local laws and regulations
- **Responsible Disclosure**: Report any discovered vulnerabilities responsibly

## 📁 Project Structure

```
CodeAlpha_NetworkSniffer/
├── packet_sniffer.py      # Main sniffer application
├── requirements.txt       # Python dependencies
├── Makefile              # Build and run commands
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── captured_packets.json # Generated output file (when using --save)
```

## 🎓 Learning Objectives

This project demonstrates understanding of:

1. **Network Protocols**: TCP/IP stack, Ethernet, ARP
2. **Packet Analysis**: Header structure, payload examination
3. **Network Security**: Traffic monitoring, intrusion detection basics
4. **Python Programming**: Scapy library usage, argument parsing
5. **System Programming**: Low-level network access, packet capture

## 🤝 Contributing

This is an internship project for CodeAlpha. For educational improvements or bug fixes:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is created for educational purposes as part of the CodeAlpha Cybersecurity Internship program.

## 👨‍💻 Author

**[Your Name]**
- CodeAlpha Cybersecurity Intern
- GitHub: [@musagithub1](https://github.com/musagithub1)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/mussa-khan-49b784375/)

## 🙏 Acknowledgments

- **CodeAlpha** for the internship opportunity
- **Scapy** developers for the excellent packet manipulation library
- **Python Community** for comprehensive networking tools

---

**⚠️ Disclaimer**: This tool is intended for educational and authorized security testing purposes only. Users are responsible for ensuring compliance with applicable laws and obtaining proper authorization before using this tool on any network.
