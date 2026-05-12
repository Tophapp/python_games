import random
import pygame

pygame.init()

height = 800
width=1000
ex = 1
players = []
hit = 10

class player():
    def __init__(self,type):
        self.type = type# 1=Rock, 2=Paper, 3=Scissors
        self.pos = pygame.Vector2(random.randrange(1,width),random.randrange(1,height))
        self.dir = 0
        self.timer = 0

    def render(self):
        if self.timer <= 0:
            self.dir = random.randint(1,4)
            self.timer = 10
        if self.dir == 4:
            self.pos.x += ex
        elif self.dir == 2:
            self.pos.x -= ex
        elif self.dir == 1:
            self.pos.y += ex
        elif self.dir == 3:
            self.pos.y -= ex
        self.timer -= 1
        if self.pos.x > width or self.pos.x < 0:
            self.pos.x = random.randrange(1,width)
        if self.pos.y > height or self.pos.y < 0:
            self.pos.y = random.randrange(1,height)
        for e in players:
            if e.pos.x < self.pos.x+hit and e.pos.x > self.pos.x-hit:
                if e.pos.y < self.pos.y+hit and e.pos.y > self.pos.y-hit:
                    if e.type == 1 and self.type == 3:
                        self.type=1
                    elif e.type == 2 and self.type == 1:
                        self.type=2
                    elif e.type == 3 and self.type == 1:
                        e.type=1
                    elif e.type == 1 and self.type == 2:
                        e.type=2
                    elif e.type == 2 and self.type == 3:
                        e.type=3
                    elif e.type == 3 and self.type == 2:
                        self.type=3
        if self.type==1:
            pygame.draw.rect(surface, (116,116,132), pygame.Rect(self.pos.x, self.pos.y-hit, hit*2, hit*2))
        elif self.type==2:
            pygame.draw.rect(surface, (235,235,235), pygame.Rect(self.pos.x, self.pos.y-hit, hit*2, hit*2))
        elif self.type==3:
            pygame.draw.rect(surface, (244,13,48), pygame.Rect(self.pos.x, self.pos.y-hit, hit*2, hit*2))
        
    def render2(self):
        if self.type==1:
            pygame.draw.rect(surface, (116,116,132), pygame.Rect(self.pos.x, self.pos.y-hit, hit*2, hit*2))
        elif self.type==2:
            pygame.draw.rect(surface, (235,235,235), pygame.Rect(self.pos.x, self.pos.y-hit, hit*2, hit*2))
        elif self.type==3:
            pygame.draw.rect(surface, (244,13,48), pygame.Rect(self.pos.x, self.pos.y-hit, hit*2, hit*2))

def makeplayer():
    curr = player(random.randint(1,3))
    players.append(curr)

for g in range(1,random.randint(40,70)):
    makeplayer()

surface = pygame.display.set_mode((width,height))
running = True
text =""
while running:

    surface.fill((150,106,60))

    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    if text =="":
        alive = [0,0,0]
        for p in players:
            p.render()
            if p.type==1:
                alive[0]+=1
            elif p.type==2:
                alive[1]+=1
            elif p.type==3:
                alive[2]+=1
    else:
        for p in players:
            p.render2()
    if alive[0] == 0:
        text="Scissors Win"
    elif alive[1] == 0:
        text="Papers Win"
    elif alive[2] == 0:
        text="Rocks Win"
    font = "Comic San MS"
    myFont = pygame.font.SysFont(font, 100)
    text_surface_start = myFont.render(text,True,(0,0,0))
    surface.blit(text_surface_start, (width/2,height/2))

    pygame.display.flip()

