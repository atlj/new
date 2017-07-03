import os


#coder:easyly
#startdart burakgunerasistant module

# Consol Renkleri
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # Mor
C = '\033[36m'  # Cyan
GR = '\033[37m'  # Gri




def check_net():
    hostname = "google.com" #example
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        print(G+"Internet e baglisiniz ! "+W)
    else:
        print(R+"internete e bagli degilsiniz !"+W)
  
