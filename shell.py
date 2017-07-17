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
import crypter
import decrypter
import config
import mailconfig
import asistanmail
import helper





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
	print(text2.format(user.assistant, user.isim, hitap)+W+ "merhaba!\nkullanilabilir komutlari goruntulemek icin "+P+"komutlar "+W+"yazin\nyardim icin "+C+"help \n"+W+"cikmak icin "+R+"cikis"+W+" yazin\nmenuyu goruntulemek icin "+G + "\"ctrl + c\""+ W+" tuslarina basin.")
	
charset = ['saat', 'komutlar', 'cikis', 'kullanici', 'sifirla', 'help', 'merhaba', 'credits', 'version', 'hesap', 'clear','tara','androidpy','crypter','decrypter', 'bilgiler', 'figlet','internet', 'ls', 'exit','email','chatserver','chatclient', 'config', 'delconf', 'email', 'mailconfig']

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
		  
		elif komut == "mailconfig":
		  mailconfig.main()
	
		elif komut== 'chatserver':
			asistchatserver.uygulama()

		elif komut== 'chatclient':
			asistchatclient.uygulama()

		elif komut == 'bilgiler':
			sysinfo.getos()

		elif komut == 'iptest':
			print(ip)
			
		elif komut == 'crypter':
		  crypter.main()
		  
		elif komut == 'decrypter':
		  decrypter.main()
		 
		
		elif 'help' in komut:
		 try:
		  komut = komut.split(" ")
		  helper.arg=komut[1]
		  helper.arg="".join(helper.arg)
		  helper.main()
		 except IndexError:
		  print("yardim icerigi goruntulemek icin\nbir komut giriniz.\nornek: help ls")


		elif komut == 'clear':
			os.system("clear")

		elif komut == 'hesap':
			calculator.main()
		
		elif komut == 'tara':
			scannt.scan()
	
		elif komut == 'androidpy':
			autopayload.autopystart()
	  
		elif komut == 'internet':
			assistping.check_net()
		
		elif komut == 'email':
		  asistanmail.main()

		elif komut == 'ls':
			textdizin = input("lutfen goruntulemek istediginiz dizini giriniz ==> ")
			textgoruntulenen = '{} dizini goruntuleniyor\n'
			textls = 'ls {}'
			print(textmain, textgoruntulenen.format(textdizin), os.popen(textls.format(textdizin)).read())

		elif komut == 'version':
			print(textmain, "versiyon: ", __main__.version)
	
		elif komut == 'exit':
			sys.exit()
		
		elif komut == 'delconf':
			if os.path.isfile(config.config_dir):
				os.remove(config.config_dir)
				print("DEBUG==config silindi.==DEBUG")
				sys.exit()
			else:
				print("DEBUG==oyle bir dosya yok.==DEBUG")

		elif komut == 'sifirla':
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

		elif komut == 'merhaba':
			textmerhaba = 'size de merhaba {} {}'
			print(text2.format(user.assistant, user.isim, hitap), textmerhaba.format(user.isim, hitap))
		
		elif komut == 'kullanici':
			text5 = '\n\t Kullanici : {} {}\n\t Asistan ismi : {}\n\t'
			print("kullanici bilgileri siralaniyor..\n\n", "\t", '=' * 25, text5.format(user.isim, hitap, user.assistant), "=" * 25, "\n")
	
		elif komut == 'komutlar':
			sayac = 0
			text4 = 'kullanilabilir komutlar:\n\t ===================================\n\t '
			for a in charset:
				sayac = sayac + 1
				text4 = text4 + a 
				text4 = text4 + '  '
				if sayac%4 == 0:
					text4 = text4 + '\n\t '
			print(__main__.G + text4 + __main__.B, "\n\t",G + '=' * 35 + B)
		elif komut == 'saat':
			zaman = time.ctime()
			print("\n\n\t", '=' * 25,"\n\t", zaman, "\n\t", '=' * 25, "\n\n")

		elif komut == 'credits':
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




		elif komut == 'cikis':
			sys.exit()
		
		elif komut == 'config':
			config.runtime()
		else:
		 print("komut bulunamadi.")
			
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

	
