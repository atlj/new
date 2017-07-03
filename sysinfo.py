import platform
import os
import time

#coder:easyly
#startdart burakgunerassistan module


def getos():
    dagitim=platform.dist()
    dagitim=dagitim[0]
    mimari=platform.machine()
    osys=platform.system()
    unumber = os.getuid()
    zaman=time.ctime()
    if unumber==0:
        kulanici="root"
    else:
        kulanici="No root"
    
    
    bilgi="""
        ============================
        CPU: {}
        OS: {}
        DAGITIM: {}
        KULANICI: {}
        ZAMAN: {}
       ============================""".format(mimari,osys,dagitim,kulanici,zaman)
    print(bilgi)
    
        
        
        
    
        
        
    
    
    
   
    
