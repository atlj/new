from configparser import SafeConfigParser
import os
import shell
import __main__
from terminaltables import AsciiTable

#Console Colors
B = '\033[0m'
G = '\033[32m'
R = '\033[31m'
C = '\033[36m'
W = '\033[0m'
P = '\033[35m' 
PE = '\x1b[6;36;40m'
WE = '\x1b[0m'

config2 = SafeConfigParser()
directory = os.path.dirname(os.path.realpath(__file__))
real_directory = directory + '/'
config_dirtoformat = '{}/options.ini'
config_dir = config_dirtoformat.format(directory)
succes = 'ayar basariyla uygulandi!'

def load():
	global figlet
	global androidpy
	if not os.path.isfile(config_dir):
		dosya = open(config_dir, 'w')
		config2.read(config_dir)
		config2.add_section('config')
		config2.set('config', 'figlet', 'tek')
		config2.set('config', 'androidpy', 'lan')
		config2.write(dosya) 
	config2.read(config_dir)
	figlet = config2.get('config', 'figlet')
	androidpy = config2.get('config', 'androidpy')


def runl():
	column1 = 'Figlet\nAndroidpy'
	column2 = '     ' + figlet + '\n' + '     ' + androidpy
	column3 = '[0]\n[1]'
	tabledata = [
		['Modul', 'Su Anki Ayari', 'Index'], [column1, column2, column3]]
	table = AsciiTable(tabledata)
	print(shell.textmain, "lutfen degistirmek istediginiz ayarin yanindaki Index degerini giriniz menu icin " + C + "\"ctrl + c\""+ W + " tuslarina basiniz.")
	print("\t", table.table)
	
	
	
	
def main():
	try:	
		listen = int(input(P+'config >> '+W))
	except ValueError:
		print(shell.textmain, R + "lutfen dogru bir deger giriniz." + W)
		main()
	if not listen:
		print(shell.textmain, "lutfen figlet icin deger seciniz tek/coklu")
		cc = input(P+'config >> '+W)
		if cc == 'tek':
			setter('figlet', 'tek')
			print(G + succes + B)
		elif cc == 'coklu':
			setter('figlet', 'coklu')
			print(G + succes + B)
		else:
			print(shell.textmain, R + "yanlis bir deger girdiniz.\n" + W)
			main()

	if listen:
		print(shell.textmain, "lutfen androidpy icin bir ayar ekleyin wan/lan")
		cc = input(P+'config >> '+W)
		if cc == 'wan':
			setter('androidpy', 'wan')
			print(G + succes + B)
		elif cc == 'lan':
			setter('androidpy', 'lan')
			print(G + succes + B)
		else:
			print(shell.textmain, R + "yanlis bir deger girdiniz.\n" + W)
			runtime()
		
	
def setter(opt, value):
	config2.read(config_dir)
	config2.set('config', opt, value)
	dosya2 = open(config_dir, 'w')
	config2.write(dosya2)
	
def runtime():
	load()
	runl()
	main()
	
			


