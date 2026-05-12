import pygame
import math

pygame.init()
width = 500
height = 500
armies = []
font = "Comic San MS"
myFont = pygame.font.SysFont(font, 20)
surface = pygame.display.set_mode((width,height))

class army():
    def __init__(self,pos,count,index):
        self.side =0
        self.pos = pos
        self.count = count
        self.index = index
        
    def update(self):
        if armies[self.index] != None:
                pygame.draw.rect(surface, (125, 230, 97), pygame.Rect(self.pos.x, self.pos.y, hit, hit))
                text_surface_start = myFont.render(str(self.count),True,(0,0,0))
                surface.blit(text_surface_start, (self.pos.x,self.pos.y))
            
    def delete(self):
        armies[self.index] = None

class wire():
    def __init__(self,pos1,pos2,ind):
        self.points = []
        self.pos1 = pos1
        self.pos2 = pos2
        self.dir = (pos2-pos1).normalize()
        t = 0
        self.index = ind
        point = pos1 +self.dir*(hit/2-0.001)
        while math.hypot(pos2.x-point.x,pos2.y-point.y) > hit:
            t += 1
            point = pos1 +self.dir*t*(hit/2-0.001)
            self.points.append(point)
        
    def update(self):
        for j in self.points:
            pygame.draw.circle(surface,(192,192,192),j,hit/2,2)
        pygame.draw.rect(surface, (255,255,0), pygame.Rect(self.pos1.x, self.pos1.y, hit, hit))
    def delete(self):
        wires[self.index] = None

class wall():
    def __init__(self,pos1,pos2,life,ind):
        self.points = []
        self.pos1 = pos1
        self.lives = life
        self.pos2 = pos2
        self.dir = (pos2-pos1).normalize()
        t = 0
        self.index = ind
        point = pos1 +self.dir*(hit/2-0.001)
        while math.hypot(pos2.x-point.x,pos2.y-point.y) > hit:
            t += 1
            point = pos1 +self.dir*t*(hit/2-0.001)*0.5
            self.points.append(point)
        
    def update(self):
        for j in self.points:
            pygame.draw.circle(surface,(213,207,207),j,hit/2)
        pygame.draw.rect(surface, (30,30,255), pygame.Rect(self.pos1.x, self.pos1.y, hit, hit))
        text_surface_start = myFont.render(str(self.lives),True,(0,0,0))
        surface.blit(text_surface_start, (self.pos1.x,self.pos1.y))
    def delete(self):
        walls[self.index] = None

class flag():
    def __init__(self,pos,count):
        self.count = count
        self.pos = pos
    
    def update(self):
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.pos.x, self.pos.y, hit*1.5, hit*1.5))
        text_surface_start = myFont.render(str(self.count),True,(0,0,0))
        surface.blit(text_surface_start, (self.pos.x,self.pos.y))
wirepoints = []
wires = []

class enemy():
    def __init__(self,pos,count,index):
        self.pos = pos
        self.side = 1
        self.count = count
        self.index = index
        
    def update(self):
        if armies[self.index] != None:
                pygame.draw.rect(surface, (214,32,78), pygame.Rect(self.pos.x, self.pos.y, hit, hit))
                text_surface_start = myFont.render(str(self.count),True,(0,0,0))
                surface.blit(text_surface_start, (self.pos.x,self.pos.y))
            
    def delete(self):
        armies[self.index] = None

class whym():
    def __init__(self):
        self.action = False
why = whym()
epos = []
gpos = []
wallpos = []
walls = []
end = None
wallpoints = []
wirepos = []
def makearmyg(pos,cou):
    temp = army(pos,cou,len(armies))
    armies.append(temp)
    gpos.append(temp.pos)

def makearmye(pos,cou):
    temp = enemy(pos,cou,len(armies))
    armies.append(temp)
    epos.append(temp.pos)

def makewire(pos1,pos2):
    temp = wire(pos1,pos2,len(wires))
    wires.append(temp)
    wirepos.append([temp.pos1,temp.pos2])

def makewall(pos1,pos2):
    temp = wall(pos1,pos2,1,len(walls))
    walls.append(temp)
    wallpos.append([temp.pos1,temp.pos2])

