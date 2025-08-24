# 🔍 Python Nmap Scanner

A simple Python automation tool built using the **python-nmap** library.  
It allows you to run different types of port scans (TCP SYN, UDP, and comprehensive scans) with a simple CLI menu.

---

## ⚡ Features
- Run **SYN ACK scans** for TCP ports.
- Run **UDP scans**.
- Run **comprehensive scans** with service/OS detection.
- Scans ports in the range **1–1024**.
- Displays host status, protocols, and open ports.

---

## 📦 Requirements
- Kali Linux (or any Linux with Python3 and Nmap installed).
- [Nmap](https://nmap.org) installed:

  sudo apt install nmap -y

Python library python-nmap:
    pip3 install python-nmap

Run the script with sudo (needed for SYN/UDP scans):
    sudo python3 scanner.py

    
