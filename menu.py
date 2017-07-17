import curses
import os

def create(liste):
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)
    s = curses.color_pair(1)
    h = curses.A_NORMAL
    pos = 0

    while 1:
        curses.noecho()
        screen.clear()
        screen.border(0)
        screen.keypad(True)
        screen.addstr(1,2,"(w)Yukari/Up (s)Asagi/Down (e)Sec", curses.A_BOLD)
        a = 0
        b = 4
        c = 3
        for oge in liste:
            if int(a/15)<1:
                if pos == a:
                    screen.addstr(b, 4, "".join(liste[a]), s)
                else:
                    screen.addstr(b, 4, "".join(liste[a]), h)
            else:
                c = c + 1
                if pos == a:
                    screen.addstr(c, 23, "".join(liste[a]), s)
                else:
                    screen.addstr(c, 23, "".join(liste[a]), h)
            
            
            a = a + 1
            b = b + 1
        screen.refresh()
        try:
            inp = screen.getkey(1,1)
        
            if inp == 'e':
                screen.refresh()
                curses.echo()
                screen.keypad(False)
                curses.endwin()
                break
            if inp == 'w':
                if pos > 0:
                    pos = pos - 1
                else:
                    pos = len(liste)-1
            if inp== 's':
                if pos < len(liste)-1:
                    pos = pos + 1
                else:
                    pos=0
        except Exception as e:
            pass
    return pos
    
if __name__=="__main__":
    list = input("ogeleri giriniz.").split(" ")
    print(list[create(list)]+" secenegini sectiniz.")
