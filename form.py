#-*-coding:utf8;-*-
import curses
import os
def create(formadi,liste):
    global isim
    global asistan
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    s = curses.color_pair(1)
    h = curses.A_NORMAL
    pos = 0
    gl = "________ "*len(liste)
    liste2 = gl.split(" ")
    select = 0
    while 1:
        b = 4
        a = 0
        f = 4
        d = 0
        screen.clear()
        screen.border(0)
        screen.refresh()
        screen.addstr(1,1,formadi, curses.A_BOLD)
        screen.addstr(2,1,"(w)Yukari (s)Asagi (e)Sec (c)Devam Et")
        screen.addstr(pos + 4, 1, "-->")
        for oge in liste:
            if pos == a:
                screen.addstr(b, 5, liste[a], s)
            else:
                screen.addstr(b,5,liste[a], h)
            a = a + 1
            b = b + 1
        for oge in liste2:
            if pos == d:
                screen.addstr(f,24,liste2[d])
                if select ==1:
                    liste2[d] = screen.getstr(f, 24).decode("utf-8")
                    select = 0
            else:
                screen.addstr(f, 24, liste2[d])
            f = f + 1
            d = d + 1
        curses.noecho()
        screen.keypad(True)
        try:
            getkey = screen.getkey(15,1)
        except Exception as e:
            pass
        curses.echo()
        screen.keypad(False)
        if getkey == "w":
            if pos > 0:
                pos = pos - 1
            else:
                pos = len(liste)-1
        if getkey == "s":
            if pos < len(liste)-1:
                pos = pos + 1
            else:
                pos = 0
        if getkey == "e":
            select = 1
        if getkey == "c":
            break
        
        
                
           
    screen.refresh()
    curses.endwin()
    curses.echo()
    os.system("clear")
    return liste2

if __name__ == "__main__":
    form = input("//")
    liste = input(">>").split(" ")
    print(create(form, liste))