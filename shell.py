import os
import rlcompleter
import time
import sys
import __main__
import math
import calculator
import scannt
import autopayload
import sysinfo
import figlet
import assistping
import asistchatserver
import asistchatclient
import config




#Console Colors
B = '\033[0m'
G = '\033[32m'
R = '\033[31m'
C = '\033[36m'
W = '\033[0m'
P = '\033[35m' 
PE = '\x1b[6;36;40m'
WE = '\x1b[0m'


class user():
	isim = ""
	gendr = ""
	assistant = ""

#shell i yukler, her acilista calismasi hayatsaldir
def shellinit():
	global text1
	global text2
	global hitap
	global directory
	directory = __main__.directory
	user.isim = __main__.user.isim
	user.gendr = __main__.user.gendr
	user.assistant = __main__.user.assistant
	if user.gendr == 'e':
		hitap = 'bey'
	if user.gendr == 'k':
		hitap = 'hanim'
	text1 = '==> '
	text2 = '{} :({} {})>> ' 
	print(text2.format(user.assistant, user.isim, hitap)+W+ "merhaba!\nkullanilabilir komutlari goruntulemek icin "+P+"komutlar "+W+"yazin\ncikmak icin "+R+"cikis"+W+" yazin\nmenuyu goruntulemek icin "+G + "\"ctrl + c\""+ W+" tuslarina basin.")
	
charset = ['saat', 'komutlar', 'cikis', 'kullanici', 'sifirla', 'merhaba', 'credits', 'version', 'hesap', 'clear','tara','androidpy', 'bilgiler', 'figlet','internet', 'ls', 'exit','chatserver','chatclient', 'config', 'delconf']

#olayin koptugu yer, kullanicidan aldigi komutu kutuphanesinde bulunan komutlarla karsilastirarak geribildirim verir.
def shell():
	global ip
	try:
		komut = input(text1)
		ip = __main__.localip		

		global textmain
		textmain = text2.format(user.assistant, user.isim, hitap)

		if komut == 'figlet':
		  figlet.main()
	
		if komut== 'chatserver':
			asistchatserver.uygulama()

		if komut== 'chatclient':
			asistchatclient.uygulama()

		if komut == 'bilgiler':
			sysinfo.getos()

		if komut == 'iptest':
			print(ip)

		if komut == 'clear':
			os.system("clear")

		if komut == 'hesap':
			calculator.main()
		
		if komut == 'tara':
			scannt.scan()
	
		if komut == 'androidpy':
			autopayload.autopystart()
	  
		if komut == 'internet':
			assistping.check_net()

		if komut == 'ls':
			textdizin = input("lutfen goruntulemek istediginiz dizini giriniz ==> ")
			textgoruntulenen = '{} dizini goruntuleniyor\n'
			textls = 'ls {}'
			print(textmain, textgoruntulenen.format(textdizin), os.popen(textls.format(textdizin)).read())

		if komut == 'version':
			print(textmain, "versiyon: ", __main__.version)
	
		if komut == 'exit':
			sys.exit()
		
		if komut == 'delconf':
			if os.path.isfile(config.config_dir):
				os.remove(config.config_dir)
				print("DEBUG==config silindi.==DEBUG")
				sys.exit()
			else:
				print("DEBUG==oyle bir dosya yok.==DEBUG")

		if komut == 'sifirla':
			print(textmain, C + "sifirlama islemini gerceklestirmek icin \"ctrl + c\" tuslarina basin" + B)
			try:
				rand = input(">>")
				print(textmain, R + "sifirlama islemi iptal edildi" + B)
				shell()
			except KeyboardInterrupt:	
				os.remove(__main__.config_dir)
				os.remove(config.config_dir)
				print("\n", textmain, G + "sifirlanma islemi tamamlandi." + B)
				sys.exit()

		if komut == 'merhaba':
			textmerhaba = 'size de merhaba {} {}'
			print(text2.format(user.assistant, user.isim, hitap), textmerhaba.format(user.isim, hitap))
		
		if komut == 'kullanici':
			text5 = '\n\t Kullanici : {} {}\n\t Asistan ismi : {}\n\t'
			print("kullanici bilgileri siralaniyor..\n\n", "\t", '=' * 25, text5.format(user.isim, hitap, user.assistant), "=" * 25, "\n")
	
		if komut == 'komutlar':
			sayac = 0
			text4 = 'kullanilabilir komutlar:\n\t ===================================\n\t '
			for a in charset:
				sayac = sayac + 1
				text4 = text4 + a 
				text4 = text4 + '  '
				if sayac%4 == 0:
					text4 = text4 + '\n\t '
			print(__main__.G + text4 + __main__.B, "\n\t",G + '=' * 35 + B)
		if komut == 'saat':
			zaman = time.ctime()
			print("\n\n\t", '=' * 25,"\n\t", zaman, "\n\t", '=' * 25, "\n\n")

		if komut == 'credits':
			print(G + """
	|===========================|
	|Runtime And Shell Coded by:|
	|	    atli	    |
	|************************** |
	| Module Developement and   |
	|  Integration of Modules   |
	|	  Made by:          |
	|	    atli	    |
	|	    and		    |
	|	   Easyly	    |
	|===========================|""" + B)




		if komut == 'cikis':
			sys.exit()
		
		if komut == 'config':
			config.runtime()
	
		shell()
	
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
				shell()
		except ValueError:
			print("hatali bir komut girildi uygulama tekrar baslatiliyor")
			__main__.main()

	
