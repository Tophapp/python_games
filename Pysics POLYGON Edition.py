import math
import pygame
import time
import random

pygame.init()
objects = []
window = pygame.display.set_mode((800, 800))
global color
global mousepos
mousepos = pygame.Vector2(0,0)
global lastmousepos
currenttime = time.time()
lastmousepos = pygame.Vector2(0,0)
global lastlastmousepos 
lastlastmousepos = pygame.Vector2(0,0)
color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))

#rotating functions
def rotate(pos,rot,width,height):

    # Rotate
    if rot != 0:
        pos2 = pygame.Vector2(pos.x - width/2,pos.y - height/2)
        x_rotated = pos2.x * math.cos(rot) - pos2.y * math.sin(rot)
        y_rotated = pos2.x * math.sin(rot) + pos2.y * math.cos(rot)

        # Translate back
        x_rotated += width/2
        y_rotated += height/2

        return pygame.Vector2(x_rotated, y_rotated)
    else:
        return pygame.Vector2(pos.x, pos.y)
    
#stolen line intersection code
def ccw(A,B,C):
    return round((C.y-A.y) * (B.x-A.x),1) > round((B.y-A.y) * (C.x-A.x),1)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

#polygon collision detection
def polycoll(polygon1=[],polygon2=[]):
    for line in polygon1:
        for line2 in polygon2:
            if intersect(line,polygon1[(polygon1.index(line)+1)%len(polygon1)],line2,polygon2[(polygon2.index(line2)+1)%len(polygon2)]):
                return True
    return False

#polygon collision detection2
def polycoll2(polygon1=[],polygon2=[]):
    for line in polygon1:
        for line2 in polygon2:
            if intersect(line,polygon1[(polygon1.index(line)+1)%len(polygon1)],line2,polygon2[(polygon2.index(line2)+1)%len(polygon2)]):
                return [[line,polygon1[(polygon1.index(line)+1)%len(polygon1)]],[line2,polygon2[(polygon2.index(line2)+1)%len(polygon2)]]]

