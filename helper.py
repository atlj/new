#-*-coding:utf8;-*-

arg =''
def main():
    a = 0
    if arg=="androidpy":
        print("androidpy sisteminizde metsploit framework\n yukluyse payload olusturmanizi \nsaglayan bir aractir.")
        a=1                      
    if arg=="internet":
        print("internet baglantinizi test eder.")
        a=1
    if arg=="config":
        print("cesitli ayarlari degistirmenizi\nsaglar.")
        a=1
    if arg=="ls":
        print("bir dizinin icerigini goruntuler.")
        a=1
    if arg=="saat":
        print("saati goruntuler.")
        a=1
    if arg=="komutlar":
        print("kullanilabilir komutlari goruntuler")
        a=1
    if arg=="kullanici":
        print("gecerli kullanici bilgilerini\ngoruntuler")
        a=1
    if arg=="sifirla":
        print("gecerli kullaniciyi sifirlar.")
        a=1
    if arg=="hesap":
        print("hesap konutu ile bir hesap\nmakinesi islemi baslatabilirsiniz.")
        a=1
    if arg=="clear":
        print("ekrani temizler.")
        a=1
    if arg=="tara":
        print("aginiza bagli olan cihazlari listeler.")
        a=1
    if arg=="bilgiler":
        print("sistem bilgilerinizi siralar.")
        a=1
    if arg=="chatserver":
        print("bir chat serveri baslatir")
        a=1
    if arg=="chatclient":
        print("bir chat clienti baslatir\ncalismasi icin baska birinin chatserver\nkomutu ile chat serveri\nbaslatmasi gerekir.")
        a=1
    if arg=="delconf":
        print("config komutunun yaptigi ayarlamayi siler\nbir debug komutudur.")
        a=1
    if arg=="mailconfig":
        print("mail adresinizi ve sifrenizi ayarlar")
        a=1
    if arg=="email":
        print("email gondermenizi saglar.")
        a=1
    if not a:
        print("boyle bir yardim icerigi\nbulunamadi.")