hit =20 
running = True
level = []
while running:
    surface.fill((60,60,60))
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[2]:
        for army1 in range(1,len(armies)+1):
            if armies[army1-1] != None:
                if mx >= armies[army1-1].pos.x and mx <= armies[army1-1].pos.x+hit:
                    if my >= armies[army1-1].pos.y and my <= armies[army1-1].pos.y+hit:
                        armies[army1-1].delete()
        for army1 in range(1,len(wires)+1):
                if wires[army1-1] != None:
                    if mx >= wires[army1-1].pos1.x and mx <= wires[army1-1].pos1.x+hit:
                        if my >= wires[army1-1].pos1.y and my <= wires[army1-1].pos1.y+hit:
                            wires[army1-1].delete()
        for army1 in range(1,len(walls)+1):
                if walls[army1-1] != None:
                    if mx >= walls[army1-1].pos1.x and mx <= walls[army1-1].pos1.x+hit:
                        if my >= walls[army1-1].pos1.y and my <= walls[army1-1].pos1.y+hit:
                            walls[army1-1].delete()
    b = False
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        elif event.type == pygame.KEYDOWN:
            for army1 in range(1,len(armies)+1):
                if armies[army1-1] != None:
                    if mx >= armies[army1-1].pos.x and mx <= armies[army1-1].pos.x+hit:
                        if my >= armies[army1-1].pos.y and my <= armies[army1-1].pos.y+hit:
                            armies[army1-1].count += 1
                            b = True
            for army1 in range(1,len(walls)+1):
                if walls[army1-1] != None:
                    if mx >= walls[army1-1].pos1.x and mx <= walls[army1-1].pos1.x+hit:
                        if my >= walls[army1-1].pos1.y and my <= walls[army1-1].pos1.y+hit:
                            walls[army1-1].lives += 1
                            b = True
            if end != None:
                if mx >= end.pos.x and mx <= end.pos.x+hit:
                    if my >= end.pos.y and my <= end.pos.y+hit:
                        end.count += 1
                        b = True
            if b != True:
                if event.key == pygame.K_a:
                    makearmyg(pygame.Vector2(mx,my),1)
                elif event.key == pygame.K_e:
                    makearmye(pygame.Vector2(mx,my),1)
                elif event.key == pygame.K_w:
                    wirepoints.append(pygame.Vector2(mx,my))
                    if len(wirepoints) == 2:
                        makewire(pygame.Vector2(mx,my),wirepoints[0])
                        wirepoints = []
                elif event.key == pygame.K_d:
                    wallpoints.append(pygame.Vector2(mx,my))
                    if len(wallpoints) == 2:
                        makewall(pygame.Vector2(mx,my),wallpoints[0])
                        wallpoints = []
                elif event.key == pygame.K_f:
                    end = flag(pygame.Vector2(mx,my),1)
                elif event.key == pygame.K_r:
                    print(level)
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None:
            armies[army1-1].update()
    for army1 in range(1,len(wires)+1):
        if wires[army1-1] != None:
            wires[army1-1].update()
    for army1 in range(1,len(walls)+1):
        if walls[army1-1] != None:
            walls[army1-1].update()
    if end != None:
        end.update()
    #level = [[],[],[],pygame.Vector2(0,0),0,[]]
    level = ""
    '''
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None and armies[army1-1].side == 0:
            level[0].append(armies[army1-1].pos)
            level[2].append(armies[army1-1].count)
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None and armies[army1-1].side == 1:
            level[1].append(armies[army1-1].pos)
            level[2].append(armies[army1-1].count)
    for army1 in range(1,len(wires)+1):
        if wires[army1-1] != None:
            level[5].append([wires[army1-1].pos1,wires[army1-1].pos2])
    if end != None:
        level[4] = end.count
        level[3] = end.pos
    '''
    level += ",[["
    done = False
    for army1 in range(1,len(armies)+1):
        try:
            if armies[army1-1] != None and armies[army1-1].side == 0 and done != True:
                level += "pygame.Vector2(" + str(armies[army1-1].pos.x) + "," + str(armies[army1-1].pos.y) + ")"
                done = True
            elif armies[army1-1] != None and armies[army1-1].side == 0 and done == True:
                level += ",pygame.Vector2(" + str(armies[army1-1].pos.x) + "," + str(armies[army1-1].pos.y) + ")"
        except:
            one=1
    level += "]"
    level += ",["
    done = False
    for army1 in range(1,len(armies)+1):
        try:
            if armies[army1-1] != None and armies[army1-1].side == 1 and done != True:
                level += "pygame.Vector2(" + str(armies[army1-1].pos.x) + "," + str(armies[army1-1].pos.y) + ")"
                done = True
            elif armies[army1-1] != None and armies[army1-1].side == 1 and done == True:
                level += ",pygame.Vector2(" + str(armies[army1-1].pos.x) + "," + str(armies[army1-1].pos.y) + ")"
        except:
            one = 1
    level += "]"
    level += ",["
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None and armies[army1-1].side == 0:
            level += str(armies[army1-1].count) + ","
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None and armies[army1-1].side == 1:
            level += str(armies[army1-1].count) + ","
    level += "0]"
    level += ","
    if end != None:
        level += "pygame.Vector2(" + str(end.pos.x) + "," + str(end.pos.y) + ")"
        level +=  "," + str(end.count) + ","
    level += "["
    done = False
    for army1 in range(1,len(wires)+1):
        try:
            
            if wires[army1-1] != None and done != True:
                level += "[" + "pygame.Vector2(" + str(wires[army1-1].pos1.x) + "," + str(wires[army1-1].pos1.y) + ")," + "pygame.Vector2(" + str(wires[army1-1].pos2.x) + "," + str(wires[army1-1].pos2.y) + ")]"
                done = True
            elif wires[army1-1] != None and done == True:
                level += ",[" + "pygame.Vector2(" + str(wires[army1-1].pos1.x) + "," + str(wires[army1-1].pos1.y) + ")," + "pygame.Vector2(" + str(wires[army1-1].pos2.x) + "," + str(wires[army1-1].pos2.y) + ")]"
        except:
            one =1
    level += "],["
    done = False
    for army1 in range(1,len(walls)+1):
        try:
            
            if walls[army1-1] != None and done != True:
                level += "[" + "pygame.Vector2(" + str(walls[army1-1].pos1.x) + "," + str(walls[army1-1].pos1.y) + ")," + "pygame.Vector2(" + str(walls[army1-1].pos2.x) + "," + str(walls[army1-1].pos2.y) + ")]"
                done = True
            elif walls[army1-1] != None and done == True:
                level += ",[" + "pygame.Vector2(" + str(walls[army1-1].pos1.x) + "," + str(walls[army1-1].pos1.y) + ")," + "pygame.Vector2(" + str(walls[army1-1].pos2.x) + "," + str(walls[army1-1].pos2.y) + ")]"
        except:
            one =1
    level += "],["
    for army1 in range(1,len(walls)+1):
        if walls[army1-1] != None:
            level += str(walls[army1-1].lives) + ","
    level += "0]]"
    level = level
    pygame.display.flip()