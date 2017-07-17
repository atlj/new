#!/usr/bin/python3

import smtplib
import os
import platform
import time
import shell
import mailconfig

# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri

directory = os.path.dirname(os.path.realpath(__file__))
real_directory = directory + '/'
config_dirtoformat = '{}/mail.ini'
config_dir = config_dirtoformat.format(directory)

def check_dir():
    if os.path.isfile(config_dir):
        mailconfig.firstrun=0
        mailconfig.saveload()      
    else:
        mailconfig.main()
        


def getos():
    global bilgi
    raw_ip=os.popen('hostname -I').read().split('\n')
    proc=platform.processor()
    l_ip=raw_ip[0]
    dagitim=platform.dist()
    dagitim=dagitim[0]
    mimari=platform.machine()
    osys=platform.system()
    unumber = os.getuid()
    zaman=time.ctime()
    if unumber==0:
        kulanici="root"
    else:
        kulanici="No root"
    
    
    bilgi="""
        ============================
        CPU: {}
        OS: {}
        DAGITIM: {}
        KULANICI: {}
        LOCAL IP: {}
        ASISTAN KULANICI ADI: {}
        ZAMAN: {}
       ============================""".format(mimari,osys,dagitim,kulanici,l_ip,shell.user.isim,zaman)
    

def send_mail(usr_adres,usr_pass,adres,mesaj):
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(usr_adres,usr_pass)
    mail.sendmail(usr_adres,adres,mesaj+'\n\n---Python New asistan tarafindan gonderildi---\nhttp://github.com/atlj/new')
    
def main():
    check_dir()
    print('E-posta adresiniz: '+P+mailconfig.addr)
    adres=input(C+'Gondereceginiz e-posta adresini giriniz: '+W)
    mesaj=input(C+'E-posta icerigini yaziniz: '+W)
    soru=input('Sistem bilgilerinide gondermek istiyor musunuz?'+G+'[e/h] '+W)
    if soru=='e':
        try:
            getos()
            send_mail(mailconfig.addr,mailconfig.passwd,adres,mesaj+'\n'+bilgi)
            print(G+'[+] E-posta gonderildi.'+W)
            print(mailconfig.addr+'--->'+adres)
            shell.shell()
        except Exception as e:
            print(R+"[-] ineternet baglantisini kontrol ediniz.")
            print(e+W)
    elif soru=='h':
        try:
            send_mail(mailconfig.addr,mailconfig.passwd,adres,mesaj)
            print(G+'[+] E-posta gonderildi.'+W)
            print(mailconfig.addr+'--->'+adres)
            shell.shell()
        except Exception as e:
            print(R+'[-] Asagidaki hata olustu.')
            print(e+W)
    else:
        print('Anlasilamadi')
        main()
        
