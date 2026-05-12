import pygame
import math
import random

pygame.init()

#id (#,Type, 1=powder,2=liquid) Empty = 0,Sand =11,water = 12
idtocolor = {11:(226, 202, 118),12:(0,94,184),13:(146, 142, 133),14:(89,58,14),15:(232,233,229),16:(39,18,1),23:(168,204,215),26:(255, 105, 41),24:(230, 180, 0),999:(255, 105, 41),899:(185,232,234),9999:(255, 105, 41),8999:(185,232,234)}
ids  = [11,12,13,14,15,16,26,23,24,999,899,9999,8999]
names =["Sand","Water","Stone","Dirt","Steam","Mud","M Glass","Glass","W Sand","Heat","Cool","S Heat", "S Cool"]
fontcolor = {11:(255,255,255),12:(255,255,255),13:(255,255,255),14:(255,255,255),15:(0,0,0),16:(255,255,255),23:(0,0,0),26:(0,0,0),24:(0,0,0),999:(0,0,0),899:(0,0,0),9999:(0,0,0),8999:(0,0,0)}
heatval = {11:0,12:-25,13:0,14:0,15:150,16:-10,23:0,26:350,24:-5}
height = 100
width =100
psize = 7
new = []
grid = []
cid = 11
htrans=0.02
elnum = len(ids)
thickprob = 0.1
thickprob = 1-thickprob
F = 1
theat = 5
sheat = 15
bwid, bhei = 50,50
font = "Comic San MS"
myFont = pygame.font.SysFont(font, 20)

class button():
    def __init__(self,x,y,idt):
        self.id = idt
        self.x = x 
        self.y = y
        self.width = bwid
        self.height = bhei
        self.text =names[ids.index(self.id)]
        self.color = idtocolor[self.id]
    
    def draw(self):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        text_surface_start = myFont.render(self.text,True,fontcolor[self.id])
        surface.blit(text_surface_start, (self.x+self.width/20,self.y+self.height/2-5))

    def click(self):
        selid = None
        if mouse_x > self.x and mouse_x < self.x+self.width:
            if mouse_y > self.y and mouse_y < self.y+self.height:
                selid = self.id
        return selid
        

for y in range(1,height+1):
    row = []
    for x in range(1,width+1):
        row.append(0)
    grid.append(row)
heat= []
for y in range(1,height+1):
    row = []
    for x in range(1,width+1):
        row.append(0)
        heat.append(row)

def getneigbors(heaton,xx,yy):
    neigborsy = []
    if heaton == True:
        if yy < height-1:
            neigborsy.append(heat[yy+1][xx])
        else:
            neigborsy.append(0)
        if yy > 0:
            neigborsy.append(heat[yy-1][xx])
        else:
            neigborsy.append(0)
        if xx < width-1:
            neigborsy.append(heat[yy][xx+1])
        else:
            neigborsy.append(0)
        if xx > 0:
            neigborsy.append(heat[yy][xx-1])
        else:
            neigborsy.append(0)
    else:
        if yy < height-1:
            neigborsy.append(grid[yy+1][xx])
        else:
            neigborsy.append(0)
        if yy > 0:
            neigborsy.append(grid[yy-1][xx])
        else:
            neigborsy.append(0)
        if xx < width-1:
            neigborsy.append(grid[yy][xx+1])
        else:
            neigborsy.append(0)
        if xx > 0:
            neigborsy.append(grid[yy][xx-1])
        else:
            neigborsy.append(0)
    return neigborsy


