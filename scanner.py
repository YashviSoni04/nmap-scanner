#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is:", ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""")
print("You have selected option:", resp)

resp_dict = {
    '1': ['-v -sS', 'tcp'],
    '2': ['-v -sU', 'udp'],
    '3': ['-v -sS -sV -sC -A -O', 'tcp']
}

if resp not in resp_dict:
    print("Enter a valid option")
else:
    print("nmap version:", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", resp_dict[resp][0])
    print("Scan Info:", scanner.scaninfo())

    if ip_addr in scanner.all_hosts():
        print("Scanner Status:", scanner[ip_addr].state())
        protocols = scanner[ip_addr].all_protocols()
        print("Protocols:", protocols)

        if resp_dict[resp][1] in protocols:
            open_ports = scanner[ip_addr][resp_dict[resp][1]].keys()
            if open_ports:
                print("Open Ports:", list(open_ports))
            else:
                print("No open ports found in range 1-1024")
        else:
            print("No ports detected for protocol:", resp_dict[resp][1])
    else:
        print("Host seems down or not responding")
