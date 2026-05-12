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

#initialize rigid body
class rigidbody():
    def __init__(self,iden,position = pygame.Vector2(400,100),velocity=pygame.Vector2(0,0),wid = 20, hei = 20, col = color,sta = False,rotation=0):
        self.pos = position
        global color
        color = (random.randint(1,205+50),random.randint(1,205+50),random.randint(1,205+50))
        self.vel = velocity
        self.lasttime = time.time()
        self.grounded = False
        self.width = wid
        self.height = hei
        self.color = col
        self.static = sta
        self.clicked = False
        self.identify = iden
        self.rot = 0
        self.rotspeed = 2.0533

    #update and display
    def update(self):
        tolerence = 0.5
        global mousepos
        noobjectsleft = True
        noobjectsright = True
        #if not picked up
        if self.clicked == False:

            self.grounded = False

            #collision detection
            for object in objects:
                if object != self:
                    #(((self.pos.y +self.height) >object.pos.y) and (self.pos.y < (object.pos.y+object.height))) and (((self.pos.x +self.width) >object.pos.x) and (self.pos.x < (object.pos.x+object.width)))
                    if (((self.pos.y +self.height) >object.pos.y) and (self.pos.y + self.height/1.5 < (object.pos.y+object.height))) and (((self.pos.x +self.width) >object.pos.x+object.width/2) and (self.pos.x+self.width/2 < (object.pos.x+object.width))):
                        self.grounded = True
                    elif (((object.pos.y +object.height) >((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).y+tolerence)) and (object.pos.y < ((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).y+tolerence))) and ((object.pos.x +object.width) >((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).x) and (object.pos.x < ((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).x))) and (((object.pos.y +object.height) >((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).y+tolerence)) and (object.pos.y < ((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).y+tolerence))) and ((object.pos.x +object.width) >(((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).x)) and (object.pos.x < (((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).x)))):
                        self.grounded = True
                    
                    if  not self.static:
                        
                        #rotation detecton
                        if self.grounded == False and(((object.pos.y +object.height) >((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).y+tolerence)) and (object.pos.y < ((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).y+tolerence))) and ((object.pos.x +object.width) >((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).x) and (object.pos.x < ((self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)).x))):
                            noobjectsright = False
                        if self.grounded == False and (((object.pos.y +object.height) >((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).y+tolerence)) and (object.pos.y < ((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).y+tolerence))) and ((object.pos.x +object.width) >(((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).x)) and (object.pos.x < (((self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height)).x)))):
                            noobjectsleft = False
                        
            if not self.static:
                #rotation
                if noobjectsright == True and self.grounded == False and noobjectsleft == False:
                    self.rot-=self.rotspeed*(time.time() -self.lasttime)
                    self.vel = pygame.Vector2(self.vel.x-0.2,self.vel.y)
                if noobjectsleft == True and self.grounded == False and noobjectsright==False:
                    self.rot+=self.rotspeed*(time.time() -self.lasttime)
                    self.vel = pygame.Vector2(self.vel.x+0.2,self.vel.y)
                if noobjectsleft == False and noobjectsright == False:
                    self.grounded = True

            #if not static body
            if not self.static:

                #gravity
                if self.grounded == False:
                    self.vel = pygame.Vector2(self.vel.x,self.vel.y+1000*(time.time() -self.lasttime))
                elif self.vel.y>=0:
                    self.vel = pygame.Vector2(self.vel.x*0.01,0)

                #movement calculations
                self.pos += self.vel *(time.time() -self.lasttime)
                self.vel -= (time.time() -self.lasttime)*self.vel
        else:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.rot += self.rotspeed*(time.time() -self.lasttime)
            #set position to mouse position
            self.pos = mousepos-pygame.Vector2(self.width/2,self.height/2)
            self.vel=pygame.Vector2(0,0)

        #display
        bodysprite = pygame.rect.Rect(self.pos.x,self.pos.y,self.width,self.height)
        pygame.draw.polygon(window,self.color,[self.pos+rotate(pygame.Vector2(0,0),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,0),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(self.width,self.height),self.rot,self.width,self.height),self.pos+rotate(pygame.Vector2(0,self.height),self.rot,self.width,self.height)])
        #pygame.draw.rect(window,self.color,bodysprite)
        self.lasttime = time.time()
    
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
                    self.rot = 0
                    self.vel=pygame.Vector2(0,0)
                    self.clicked = True

    #putting down function
    def release(self):
        limit = 400
        if not self.static:
            if self.clicked == True:
                self.vel=(mousepos-((lastmousepos+lastlastmousepos)/2))*(0.02/((time.time() -self.lasttime)+0.000001))*2
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
