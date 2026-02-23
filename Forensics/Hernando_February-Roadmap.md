# 1-Month Network Forensics Roadmap (February)

## Overview
This roadmap focuses on **Network Forensics** as the core discipline.  
Weeks 1 and 2 introduce foundational knowledge, while Weeks 3 and 4 reinforce learning through **hands-on forensic challenges and CTF-style investigations**, emphasizing analysis, reasoning, and reporting rather than introducing new theory.

---

## Week 1 — Network Forensics Fundamentals & Packet Analysis
**Goal:** Understand how network evidence is captured, structured, and interpreted.

### Topics to Cover
- Introduction to Network Forensics
- Role of Network Forensics in Incident Response
- Types of Network Evidence
  - PCAP files
  - Logs
  - NetFlow
- Evidence Handling and Chain of Custody
- OSI and TCP/IP Models (Forensic Perspective)
- Packet Structure and Headers

### Core Protocols
- Ethernet
- ARP
- IP
- TCP vs UDP
- ICMP

### Traffic Capture Basics
- PCAP files
- Network traffic capture concepts

### Network Forensic Tools
- Wireshark
- tcpdump
- tshark

### Practice
- Open and inspect PCAP files
- Identify protocols and packet fields
- Apply Wireshark display filters
- Follow TCP streams
- Solve beginner network forensic CTF challenges

---

## Week 2 — Protocol Analysis & Suspicious Network Activity
**Goal:** Detect abnormal and malicious behavior through protocol analysis.

### Topics to Cover
- HTTP and HTTPS forensic analysis
- DNS traffic analysis and abuse techniques
- FTP, SMTP, and SMB traffic basics

### Indicators of Suspicious Activity
- Unusual ports and protocols
- Beaconing patterns
- Repeated failed connections
- Traffic filtering and stream reconstruction
- File extraction from network traffic

### Common Attack Patterns
- Network scanning
- Brute-force attacks
- Unauthorized data transfer

### Practice
- Analyze HTTP sessions and headers
- Identify suspicious DNS queries
- Extract files from PCAP traffic
- Detect scanning or brute-force behavior
- Solve protocol-focused forensic CTF challenges

---

## Week 3 — Applied Network Forensics Challenges
**Goal:** Reinforce Weeks 1–2 concepts through guided forensic challenges.

### Focus Areas (No New Topics)
- Packet and protocol identification
- TCP and UDP stream reconstruction
- HTTP and DNS analysis
- Detection of abnormal traffic patterns
- File and data extraction from traffic

### Practice
- Solve beginner to intermediate network forensic CTFs
- Analyze small to medium PCAP datasets
- Answer investigation questions:
  - What protocol was abused?
  - Which IPs or domains are suspicious?
  - What data was transferred?
- Re-analyze PCAPs using different filtering strategies
- Document findings in structured notes

### Expected Outcome
- Systematic approach to solving forensic challenges
- Improved speed and confidence in PCAP analysis

---

## Week 4 — Advanced Network Forensic Challenges & Mini Investigation
**Goal:** Perform full network-centric investigations using realistic datasets.

### Focus Areas
- Multi-stage attack analysis
- Timeline reconstruction from PCAP evidence
- Identifying:
  - Initial access
  - Command activity
  - Data exfiltration
- Correlating multiple suspicious behaviors
- Working with large PCAP files

### Practice
- Solve intermediate to advanced forensic CTF challenges
- Analyze realistic PCAPs independently
- Identify attacker infrastructure and victim activity
- Perform a mini network forensic investigation project

### Forensic Report Requirements
Include:
- Scope and assumptions
- Key findings
- Supporting evidence
- Conclusion

### Expected Outcome
- End-to-end network evidence analysis capability
- Experience with DFIR-style investigations

---

## Expected Outcomes After February
By completing this roadmap, you should be able to:

- Understand the network forensic investigation workflow
- Analyze and interpret PCAP files confidently
- Detect suspicious and malicious network activity
- Reconstruct sessions and extract transferred data
- Solve beginner to intermediate forensic CTF challenges
- Conduct a basic network-focused forensic investigation
- Write clear and defensible forensic reports

---

## Recommended Platforms
- TryHackMe (Network Forensics rooms)
- Hack The Box Academy
- CyberDefenders
- Blue Team Labs Online
- PicoCTF (Forensics category)

---
