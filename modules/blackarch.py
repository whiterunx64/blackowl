class BlackArchData:
    """
    Holds BlackArch group metadata and slim ISO tool list.
    """
    def __init__(self):
        # === Groups with Descriptions ===
        self.groups = {
            "blackarch-webapp": (
                "Web Applications",
                "Tools for testing, auditing, and exploiting web applications and services."
            ),
            "blackarch-fuzzer": (
                "Fuzzing",
                "Automated tools for finding bugs and vulnerabilities by sending malformed input."
            ),
            "blackarch-scanner": (
                "Network Scanners",
                "Network and vulnerability scanners for discovering hosts, services, and weaknesses."
            ),
            "blackarch-proxy": (
                "Proxy Tools",
                "HTTP/HTTPS and other proxy tools for intercepting and modifying traffic."
            ),
            "blackarch-windows": (
                "Windows Tools",
                "Security and exploitation tools specifically for Windows environments."
            ),
            "blackarch-dos": (
                "Denial of Service",
                "Tools for performing and testing Denial of Service (DoS) attacks."
            ),
            "blackarch-disassembler": (
                "Disassemblers",
                "Tools for converting binaries into assembly code for analysis."
            ),
            "blackarch-sniffer": (
                "Sniffing &amp; Spoofing",
                "Network sniffers and spoofers for capturing and manipulating network traffic."
            ),
            "blackarch-voip": (
                "VoIP Tools",
                "Voice over IP analysis and attack tools."
            ),
            "blackarch-fingerprint": (
                "Fingerprinting",
                "Tools for identifying systems, services, and software versions."
            ),
            "blackarch-networking": (
                "Networking",
                "General networking utilities for diagnostics and analysis."
            ),
            "blackarch-recon": (
                "Reconnaissance",
                "Information gathering and reconnaissance tools."
            ),
            "blackarch-cracker": (
                "Password Cracking",
                "Tools for brute-forcing and cracking passwords and hashes."
            ),
            "blackarch-exploitation": (
                "Exploitation",
                "Frameworks and tools for exploiting vulnerabilities."
            ),
            "blackarch-spoof": (
                "Spoofing",
                "Tools for spoofing network identities and traffic."
            ),
            "blackarch-forensic": (
                "Forensics",
                "Digital forensics tools for investigation and analysis."
            ),
            "blackarch-crypto": (
                "Cryptography",
                "Cryptographic tools for encryption, decryption, and analysis."
            ),
            "blackarch-backdoor": (
                "Backdoors",
                "Tools for creating and managing backdoors."
            ),
            "blackarch-defensive": (
                "Defensive Tools",
                "Security tools for defense, monitoring, and protection."
            ),
            "blackarch-wireless": (
                "Wireless Attacks",
                "Tools for attacking and analyzing wireless networks."
            ),
            "blackarch-automation": (
                "Automation",
                "Automation frameworks and scripting tools."
            ),
            "blackarch-radio": (
                "Radio Tools",
                "Software-defined radio and RF analysis tools."
            ),
            "blackarch-binary": (
                "Binary Analysis",
                "Tools for analyzing binary files and executables."
            ),
            "blackarch-packer": (
                "Packers",
                "Tools for packing and obfuscating binaries."
            ),
            "blackarch-reversing": (
                "Reverse Engineering",
                "Reverse engineering tools for software and hardware."
            ),
            "blackarch-mobile": (
                "Mobile Tools",
                "Security tools for mobile devices and applications."
            ),
            "blackarch-malware": (
                "Malware Analysis",
                "Tools for analyzing and dissecting malware."
            ),
            "blackarch-code-audit": (
                "Code Auditing",
                "Source code auditing and static analysis tools."
            ),
            "blackarch-social": (
                "Social Engineering",
                "Tools for social engineering and human-based attacks."
            ),
            "blackarch-honeypot": (
                "Honeypots",
                "Decoy systems for detecting and studying attacks."
            ),
            "blackarch-misc": (
                "Miscellaneous",
                "Various tools that don't fit other categories."
            ),
            "blackarch-wordlist": (
                "Wordlists",
                "Collections of passwords and wordlists for attacks."
            ),
            "blackarch-decompiler": (
                "Decompilers",
                "Tools for converting binaries back to source code."
            ),
            "blackarch-config": (
                "Configuration",
                "Tools for managing and auditing configurations."
            ),
            "blackarch-debugger": (
                "Debuggers",
                "Debugging tools for software and binaries."
            ),
            "blackarch-bluetooth": (
                "Bluetooth Tools",
                "Bluetooth protocol analysis and attack tools."
            ),
            "blackarch-database": (
                "Database Tools",
                "Database assessment and exploitation tools."
            ),
            "blackarch-automobile": (
                "Automobile Hacking",
                "Tools for vehicle and CAN bus security testing."
            ),
            "blackarch-hardware": (
                "Hardware Hacking",
                "Tools for hardware analysis and hacking."
            ),
            "blackarch-nfc": (
                "NFC Tools",
                "Near Field Communication and RFID tools."
            ),
            "blackarch-tunnel": (
                "Tunneling",
                "Tunneling and VPN tools for network traffic."
            ),
            "blackarch-drone": (
                "Drone Hacking",
                "Tools for drone analysis and exploitation."
            ),
            "blackarch-unpacker": (
                "Unpackers",
                "Tools for unpacking and deobfuscating binaries."
            ),
            "blackarch-firmware": (
                "Firmware Analysis",
                "Firmware extraction and analysis tools."
            ),
            "blackarch-keylogger": (
                "Keyloggers",
                "Tools for recording keystrokes."
            ),
            "blackarch-stego": (
                "Steganography",
                "Tools for hiding and extracting data in files."
            ),
            "blackarch-anti-forensic": (
                "Anti-Forensics",
                "Tools for evading forensic analysis."
            ),
            "blackarch-ids": (
                "Intrusion Detection",
                "Intrusion detection and prevention systems."
            ),
            "blackarch-threat-model": (
                "Threat Modeling",
                "Tools for modeling and assessing threats."
            ),
            "blackarch-gpu": (
                "GPU Tools",
                "GPU-accelerated security and cracking tools."
            ),
        }

        # === all the tool from blackarch slim iso  ===
        self.slim_Edition = [
            "mass", "arp-scan", "aquatone", "binwalk", "bulk-extractor", "bully", "burpsuite", "cewl", "chaos-client", "chntpw", "commix", "crackmapexec", "creddump",
            "crunch", "davtest", "dbd", "dirb", "dirbuster", "dmitry", "dns2tcp", "dnschef", "dnsenum", "dnsrecon", "dnsx", "enum4linux", "exiv2", "exploitdb",
            "faradaysec", "fern-wifi-cracker", "ffuf", "fierce", "findomain", "fping", "gobuster", "guymager", "hashcat", "hashcat-utils", "hashdeep", "hashid",
            "hash-identifier", "hping", "hotpatch", "httpx", "hydra", "ike-scan", "inetsim", "iodine", "john", "kismet", "laudanum", "lbd", "legion", "lulzbuster",
            "macchanger", "magicrescue", "maltego", "maskprocessor", "massdns", "masscan", "metasploit", "msfdb", "mimikatz", "mitmproxy", "multimac", "nbtscan",
            "ncrack", "netdiscover", "netmask", "netsed", "netsniff-ng", "ngrep", "nikto", "nmap", "nuclei", "nuclei-templates", "onesixtyone", "openbsd-netcat",
            "ophcrack", "patator", "pdfid", "pdf-parser", "pipal", "pixiewps", "powersploit", "proxychains-ng", "proxytunnel", "proxify", "pth-toolkit", "ptunnel",
            "pwnat", "radare2", "reaver", "rebind", "recon-ng", "redsocks", "responder", "rsmangler", "sakis3g", "samdump2", "sbd", "scalpel", "scrounge-ntfs",
            "seclists", "set", "skipfish", "sleuthkit", "smbmap", "snmpcheck", "socat", "sploitctl", "spiderfoot", "spooftooph", "sqlmap", "ssldump", "sslscan",
            "sslsplit", "sslyze", "statsprocessor", "stunnel", "subfinder", "swaks", "tcpdump", "tcpick", "tcpreplay", "thc-ipv6", "thc-pptp-bruter", "torctl",
            "theharvester", "udptunnel", "unix-privesc-check", "voiphopper", "wafw00f", "wce", "webshells", "weevely", "wfuzz", "whatweb", "whois", "wifite",
            "windows-binaries", "winexe", "wireshark-qt", "wordlistctl", "wpscan", "zaproxy", "zdns", "zgrab2"
        ]

    def get_groups(self):
        return self.groups

    def get_slim_tools(self):
        return self.slim_Edition
