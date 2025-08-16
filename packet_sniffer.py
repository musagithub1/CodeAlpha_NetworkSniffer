from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP, Ether, DNS, Raw
import argparse
import socket
import time
from datetime import datetime
import json

# Dictionary to map protocol numbers to names
PROTOCOL_NAMES = {
    1: 'ICMP',
    6: 'TCP',
    17: 'UDP',
    2: 'IGMP',
    89: 'OSPF',
    47: 'GRE',
}

# Dictionary for common ports
COMMON_PORTS = {
    20: 'FTP-DATA',
    21: 'FTP',
    22: 'SSH',
    23: 'TELNET',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP-SERVER',
    68: 'DHCP-CLIENT',
    69: 'TFTP',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    993: 'IMAPS',
    995: 'POP3S',
    3389: 'RDP',
    5432: 'PostgreSQL',
    3306: 'MySQL',
    1521: 'Oracle',
    27017: 'MongoDB'
}

class PacketAnalyzer:
    def __init__(self, save_to_file=False):
        self.packet_count = 0
        self.save_to_file = save_to_file
        self.captured_packets = []
        
    def get_protocol_name(self, proto_id):
        return PROTOCOL_NAMES.get(proto_id, f'Unknown({proto_id})')
    
    def get_service_name(self, port):
        return COMMON_PORTS.get(port, str(port))
    
    def analyze_payload(self, payload, max_length=100):
        """Analyze payload and return readable format"""
        try:
            payload_bytes = bytes(payload)
            if len(payload_bytes) == 0:
                return "Empty payload"
            
            # Try to decode as UTF-8
            try:
                decoded = payload_bytes.decode('utf-8', errors='ignore')
                # Only show printable characters
                printable = ''.join(c for c in decoded if c.isprintable() or c in '\n\r\t')
                if len(printable) > max_length:
                    printable = printable[:max_length] + "..."
                return f"Text: {printable}" if printable.strip() else f"Binary data ({len(payload_bytes)} bytes)"
            except:
                return f"Binary data ({len(payload_bytes)} bytes): {payload_bytes[:20].hex()}{'...' if len(payload_bytes) > 20 else ''}"
        except:
            return "Could not analyze payload"
    
    def packet_callback(self, packet):
        self.packet_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\n{'='*60}")
        print(f"Packet #{self.packet_count} - {timestamp}")
        print(f"{'='*60}")
        
        packet_info = {
            'packet_number': self.packet_count,
            'timestamp': timestamp,
            'layers': []
        }
        
        # Ethernet Layer Analysis
        if Ether in packet:
            eth_info = {
                'layer': 'Ethernet',
                'src_mac': packet[Ether].src,
                'dst_mac': packet[Ether].dst,
                'type': hex(packet[Ether].type)
            }
            packet_info['layers'].append(eth_info)
            print(f"🔗 Ethernet Frame:")
            print(f"   Source MAC:      {packet[Ether].src}")
            print(f"   Destination MAC: {packet[Ether].dst}")
            print(f"   Type:           {hex(packet[Ether].type)}")
        
        # IP Layer Analysis
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            protocol_id = packet[IP].proto
            protocol_name = self.get_protocol_name(protocol_id)
            
            ip_info = {
                'layer': 'IP',
                'src_ip': ip_src,
                'dst_ip': ip_dst,
                'protocol': protocol_name,
                'ttl': packet[IP].ttl,
                'length': packet[IP].len
            }
            packet_info['layers'].append(ip_info)
            
            print(f"🌐 IP Packet:")
            print(f"   Source IP:      {ip_src}")
            print(f"   Destination IP: {ip_dst}")
            print(f"   Protocol:       {protocol_name}")
            print(f"   TTL:           {packet[IP].ttl}")
            print(f"   Total Length:   {packet[IP].len} bytes")
            
            # TCP Analysis
            if TCP in packet:
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                flags = packet[TCP].flags
                
                tcp_info = {
                    'layer': 'TCP',
                    'src_port': f"{src_port} ({self.get_service_name(src_port)})",
                    'dst_port': f"{dst_port} ({self.get_service_name(dst_port)})",
                    'flags': str(flags),
                    'seq': packet[TCP].seq,
                    'ack': packet[TCP].ack
                }
                packet_info['layers'].append(tcp_info)
                
                print(f"🚢 TCP Segment:")
                print(f"   Source Port:     {src_port} ({self.get_service_name(src_port)})")
                print(f"   Dest Port:       {dst_port} ({self.get_service_name(dst_port)})")
                print(f"   Flags:          {flags}")
                print(f"   Sequence:       {packet[TCP].seq}")
                print(f"   Acknowledgment: {packet[TCP].ack}")
                
                if packet[TCP].payload:
                    payload_analysis = self.analyze_payload(packet[TCP].payload)
                    tcp_info['payload'] = payload_analysis
                    print(f"   Payload:        {payload_analysis}")
            
            # UDP Analysis
            elif UDP in packet:
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
                
                udp_info = {
                    'layer': 'UDP',
                    'src_port': f"{src_port} ({self.get_service_name(src_port)})",
                    'dst_port': f"{dst_port} ({self.get_service_name(dst_port)})",
                    'length': packet[UDP].len
                }
                packet_info['layers'].append(udp_info)
                
                print(f"📦 UDP Datagram:")
                print(f"   Source Port:    {src_port} ({self.get_service_name(src_port)})")
                print(f"   Dest Port:      {dst_port} ({self.get_service_name(dst_port)})")
                print(f"   Length:         {packet[UDP].len} bytes")
                
                # Check for DNS
                if DNS in packet:
                    dns_info = self.analyze_dns(packet[DNS])
                    udp_info['dns'] = dns_info
                    print(f"   DNS Query:      {dns_info}")
                elif packet[UDP].payload:
                    payload_analysis = self.analyze_payload(packet[UDP].payload)
                    udp_info['payload'] = payload_analysis
                    print(f"   Payload:        {payload_analysis}")
            
            # ICMP Analysis
            elif ICMP in packet:
                icmp_info = {
                    'layer': 'ICMP',
                    'type': packet[ICMP].type,
                    'code': packet[ICMP].code
                }
                packet_info['layers'].append(icmp_info)
                
                print(f"🔔 ICMP Packet:")
                print(f"   Type:           {packet[ICMP].type}")
                print(f"   Code:           {packet[ICMP].code}")
        
        # ARP Analysis
        elif ARP in packet:
            arp_info = {
                'layer': 'ARP',
                'operation': packet[ARP].op,
                'sender_ip': packet[ARP].psrc,
                'target_ip': packet[ARP].pdst,
                'sender_mac': packet[ARP].hwsrc,
                'target_mac': packet[ARP].hwdst
            }
            packet_info['layers'].append(arp_info)
            
            operation = "Request" if packet[ARP].op == 1 else "Reply"
            print(f"🔍 ARP {operation}:")
            print(f"   Sender IP:      {packet[ARP].psrc}")
            print(f"   Target IP:      {packet[ARP].pdst}")
            print(f"   Sender MAC:     {packet[ARP].hwsrc}")
            print(f"   Target MAC:     {packet[ARP].hwdst}")
        
        # Save packet info if requested
        if self.save_to_file:
            self.captured_packets.append(packet_info)
        
        print(f"{'='*60}")
    
    def analyze_dns(self, dns_layer):
        """Analyze DNS queries and responses"""
        try:
            if dns_layer.qr == 0:  # Query
                return f"Query for {dns_layer.qd.qname.decode('utf-8')}"
            else:  # Response
                return f"Response with {dns_layer.ancount} answers"
        except:
            return "DNS packet (could not decode)"
    
    def save_results(self, filename="captured_packets.json"):
        """Save captured packets to a JSON file"""
        if self.captured_packets:
            try:
                with open(filename, 'w') as f:
                    json.dump(self.captured_packets, f, indent=2)
                print(f"\n✅ Captured packets saved to {filename}")
            except Exception as e:
                print(f"❌ Error saving packets: {e}")
        else:
            print("🤷 No packets to save")

