# 🔍 Network Packet Sniffer

<div align="center">

**CodeAlpha Cybersecurity Internship - Task 1**

*A comprehensive Python-based network packet sniffer that captures and analyzes network traffic in real-time*

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

**🎯 Educational • 🔒 Security Analysis • 🌐 Network Protocol Understanding**

---

</div>

## ✨ Overview

This tool helps understand network protocols, data flow, and packet structure for educational and security analysis purposes. Built as part of the CodeAlpha Cybersecurity Internship program, it provides comprehensive packet analysis capabilities with an intuitive interface.

## 🚀 Key Features

<table>
<tr>
<td width="50%">

### 🌐 **Protocol Support**
- **Ethernet** - MAC addresses & frame types
- **IP** - Source/destination IPs, TTL analysis
- **TCP** - Port numbers, flags, sequences
- **UDP** - Port numbers, length, payloads
- **ICMP** - Type and code analysis
- **ARP** - Address resolution monitoring
- **DNS** - Query and response analysis

</td>
<td width="50%">

### ⚡ **Advanced Capabilities**
- **Real-time Analysis** - Instant packet display
- **Service Recognition** - HTTP, HTTPS, SSH, DNS
- **Flexible Filtering** - Berkeley Packet Filter (BPF)
- **Data Export** - JSON format for analysis
- **Detailed Information** - Comprehensive packet data
- **User-friendly Interface** - Clean, organized output

</td>
</tr>
</table>

## 📋 Requirements

<div align="center">

| Requirement | Version | Purpose |
|-------------|---------|---------|
| 🐍 **Python** | 3.6+ | Core runtime |
| 📦 **Scapy** | Latest | Packet manipulation |
| 🔐 **Root Access** | Required | Packet capture |
| 🌐 **Network Interface** | Active | Traffic monitoring |

</div>

## 📦 Quick Start Installation

### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/musagithub1/CodeAlpha_NetworkSniffer.git
cd CodeAlpha_NetworkSniffer
```

### 2️⃣ **Install Dependencies**
```bash
# Using Makefile (recommended)
make install

# Or manually
pip install -r requirements.txt
```

## 🎯 Usage Examples

### **Basic Operations**

```bash
# 🔍 Capture all packets
sudo python3 packet_sniffer.py

# 🎯 Capture specific count
sudo python3 packet_sniffer.py -c 10

# 🔧 Apply traffic filter
sudo python3 packet_sniffer.py -f "tcp port 80"
```

### **Advanced Scenarios**

```bash
# 🌐 HTTP traffic with file save
sudo python3 packet_sniffer.py -f "tcp port 80" --save

# ⚙️ Specific interface with timeout
sudo python3 packet_sniffer.py -i eth0 --timeout 30

# 🔍 DNS queries monitoring
sudo python3 packet_sniffer.py -f "port 53"

# 🎯 Target specific host
sudo python3 packet_sniffer.py -f "host google.com"
```

### **Makefile Commands**

<div align="center">

| Command | Action | Description |
|---------|--------|-------------|
| `make install` | 📦 | Install all dependencies |
| `make run` | ▶️ | Run with default settings |
| `make run-count` | 🔢 | Run with packet limit |
| `make run-filter` | 🔧 | Run with HTTP filter |
| `make clean` | 🧹 | Clean temporary files |

</div>

## ⚙️ Configuration Options

<table>
<tr>
<th width="20%">Option</th>
<th width="40%">Description</th>
<th width="40%">Example Usage</th>
</tr>
<tr>
<td><code>-c, --count</code></td>
<td>Number of packets to capture (0 = infinite)</td>
<td><code>-c 50</code></td>
</tr>
<tr>
<td><code>-f, --filter</code></td>
<td>Berkeley Packet Filter (BPF) string</td>
<td><code>-f "tcp port 443"</code></td>
</tr>
<tr>
<td><code>--save</code></td>
<td>Save captured packets to JSON file</td>
<td><code>--save</code></td>
</tr>
<tr>
<td><code>-i, --interface</code></td>
<td>Specify network interface to monitor</td>
<td><code>-i eth0</code></td>
</tr>
<tr>
<td><code>--timeout</code></td>
<td>Stop capture after specified seconds</td>
<td><code>--timeout 60</code></td>
</tr>
</table>

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

## 🏗️ Project Architecture

```
CodeAlpha_NetworkSniffer/
├── 📄 packet_sniffer.py      # Main application core
├── 📋 requirements.txt       # Python dependencies
├── ⚙️ Makefile              # Build automation
├── 🚫 .gitignore            # Version control rules
├── 📖 README.md             # Project documentation
└── 📊 captured_packets.json # Generated output (--save)
```

## 🎓 Learning Outcomes

<div align="center">

### **Core Concepts Mastered**

</div>

<table>
<tr>
<td width="50%">

#### 🌐 **Network Fundamentals**
- TCP/IP Protocol Stack
- Ethernet Frame Analysis
- Address Resolution Protocol (ARP)
- Network Layer Understanding

#### 🔒 **Security Principles**
- Traffic Monitoring Techniques
- Intrusion Detection Basics
- Network Vulnerability Assessment
- Ethical Security Testing

</td>
<td width="50%">

#### 💻 **Technical Skills**
- Python Network Programming
- Scapy Library Mastery
- Command-Line Interface Design
- System-Level Programming

#### 🔍 **Analysis Capabilities**
- Packet Header Examination
- Protocol Identification
- Payload Content Analysis
- Real-time Data Processing

</td>
</tr>
</table>

## 🔐 Security & Ethics

<div align="center">

### **⚠️ Important Guidelines**

</div>

| Principle | Description |
|-----------|-------------|
| 🎯 **Ethical Use Only** | Tool designed for educational and authorized security testing |
| 🛡️ **Privacy Respect** | Only monitor networks you own or have explicit permission |
| ⚖️ **Legal Compliance** | Ensure adherence to local laws and regulations |
| 🤝 **Responsible Disclosure** | Report discovered vulnerabilities through proper channels |

## 🤝 Contributing

<div align="center">

**This project welcomes educational improvements and bug fixes**

</div>

1. 🍴 **Fork** the repository
2. 🌟 **Create** a feature branch
3. ✨ **Make** your improvements
4. 📤 **Submit** a pull request

## 📄 License

This project is developed for educational purposes as part of the **CodeAlpha Cybersecurity Internship** program.

---

<div align="center">

## 👨‍💻 Author

**Mussa Khan**  
*CodeAlpha Cybersecurity Intern*

[![GitHub](https://img.shields.io/badge/GitHub-musagithub1-black?logo=github)](https://github.com/musagithub1)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/mussa-khan-49b784375/)

---

## 🙏 Acknowledgments

**Special Thanks To:**
- 🌟 **CodeAlpha** - For the incredible internship opportunity
- 🐍 **Scapy Developers** - For the outstanding packet manipulation library  
- 👥 **Python Community** - For comprehensive networking tools and support

---

### ⚠️ **Legal Disclaimer**

*This tool is intended exclusively for educational and authorized security testing purposes. Users assume full responsibility for ensuring compliance with applicable laws and obtaining proper authorization before monitoring any network traffic.*

---

<sub>Built with ❤️ for cybersecurity education</sub>

</div>