def update():
    hmap=[]
    o= []
    for y in range(1,height+1):
        row = []
        for x in range(1,width+1):
            row.append(0)
        o.append(row)
    for y in range(1,height+1):
        row = []
        for x in range(1,width+1):
            row.append(0)
        hmap.append(row)

    for y in range(0,height):
        for x in range(0,width):
            if grid[y][x] != 0:
                temp = 0
                direction = random.random()
                direction2 = random.random()
                if 1==1:
                    #sand
                    if grid[y][x] - math.floor(grid[y][x]/10)*10 == 1:
                        if y < height-2 and grid[y][x] - round(grid[y][x]/10)*10 == 1 and o[y+1][x]== 0 and o[y][x] == 0 and grid[y+1][x] - round(grid[y+1][x]/10)*10 != 1 and grid[y+1][x] - round(grid[y+1][x]/10)*10 != 3 and grid[y+1][x] - round(grid[y+1][x]/10)*10 != 4 and grid[y+1][x] - round(grid[y+1][x]/10)*10 != 3 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 6:
                            o[y][x] = grid[y+1][x]
                            o[y+1][x] = grid[y][x]
                            temp = heat[y][x]
                            hmap[y][x] = heat[y+1][x]
                            hmap[y+1][x] = temp
                        elif  y < height-2 and x < width-1 and grid[y][x] - round(grid[y][x]/10)*10 == 1 and o[y+1][x+1]== 0 and o[y+1][x+1] == 0 and grid[y+1][x+1] - round(grid[y+1][x+1]/10)*10 != 1 and direction> 0.5 and grid[y+1][x+1] - round(grid[y+1][x+1]/10)*10 != 3 and grid[y+1][x+1] - round(grid[y+1][x+1]/10)*10 != 4 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 6:
                            temp = grid[y][x]
                            o[y][x] = grid[y+1][x+1]
                            o[y+1][x+1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y+1][x+1]
                            hmap[y+1][x+1] = temp
                        elif y < height-2 and x > 0 and grid[y][x] - round(grid[y][x]/10)*10 == 1 and o[y+1][x-1]== 0 and o[y+1][x-1] == 0 and grid[y+1][x-1] - round(grid[y+1][x-1]/10)*10 != 1 and direction> 0.5 and grid[y+1][x-1] - round(grid[y+1][x-1]/10)*10 != 3 and grid[y+1][x-1] - round(grid[y+1][x-1]/10)*10 != 4 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 6:
                            temp = grid[y][x]
                            o[y][x] = grid[y+1][x-1]
                            o[y+1][x-1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y+1][x-1]
                            hmap[y+1][x-1] = temp
                        elif y < height-2 and  x > 0 and grid[y][x] - round(grid[y][x]/10)*10 == 1 and o[y+1][x-1]== 0 and o[y+1][x-1] == 0 and grid[y+1][x-1] - round(grid[y+1][x-1]/10)*10 != 1 and direction<= 0.5 and grid[y+1][x-1] - round(grid[y+1][x-1]/10)*10 != 3 and grid[y+1][x-1] - round(grid[y+1][x-1]/10)*10 != 4 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 6:
                            temp = grid[y][x]
                            o[y][x] = grid[y+1][x-1]
                            o[y+1][x-1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y+1][x-1]
                            hmap[y+1][x-1] = temp
                        elif y < height-2 and x < width-1 and grid[y][x] - round(grid[y][x]/10)*10 == 1 and o[y+1][x+1]== 0 and o[y+1][x+1] == 0 and grid[y+1][x+1] - round(grid[y+1][x+1]/10)*10 != 1 and direction<= 0.5 and grid[y+1][x+1] - round(grid[y+1][x+1]/10)*10 != 3 and grid[y+1][x+1] - round(grid[y+1][x+1]/10)*10 != 4 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 6:
                            temp = grid[y][x]
                            o[y][x] = grid[y+1][x+1]
                            o[y+1][x+1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y+1][x+1]
                            hmap[y+1][x+1] = temp
                        else:
                            if o[y][x] == 0: 
                                o[y][x] = grid[y][x] 
                                hmap[y][x] = heat[y][x] 

                    #dirt
                    elif grid[y][x] - math.floor(grid[y][x]/10)*10 == 4:
                        if y < height-2 and grid[y][x] - round(grid[y][x]/10)*10 == 4 and o[y+1][x]== 0 and o[y][x] == 0 and grid[y+1][x] - round(grid[y+1][x]/10)*10 != 1 and grid[y+1][x] - round(grid[y+1][x]/10)*10 != 3 and grid[y+1][x] - round(grid[y+1][x]/10)*10 != 4 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 6:
                            o[y][x] = grid[y+1][x]
                            o[y+1][x] = grid[y][x]
                            temp = heat[y][x]
                            hmap[y][x] = heat[y+1][x]
                            hmap[y+1][x] = temp
                        else:
                            if o[y][x] == 0: 
                                o[y][x] = grid[y][x] 
                                hmap[y][x] = heat[y][x] 
                    #steam
                    elif grid[y][x] - math.floor(grid[y][x]/10)*10 == 5:
                        if  y > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y-1][x]== 0 and o[y][x] == 0 and grid[y-1][x] - math.floor(grid[y-1][x]/10)*10 == 0:
                            temp = grid[y][x]
                            o[y][x] = grid[y-1][x]
                            o[y-1][x] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y-1][x]
                            hmap[y-1][x] = temp
                        elif  y > 0 and x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y-1][x+1]== 0 and o[y][x] == 0 and grid[y-1][x+1] - math.floor(grid[y-1][x+1]/10)*10 == 0 and direction2> 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y-1][x+1]
                            o[y-1][x+1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y-1][x+1]
                            hmap[y-1][x+1] = temp
                        elif  y > 0 and x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y-1][x-1]== 0 and o[y][x] == 0 and grid[y-1][x-1] - math.floor(grid[y-1][x-1]/10)*10 == 0 and direction2> 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y-1][x-1]
                            o[y-1][x-1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y-1][x-1]
                            hmap[y-1][x-1] = temp
                        elif  y > 0 and x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y-1][x-1]== 0 and o[y][x] == 0 and grid[y-1][x-1] - math.floor(grid[y-1][x-1]/10)*10 == 0 and direction2< 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y-1][x-1]
                            o[y-1][x-1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y-1][x-1]
                            hmap[y-1][x-1] = temp
                        elif  x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y][x-1]== 0 and o[y][x] == 0 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 == 0 and direction2< 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y][x-1]
                            o[y][x-1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y][x-1]
                            hmap[y][x-1] = temp
                        elif  y > 0 and x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y-1][x+1]== 0 and o[y][x] == 0 and grid[y-1][x+1] - math.floor(grid[y-1][x+1]/10)*10 == 0 and direction2< 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y-1][x+1]
                            o[y-1][x+1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y-1][x+1]
                            hmap[y-1][x+1] = temp
                        elif x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y][x+1]== 0 and o[y][x] == 0 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 == 0 and direction2> 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y][x+1]
                            o[y][x+1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y][x+1]
                            hmap[y][x+1] = temp
                        elif  x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y][x-1]== 0 and o[y][x] == 0 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 == 0 and direction2> 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y][x-1]
                            o[y][x-1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y][x-1]
                            hmap[y][x-1] = temp
                        elif x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 5 and o[y][x+1]== 0 and o[y][x] == 0 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 == 0 and direction2< 0.5:
                            temp = grid[y][x]
                            o[y][x] = grid[y][x+1]
                            o[y][x+1] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y][x+1]
                            hmap[y][x+1] = temp
                        else:
                            if o[y][x] == 0: 
                                o[y][x] = grid[y][x] 
                                hmap[y][x] = heat[y][x] 
                    #Water
                    elif grid[y][x] - math.floor(grid[y][x]/10)*10 == 2:
                        if ((y < height-2 and grid[y+1][x]== 0 and o[y+1][x]== 0 and y < height-2) or (y < height-2  and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 == 5 or  o[y+1][x] - math.floor(o[y+1][x]/10)*10 == 5 and y < height-2)) and (o[y][x] == 0 or  o[y][x] - math.floor(o[y][x]/10)*10 == 5):
                            temp = grid[y][x]
                            o[y][x] = grid[y+1][x]
                            o[y+1][x] = temp
                            temp = heat[y][x]
                            hmap[y][x] = heat[y+1][x]
                            hmap[y+1][x] = temp
                        elif 1==1:
                            if random.random() > 0.5:
                                if (y < height-2 and x < width-1 and grid[y][x+1]== 0 and o[y][x+1]== 0 and o[y][x] == 0 ) or (y < height-2 and x < width-1 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 == 5 and  o[y][x+1] - math.floor(o[y][x+1]/10)*10 == 5 and  o[y][x+1] - math.floor(o[y][x+1]/10)*10 == 5):
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x+1]
                                    o[y][x+1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x+1]
                                    hmap[y][x+1] = temp
                                elif (y < height-2 and x > 0 and grid[y][x-1]== 0 and o[y][x-1]== 0 and o[y][x] == 0 ) or (y < height-2 and x > 0 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 == 5 and  o[y][x-1] - math.floor(o[y][x-1]/10)*10 == 5 and  o[y][x-1] - math.floor(o[y][x-1]/10)*10 == 5):
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x-1]
                                    o[y][x-1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x-1]
                                    hmap[y][x-1] = temp
                                else:
                                    if o[y][x] == 0: 
                                        o[y][x] = grid[y][x] 
                                        hmap[y][x] = heat[y][x] 
                            else:
                                if (y < height-2 and x > 0 and grid[y][x-1] == 0 and o[y][x-1] == 0 and o[y][x] == 0 ) or  (y < height-2 and x > 0 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 == 5 and  o[y][x-1] - math.floor(o[y][x-1]/10)*10 == 5 and  o[y][x-1] - math.floor(o[y][x-1]/10)*10 == 5):
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x-1]
                                    o[y][x-1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x-1]
                                    hmap[y][x-1] = temp
                                elif (y < height-2 and x < width-1 and grid[y][x+1] == 0 and o[y][x+1] == 0 and o[y][x] == 0 ) or  (y < height-2 and x < width-1 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 == 5 and  o[y][x+1] - math.floor(o[y][x+1]/10)*10 == 5 and  o[y][x+1] - math.floor(o[y][x+1]/10)*10 == 5):
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x+1]
                                    o[y][x+1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x+1]
                                    hmap[y][x+1] = temp
                                else:
                                    if o[y][x] == 0: 
                                        o[y][x] = grid[y][x] 
                                        hmap[y][x] = heat[y][x] 
                        else:
                            print("FATAL MATH ERROR HAS OCCURED!!!  AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Please Replace This Computer's CPU!  It Thinks 1 Does Not Equal 1!!!!!!")
                    #thick liquid
                    elif grid[y][x] - math.floor(grid[y][x]/10)*10 == 6:
                        if 1==1:
                            if y < height-2 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y+1][x]== 0 and o[y][x] == 0 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 1 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 3 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 4 and grid[y+1][x] - math.floor(grid[y+1][x]/10)*10 != 6:
                                o[y][x] = grid[y+1][x]
                                o[y+1][x] = grid[y][x]
                                temp = heat[y][x]
                                hmap[y][x] = heat[y+1][x]
                                hmap[y+1][x] = temp
                            elif random.random() > thickprob:
                                if  y < height-2 and x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y+1][x+1]== 0 and o[y+1][x+1] == 0 and grid[y+1][x+1] - math.floor(grid[y+1][x+1]/10)*10 != 1 and direction> 0.5 and grid[y+1][x+1] - math.floor(grid[y+1][x+1]/10)*10 != 3 and grid[y+1][x+1] - math.floor(grid[y+1][x+1]/10)*10 != 4 and grid[y+1][x+1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y+1][x+1]
                                    o[y+1][x+1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y+1][x+1]
                                    hmap[y+1][x+1] = temp
                                elif y < height-2 and x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y+1][x-1]== 0 and o[y+1][x-1] == 0 and grid[y+1][x-1] - math.floor(grid[y+1][x-1]/10)*10 != 1 and direction> 0.5 and grid[y+1][x-1] - math.floor(grid[y+1][x-1]/10)*10 != 3 and grid[y+1][x-1] - math.floor(grid[y+1][x-1]/10)*10 != 4 and grid[y+1][x-1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y+1][x-1]
                                    o[y+1][x-1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y+1][x-1]
                                    hmap[y+1][x-1] = temp
                                elif y < height-2 and  x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y+1][x-1]== 0 and o[y+1][x-1] == 0 and grid[y+1][x-1] - math.floor(grid[y+1][x-1]/10)*10 != 1 and direction<= 0.5 and grid[y+1][x-1] - math.floor(grid[y+1][x-1]/10)*10 != 3 and grid[y+1][x-1] - math.floor(grid[y+1][x-1]/10)*10 != 4 and grid[y+1][x-1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y+1][x-1]
                                    o[y+1][x-1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y+1][x-1]
                                    hmap[y+1][x-1] = temp
                                elif y < height-2 and x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y+1][x+1]== 0 and o[y+1][x+1] == 0 and grid[y+1][x+1] - math.floor(grid[y+1][x+1]/10)*10 != 1 and direction<= 0.5 and grid[y+1][x+1] - math.floor(grid[y+1][x+1]/10)*10 != 3 and grid[y+1][x+1] - math.floor(grid[y+1][x+1]/10)*10 != 4 and grid[y+1][x+1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y+1][x+1]
                                    o[y+1][x+1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y+1][x+1]
                                    hmap[y+1][x+1] = temp
                                elif y < height-2 and  x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y][x-1]== 0 and o[y][x-1] == 0 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 != 1 and direction<= 0.5 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 != 3 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 != 4 and grid[y][x-1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x-1]
                                    o[y][x-1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x-1]
                                    hmap[y][x-1] = temp
                                elif y < height-2 and x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y][x+1]== 0 and o[y][x+1] == 0 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 != 1 and direction<= 0.5 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 != 3 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 != 4 and grid[y][x+1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x+1]
                                    o[y][x+1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x+1]
                                    hmap[y][x+1] = temp
                                elif y < height-2 and x < width-1 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y][x+1]== 0 and o[y][x+1] == 0 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 != 1 and direction> 0.5 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 != 3 and grid[y][x+1] - math.floor(grid[y][x+1]/10)*10 != 4 and grid[y][x+1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x+1]
                                    o[y][x+1] = temp 
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x+1]
                                    hmap[y][x+1] = temp
                                elif y < height-2 and  x > 0 and grid[y][x] - math.floor(grid[y][x]/10)*10 == 6 and o[y][x-1]== 0 and o[y][x-1] == 0 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 != 1 and direction> 0.5 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 != 3 and grid[y][x-1] - math.floor(grid[y][x-1]/10)*10 != 4 and grid[y][x-1] - math.floor(grid[y+1][x]/10)*10 != 6:
                                    temp = grid[y][x]
                                    o[y][x] = grid[y][x-1]
                                    o[y][x-1] = temp
                                    temp = heat[y][x]
                                    hmap[y][x] = heat[y][x-1]
                                    hmap[y][x-1] = temp
                                else:
                                    if o[y][x] == 0: 
                                        o[y][x] = grid[y][x] 
                                        hmap[y][x] = heat[y][x] 
                            else:
                                if o[y][x] == 0: 
                                    o[y][x] = grid[y][x] 
                                    hmap[y][x] = heat[y][x] 
                    else:
                        if o[y][x] == 0: 
                            o[y][x] = grid[y][x]
                            hmap[y][x] = heat[y][x] 
                heatneigbors = getneigbors(True,x,y)
                neigbors = getneigbors(False,x,y)
                if hmap[y][x] > 0:
                    hmap[y][x] -= htrans*4
                    if heatneigbors[0] < hmap[y][x] and neigbors[0] != 0:
                        hmap[y+1][x] +=htrans
                    if heatneigbors[1] < hmap[y][x] and neigbors[1] != 0:
                        hmap[y-1][x] +=htrans
                    if heatneigbors[2] < hmap[y][x] and neigbors[2] != 0:
                        hmap[y][x+1] +=htrans
                    if heatneigbors[3] < hmap[y][x] and neigbors[3] != 0:
                        hmap[y][x-1] +=htrans
                elif hmap[y][x] < 0:
                    if heatneigbors[0] > hmap[y][x] and neigbors[0] != 0:
                        hmap[y+1][x] -=htrans
                        hmap[y][x] += htrans
                    if heatneigbors[1] > hmap[y][x] and neigbors[1] != 0:
                        hmap[y-1][x] -=htrans
                        hmap[y][x] += htrans
                    if heatneigbors[2] > hmap[y][x] and neigbors[2] != 0:
                        hmap[y][x+1] -=htrans
                        hmap[y][x] += htrans
                    if heatneigbors[3] > hmap[y][x] and neigbors[3] != 0:
                        hmap[y][x-1] -=htrans
                        hmap[y][x] += htrans
                if o[y][x] == 23 and hmap[y][x] > 300:
                    o[y][x] = 26
                elif o[y][x] == 11 and hmap[y][x] > 300:
                    o[y][x] = 26
                elif o[y][x] == 26 and hmap[y][x] < 290:
                    o[y][x] = 23
                elif o[y][x] == 16 and hmap[y][x] > 100:
                    o[y][x] = 14
                elif o[y][x] == 24 and hmap[y][x] > 100:
                    o[y][x] = 11
                elif o[y][x] == 12 and hmap[y][x] > 100:
                    o[y][x] = 15
                elif o[y][x] == 15 and hmap[y][x] < 90:
                    o[y][x] = 12
                if neigbors[0] == 12:
                    if o[y][x] == 11:
                        o[y][x] = 24
                        o[y+1][x] = 0
                    elif o[y][x] == 14:
                        o[y][x] = 16
                        o[y+1][x] = 0
                elif neigbors[1] == 12:
                    if o[y][x] == 11:
                        o[y][x] = 24
                        o[y-1][x] = 0
                    elif o[y][x] == 14:
                        o[y][x] = 16
                        o[y-1][x] = 0
                elif neigbors[2] == 12:
                    if o[y][x] == 11:
                        o[y][x] = 24
                        o[y][x+1] = 0
                    elif o[y][x] == 14:
                        o[y][x] = 16
                        o[y][x+1] = 0
                elif neigbors[3] == 12:
                    if o[y][x] == 11:
                        o[y][x] = 24
                        o[y][x-1] = 0
                    elif o[y][x] == 14:
                        o[y][x] = 16
                        o[y][x-1] = 0

    listof=[o , hmap]
    return listof

