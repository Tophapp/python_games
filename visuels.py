import os
cha = input("Select A Charicter: ")




#Set the initial game grid size
GridWidth = 10
GridHeight = 20

#Declase a new array that is the game grid
GameGrid = []

# loop through each row - this will create a 2 dimentional array
for i in range(GridHeight):
    GridRow = []

    #Loop though each column and initialize it to '*'
    for j in range(GridWidth):
        GridRow.append("*")

    #Add the new row to the game grid
    GameGrid.append(GridRow)

#starting position
StartXPos = (GridWidth - 1) // 2
StartYPos = (GridHeight - 1) // 2

GameGrid[StartXPos][StartYPos] = "p"

x1 = "*"
x2 = "*"
x3 = "*"
x4 = "*"
x5 = "*"
x6 = cha
x7 = "*"
x8 = "*"
y1 = "*"
y2 = "*"
y3 = "*"
y4 = "*"
y5 = "*"
y6 = "*"
y7 = "*"
y8 = "*"
c1 = "*"
c2 = "*"
c3 = "*"
c4 = "*"
c5 = "*"
c6 = "*"
c7 = "*"
c8 = "*"
cs = [c1,c2,c3,c4,c5,c6,c7,c8]
xs = [x1,x2,x3,x4,x5,x6,x7,x8]
ys = [y1,y2,y3,y4,y5,y6,y7,y8]
roomnum = 1
print(c1,c2,c3,c4,c5,c6,c7,c8)
print(y1,y2,y3,y4,y5,y6,y7,y8)
print(f"{x1} {x2} {x3} {x4} {x5} {x6} {x7} {x8}")
def checurpos (x1,x2,x3,x4,x5,x6,x7,x8,look):
    pospos = []
    pospos.append(x1)
    pospos.append(x2)
    pospos.append(x3)
    pospos.append(x4)
    pospos.append(x5)
    pospos.append(x6)
    pospos.append(x7)
    pospos.append(x8)
    return pospos.index(look)
