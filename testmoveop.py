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

x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8 = cha,"*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"

cs = [c1,c2,c3,c4,c5,c6,c7,c8]
xs = [x1,x2,x3,x4,x5,x6,x7,x8]
ys = [y1,y2,y3,y4,y5,y6,y7,y8]
ss = [x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8]

def getpos (q1,q2,q3,q4,q5,q6,q7,q8,w1,w2,w3,w4,w5,w6,w7,w8,e1,e2,e3,e4,e5,e6,e7,e8,r1,r2,r3,r4,r5,r6,r7,r8,look):
    pospos = []
    pospos.append(q1)
    pospos.append(q2)
    pospos.append(q3)
    pospos.append(q4)
    pospos.append(q5)
    pospos.append(q6)
    pospos.append(q7)
    pospos.append(q8)
    pospos.append(w1)
    pospos.append(w2)
    pospos.append(w3)
    pospos.append(w4)
    pospos.append(w5)
    pospos.append(w6)
    pospos.append(w7)
    pospos.append(w8)
    pospos.append(e1)
    pospos.append(e2)
    pospos.append(e3)
    pospos.append(e4)
    pospos.append(e5)
    pospos.append(e6)
    pospos.append(e7)
    pospos.append(e8)
    pospos.append(r1)
    pospos.append(r2)
    pospos.append(r3)
    pospos.append(r4)
    pospos.append(r5)
    pospos.append(r6)
    pospos.append(r7)
    pospos.append(r8)
    return pospos.index(look)

roomnum = 1
print(r1,r2,r3,r4,r5,r6,r7,r8)
print(c1,c2,c3,c4,c5,c6,c7,c8)
print(y1,y2,y3,y4,y5,y6,y7,y8)
print(f"{x1} {x2} {x3} {x4} {x5} {x6} {x7} {x8}")
def chepos(x1,x2,x3,x4,x5,x6,x7,x8,cha):
    pospos = []
    pospos.append(x1)
    pospos.append(x2)
    pospos.append(x3)
    pospos.append(x4)
    pospos.append(x5)
    pospos.append(x6)
    pospos.append(x7)
    pospos.append(x8)
    if cha in pospos:
        return pospos.index(cha)

for y in range(1,2000):
    move = input("")
    if chepos(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],cha) != None:
        roomnum =  1
    elif chepos(ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],cha) != None:
        roomnum = 2
    elif chepos(ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],cha) != None:
        roomnum = 3
    elif chepos(ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30],cha) != None:
        roomnum = 4

    if move == "right"or  move == "d":
        pos = getpos(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30],cha)
        ss[pos] = "*"
        ss[pos + 1] = cha
        x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8 = ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30]
    
    if move == "left" or move == "a":

        pos = getpos(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30],cha)
        ss[pos] = "*"
        ss[pos - 1] = cha
        x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8 = ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30]

    if move == "dashright" or move == "dd":
        pos = getpos(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30],cha)
        ss[pos] = "*"
        ss[pos + 2] = cha
        x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8 = ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30]

    if move == "dashleft" or move == "aa":
        pos = getpos(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30],cha)
        ss[pos] = "*"
        ss[pos - 2] = cha
        x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8 = ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30]
    if move == "up" or move == "w":
        pos = getpos(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30],cha)
        ss[pos] = "*"
        ss[pos +8] = cha
        x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8 = ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30]
    if move == "down" or move == "s":
        pos = getpos(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30],cha)
        ss[pos] = "*"
        ss[pos - 8] = cha
        x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,c1,c2,c3,c4,c5,c6,c7,c8,r1,r2,r3,r4,r5,r6,r7,r8 = ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9],ss[10],ss[11],ss[12],ss[13],ss[14],ss[15],ss[16],ss[17],ss[18],ss[19],ss[20],ss[21],ss[22],ss[23],ss[24],ss[25],ss[26],ss[26],ss[27],ss[28],ss[29],ss[30]
    os.system('cls')
    print("THE COLLECTOR")
    print("Don't Go Beyond The Border")
    print(r1,r2,r3,r4,r5,r6,r7,r8)
    print(c1,c2,c3,c4,c5,c6,c7,c8)
    print(y1,y2,y3,y4,y5,y6,y7,y8)
    print(x1,x2,x3,x4,x5,x6,x7,x8)
#ss[1]ss[2]ss[3]ss[4]ss[5]ss[6]ss[7]ss[8]ss[9]ss[10]ss[11]ss[12]ss[13]ss[14]ss[15]ss[16]ss[17]ss[18]ss[19]ss[20]ss[21]ss[22]ss[23]