import random
import pygame
import keyboard
import math
#Unfinished
money = 10
mers = []
eve = []
size = 7000
pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(),32)
poscolors = []
onplanet = False
print("Welcolm To Saturn-E The Game About Exploring(And Colonizing) Space")
print("Press Enter To Continue")
input("")
letters = ["a","b","c","e","h","i","j","r","s","t","u","c","e","h","i","j","r","s","t","u","v","-","1","2","3","4","5","6","7","8","9","0""1","2","3","4","5","6","7","8","9","0"]
hostilitys = [1,5,10]
posplanets = []
planets = []
running = True
screen = pygame.display.set_mode((800, 820))#x,y
playerpos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enemey = []
iron = 0
gold = 0
coal = 0
ti = 0
plat = 0
lead = 0
silver = 0

posrec = ["iron","coal","gold","ti","plat","silver","lead"]
ev = pygame.event.get()

pygame.display.set_caption("Space")

clock = pygame.time.Clock()
pygame.init()
left, middle, right = pygame.mouse.get_pressed()
class shockcard():
    def __init__(self):
        self.cardname = "Shock"
        self.desc = "Stuns An Enemey For 2 Turns"
    


    def play(self,Ehp,E):
        Ehp -= 2
        E.stun = 2
        return Ehp
class burncard():
    def __init__(self):
        self.cardname = "Burn"
        self.desc = "Deals 7 damage"
    


    def play(self,Ehp,E):
        Ehp -= 7
        
        return Ehp
        

for x in range(1, 130):
    randomint = random.randint(1, 6)
    letter = random.choice(letters)
    sent = ""
    for s in range(1, random.randint(4,7)+1):
        letter = random.choice(letters)
        sent += letter
    posplanets.append(sent)
for d in range(130):
    kelp = []
    kelp.append(random.randint(1,255))
    kelp.append(random.randint(1,255))
    kelp.append(random.randint(1,255))
    poscolors.append(kelp)
class drill():
    def __init__(self):
        self.rec = ""

        self.pos = pygame.Vector2(0.0,0.0)
        self.ont = pygame.font.SysFont(pygame.font.get_default_font(),16)
        self.text = self.ont.render("[_]>", True,"white")
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.pos.x,self.pos.y)
    def drill(self,rec):
        if tick % 200 == 0:
            rec += 1

            

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
class merchant():
    def __init__(self):
        self.rec = {"iron":{"stock":12,"price":13}}#stock,price
        self.sale = {}
        self.pos = pygame.Vector2(0,0)
        self.pos.x = random.randint(100,size)
        self.pos.y = random.randint(100,size)
        self.R = 10

        for v in planets:
            
            dis = math.hypot(self.pos.x - v.pos.x,self.pos.y - v.pos.y)
            if dis < self.R:
                self.pos.x = random.randint(100,size)
                self.pos.y = random.randint(100,size)
        self.ont = pygame.font.SysFont(pygame.font.get_default_font(),16)
        self.text = self.ont.render("o`", True,"black")
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.pos.x,self.pos.y)
        
    def make(self):
        self.stock1 = random.randint(1,23)
        self.price1 = random.randint(3,17)
        self.sale[random.choice(posrec)] = [self.stock1,str(self.price1)+"$"]
    def map(self):
        self.textRect.center = (self.pos.x,self.pos.y)
        if self.pos.x < 800 and self.pos.x > 0:
            if self.pos.y < 820 and self.pos.y > 0:  
                pygame.draw.circle(screen,"white",self.pos,self.R)
                screen.blit(self.text, self.textRect)
        elif tick % 3000 == 0:
            self.sale = {}
            self.make()
            self.make()
            self.make()
            self.make()
            self.make()
            self.make()
            self.make()
    
    




        

