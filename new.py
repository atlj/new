#-*-coding:utf-8-*-

import os
import time
import shell
import sys
from configparser import SafeConfigParser


config = SafeConfigParser()
directory = os.path.dirname(os.path.realpath(__file__))
real_directory = directory + '/'
config_dirtoformat = '{}/config.ini'
config_dir = config_dirtoformat.format(directory)


class user():
	isim = ''
	gendr = ''
	assistant = ''

#Console Colors
B = '\033[0m'
G = '\033[32m'
R = '\033[31m'
C = '\033[36m'
# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri

#ilk açılış mi diye ini dosyasını kontrol eder
def check_if_first_run():
	global first_run
	if os.path.isfile(config_dir):
		first_run = 0
	else:
		first_run = 1

#kullanıcı ismi sorar
def getname(first_run):
	if first_run:
		print(P + "\nconfig.ini dosyasi tespit edilemedi yeni kullanici kaydi baslatiliyor.\n" + W)
		user.isim = str(input("isminiz?\n>> "))
		if not user.isim:
			print(R +"Lutfen isim yerini bos birakmayiniz."+W)
			getname(first_run)
#cinsiyet sorar
def getgender(first_run):
	global hitap
	if first_run:
		user.gendr = str(input("cinsiyetiniz (e/k)\n>> ")).lower()
			
		if user.gendr == "e": 
			hitap = 'bey'
			
		elif user.gendr == "k":
			hitap = 'hanim'

		else:
			print(R+"Lutfen cinsiyet giriniz"+W)
			getgender(first_run)

#cinsiyete göre bey ya da hanim olarak hitap degiskenini atar
def definehitap():
	global hitap
	if user.gendr == "e":
		hitap = 'bey'
	if user.gendr == "k":
		hitap = 'hanim'	

#asistanin ismini sorar
def getassistantname(first_run):
	if first_run:
		user.assistant = str(input("Beni ne olarak cagimak istersiniz ?\n>> "))
		if not user.assistant or user.assistant == ' ':
			print(R+"Lutfen bana bir isim koyun."+W)
			getassistantname(first_run)
		
#config dosyasını eger ilk acilissa yazar degilse yukleme yapar
def saveload(first_run):
	
	global version
	global localip
	version = """
  ___  _____ 
 / _ \|___  |
| | | |  / / 
| |_| | / /  
 \___(_)_/   """

	config.read(config_dir)
	if first_run:
		rawip = os.popen("hostname -I").read()
		rawip = rawip.split("\n")
		localip = rawip[0]
		config.add_section('user')
		config.set('user', 'ip', localip)
		config.set('user', 'username', user.isim)
		config.set('user', 'gendr', user.gendr)
		config.set('user', 'assist', user.assistant)
		dosya = open(config_dir, 'w')
		config.write(dosya)
	config.read(config_dir)
	localip = config.get('user', 'ip')
	user.isim = config.get('user', 'username')
	user.gendr = config.get('user', 'gendr')
	user.assistant = config.get('user', 'assist')
	print(G + "kaydetme/yukleme tamamlandi. \n" + B)
	


#tum komutlari bir sira icerisinde yurutur
	
def main():
	check_if_first_run()
	getname(first_run)  
	getgender(first_run)
	getassistantname(first_run)
	saveload(first_run)
	definehitap()
	text5 = '\n\t Kullanici : {} {}\n\t Asistan ismi : {}\n\t'
	print(W +"\n", "\t", '=' * 25, text5.format(user.isim, hitap, user.assistant), "=" * 25, "\n\n" + W)
	yazi1 = 'Hos geldiniz {} {}'
	print(user.assistant, ": ", yazi1.format(user.isim, hitap))
	shell.shellinit()
	shell.shell()

#ctrl c de hata vermemesi icin 
def runtime():
	try:	
		main()
	except KeyboardInterrupt:
		print(R + """
Klavye tarafindan kesinti algilandi lutfen bir islem secin:
shell'e don(kayit sirasinda kullanilamaz)	(0)
uygulamadan cik					(1)""" + B)
		try:
			back = int(input(">> "))
			if back:
				sys.exit()
			elif not back:
				shell.shell()
		except ValueError:
			print("hatali bir komut girildi uygulama tekrar baslatiliyor")
			main()

if __name__ == '__main__':
	print(os.popen("clear").read())
	runtime()

		