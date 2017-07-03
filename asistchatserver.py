
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

class uygulama():
    def al(self,baglan,konum):
        while True:
            veri=baglan.recv(1024)
            veri=str(veri)
            veri=veri[1:]
            if veri=="''":
                sys.exit()
            else:
                pass
                
            print(C+"\n<"+konum[0]+">"+W+veri,sep="")
    
    def al_calistir(self,baglan,konum):
        global islem
        islem=Thread(target=self.al,args=(baglan,konum))
        islem.start()
        
    def __init__(self):
        global konum
        baslik="""{}
           ____________________________
          |                            |
          | CHAT MODULUNE HOSGELDINIZ  |
          |                            |
          |       coder:easyly         |
          |   <ooruc471@yandex.com>    |
          |                            |
          |          {}SERVER{}            |
          |____________________________|{}
          """.format(C,R,C,W)
        print(baslik)
        sunucu="127.0.0.1"
        port=2112
        sunucu=input(O+"Lutfen IP adresinizi yaziniz.\n>>"+W)
        if not sunucu:
            sunucu="127.0.0.1"
        else:
            pass
            
        try:
            baglanti=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            baglanti.bind((sunucu,port))
            print(G+"Sunucu {}:{} baslatildi !!".format(sunucu,port))
            print(B+"Baglanti bekleniyor..."+W)
            baglanti.listen(1)
            baglan,konum=baglanti.accept()
            print(C+"Kulanici baglandi --> "+P+konum[0])
            
            self.al_calistir(baglan,konum)
            while True:
                gonderilecek=bytes(input(G+"Gonder: "+W),"UTF-8")
                baglan.send(gonderilecek)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(R+"\n(ctrl+c) algilandi cikiliyor..."+W)
            baglanti.close()
            sys.exit
        except :
            print("[HATA] Beklenmeyen bir hata !! ")
            baglanti.close()
            sys.exit()
            
if __name__=="__main__":
    def run():
        yazilim=uygulama()
            
            
    
        
    