#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP    
class planet():
    def __init__(self):
        self.drillpos = []
        self.rockpos = []
        for g in range(1,8):
            self.rockpos.append((random.randint(100,700),random.randint(100,700)))
        self.rec = []
        self.name = random.choice(posplanets)
        posplanets.remove(self.name)
        self.hostility = random.choice(hostilitys)
        self.color = random.choice(poscolors)
        poscolors.remove(self.color)
        self.listpos = 1
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.pos.x = random.randint(100,size)
        self.pos.y = random.randint(100,size)
        self.R = random.randint(20,35)

        if len(planets) != 0:
            for v in planets:
                if planets.index(v) != self.listpos:
                    dis = math.hypot(self.pos.x - v.pos.x,self.pos.y - v.pos.y)
                    if dis < self.R:
                        self.pos.x = random.randint(100,size)
                        self.pos.y = random.randint(100,size)
                        


                    
        for g in range(1,random.randint(2,5)+1):
            self.rec.append(random.choice(posrec))



    def map(self):
        if self.pos.x < 800 and self.pos.x > 0:
            if self.pos.y < 820 and self.pos.y > 0:
                pygame.draw.circle(screen,self.color,self.pos,self.R)
                if len(planets) != 0:
                    for v in planets:
                        if planets.index(v) != self.listpos:
                            dis = math.hypot(self.pos.x - v.pos.x,self.pos.y - v.pos.y)
                            if dis < self.R:
                                self.pos.x = random.randint(100,size)
                                self.pos.y = random.randint(100,size)

                        
#PLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
class player():
    def __init__(self):

        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 20, 20)
        self.speed = 3
        
    def move(self,color,onplanet,currplanet,onmer):
        
        if keyboard.is_pressed("D"):
            for k in eve:
                k.pos.x -= self.speed
        if keyboard.is_pressed("A"):
            for k in eve:
                k.pos.x += self.speed
        if keyboard.is_pressed("W"):
            for k in eve:
                k.pos.y+= self.speed
            
        if keyboard.is_pressed("S"):
            for k in eve:
                k.pos.y -= self.speed
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 20, 20)
        pygame.draw.rect(screen,"white",self.rect)
        if keyboard.is_pressed("space"):
            
            for v in planets:
                    
                dis = math.hypot(self.pos.x - v.pos.x,self.pos.y - v.pos.y)
                if dis < v.R:
                    onplanet = True
                    color = v.color
                    currplanet = v.listpos
            for v in mers:
                
                dis = math.hypot(self.pos.x - v.pos.x,self.pos.y - v.pos.y)
                if dis < v.R*2:
                    onmer = True

        return color,onplanet,currplanet,onmer

            
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class xabla():
    def __init__(self):
        self.hp = random.randint(20,40)
        self.name = "xabla"
        self.stun = 0
        self.listin = 0
    def attack(self):
        self.stun -= 1
        if self.hp <= 0:
            enemey.pop(self.listin)
        if self.stun < 0:
            self.name
def makealien():
    rand = random.randint(1,1)
    if rand  == 1:
        al = xabla()
    enemey.append(al)
    al
#RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
class rock():
    def __init__(self):
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.pos.x = random.randint(100,size)
        self.pos.y = random.randint(100,size)
        self.rect = (self.pos.x,self.pos.y,30,15)
        self.size = random.randint(40,70)
        self.size1 = random.randint(30,50)
    def exist(self):
        self.rect = (self.pos.x,self.pos.y,self.size,self.size1)
        pygame.draw.rect(screen,"gray",self.rect)

class star():
    def __init__(self):
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.pos.x = random.randint(100,size)
        self.pos.y = random.randint(100,size)
    def do(self):
        
        if self.pos.x < 800 and self.pos.x > 0:
            if self.pos.y < 820 and self.pos.y > 0:
                pygame.draw.circle(screen,"white",self.pos,random.randint(200,400)/100)

def makeplanet():
    curr = planet()
    planets.append(curr)
    curr.listpos = len(planets)-1
    eve.append(curr)
