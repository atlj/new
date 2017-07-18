from terminaltables import AsciiTable
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
import mailconfig
import asistanmail
import helper
import game
import menu





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
	
charset = ['gui','menu', 'saat', 'komutlar', 'cikis', 'kullanici', 'sifirla', 'help', 'merhaba','2048', 'credits', 'version', 'hesap', 'clear','tara','androidpy','crypter','decrypter', 'bilgiler', 'figlet','internet', 'ls', 'exit','email','chatserver','chatclient', 'config', 'delconf', 'email', 'mailconfig']
chb = ['komutlar', 'help', 'saat']
#olayin koptugu yer, kullanicidan aldigi komutu kutuphanesinde bulunan komutlarla karsilastirarak geribildirim verir.
def shell():
	global ip
	try:
		komut = input(text1)
		ip = __main__.localip		

		global textmain
		textmain = text2.format(user.assistant, user.isim, hitap)

		if komut == "gui":
		  komut =  charset[menu.create(charset)]
		  os.system("clear")
		  komut = "".join(komut)
		  
		if komut =="menu":
		  items = ["Cikis Yap", "Shell'e Don"]
		  sonuc = menu.create(items)
		  if sonuc == 0:
		    sys.exit()
		  if sonuc == 1:
		    pass
	
	
		if komut == 'figlet':
		  figlet.main()
		  
		if komut == "mailconfig":
		  mailconfig.main()
		  
		  	
		if komut== 'chatserver':
			asistchatserver.uygulama()

		if komut== 'chatclient':
			asistchatclient.uygulama()

		if komut == 'bilgiler':
			sysinfo.getos()

		if komut == 'iptest':
			print(ip)
			
		if komut == 'crypter':
		  crypter.main()
		  
		if komut == 'decrypter':
		  decrypter.main()
		
		if komut == '2048':
		  game.ana()
		 
		

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
		
		if komut == 'email':
		  asistanmail.main()

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
			print("sifirlama islemi icin (y) tusuna basin.")
			if input(">>") == "y":
			  sifir = ["Sifirla", "Iptal Et"]
			  donut = menu.create(sifir)
			  if donut == 0:
			    os.remove(__main__.config_dir)
			    print("basariyla sifirlandi.")
			    sys.exit()
			  else:
			    pass

		if komut == 'merhaba':
			textmerhaba = 'size de merhaba {} {}'
			print(text2.format(user.assistant, user.isim, hitap), textmerhaba.format(user.isim, hitap))
		
		if komut == 'kullanici':
			table_data = [['Kulanici','Asistan','Yuklu komutlar'],
			              [user.isim,user.assistant,len(charset)]]
			table = AsciiTable(table_data)
			print(table.table)
	
		if komut == 'komutlar':
		  komutaciklamalist=[]
		  komutlist= '\n\n'.join(charset)
		  for i in charset:
		     komutaciklamalist.append(helper.main(i))
		  komutaciklama='\n\n'.join(komutaciklamalist)
		  
		  
		    
		  tablo_verisi = [['Komut','Aciklama'],[komutlist,komutaciklama]]
		  table = AsciiTable(tablo_verisi)
		  print(table.table)
			    
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
	  items = ["Cikis Yap", "Shell'e Don"]
	  sonuc = menu.create(items)
	  if sonuc == 0:
	    sys.exit()
	  if sonuc == 1:
	    shell()


	
