import shell

textislemiste = '{} \ntoplama icin\t(1)\ncikarma icin\t(2)\ncarpma icin\t(3)\nbolme icin\t(4)\n: '
textilk = '{} lutfen ilk sayiyi giriniz.\n: '
textikinci = '{} lutfen ikinci sayiyi giriniz.\n: '

class sayilar():
	sayi1 = ''
	sayi2 = ''
	islem = ''
	isaret = ''
	sonuc = ''


def islemiste():
	try:
		sayilar.islem = int(input(textislemiste.format(shell.textmain)))
	except ValueError:
		print(shell.textmain, "lutfen bir islem belirtiniz")
		shell.shell()
def sayi1al():
	try:
		sayilar.sayi1 = int(input(textilk.format(shell.textmain)))
	except ValueError:
		print(shell.textmain, "lutfen bir sayi giriniz.")
		shell.shell()

def sayi2al():
	try:
		sayilar.sayi2 = int(input(textikinci.format(shell.textmain)))
	except ValueError:
		print(shell.textmain, "lutfen bir sayi giriniz.")
		shell.shell()
def hesapla():
	if sayilar.islem == 1:
		sayilar.sonuc = sayilar.sayi1 + sayilar.sayi2
	elif sayilar.islem == 2:
		sayilar.sonuc = sayilar.sayi1 - sayilar.sayi2
	elif sayilar.islem == 3:
		sayilar.sonuc = sayilar.sayi1 * sayilar.sayi2
	elif sayilar.islem == 4:
		try:
			sayilar.sonuc = sayilar.sayi1 / sayilar.sayi2
		except ZeroDivisionError:
			print(shell.textmain, "sifira bolum yapamazsiniz.")
			shell.shell()
	else:
		print("debug error")

def yazdir():
	metin = 'cevap = {}'
	print(shell.textmain, metin.format(sayilar.sonuc))

def main():
	islemiste()
	sayi1al()
	sayi2al()
	hesapla()
	yazdir()

if __name__ == '__main__':
	main()
		


