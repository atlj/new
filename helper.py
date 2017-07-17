#-*-coding:utf8;-*-

arg =''
def main(arg):
    a = 0
    if arg=="androidpy":
        return "payload olusturmanizi saglayan bir aractir."
        a=1                      
    if arg=="internet":
        return "internet baglantinizi test eder."
        a=1
    if arg=="config":
        return"cesitli ayarlari degistirmenizi saglar."
        a=1
    if arg=="ls":
        return "bir dizinin icerigini goruntuler."
        a=1
    if arg=="saat":
        return "saati goruntuler."
        a=1
    if arg=="komutlar":
        return "kullanilabilir komutlari goruntuler"
        a=1
    if arg=="kullanici":
        return "gecerli kullanici bilgilerini goruntuler"
        a=1
    if arg=="sifirla":
        return "gecerli kullaniciyi sifirlar."
        a=1
    if arg=="hesap":
        return "hesap makinesi islemi baslatabilirsiniz."
        a=1
    if arg=="clear":
        return "ekrani temizler."
        a=1
    if arg=="tara":
        return "aginiza bagli olan cihazlari listeler."
        a=1
    if arg=="bilgiler":
        return "sistem bilgilerinizi siralar."
        a=1
    if arg=="chatserver":
        return "bir chat serveri baslatir"
        a=1
    if arg=="chatclient":
        return "bir chat clienti baslatir."
        a=1
    if arg=="delconf":
        return "config komutunun yaptigi ayarlamayi siler."
        a=1
    if arg=="mailconfig":
        return "mail adresinizi ve sifrenizi ayarlar"
        a=1
    if arg=="email":
        return "email gondermenizi saglar."
        a=1
    if arg=='cikis':
        return "Asistandan cikarsiniz."
    if arg=='merhaba':
        return "Asistan sizi selamlar"
    if arg=='2048':
        return "2048 oyunu keyfini.cikarin"
    if arg=='credits':
        return "uygulama kim tarafindan kodlandi?"
    if arg=='version':
        return "Asistan versyonunu gosterir"
    if arg=='crypter':
        return "Dosyalari AES ile sifreler"
    if arg=='decrypter':
        return "AES ile sifrelenen dosyalari cozer."
    if arg=='figlet':
        return "AsciiArt yapmanizi saglar."
    if arg=='exit':
        return "Asistandan cikarsiniz."
        
    if not a:
        return "boyle bir yardim icerigi bulunamadi."
