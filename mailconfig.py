#-*-coding:utf8;-*-
import os
import sys
from configparser import SafeConfigParser
import shell
import asistanmail

directory = os.path.dirname(os.path.realpath(__file__))
real_directory = directory + '/'
config_dirtoformat = '{}/mail.ini'
config_dir = config_dirtoformat.format(directory)
cfg = SafeConfigParser()


def check():
    global firstrun
    if not os.path.isfile(config_dir):
        firstrun= 1
    else:
        firstrun=0
        
def setter():
    global addr
    global passwd
    global firstrun
    print('BIR KERELIK BIR ISLEMDIR.\n')
    addr=input("Mail Adresiniz(Sadece Gmail): ")
    passwd=input("Sifrenizi giriniz: ")
    firstrun = 1
    saveload()

def saveload():
    global addr
    global passwd
    if firstrun:
        cfgfile=open(config_dir, "w")
        cfg.read(config_dir)
        cfg.add_section('mail')
        cfg.set('mail', 'addr', addr)
        cfg.set('mail', 'passwd', passwd)
        cfg.write(cfgfile)
    cfg.read(config_dir)
    addr = cfg.get('mail', 'addr')
    passwd = cfg.get('mail', 'passwd')
    
def printer():
    global firstrun
    if firstrun:
        setter()
        firstrun = 0
        saveload()
    metin = "\n\tkullanici adi:{}\n\tsifre:{}\n"
    print(metin.format(addr, passwd))
    print("Ayarlar kaydedildi devam etmek icin ENTER tekrar denemek icin 1 e basiniz...")
    try:
        opt = int(input(">>"))
        if opt:
            os.remove(config_dir)
            print(shell.G+"ayarlar basariyla silindi."+shell.B)
            sys.exit()
        else :
            asistanmail.main()
            
    except ValueError:
        asistanmail.main()
        
def main():
    check()
    printer()
    
if __name__=="__main__":
    main()
        