for y in range(1,2000):
    move = input("")

    if move == "right"or  move == "d":
        if roomnum == 1:
            pos = checurpos(x1,x2,x3,x4,x5,x6,x7,x8,cha)
            xs[pos] = "*"
            xs[pos + 1] = cha
            x1 = xs[1-1]
            x2 = xs[2-1]
            x3 = xs[3-1]
            x4 = xs[4-1]
            x5 = xs[5-1]
            x6 = xs[6-1]
            x7 = xs[7-1]
            x8 = xs[8-1]
        elif roomnum == 2:
            pos = checurpos(y1,y2,y3,y4,y5,y6,y7,y8,cha)
            ys[pos] = "*"
            ys[pos + 1] = cha
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
        elif roomnum == 3:
            pos = checurpos(c1,c2,c3,c4,c5,c6,c7,c8,cha)
            cs[pos] = "*"
            cs[pos + 1] = cha
            c1 = cs[1-1]
            c2 = cs[2-1]
            c3 = cs[3-1]
            c4 = cs[4-1]
            c5 = cs[5-1]
            c6 = cs[6-1]
            c7 = cs[7-1]
            c8 = cs[8-1]
    
    if move == "left" or move == "a":
        if roomnum == 1:
            pos = checurpos(x1,x2,x3,x4,x5,x6,x7,x8,cha)
            xs[pos] = "*"
            xs[pos - 1] = cha
            x1 = xs[1-1]
            x2 = xs[2-1]
            x3 = xs[3-1]
            x4 = xs[4-1]
            x5 = xs[5-1]
            x6 = xs[6-1]
            x7 = xs[7-1]
            x8 = xs[8-1]
        elif roomnum == 2:
            pos = checurpos(y1,y2,y3,y4,y5,y6,y7,y8,cha)
            ys[pos] = "*"
            ys[pos - 1] = cha
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
        elif roomnum == 3:
            pos = checurpos(c1,c2,c3,c4,c5,c6,c7,c8,cha)
            cs[pos] = "*"
            cs[pos - 1] = cha
            c1 = cs[1-1]
            c2 = cs[2-1]
            c3 = cs[3-1]
            c4 = cs[4-1]
            c5 = cs[5-1]
            c6 = cs[6-1]
            c7 = cs[7-1]
            c8 = cs[8-1]

    if move == "dashright" or move == " d":
        if roomnum == 1:
            pos = checurpos(x1,x2,x3,x4,x5,x6,x7,x8,cha)
            xs[pos] = "*"
            xs[pos + 2] = cha
            x1 = xs[1-1]
            x2 = xs[2-1]
            x3 = xs[3-1]
            x4 = xs[4-1]
            x5 = xs[5-1]
            x6 = xs[6-1]
            x7 = xs[7-1]
            x8 = xs[8-1]
        elif roomnum == 2:
            pos = checurpos(y1,y2,y3,y4,y5,y6,y7,y8,cha)
            ys[pos] = "*"
            ys[pos + 2] = cha
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
        elif roomnum == 3:
            pos = checurpos(c1,c2,c3,c4,c5,c6,c7,c8,cha)
            cs[pos] = "*"
            cs[pos + 2] = cha
            c1 = cs[1-1]
            c2 = cs[2-1]
            c3 = cs[3-1]
            c4 = cs[4-1]
            c5 = cs[5-1]
            c6 = cs[6-1]
            c7 = cs[7-1]
            c8 = cs[8-1]

    if move == "dashleft" or move == " a":
        if roomnum == 1:
            pos = checurpos(x1,x2,x3,x4,x5,x6,x7,x8,cha)
            xs[pos] = "*"
            xs[pos - 2] = cha
            x1 = xs[1-1]
            x2 = xs[2-1]
            x3 = xs[3-1]
            x4 = xs[4-1]
            x5 = xs[5-1]
            x6 = xs[6-1]
            x7 = xs[7-1]
            x8 = xs[8-1]
        elif roomnum == 2:
            pos = checurpos(y1,y2,y3,y4,y5,y6,y7,y8,cha)
            ys[pos] = "*"
            ys[pos - 2] = cha
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
        elif roomnum == 3:
            pos = checurpos(c1,c2,c3,c4,c5,c6,c7,c8,cha)
            cs[pos] = "*"
            cs[pos - 2] = cha
            c1 = cs[1-1]
            c2 = cs[2-1]
            c3 = cs[3-1]
            c4 = cs[4-1]
            c5 = cs[5-1]
            c6 = cs[6-1]
            c7 = cs[7-1]
            c8 = cs[8-1]

    if move == "up" or move == "w":
        if roomnum == 1:
            pos = checurpos(x1,x2,x3,x4,x5,x6,x7,x8,cha)
            ys[pos] = cha
            xs[pos] = "*"
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
            x1 = xs[1-1]
            x2 = xs[2-1]
            x3 = xs[3-1]
            x4 = xs[4-1]
            x5 = xs[5-1]
            x6 = xs[6-1]
            x7 = xs[7-1]
            x8 = xs[8-1]
            roomnum = 2
        elif roomnum == 2:
            pos = checurpos(y1,y2,y3,y4,y5,y6,y7,y8,cha)
            cs[pos] = cha
            ys[pos] = "*"
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
            c1 = cs[1-1]
            c2 = cs[2-1]
            c3 = cs[3-1]
            c4 = cs[4-1]
            c5 = cs[5-1]
            c6 = cs[6-1]
            c7 = cs[7-1]
            c8 = cs[8-1]
            roomnum = 3

    if move == "down" or move == "s":
        if roomnum == 2:
            pos = checurpos(y1,y2,y3,y4,y5,y6,y7,y8,cha)
            ys[pos] = "*"
            xs[pos] = cha
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
            x1 = xs[1-1]
            x2 = xs[2-1]
            x3 = xs[3-1]
            x4 = xs[4-1]
            x5 = xs[5-1]
            x6 = xs[6-1]
            x7 = xs[7-1]
            x8 = xs[8-1]
            roomnum = 1
        if roomnum == 3:
            pos = checurpos(c1,c2,c3,c4,c5,c6,c7,c8,cha)
            cs[pos] = "*"
            ys[pos] = cha
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
            c1 = cs[1-1]
            c2 = cs[2-1]
            c3 = cs[3-1]
            c4 = cs[4-1]
            c5 = cs[5-1]
            c6 = cs[6-1]
            c7 = cs[7-1]
            c8 = cs[8-1]
            roomnum = 2
    os.system('cls')

    print("Don't Go Beyond The Border")
    print(c1,c2,c3,c4,c5,c6,c7,c8)
    print(y1,y2,y3,y4,y5,y6,y7,y8)
    print(x1,x2,x3,x4,x5,x6,x7,x8)

    '''for i in range(GridHeight):
        PrintRow = ""

        for j in range(GridWidth):
            PrintRow += GameGrid[i][j] + " "

        print(PrintRow)'''
'''
            y1 = ys[1-1]
            y2 = ys[2-1]
            y3 = ys[3-1]
            y4 = ys[4-1]
            y5 = ys[5-1]
            y6 = ys[6-1]
            y7 = ys[7-1]
            y8 = ys[8-1]
            x1 = xs[1-1]
            x2 = xs[2-1]
            x3 = xs[3-1]
            x4 = xs[4-1]
            x5 = xs[5-1]
            x6 = xs[6-1]
            x7 = xs[7-1]
            x8 = xs[8-1]
            c1 = cs[1-1]
            c2 = cs[2-1]
            c3 = cs[3-1]
            c4 = cs[4-1]
            c5 = cs[5-1]
            c6 = cs[6-1]
            c7 = cs[7-1]
            c8 = cs[8-1]






'''