surface = pygame.display.set_mode((width*psize + bwid*4+psize*2,height*psize))
# Initializing Color
color = (255,0,0)
# Drawing Rectangle
pygame.display.set_caption('Falling sand')
q = 0
buttons = []

def makebutton (mid,yx,yy):
    curr = button(yx,yy,mid)
    buttons.append(curr)

for u in range(1,elnum+1):
    makebutton(ids[u-1],width*psize+(((u-1)%4)*bwid+psize*2),((math.floor((u-1)/4))*bhei))

running = True
while running:
    surface.fill((30,30,30))
    for but in buttons:
        but.draw()
    q += 1
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col, row = mouse_x // psize, mouse_y // psize
        if 1 <= col <= width-2 and 1 <= row <= height-2 and cid != 999 and cid != 9999 and cid != 8999 and cid != 899:
            grid[row][col] = cid
            grid[row][col+1] = cid
            grid[row][col-1] = cid
            grid[row+1][col] = cid
            grid[row-1][col] = cid
            heat[row][col] = heatval[cid]
            heat[row][col+1] = heatval[cid]
            heat[row][col-1] = heatval[cid]
            heat[row+1][col] = heatval[cid]
            heat[row-1][col] = heatval[cid]
        elif 0 <= col <= width-2 and 0 <= row <= height-2 and cid == 999:
            heat[row][col] += theat
            heat[row][col+1] += theat
            heat[row][col-1] += theat
            heat[row+1][col] += theat
            heat[row-1][col] += theat
        elif 0 <= col <= width-2 and 0 <= row <= height-2 and cid == 899:
            heat[row][col] -= theat
            heat[row][col+1] -= theat
            heat[row][col-1] -= theat
            heat[row+1][col] -= theat
            heat[row-1][col] -= theat
        elif 0 <= col <= width-2 and 0 <= row <= height-2 and cid == 9999:
            heat[row][col] += sheat
            heat[row][col+1] += sheat
            heat[row][col-1] += sheat
            heat[row+1][col] += sheat
            heat[row-1][col] += sheat
        elif 0 <= col <= width-2 and 0 <= row <= height-2 and cid == 8999:
            heat[row][col] -= sheat
            heat[row][col+1] -= sheat
            heat[row][col-1] -= sheat
            heat[row+1][col] -= sheat
            heat[row-1][col] -= sheat
        for a in buttons:
            if a.click() != None:
                cid = a.click()
    if pygame.mouse.get_pressed()[2]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col, row = mouse_x // psize, mouse_y // psize
        if 0 <= col <= width-2 and 0 <= row <= height-2:
            grid[row][col] = 0
            grid[row][col+1] = 0
            grid[row][col-1] = 0
            grid[row+1][col] = 0
            grid[row-1][col] = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    h =0
    k = 0
    
    if q > F:
        new = []
        listoflist =update()
        new = listoflist[0]
        heat = listoflist[1]
        grid = new
        q = 0
    """mouse_x, mouse_y = pygame.mouse.get_pos()
    col, row = mouse_x // psize, mouse_y // psize
    if 0 <= col <= width-1 and 0 <= row <= height-1:
        if grid[row][col] != 0:
            print(names[ids.index(grid[row][col])]," ", heat[row][col])"""

    for g in grid:
        k = 0
        h +=1
        for j in g:
            k+=1
            if j != 0 and j in ids:
                color = idtocolor[j]
                mainrect = pygame.Rect(k*psize, h*psize, psize, psize)
                pygame.draw.rect(surface, color, mainrect)
           
    pygame.display.flip()
