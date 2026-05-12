import curses
import random

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
bush = "❋"
rock = "∎"
grass= "·"
begin_x = 0; begin_y = 0
height = 10; width = 20
win = curses.newwin(height, width, begin_y, begin_x)
curses.curs_set(False)
screen.nodelay(True)
rot = 1
x,y = 0,0
terrain = []
def mine(x1,y1):
    index = 0
    terrain2 = terrain.copy()
    for m in range(height*2+1):
        for m2 in range(width+1):
            index+=1
            if terrain[index-1] == rock:
                if m == y1 and m2==x1:
                    terrain2[index-1] = grass
                    
                    return terrain2
    return terrain2

def getwall(x1,y1):
    index = 0
    for m in range(height):
        for m2 in range(width+1):
            index+=1
            if terrain[index-1] == bush:
                if m == y1 and m2==x1:
                    return True
            elif terrain[index-1] == rock:
                if m == y1 and m2==x1:
                    return True
    return False

for b in range(height*2+1):
    for b2 in range(width+1):
        if random.random()>0.2:
            terrain.append(grass)
        elif random.random()>0.7:
            terrain.append(bush)
        else:
            terrain.append(rock)

while True:
    c = screen.getch()
    if c == ord('d') and x<width and getwall(x+1,y) != True:
        x+=1
        rot = 3
    elif c == ord('a') and x>0 and getwall(x-1,y) != True:
        x-=1
        rot = 1
    elif c == ord('w') and y>0 and getwall(x,y-1) != True:
        y-=1
        rot = 2
    elif c == ord('s') and y<height-1 and getwall(x,y+1) != True:
        y+=1
        rot = 4
    if c == ord('d'):
        rot = 3
    elif c == ord('a'):
        rot = 1
    elif c == ord('w'):
        rot = 2
    elif c == ord('s'):
        rot = 4
    elif c == ord('-'):
        print("Flatline: You Quit The Game")
        break  # Exit the while loop
    if c == ord(" "):
        if rot == 1:
            terrain =mine(x-1,y)
        elif rot == 2:
            terrain = mine(x,y-1)
        elif rot == 3:
            terrain =mine(x+1,y)
        elif rot == 4:
            terrain =mine(x,y+1)
        screen.erase()
    ind = 0
    for b in range(height):
        for b2 in range(width+1):
            ind+=1
            if b2 != x or b != y:
                screen.addstr(b,b2,terrain[ind-1])
    if rot == 1:
        screen.addstr(y,x,"◁")
    elif rot == 2:
        screen.addstr(y,x,"△")
    elif rot == 3:
        screen.addstr(y,x,"▷")
    elif rot == 4:
        screen.addstr(y,x,"▽")
    screen.refresh()

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()