import pygame
import random
import math
#Unfinished
(width, height) = (800,800)
screen = pygame.display.set_mode((width, height))
objects = []

class metal():
    def __init__(self):
        self.speed = 0.05
        self.speedval = self.speed
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.angle = 0
        self.width = random.randint(10,60)
        self.hight = random.randint(10,60)
        self.mass = ((self.width + self.hight) / 2)
        self.speed -= (self.mass/4)
        if self.speed <= 0:
            self.speed = 0.1
        self.rect = pygame.Rect(self.pos.x,self.pos.y, self.width, self.hight)
        self.drag = 0.99
        self.grounded = False
        self.timepassedlastgroundtouch = 0

        self.istouchingwall = False
        self.whatwalltouch = 0
        self.isclicked = False
        

    def exist(self):

        self.grounded = False
        self.istouchingwall = False
        self.whatwalltouch = 0
        self.istouchingwall, self.whatwalltouch = istouchingboundries(self.pos,self.width,self.hight)
        self.isclicked = mousedetectleft(self.rect,self.isclicked)
        if self.isclicked == True:
            self.grounded = True
            if mouseoutsidebord[0] == False:
                self.pos = pygame.Vector2((mousepos[0] - self.width /2),(mousepos[1] - self.hight /2))


        self.rect = pygame.Rect(self.pos.x,self.pos.y, self.width, self.hight)
        if self.istouchingwall == True:
            setback(self.pos,self.whatwalltouch,self.width,self.hight)
        if self.whatwalltouch == 3:
            self.grounded = True


        self.rect = pygame.Rect(self.pos.x,self.pos.y, self.width, self.hight)
        pygame.draw.rect(screen, "grey", self.rect)
        if self.grounded == True:
            self.speed = self.speedval
        else:
            self.pos = gravity(self.pos,self.drag,self.mass)
def mousedetectleft(rect,isclicked):
    if rect.collidepoint(pygame.Vector2(mousepos)):
        if left:
            return True
    elif isclicked == True and left == True:
        return True

def setback(pos,whatwall,widths,heights):
    heights // 2
    widths // 2
    if whatwall == 1:
        pos.x -= pos.x -(width-widths)
    if whatwall == 2:
        pos.x -= pos.x -(0+widths)
    if whatwall == 3:
        pos.y -= pos.y -(height-heights)
    if whatwall == 4:
        pos.y -= pos.y -(0+heights)
def istouchingboundries(pos,widths,heights):
    heights // 2
    widths // 2
    if pos.x > width-widths:#>
        return True, 1
    elif pos.x < 0+widths:#<
        return True, 2
    elif pos.y > height-heights:#v
        return True, 3
    elif pos.y < 0+heights:#^
        return True, 4
    else:
        return False, 0
def gravity(pos,drag,mass):
    dr = move(pos,(0.99 * drag * (mass/20)),0)
    return dr
def move(pos,speed,angle):
    
    pos.x += math.sin(angle * 0.0174533) * speed
    pos.y += math.cos(angle * 0.0174533) * speed
    return pos



def makemetal():
    curr = metal()
    objects.append(curr)
makemetal()
running = True
tick = 0
mousepos = pygame.mouse.get_pos()
mouseoutsidebord = istouchingboundries(pygame.Vector2(mousepos),2,2)
left,right,middle = pygame.mouse.get_pressed(3)
while running:
    mousepos = pygame.mouse.get_pos()
    mouseoutsidebord = istouchingboundries(pygame.Vector2(mousepos),2,2)
    print(mouseoutsidebord,objects[0].isclicked,objects[0].pos,objects[0].drag,objects[0].mass)
    left,right,middle = pygame.mouse.get_pressed(3)
    screen.fill((40,40,40))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    for apples in objects:

        apples.exist()

    pygame.display.flip()