def main():
    parser = argparse.ArgumentParser(
        description="Enhanced Network Packet Sniffer - CodeAlpha Internship Project",
        epilog="Example usage: sudo python3 packet_sniffer.py -c 10 -f 'tcp port 80' --save"
    )
    parser.add_argument("-c", "--count", type=int, default=0, 
                       help="Number of packets to capture (0 for infinite)")
    parser.add_argument("-f", "--filter", type=str, default="", 
                       help="BPF filter string (e.g., 'tcp port 80', 'host google.com')")
    parser.add_argument("--save", action="store_true", 
                       help="Save captured packets to JSON file")
    parser.add_argument("-i", "--interface", type=str, 
                       help="Network interface to capture on")
    parser.add_argument("--timeout", type=int, default=0,
                       help="Stop capture after specified seconds (0 for no timeout)")
    
    args = parser.parse_args()
    
    print("🚀 Enhanced Network Packet Sniffer")
    print("📡 CodeAlpha Cybersecurity Internship Project")
    print("="*50)
    
    # Create analyzer instance
    analyzer = PacketAnalyzer(save_to_file=args.save)
    
    # Display capture settings
    print(f"Interface: {args.interface if args.interface else 'Default'}")
    print(f"Filter: {args.filter if args.filter else 'None (all packets)'}")
    print(f"Count: {'Infinite' if args.count == 0 else args.count}")
    print(f"Timeout: {'None' if args.timeout == 0 else f'{args.timeout} seconds'}")
    print(f"Save to file: {'Yes' if args.save else 'No'}")
    print("\n🎯 Starting packet capture... Press Ctrl+C to stop.\n")
    
    try:
        # Start packet capture
        sniff(
            prn=analyzer.packet_callback, 
            count=args.count, 
            filter=args.filter,
            iface=args.interface,
            timeout=args.timeout
        )
    except KeyboardInterrupt:
        print("\n\n🛑 Capture interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during capture: {e}")
    finally:
        print(f"\n📊 Total packets captured: {analyzer.packet_count}")
        if args.save:
            analyzer.save_results()
        print("✅ Packet capture finished.")

if __name__ == "__main__":
    main()