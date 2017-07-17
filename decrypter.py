#/usr/bin/python3

import pickle
import os
import pyaes
import sys
import time


# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri


### SIMPLE AES DECRYPTER WITH KEY ###




## Calisacagimiz dizinler.

dizin=os.getcwd()+'/EasyCrypter/key_dosyasi'
dizin2=os.getcwd()+'/EasyCrypter/sifreli_dosyalar'
dizin3=os.getcwd()+'/EasyCrypter/sifresi_cozulmus_dosyalar'



## Key.dosyasini aliyoruz bu olmadan sifre cozulemez.

def key_al():
    global anahtar
    anahtar_dosyasi=open(dizin+'/key.k3y','rb')
    anahtar=pickle.load(anahtar_dosyasi)


## Calisacak dizinleri kontrol ediyoruz

def kontrol():
    try:
        liste=os.listdir(os.getcwd()+'/EasyCrypter')
    except:
        print('EasyCrypter Dizini Bulunamadi')
        exit()
    if liste.count('key_dosyasi')==0:
        print('KEY dosyasi bulunamadi!')
        sys.exit()
    if liste.count('sifreli_dosyalar')==0:
        print('Sifreli dosyalar bulunamadi!')
        sys.exit()
    if liste.count('sifresi_cozulmus_dosyalar')==0:
        os.mkdir(dizin3)
    


## Sifresi cozulnesiniz istedigimiz dosyalari(varsa) listeye teket teker ekliyoruz.


def dizin_dosyalari(dizin2):
    global dizindosyalari
    dizindosyalari=[]
    for i in os.listdir(dizin2):
        i=i.split('.cCc')
        i=i[0]
        dizindosyalari.append(i)
    return dizindosyalari


## aldigimiz anhtar ile AES sifrelemeyi cozuyoruz.


def sifre_coz(anahtar):
    aes=pyaes.AESModeOfOperationCTR(anahtar)
    for a in dizindosyalari:
        print('\n'+a+' dosyasinin sifresi cozuluyor...')
        time.sleep(0.1)
        sifreli_dosya=open(dizin2+'/'+a+'.cCc','rb')
        sifreli_dosya_verileri=sifreli_dosya.read()
        sifreli_dosya.close()
        sifresiz_dosya_verileri=aes.decrypt(sifreli_dosya_verileri)
        decrypt_dosyalar=open(dizin3+'/'+a,'wb')
        decrypt_dosyalar.write(sifresiz_dosya_verileri)
        decrypt_dosyalar.close()
        print(G+'\n'+a+' dosyasinin sifresi cozuldu.--> '+dizin3+'/'+a+W)
        time.sleep(0.1)
    
    print('\n'+'-'*30)
    print(C+'Sifresi cozulen dosyalar: ')
    for i in dizindosyalari:
        print(P+'>> '+W+i+' ')
    print('-'*30)
        

def header():

    header="""
    \t\t   __________________________
    \t\t|=|                          |=|
    \t\t|=|                          |=|
    \t\t|=|==> AES File DeCrypter <==|=|
    \t\t|=|         v 1.0            |=|
    \t\t|=|                          |=|
    \t\t|=|==>    coder: easyly   <==|=|
    \t\t|=|                          |=|
    \t\t|=|__________________________|=|"""
    
    print(O+header+'\n\n'+W)

def main():
    header()
    print('Lutfen '+dizin2+' dizininde sifreli dosya oldugundan emin olun. Devam etmek icin ENTER a basiniz.')
    input()
    kontrol()       
    key_al()
    dizin_dosyalari(dizin2)
    sifre_coz(anahtar)

      