suit = player()
stars = []
tick = 0
def makestar():
    m = star()
    stars.append(m)
    eve.append(m)
def makemerchant():
    m = merchant()
    mers.append(m)
    eve.append(m)
    m.make()
    m.make()
    m.make()
    m.make()
    m.make()
    m.make()
    m.make()
rocks = []
def makerock():
    m = rock()
    rocks.append(m)

for x in range(1,400):
    makestar()
for x in range(1,11):
    makemerchant()
for l in range(1,120):
    makeplanet()
for l in range(1,8):
    makerock()

text = font.render(str(money)+"$", True,"white")
textlead = font.render(str(lead)+" Lead", True,"white")
textgold = font.render(str(gold)+" Gold", True,"white")
texttitanium = font.render(str(ti)+" Titanium", True,"white")
textiron = font.render(str(iron)+" Iron", True,"white")
textcoal = font.render(str(coal)+" Coal", True,"white")
textplatnum = font.render(str(plat)+" Platnum", True,"white")
textsilver = font.render(str(silver)+" Silver", True,"white")

textRect = text.get_rect()
textRect.center = (20,20)

textRect1 = textlead.get_rect()
textRect1.center = (100,20)
textRect2 = textgold.get_rect()
textRect2.center = (200,20)
textRect3 = texttitanium.get_rect()
textRect3.center = (300,20)
textRect4 = textiron.get_rect()
textRect4.center = (400,20)
textRect5 = textcoal.get_rect()
textRect5.center = (500,20)
textRect6 = textplatnum.get_rect()
textRect6.center = (600,20)
textRect7 = textsilver.get_rect()
textRect7.center = (700,20)
bart = 0
gart = -1
currplanet = 0



onmer = False
topbar = pygame.Rect(0,0,800,40)
while running:
    
    text = font.render(str(money)+"$", True,"white")
    textlead = font.render(str(lead)+" Lead", True,"white")
    textgold = font.render(str(gold)+" Gold", True,"white")
    texttitanium = font.render(str(ti)+" Titanium", True,"white")
    textiron = font.render(str(iron)+" Iron", True,"white")
    textcoal = font.render(str(coal)+" Coal", True,"white")
    textplatnum = font.render(str(plat)+" Platnum", True,"white")
    textsilver = font.render(str(silver)+" Silver", True,"white")
    tick += 1
    if onplanet == True and keyboard.is_pressed("B") == True:
        onplanet = False
    if onmer == True and keyboard.is_pressed("B") == True:
        onmer = False

    if onplanet == False:
        color = (0,0,0)
    if onmer == True:
        color = (255,255,255)

    screen.fill(color)
    pygame.draw.rect(screen,"dark gray",topbar)
    if onplanet == True:
        gart = -1
        for u in rocks:
            gart += 1
            bart = planets[currplanet]
            if len(bart.rockpos) != 0:
                bart = planets[currplanet]
                farg = random.choice(bart.rockpos)
                u.pos.x = farg[0]
                u.pos.y = farg[1]
                bart.rockpos.remove(farg)
            
            u.exist()
    if keyboard.is_pressed("T"):
        imput = input()
        split = imput.split(" ")
    if onplanet == True:
        for u in rocks:
            u.exist()
    if onplanet == False and onmer == False:
        for u in planets:
            u.map()
        for u in stars:
            u.do()
        for u in mers:
            u.map()
        color,onplanet,currplanet,onmer = suit.move(color,onplanet,currplanet,onmer)
    #if onplanet == True:
        
    screen.blit(text, textRect)

    screen.blit(textlead, textRect1)
    screen.blit(textgold, textRect2)
    screen.blit(texttitanium, textRect3)
    screen.blit(textiron, textRect4)
    screen.blit(textcoal, textRect5)
    screen.blit(textplatnum, textRect6)
    screen.blit(textsilver, textRect7)

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    

    clock.tick(60)  # limits FPS to 60


pygame.quit()
