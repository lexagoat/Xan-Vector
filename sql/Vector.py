#!/usr/bin/env/ python

import os
import sys,time,random
from colorama import Fore, Back, Style

os.system("apt-get install figlet")
os.system("clear")

banner = """    :::     ::: :::::::::: :::::::: ::::::::::: ::::::::  ::::::::: 
  :+:     :+: :+:       :+:    :+:    :+:    :+:    :+: :+:    :+: 
 +:+     +:+ +:+       +:+           +:+    +:+    +:+ +:+    +:+  
+#+     +:+ +#++:++#  +#+           +#+    +#+    +:+ +#++:++#:    
+#+   +#+  +#+       +#+           +#+    +#+    +#+ +#+    +#+    
#+#+#+#   #+#       #+#    #+#    #+#    #+#    #+# #+#    #+#     
 ###     ########## ########     ###     ########  ###    ###      
                                  
                                  by lexa#0001 & lexa#1000"""
print(Fore.RED + banner)
time.sleep(3)

typing_speed = 50
def slow_type(t):
    for l in t:
        sys.stdout.write(1)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
print(Fore.LIGHTRED_EX + """
[!] Database Grabber Tool
""")
print(Fore.MAGENTA + """
[1] Vulnerability Link
[2] Vulnerability Link and Database Name
""")


choice = input("Enter choice")
if(choice == "1"):
    vuln = input("Enter Vulnerability Link: ")
    os.system("sqlmap -u + vuln + --dbs --random -agent")

elif(choice == "2"):
    vuln = input("Enter Vulnerability Link: ")
    database = input("Enter Database Name: ")
    os.system("sqlmap -u vuln" + " -D " + database + " --tables --randomagent")
