import os
import shell
import config

# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri


def check_figlet():
    list=os.listdir("/usr/bin")
    konrtol=list.count("figlet")
    if konrtol==1:
        pass
    else:
        print("Figlet sistemde yuklu degil !! 'apt-get install figlet' yazarak yukleyebilirsiniz.")
        shell.shell()
        
    
    
    
def main():
	config.load()
	check_figlet()
	print(P+shell.textmain,"lutfen ascii art yapmak istediginiz metni giriniz") 
	txt = input(O+"[FIGLET]==>"+C)
	figlettxt = 'figlet {}'
	print(shell.textmain, "\n", os.popen(figlettxt.format(txt)).read(), "\n"+W)
	if config.figlet == 'tek':
		shell.shell()
	elif config.figlet == 'coklu':
		main() 

if __name__ == '__main__':
	  main()
	