def whereintersect(line1,line2):
        x1, y1, x2, y2 = round(line1[0].x,3),round(line1[0].y,3),round(line1[1].x,3),round(line1[1].y,3)
        x3, y3, x4, y4 = round(line2[0].x,3),round(line2[0].y,3),round(line2[1].x,3),round(line2[1].y,3)
        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if det == 0:
            return None
        t = round(((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / det,3)

        x = round(x1 + t * (x2 - x1),3)
        y = round(y1 + t * (y2 - y1),3)
        return pygame.Vector2(x, y)

#initialize rigid body
class rigidbody():
    def __init__(self,iden,position = pygame.Vector2(400,100),velocity=pygame.Vector2(0,0),wid = 20, hei = 20, col = color,sta = False,rotation=0):
        self.pos = position
        global color
        color = (random.randint(1,205+50),random.randint(1,205+50),random.randint(1,205+50))
        self.vel = velocity
        self.grounded = False
        self.width = wid
        self.height = hei
        self.color = col
        self.static = sta
        self.clicked = False
        self.identify = iden
        self.rot = 0
        self.polygonlist3 = []
        tolerence = 2
        self.center = self.pos + pygame.Vector2(self.width/2,self.height/2)
        self.radii = self.width if self.width >= self.height else self.height
        self.polygonlist2 = [self.pos+rotate(pygame.Vector2(0,tolerence),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,tolerence),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,self.height+tolerence),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(0,self.height+tolerence),self.rot,self.width,self.height)]
        self.polygonlist = [self.pos+rotate(pygame.Vector2(0,0),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,0),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)]

    #update and display
    def update(self):
        self.pos = pygame.Vector2(round(self.pos.x,3),round(self.pos.y,3))
        self.radii = self.width if self.width >= self.height else self.height
        self.center = self.pos + pygame.Vector2(self.width/2,self.height/2)
        tolerence = 2
        global mousepos
        self.polygonlist2 = [self.pos+rotate(pygame.Vector2(0,tolerence),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,tolerence),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,self.height+tolerence),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(0,self.height+tolerence),self.rot,self.width,self.height)]
        self.polygonlist = [self.pos+rotate(pygame.Vector2(0,0),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,0),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)]
        self.polygonlist3 = []
        polygon2copy = []
        for point in range(len(self.polygonlist)):
            self.polygonlist[point] = pygame.Vector2(round(self.polygonlist[point].x,1),round(self.polygonlist[point].y,1))

        for point in range(len(self.polygonlist)):
            self.polygonlist2[point] = pygame.Vector2(round(self.polygonlist2[point].x,1),round(self.polygonlist2[point].y,1))

        #make lines below box for collison detection on floor
        for point in self.polygonlist2:
            polygon2copy.append(point.y-tolerence)

        self.polygonlist3.append(self.polygonlist2.pop(polygon2copy.index(max(polygon2copy))))
        self.polygonlist3.append(pygame.Vector2(self.polygonlist3[0].x,round(self.polygonlist3[0].y + self.height+tolerence+(self.vel.y*(currenttime -lasttime)*1.2),1)))
        self.polygonlist3.append(self.polygonlist2.pop(polygon2copy.index(max(polygon2copy))))
        self.polygonlist3.append(pygame.Vector2(self.polygonlist3[2].x,round(self.polygonlist3[2].y + self.height+tolerence+(self.vel.y*(currenttime -lasttime)*1.2),1)))
        self.polygonlist3.append(pygame.Vector2((self.polygonlist3[0].x +self.polygonlist3[2].x)/2,self.pos.y + self.height+tolerence))
        self.polygonlist3.append(pygame.Vector2(self.polygonlist3[4].x,round(self.polygonlist3[4].y + self.height+tolerence+(self.vel.y*(currenttime -lasttime)*1.2),1)))

        #if not picked up
        if self.clicked == False:
            self.grounded = False
            math.hypot()
            #collision detection
            if not self.static:
                for object in objects:
                    if object != self:
                        #if abs(math.sqrt((object.center.x - self.center.x)**2+ (object.center.y - self.center.y)**2)) < self.radii+tolerence and abs(math.sqrt((object.center.x - self.center.x)**2+ (object.center.y - self.center.y)**2)) < object.radii+tolerence:
                        if abs(math.sqrt((object.center.x - self.center.x)**2+ (object.center.y - self.center.y)**2)) < self.radii+tolerence+object.radii:
                            #(((self.pos.y +self.height) >object.pos.y) and (self.pos.y < (object.pos.y+object.height))) and (((self.pos.x +self.width) >object.pos.x) and (self.pos.x < (object.pos.x+object.width)))
                            if polycoll(self.polygonlist3,object.polygonlist2):
                                #if whereintersect(polycoll2(self.polygonlist3,object.polygonlist2)[0],polycoll2(self.polygonlist3,object.polygonlist2)[1]) != None:
                                    polycollresults = polycoll2(self.polygonlist3,object.polygonlist2)
                                    self.pos = pygame.Vector2(self.pos.x,round(whereintersect(polycollresults[0],polycollresults[1]).y-self.height-tolerence,1))
                                    self.grounded = True

            #if not static body
            if not self.static:

                #gravity
                if self.grounded == False:
                    self.vel = pygame.Vector2(self.vel.x,self.vel.y+1300*(currenttime -lasttime))
                elif self.vel.y>=0:
                    self.vel = pygame.Vector2(self.vel.x*0.01,0)

                #movement calculations
                self.pos += self.vel *(currenttime -lasttime)
                self.vel -= (currenttime -lasttime)*self.vel
        else:
            #The nation of rotationmation
            keys=pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.rot += 1*(currenttime -lasttime)

            #set position to mouse position
            self.pos = mousepos-pygame.Vector2(self.width/2,self.height/2)
            self.vel=pygame.Vector2(0,0)

        #display
        bodysprite = pygame.rect.Rect(self.pos.x,self.pos.y,self.width,self.height)
        pygame.draw.polygon(window,self.color,self.polygonlist)
        #pygame.draw.rect(window,self.color,bodysprite)
        
    
    #picking up function
    def click(self,position):
        alreadyclicked = False
        if not self.static:
            if (((self.pos.y +self.height) >position.y) and (self.pos.y < (position.y))) and (((self.pos.x +self.width) >position.x) and (self.pos.x < (position.x))):
                for object in objects:
                    if object.clicked ==True:
                        alreadyclicked = True
                if alreadyclicked == False:
                    self.pos = position
                    self.vel=pygame.Vector2(0,0)
                    self.clicked = True

    #putting down function
    def release(self):
        global mousepos
        limit = 400
        if not self.static:
            if self.clicked == True:
                for  event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mousepos = pygame.Vector2(event.pos[0],event.pos[1])
                self.vel=((mousepos-lastlastmousepos)*7)
                if self.vel.x >=limit:
                    self.vel = pygame.Vector2(limit,self.vel.y)
                if self.vel.x <=-limit:
                    self.vel = pygame.Vector2(-limit,self.vel.y)
                if self.vel.y >=limit:
                    self.vel = pygame.Vector2(self.vel.x,limit)
                if self.vel.y <=-limit:
                    self.vel = pygame.Vector2(self.vel.x,-limit)
                self.clicked = False

#make rigid body instance
def makerigidbody(position = pygame.Vector2(400,100),velocity=pygame.Vector2(0,0),wid = 20, hei = 20, col = None,sta = False,rotation=0):
    global color 
    if col == None:
        col = color
    color = (random.randint(1,205+50),random.randint(1,205+50),random.randint(1,205+50))
    body = rigidbody(iden=len(objects),position=position,velocity=velocity,wid=wid,hei=hei,col=col,sta=sta,rotation=rotation)
    objects.append(body)

makerigidbody()
makerigidbody(position=pygame.Vector2(-100,750),wid=1000,hei=100,sta=True,col=(10,10,10))

#main loop
running = True
while running:
    lasttime = currenttime
    currenttime = time.time()
    
    lastlastmousepos = lastmousepos
    lastmousepos = mousepos

    #if press X button on window, close widnow
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for object in objects:
                    object.click(pygame.Vector2(event.pos[0],event.pos[1]))
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                for object in objects:
                    object.release()
        if event.type == pygame.MOUSEMOTION:
            mousepos = pygame.Vector2(event.pos[0],event.pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                makerigidbody(position=pygame.Vector2(400,100))

    #fill background color
    window.fill((35,35,35))

    #update all objects
    for object in objects:
        object.update()

    #update screen
    pygame.display.flip()
