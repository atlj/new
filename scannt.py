# -*- coding: utf-8 -*-

import os
import sys
import shell
try:
    from terminaltables import AsciiTable
except:
    print("terminaltables modulu yuklu degil !! 'pip3 install terminaltables' yazarak yukleyebilirsiniz.")
    shell.shell()

#kulanimi:
#import et scannt.scan() diye calistir


#coder:easyly
#startdart burakgunerassistant module


def get_gateway():
    global gateway
    gateway = os.popen("ip route show | grep -i 'default via'| awk '{print $3 }'").read()
    gateway=gateway.replace("\n","")
    
    
def scan():
    get_gateway()
    scan = os.popen("nmap " + gateway + "/24 -n -sP ").read()
    f = open(os.getcwd()+'/scanlog.txt','w')
    f.write(scan)
    f.close()
    devices = os.popen(" grep report "+os.getcwd()+"/scanlog.txt | awk '{print $5}'").read()
    devices_mac = os.popen("grep MAC "+os.getcwd()+"/scanlog.txt | awk '{print $3}'").read() + os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read().upper()# get devices mac and localhost mac address
    devices_name = os.popen("grep MAC "+os.getcwd()+"/scanlog.txt | awk '{print $4 ,S$5 $6}'").read() + "\033[1;32m(Bu Cihaz)\033[0m"
    table_data = [
        ['IP Adres', 'Mac Adres','Uretici'],
        [devices, devices_mac,devices_name]
        ]
    table = AsciiTable(table_data)
    print("[+]------------------[Aginizda Bulunan Cihazlar ]----------------[+]\n")
    print(table.table)
    
		
        
    
    
    
            
     

    
