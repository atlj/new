#!/usr/bin/python3

### SIMPLE AES FILE CRYPTER ###

import os
import pickle
import pyaes


# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri

dizin = os.getcwd()+'/EasyCrypter/sifrelenecek_dosyalar'
dizin2 = os.getcwd()+'/EasyCrypter/sifreli_dosyalar'
dizin3 = os.getcwd()+'/EasyCrypter/key_dosyasi'
  
  
  
## gerekli dizin dosyalarari kontrol edilir
## eger yoksa olusturulur     
def kontrol():
    
    if os.listdir(os.getcwd()).count('EasyCrypter')==0:
        os.mkdir(os.getcwd()+'/EasyCrypter')
        os.mkdir(dizin)
        os.mkdir(dizin2)
        os.mkdir(dizin3)
    else:
        pass
        
        
    
    
## rasgele anahtar olusturulur 'key.k3y'
def anahtar_olustur(dizin):
    global anahtar
    anahtar=os.urandom(32)
    anahtar_dosyasi=open(dizin3+'/key.k3y','wb')
    pickle.dump(anahtar,anahtar_dosyasi)
    
    


## sifrelenmek istenilen dosylara tek tek bir listeye.eklenir    
def dizin_dosyalari(dizin):
    global dizindosyalari
    dizindosyalari=[]
    for i in os.listdir(dizin):
        dizindosyalari.append(i)
    
    
            

## En onemli fonksyon olan bu sifrele() daha once listeledigimiz dosyalari
## tek tek acip icindeki veriyi AES ile sifreler sonuna .cCc uzantisi ekler
## ve kaydeder.
            
            
def sifrele(anahtar):
    global sifreli_dosya_verileri
    
    aes=pyaes.AESModeOfOperationCTR(anahtar)
    for a in dizindosyalari:
        print('\n'+a+' dosyasi sifreleniyor.')
        dosya=open(dizin+'/'+a,'rb')
        dosya_verileri=dosya.read()
        sifreli_dosya_verileri=aes.encrypt(dosya_verileri)
        f=open(dizin2+'/'+a+'.cCc','wb')
        f.write(sifreli_dosya_verileri)
        f.seek(0)
        f.close()
        print(G+'\n'+a+' dosyasi sifrelendi --> '+dizin2+'/'+a+'.cCc'+W)
    
    print('-'*30)
    print('Butun dosylara sifrelendi !!')
    for s in dizindosyalari:
        print(P+'>> '+C, s+W)
    print('-'*30)


def header():
    header="""
    \t\t   ________________________
    \t\t|=|                        |=|
    \t\t|=|                        |=|
    \t\t|=|==> AES File Crypter <==|=|
    \t\t|=|         v 1.0          |=|
    \t\t|=|                        |=|
    \t\t|=|==>   coder: easyly  <==|=|
    \t\t|=|                        |=|
    \t\t|=|________________________|=|"""
    
    print(header+'\n\n')
   
    
       
        

def main():
    kontrol()
    header()
    print("Lutfen "+dizin+" adli dizine sifrelemek istediginiz dosyalari atin ENTER a basiniz")
    input()
    anahtar_olustur(dizin)
    dizin_dosyalari(dizin)
    sifrele(anahtar)


            

    
            
        

    
