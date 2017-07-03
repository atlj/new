

# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri



import socket,time,sys
from threading import Thread
import shell

class uygulama():
    def al(self,baglan):
        while True:
            try:
                veri=baglan.recv(1024)
                veri=str(veri)
                veri=veri[1:]
                if veri=="''":
                    sys.exit()
                else:
                    pass
                print(C+"\n<"+sunucu+">"+W+veri,sep="")
            except KeyboardInterrupt:
                exit()
             
    def al_calistir(self,baglan):
        islem=Thread(target=self.al, args=(baglan,))
        islem.start()
        
    def __init__(self):
        global sunucu
        baslik="""{}
           ____________________________
          |                            |
          | CHAT MODULUNE HOSGELDINIZ  |
          |                            |
          |       coder:easyly         |
          |   <ooruc471@yandex.com>    |
          |                            |
          |          {}CLIENT{}            |
          |____________________________|{}
          """.format(C,R,C,W)
        print(baslik)
        port=2112
        
        sunucu=input(G+"Lutfen baglanmak istediginiz sunucunun IP sini girin (or:192.168.1.102)\n>>")
        if not sunucu:
            sunucu="127.0.0.1"
        else:
            pass
        try:    
            baglanti=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            baglanti.connect((sunucu,port))
        except:
            print(R+"Sunucu Bulunamadi"+W)
            shell.shell()
            
        print(G+"Server a giris yapildi --> "+P+sunucu)
            
            
        self.al_calistir(baglanti)
        
        while True:
            try:
                gonderilecek=bytes(input(O+"Gonder : "+W),"UTF-8")
                baglanti.sendto(gonderilecek,(sunucu,port))
                time.sleep(0.1)
            except KeyboardInterrupt:
                print(R+"(ctrl+c) algilandi cikiliyor"+W)
                shell.shell()
            
if __name__=="__main__":
    def run():
        yazilim=uygulama()
    
    
            
        
