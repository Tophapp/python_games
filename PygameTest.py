import pygame
import math
import random

pygame.init()

height = 500
td = False
width =1000
font = "Comic San MS"
myFont = pygame.font.SysFont(font, 20)
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #fullscreen
sx = surface.get_width() / width
sy = surface.get_height() / height
worldset = [[pygame.Vector2(300,150),[],[],[],[]]]
CASTED_RAYS=  100
MAX_DEPTH = 300
bcolor = (30,30,30)

class player():
    def __init__(self,pos):
        self.pos = pos
        self.rot = 0
        self.speed = 1.5
        self.buf = 1
        
    def update(self):
        s = 0
        while True:
            s = 0
            for o in objects:
                if self.pos.x > o.pos.x and self.pos.x < o.pos.x+o.sizex:
                    if self.pos.y > o.pos.y and self.pos.y < o.pos.y+o.sizey:
                        s += 1
            if s != 0:
                self.pos = pygame.Vector2(random.randint(20,width-20),random.randint(20,height-20))
            else:
                break

        rot = self.rot-CASTED_RAYS/2
        if td != True:
            for ra in range(MAX_DEPTH):
                r = ra*3
                if ((MAX_DEPTH)-r)/MAX_DEPTH*floor.color[0] > bcolor[0] or ((MAX_DEPTH)-r)/MAX_DEPTH*floor.color[1] > bcolor[1] or ((MAX_DEPTH)-r)/MAX_DEPTH*floor.color[2] > bcolor[2]:
                    pygame.draw.line(surface,(((MAX_DEPTH)-r)/MAX_DEPTH*floor.color[0],((MAX_DEPTH)-r)/MAX_DEPTH*floor.color[1],((MAX_DEPTH)-r)/MAX_DEPTH*floor.color[2]),pygame.Vector2(0,round(sy*(height-r/2))),pygame.Vector2(round(sx*width),round(sy*(height-r/2))),math.ceil(11*sx))
            for ray in range(CASTED_RAYS):
                b = False        
                for depth in range(MAX_DEPTH):
                    if b== True:
                        break             
                    targetx = self.pos.x - math.cos(rot) * depth
                    targety = self.pos.y - math.sin(rot) * depth

                    for o in objects:
                        if targetx > o.pos.x and targetx < o.pos.x+o.sizex:
                            if targety > o.pos.y and targety < o.pos.y+o.sizey:
                                if ((MAX_DEPTH)-depth)/MAX_DEPTH*o.color[0] > bcolor[0] or ((MAX_DEPTH)-depth)/MAX_DEPTH*o.color[1] > bcolor[1] or ((MAX_DEPTH)-depth)/MAX_DEPTH*o.color[2] > bcolor[2]:
                                    
                                    pygame.draw.line(surface,(((MAX_DEPTH)-depth)/MAX_DEPTH*o.color[0],((MAX_DEPTH)-depth)/MAX_DEPTH*o.color[1],((MAX_DEPTH)-depth)/MAX_DEPTH*o.color[2]),pygame.Vector2(round(sx*(width/CASTED_RAYS*ray)),round(sy*(depth/2/o.height))),pygame.Vector2(round(sx*(width/CASTED_RAYS*ray)),round(sy*(height-(depth/2)))),math.ceil(11*sx))
                                    b = True
                rot += 0.004
        else:
            targetx = self.pos.x - math.cos(rot+0.2)*20
            targety = self.pos.y - math.sin(rot+0.2)*20
            pygame.draw.line(surface,floor.color,self.pos,pygame.Vector2(targetx,targety),3)
            
            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_d]:
            blue = False
            for o in objects:
                 if self.pos.x + (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x > o.pos.x-self.buf and self.pos.x + (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x < o.pos.x+o.sizex+self.buf:
                    if self.pos.y + (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y > o.pos.y-self.buf and self.pos.y + (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y < o.pos.y+o.sizey+self.buf:
                        blue = True
            if blue == False:
                self.pos -= pygame.Vector2((math.cos(self.rot-CASTED_RAYS/2+0.2+math.pi/2)),(math.sin(self.rot-CASTED_RAYS/2+0.2+math.pi/2)))*self.speed
        if keys[pygame.K_a]:
            blue = False
            for o in objects:
                if self.pos.x - (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x > o.pos.x-self.buf and self.pos.x - (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x < o.pos.x+o.sizex+self.buf:
                    if self.pos.y - (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y > o.pos.y-self.buf and self.pos.y - (pygame.Vector2((math.sin(self.rot-CASTED_RAYS/2+0.2)),(math.cos(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y < o.pos.y+o.sizey+self.buf:
                        blue = True
            if blue == False:
                self.pos += pygame.Vector2((math.cos(self.rot-CASTED_RAYS/2+0.2+math.pi/2)),(math.sin(self.rot-CASTED_RAYS/2+0.2+math.pi/2)))*self.speed
        if keys[pygame.K_w]:
            blue = False
            for o in objects:
                if self.pos.x + (pygame.Vector2((math.cos(self.rot-CASTED_RAYS/2+0.2)),(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x > o.pos.x-self.buf and self.pos.x + (pygame.Vector2((math.cos(self.rot-CASTED_RAYS/2+0.2)),(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x < o.pos.x+o.sizex+self.buf:
                    if self.pos.y + (pygame.Vector2((math.cos(self.rot-CASTED_RAYS/2+0.2)),(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y > o.pos.y-self.buf and self.pos.y + (pygame.Vector2((math.cos(self.rot-CASTED_RAYS/2+0.2)),(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y < o.pos.y+o.sizey+self.buf:
                        blue = True
            if blue == False:
                self.pos -= pygame.Vector2((math.cos(self.rot-CASTED_RAYS/2+0.2)),(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed
        if keys[pygame.K_s]:
            blue = False
            for o in objects:
                if self.pos.x + (pygame.Vector2(-(math.cos(self.rot-CASTED_RAYS/2+0.2)),-(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x > o.pos.x-self.buf and self.pos.x + (pygame.Vector2(-(math.cos(self.rot-CASTED_RAYS/2+0.2)),-(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).x < o.pos.x+o.sizex+self.buf:
                    if self.pos.y + (pygame.Vector2(-(math.cos(self.rot-CASTED_RAYS/2+0.2)),-(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y > o.pos.y-self.buf and self.pos.y + (pygame.Vector2(-(math.cos(self.rot-CASTED_RAYS/2+0.2)),-(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed).y < o.pos.y+o.sizey+self.buf:
                        blue = True
            if blue == False:
                self.pos -= pygame.Vector2(-(math.cos(self.rot-CASTED_RAYS/2+0.2)),-(math.sin(self.rot-CASTED_RAYS/2+0.2)))*self.speed
        if self.rot > 2*math.pi:
             self.rot = 0
        if self.rot < 0:
             self.rot = 2*math.pi

class object():
    def __init__(self,pos,szex,szey,color,height):
        self.pos = pos
        self.sizey = szey
        self.sizex = szex
        self.color = color
        self.height = height
        
bob = player(worldset[0][0])
objects = []
bo = False
def makeblock(color,pos,height,sizey,sizex):
     temp = object(pos,sizex,sizey,color,height)
     objects.append(temp)

for l in range(random.randint(30,60)):
    worldset[0][4].append((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
    worldset[0][1].append(pygame.Vector2(random.randint(1,width),random.randint(1,height)))
    worldset[0][2].append(random.uniform(0.7,1.5))
    worldset[0][3].append([random.randint(10,60),random.randint(10,60)])

for block in range(len(worldset[0][4])):
    makeblock(worldset[0][4][block],worldset[0][1][block],worldset[0][2][block],worldset[0][3][block][1],worldset[0][3][block][0])

class floorsurf():
    def __init__(self):
        self.color = (255,255,255)
floor = floorsurf()

running = True
while running:
    keys=pygame.key.get_pressed()
    pygame.mouse.set_visible(False)
    mpos = pygame.mouse.get_pos()
    if mpos[0] > width/2+1 and keys[pygame.K_ESCAPE] != True:
        bob.rot += (mpos[0] - width/2)/2000
        if keys[pygame.K_ESCAPE] != True:
            pygame.mouse.set_pos((width/2,height/2))
        else:
            pygame.mouse.set_visible(True)
    elif mpos[0] < width/2-1 and keys[pygame.K_ESCAPE] != True:
        bob.rot += (mpos[0] - width/2)/2000
        if keys[pygame.K_ESCAPE] != True:
            pygame.mouse.set_pos((width/2,height/2))
        else:
            pygame.mouse.set_visible(True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11 and bo == True:
            surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            sx = surface.get_width() / width
            sy = surface.get_height() / height
            bo = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11 and bo == False:
            surface = pygame.display.set_mode((width, height))
            sx = surface.get_width() / width
            sy = surface.get_height() / height
            bo = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F12 and td == True:
            td = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12 and td == False:
            td = True

    surface.fill(bcolor)
    bob.update()
    if td == True:
        for blocks in objects:
            pygame.draw.rect(surface, blocks.color, pygame.Rect(blocks.pos.x, blocks.pos.y, blocks.sizex, blocks.sizey))

    pygame.display.flip()
