#-*-coding:utf8;-*-
import curses
import os
def create():
    global isim
    global asistan
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    pos = 0
    isim = ""
    asistan = ""
    while 1:
        screen.addstr(1,4,"Adiniz:")
        screen.addstr(4,4,"Asistan Adi:")
        screen.addstr(7,2,"(w)Yukari (s)Asagi (e)Sec (c)Devam et")
        try:
            if pos == 0:
                screen.addstr(1,4,">Adiniz:")
                screen.keypad(True)
                curses.noecho()
                getkey = screen.getkey(10,5)
                screen.keypad(False)
                curses.echo()
                if getkey == "w":
                    if pos > 0:
                        pos = pos - 1
                    else:
                        pos = 1
                if getkey == 's':
                    if pos <1:
                        pos = pos + 1
                    else:
                        pos = 0
                if getkey == 'e':
                    isim = screen.getstr(1,24).decode("utf-8")
                if getkey == 'c':
                    break
            if pos == 1:
                screen.addstr(1,4,"Adiniz:")
                screen.addstr(1,24,isim)
                screen.addstr(4,4,">Asistan Adi:")
                screen.keypad(True)
                curses.noecho()
                getkey = screen.getkey(10,5)
                screen.keypad(False)
                curses.echo()
                if getkey == "w":
                    if pos > 0:
                        pos = pos - 1
                    else:
                        pos = 1
                if getkey == 's':
                    if pos <1:
                        pos = pos + 1
                    else:
                        pos = 0
                if getkey == 'e':
                    asistan = screen.getstr(4,24 ).decode("utf-8")
                if getkey == 'c':
                    break
            else:
                screen.addstr(4,4,"Asistan Adi:")
                screen.addstr(4,24,asistan)
        except Exception as a:
            pass
    screen.refresh()
    curses.endwin()
    curses.echo()
    return isim, asistan