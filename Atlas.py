import pygame
import random
import math
import time

pygame.init()
width = 500
height = 500
levelset = [[[pygame.Vector2(200,100),pygame.Vector2(100,100)],[pygame.Vector2(200,400),pygame.Vector2(250,250),pygame.Vector2(350,250)],[4,7,5,5,5],pygame.Vector2(300,300),4,[[pygame.Vector2(100,200),pygame.Vector2(500,200)]],[],[]],
            [[pygame.Vector2(2000,1000)],[pygame.Vector2(5000,1000)],[1,1],pygame.Vector2(5000,5000),100,[],[],[]]]
dest = None
font = "Comic San MS"
myFont = pygame.font.SysFont(font, 20)
myFont2 = pygame.font.SysFont(font, 100)
myFont3 = pygame.font.SysFont(font, 45)
speed = 0.03
levelnums = len(levelset)-1
class whym():
    def __init__(self):
        self.action = False
        self.action2 = False
        self.action1 =False
        self.running = True
        self.levelnum = 0
why = whym()
hit = 20
if pygame.mouse.get_pressed()[0]:
    click = True
else:
    click=False
armies = []
surface = pygame.display.set_mode((width,height))

class enemy():
    def __init__(self,side,pos,count,index):
        self.posm = pos
        self.pos = pygame.Vector2(self.posm.x-hit/2,self.posm.y-hit/2)
        self.count = count
        self.hurt = False
        self.index = index
        self.side = side
        self.dest = None
        self.hurtbuf = False
   
    def update(self):
        d = 0
        blue = False
        if self.dest != None:
                    for army1 in range(1,len(walls)+1):
                        if walls[army1-1] != None:
                            for a in range(1,len(walls[army1-1].points)+1):
                                if math.hypot(self.pos.x+((self.dest - self.pos).normalize()*(speed*1.25)).x-walls[army1-1].points[a-1].x,self.pos.y+((self.dest - self.pos).normalize()*(speed*1.25)).y-walls[army1-1].points[a-1].y) < hit:
                                    blue = True
        self.pos = pygame.Vector2(self.posm.x-hit/2,self.posm.y-hit/2)
        pygame.draw.rect(surface, (214,32,78), pygame.Rect(self.pos.x, self.pos.y, hit, hit))
        text_surface_start = myFont.render(str(self.count),True,(255,255,255))
        surface.blit(text_surface_start, (self.pos.x,self.pos.y))
        for army1 in range(1,len(armies)+1):
            if armies[army1-1] != None:
                if armies[army1-1].side != self.side:
                    dist = math.hypot(self.pos.x-armies[army1-1].pos.x, self.pos.y-armies[army1-1].pos.y)
                    if dist <= armies[army1-1].count*16 or dist < 48:
                        self.dest = armies[army1-1].pos
                    else:
                        d += 1
            else:
                d+=1
        if d == len(armies):
            self.dest = None
        if self.dest != None and blue != True:
            self.posm += ((self.dest - self.pos).normalize()*(speed*1.25))
        if self.count <= 0:
            self.delete()
       
           
    def delete(self):
        armies[self.index] = None

class army():
    def __init__(self,side,pos,count,index):
        self.posm = pos
        self.pos = pygame.Vector2(self.posm.x-hit/2,self.posm.y-hit/2)
        self.hurt = False
        self.sel = False
        self.count = count
        self.index = index
        self.side = side
        self.dest = None
        self.hurtbuf = 0
        self.breakbuf = 0
        self.breaking = False

    def update(self):
        self.pos = pygame.Vector2(self.posm.x-hit/2,self.posm.y-hit/2)
        if armies[self.index] != None:
            done = False
            for army1 in range(1,len(armies)+1):
                if armies[army1-1] != None:
                    if armies[army1-1].side != self.side:
                        if armies[army1-1].pos.x >= self.pos.x and armies[army1-1].pos.x <= self.pos.x+hit:
                            if armies[army1-1].pos.y >= self.pos.y and armies[army1-1].pos.y <= self.pos.y+hit:
                                done = True
            if done == False:  
                blue = False
                if self.dest != None and self.sel == True:
                    for army1 in range(1,len(walls)+1):
                        if walls[army1-1] != None:
                            for a in range(1,len(walls[army1-1].points)+1):
                                if math.hypot(self.pos.x+((self.dest - self.posm).normalize()*speed).x-walls[army1-1].points[a-1].x,self.pos.y+((self.dest - self.posm).normalize()*speed).y-walls[army1-1].points[a-1].y) < hit:
                                    blue = True
                g = self.sel
                if why.action == False:
                    if mx >= self.pos.x and mx <= self.pos.x+hit and click == True and self.sel == False:
                        if my >= self.pos.y and my <= self.pos.y+hit:
                            self.sel = True
                            why.action = True
                    elif mx >= self.pos.x and mx <= self.pos.x+hit and click == True and self.sel == True and self.dest == None:
                        if my >= self.pos.y and my <= self.pos.y+hit:
                            self.sel = False
                            why.action = True
                    elif mx >= self.pos.x and mx <= self.pos.x+hit and click == True and self.sel == True and self.dest != None:
                        if my >= self.pos.y and my <= self.pos.y+hit:
                            self.dest = None
                            why.action = True
               
                if mx >= self.pos.x and mx <= self.pos.x+hit and click2 == True:
                        if my >= self.pos.y and my <= self.pos.y+hit:
                            if self.count > 1 and round(self.count) == self.count and why.action2 == False:
                                done = False
                                for s in armies:
                                    try:
                                        if armies[s.index] != None:
                                            if s.pos.y >= self.pos.y+1 and s.pos.y <= self.pos.y+hit*2+1 and s.pos.x >= self.pos.x and s.pos.x <= self.pos.x+hit*2:
                                                done = True
                                    except:
                                        one=1
                                if done == False:
                                    if round(self.count/2) == self.count/2:
                                        self.count/=2
                                        makearmyg(pygame.Vector2(self.pos.x,self.pos.y+hit+1),self.count)
                                    else:
                                        self.count = round(self.count/2+0.3)
                                        makearmyg(pygame.Vector2(self.pos.x,self.pos.y+hit+1),self.count-1)
                                    why.action2 = True
                if self.dest != None and self.sel == True and blue == False:
                    self.posm += (self.dest - self.posm).normalize()*speed
                for k in armies:
                    try:
                        if armies[k.index] != None and k.side == self.side:
                            if k.pos.x > self.pos.x and k.pos.x < self.pos.x+hit:
                                if k.pos.y > self.pos.y and k.pos.y < self.pos.y+hit:
                                    self.count += k.count
                                    k.delete()
                    except:
                        self.count = self.count
                pygame.draw.rect(surface, (125, 230, 97), pygame.Rect(self.pos.x, self.pos.y, hit, hit))
                text_surface_start = myFont.render(str(self.count),True,(0,0,0))
                surface.blit(text_surface_start, (self.pos.x,self.pos.y))
                self.count = int(round(self.count))
            else:
                for army1 in range(1,len(armies)+1):
                    if armies[army1-1] != None:
                        if armies[army1-1].side != self.side:
                            if armies[army1-1].pos.x >= self.pos.x and armies[army1-1].pos.x <= self.pos.x+hit:
                                if armies[army1-1].pos.y >= self.pos.y and armies[army1-1].pos.y <= self.pos.y+hit:
                                    if random.randint(-armies[army1-1].count,self.count) <= 1:
                                        self.count -= armies[army1-1].count
                                        armies[army1-1].count -= abs(math.floor(self.count/2))
                                    else:
                                        armies[army1-1].count -= self.count
                                        self.count -= abs(math.floor(armies[army1-1].count/2))
            if self.count <= 0:
                self.delete()
           
    def delete(self):
        armies[self.index] = None

levels = []
class level():
    def __init__(self,ppos,epos,cou,enpos,flgs,wrps,wlps,lives):
        self.playerpos = ppos
        self.enemypos = epos
        self.counts = cou
        self.endpos = enpos
        self.flags = flgs
        self.wirepos = wrps
        self.wallpos = wlps
        self.lives = lives

class wire():
    def __init__(self,pos1,pos2):
        self.points = []
        self.dir = (pos2-pos1).normalize()
        t = 0
        point = pos1 +self.dir*(hit/2-0.001)
        while math.hypot(pos2.x-point.x,pos2.y-point.y) > hit:
            t += 1
            point = pos1 +self.dir*t*(hit/2-0.001)
            self.points.append(point)
       
    def update(self):
        for j in self.points:
            pygame.draw.circle(surface,(192,192,192),j,hit/2,2)
        for army1 in range(1,len(armies)+1):
            if armies[army1-1] != None:
                for j in self.points:
                    if math.hypot(armies[army1-1].pos.x-j.x,armies[army1-1].pos.y-j.y) < hit/2 and armies[army1-1].hurt != True:
                        armies[army1-1].hurt = True
                        armies[army1-1].count -= 1
wires = []

class wall():
    def __init__(self,pos1,pos2,life,ind):
        self.points = []
        self.life = life
        self.index = ind
        self.dir = (pos2-pos1).normalize()
        t = 0
        point = pos1 +self.dir*(hit/2-0.001)
        while math.hypot(pos2.x-point.x,pos2.y-point.y) > hit:
            t += 1
            point = pos1 +self.dir*t*(hit/2-0.001)*0.8
            self.points.append(point)
       
    def update(self):
        for j in self.points:
            pygame.draw.circle(surface,(213,207,207),j,hit/2)
        for army1 in range(1,len(armies)+1):
            if armies[army1-1] != None:
                for j in self.points:
                    if armies[army1-1].side == 0:
                        if math.hypot(armies[army1-1].pos.x-j.x,armies[army1-1].pos.y-j.y) < hit*1.5 and armies[army1-1].breaking != True:
                            armies[army1-1].breaking = True
                            self.life -= 1
        if self.life <= 0:
            self.delete()
           
    def delete(self):
        walls[self.index] = None
walls = []


class flag():
    def __init__(self,pos,flgs):
        self.flags = flgs
        self.pos = pos
   
    def update(self):
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.pos.x, self.pos.y, hit*1.5, hit*1.5))
        text_surface_start = myFont.render(str(self.flags),True,(0,0,0))
        surface.blit(text_surface_start, (self.pos.x,self.pos.y))
        for army1 in range(1,len(armies)+1):
            if armies[army1-1] != None:
                if armies[army1-1].side != 1:
                    if armies[army1-1].pos.x >= self.pos.x and armies[army1-1].pos.x <= self.pos.x+hit*1.5:
                        if armies[army1-1].pos.y >= self.pos.y and armies[army1-1].pos.y <= self.pos.y+hit*1.5:
                            self.flags-=armies[army1-1].count
                            armies[army1-1].delete()
        if self.flags <= 0:
            why.levelnum += 1

def makearmyg(pos,cou):
    temp = army(0,pos,cou,len(armies))
    armies.append(temp)

def makearmye(pos,cou):
    temp = enemy(1,pos,cou,len(armies))
    armies.append(temp)

def makewire(pos1,pos2):
    temp = wire(pos1,pos2)
    wires.append(temp)

def makelevel(leveltile):
    temp = level(leveltile[0],leveltile[1],leveltile[2],leveltile[3],leveltile[4],leveltile[5],leveltile[6],leveltile[7])
    levels.append(temp)

def makewall(pos1,pos2,lf):
    temp = wall(pos1,pos2,lf,len(walls))
    walls.append(temp)

for lev in range(1,levelnums+1):
    makelevel(levelset[lev-1])
makelevel(levelset[lev])
why.levelnum = 0
j = -1
while why.running:
    surface.fill((30,30,30))
    if why.levelnum != j or reset == True:
        levels = []
        levelset = [[[pygame.Vector2(200,100),pygame.Vector2(100,100)],[pygame.Vector2(200,400),pygame.Vector2(250,250),pygame.Vector2(350,250)],[4,7,5,5,5],pygame.Vector2(300,300),4,[[pygame.Vector2(100,200),pygame.Vector2(500,200)]],[],[]]
            ,[[pygame.Vector2(238.0,101.0)],[pygame.Vector2(85.0,411.0),pygame.Vector2(189.0,305.0),pygame.Vector2(93.0,288.0),pygame.Vector2(379.0,344.0),pygame.Vector2(258.0,258.0),pygame.Vector2(9.0,376.0)],[1,1,1,1,1,1,1,0],pygame.Vector2(254.0,442.0),1,[[pygame.Vector2(452.0,346.0),pygame.Vector2(152.0,154.0)],[pygame.Vector2(0.0,307.0),pygame.Vector2(134.0,219.0)],[pygame.Vector2(499.0,468.0),pygame.Vector2(195.0,337.0)],[pygame.Vector2(52.0,499.0),pygame.Vector2(181.0,425.0)],[pygame.Vector2(50.0,113.0),pygame.Vector2(64.0,262.0)],[pygame.Vector2(148.0,33.0),pygame.Vector2(42.0,123.0)],[pygame.Vector2(354.0,35.0),pygame.Vector2(148.0,42.0)],[pygame.Vector2(452.0,113.0),pygame.Vector2(342.0,31.0)],[pygame.Vector2(458.0,360.0),pygame.Vector2(458.0,123.0)],[pygame.Vector2(495.0,376.0),pygame.Vector2(460.0,356.0)]],[],[]]
            ,[[pygame.Vector2(66.0,100.0),pygame.Vector2(159.0,85.0)],[pygame.Vector2(269.0,232.0),pygame.Vector2(148.0,370.0),pygame.Vector2(460.0,287.0),pygame.Vector2(215.0,470.0),pygame.Vector2(133.0,242.0)],[5,5,4,4,3,3,6,0],pygame.Vector2(416.0,404.0),6,[[pygame.Vector2(240.0,292.0),pygame.Vector2(499.0,240.0)],[pygame.Vector2(219.0,349.0),pygame.Vector2(163.0,498.0)],[pygame.Vector2(233.0,3.0),pygame.Vector2(498.0,205.0)],[pygame.Vector2(189.0,140.0),pygame.Vector2(441.0,171.0)]],[],[]]#Tutorial
            ,[[pygame.Vector2(168.0,48.0),pygame.Vector2(50.0,47.0),pygame.Vector2(78.0,64.0),pygame.Vector2(115.0,126.0),pygame.Vector2(121.0,12.0)],[pygame.Vector2(85.0,288.0),pygame.Vector2(354.0,125.0),pygame.Vector2(478.0,121.0),pygame.Vector2(2.0,303.0),pygame.Vector2(271.0,289.0),pygame.Vector2(326.0,209.0),pygame.Vector2(181.0,311.0),pygame.Vector2(427.0,109.0),pygame.Vector2(111.0,415.0),pygame.Vector2(436.0,263.0),pygame.Vector2(317.0,372.0)],[3,2,1,3,5,2,1,2,1,2,3,1,3,4,3,5,0],pygame.Vector2(430.0,433.0),5,[[pygame.Vector2(111.0,233.0),pygame.Vector2(0.0,263.0)],[pygame.Vector2(196.0,272.0),pygame.Vector2(106.0,230.0)],[pygame.Vector2(277.0,221.0),pygame.Vector2(199.0,272.0)],[pygame.Vector2(301.0,138.0),pygame.Vector2(282.0,214.0)],[pygame.Vector2(283.0,184.0),pygame.Vector2(270.0,244.0)],[pygame.Vector2(366.0,76.0),pygame.Vector2(296.0,135.0)],[pygame.Vector2(498.0,82.0),pygame.Vector2(365.0,76.0)],[pygame.Vector2(393.0,429.0),pygame.Vector2(407.0,483.0)],[pygame.Vector2(455.0,397.0),pygame.Vector2(403.0,417.0)],[pygame.Vector2(494.0,443.0),pygame.Vector2(474.0,409.0)],[pygame.Vector2(487.0,490.0),pygame.Vector2(414.0,491.0)]],[],[]]
            ,[[pygame.Vector2(367.0,431.0),pygame.Vector2(379.0,472.0),pygame.Vector2(348.0,472.0),pygame.Vector2(340.0,444.0),pygame.Vector2(311.0,468.0)],[pygame.Vector2(199.0,132.0),pygame.Vector2(222.0,424.0),pygame.Vector2(87.0,341.0),pygame.Vector2(58.0,132.0),pygame.Vector2(311.0,252.0),pygame.Vector2(260.0,60.0)],[5,5,5,5,10,8,3,1,2,3,25,0],pygame.Vector2(15.0,25.0),10,[[pygame.Vector2(160.0,181.0),pygame.Vector2(166.0,29.0)],[pygame.Vector2(0.0,125.0),pygame.Vector2(58.0,220.0)],[pygame.Vector2(121.0,36.0),pygame.Vector2(104.0,54.0)],[pygame.Vector2(244.0,109.0),pygame.Vector2(162.0,72.0)],[pygame.Vector2(222.0,158.0),pygame.Vector2(271.0,228.0)],[pygame.Vector2(395.0,22.0),pygame.Vector2(264.0,0.0)],[pygame.Vector2(322.0,105.0),pygame.Vector2(383.0,21.0)],[pygame.Vector2(417.0,168.0),pygame.Vector2(400.0,124.0)],[pygame.Vector2(330.0,91.0),pygame.Vector2(404.0,135.0)],[pygame.Vector2(358.0,302.0),pygame.Vector2(410.0,176.0)],[pygame.Vector2(154.0,331.0),pygame.Vector2(3.0,278.0)],[pygame.Vector2(177.0,432.0),pygame.Vector2(288.0,296.0)],[pygame.Vector2(64.0,428.0),pygame.Vector2(141.0,325.0)],[pygame.Vector2(227.0,499.0),pygame.Vector2(174.0,425.0)],[pygame.Vector2(440.0,497.0),pygame.Vector2(359.0,295.0)],[pygame.Vector2(270.0,424.0),pygame.Vector2(391.0,397.0)],[pygame.Vector2(96.0,85.0),pygame.Vector2(69.0,62.0)],[pygame.Vector2(111.0,82.0),pygame.Vector2(50.0,99.0)],[pygame.Vector2(0.0,85.0),pygame.Vector2(115.0,81.0)],[pygame.Vector2(186.0,215.0),pygame.Vector2(101.0,89.0)],[pygame.Vector2(128.0,209.0),pygame.Vector2(260.0,221.0)],[pygame.Vector2(332.0,99.0),pygame.Vector2(274.0,151.0)]],[],[]]#Mals
            ,[[pygame.Vector2(61.0,49.0),pygame.Vector2(51.0,96.0),pygame.Vector2(117.0,38.0)],[pygame.Vector2(83.0,474.0),pygame.Vector2(108.0,367.0),pygame.Vector2(168.0,263.0),pygame.Vector2(254.0,214.0),pygame.Vector2(347.0,218.0),pygame.Vector2(449.0,233.0),pygame.Vector2(348.0,377.0),pygame.Vector2(309.0,417.0)],[5,3,4,4,4,4,4,4,4,3,3,0],pygame.Vector2(345.0,421.0),3,[[pygame.Vector2(93.0,306.0),pygame.Vector2(23.0,491.0)],[pygame.Vector2(246.0,182.0),pygame.Vector2(104.0,282.0)],[pygame.Vector2(486.0,207.0),pygame.Vector2(274.0,188.0)],[pygame.Vector2(68.0,263.0),pygame.Vector2(9.0,385.0)],[pygame.Vector2(221.0,160.0),pygame.Vector2(86.0,246.0)],[pygame.Vector2(494.0,176.0),pygame.Vector2(264.0,155.0)],[pygame.Vector2(255.0,347.0),pygame.Vector2(216.0,495.0)],[pygame.Vector2(378.0,329.0),pygame.Vector2(498.0,395.0)]],[],[]]
            ,[[pygame.Vector2(255.0,60.0),pygame.Vector2(235.0,58.0)],[pygame.Vector2(110.0,242.0),pygame.Vector2(402.0,313.0),pygame.Vector2(7.0,36.0),pygame.Vector2(475.0,58.0),pygame.Vector2(207.0,340.0),pygame.Vector2(267.0,180.0),pygame.Vector2(324.0,245.0),pygame.Vector2(77.0,100.0),pygame.Vector2(437.0,122.0),pygame.Vector2(231.0,375.0)],[5,5,3,4,6,6,2,3,2,2,2,2,0],pygame.Vector2(151.0,410.0),3,[[pygame.Vector2(27.0,119.0),pygame.Vector2(109.0,9.0)],[pygame.Vector2(30.0,270.0),pygame.Vector2(235.0,10.0)],[pygame.Vector2(50.0,380.0),pygame.Vector2(374.0,8.0)],[pygame.Vector2(205.0,478.0),pygame.Vector2(474.0,158.0)],[pygame.Vector2(318.0,461.0),pygame.Vector2(487.0,293.0)],[pygame.Vector2(424.0,468.0),pygame.Vector2(478.0,396.0)],[pygame.Vector2(148.0,488.0),pygame.Vector2(2.0,301.0)],[pygame.Vector2(58.0,494.0),pygame.Vector2(0.0,412.0)],[pygame.Vector2(284.0,492.0),pygame.Vector2(3.0,167.0)],[pygame.Vector2(392.0,495.0),pygame.Vector2(9.0,65.0)],[pygame.Vector2(491.0,479.0),pygame.Vector2(25.0,6.0)],[pygame.Vector2(499.0,341.0),pygame.Vector2(117.0,7.0)],[pygame.Vector2(486.0,231.0),pygame.Vector2(265.0,5.0)],[pygame.Vector2(499.0,128.0),pygame.Vector2(397.0,0.0)],[pygame.Vector2(495.0,14.0),pygame.Vector2(6.0,494.0)]],[],[]]#Grid
            ,[[pygame.Vector2(472.0,127.0),pygame.Vector2(468.0,317.0),pygame.Vector2(468.0,211.0)],[pygame.Vector2(70.0,113.0),pygame.Vector2(187.0,233.0),pygame.Vector2(48.0,360.0),pygame.Vector2(117.0,274.0),pygame.Vector2(130.0,188.0),pygame.Vector2(252.0,186.0),pygame.Vector2(199.0,142.0),pygame.Vector2(162.0,105.0),pygame.Vector2(309.0,113.0),pygame.Vector2(234.0,386.0)],[4,4,2,1,2,2,1,1,2,2,2,1,7,0],pygame.Vector2(32.0,207.0),4,[[pygame.Vector2(5.0,495.0),pygame.Vector2(497.0,1.0)],[pygame.Vector2(495.0,499.0),pygame.Vector2(5.0,3.0)]],[],[]]
            ,[[pygame.Vector2(167.0,98.0),pygame.Vector2(285.0,70.0),pygame.Vector2(209.0,50.0),pygame.Vector2(209.0,49.0),pygame.Vector2(102.0,119.0),pygame.Vector2(65.0,81.0),pygame.Vector2(54.0,155.0),pygame.Vector2(83.0,198.0),pygame.Vector2(130.0,67.0),pygame.Vector2(177.0,30.0),pygame.Vector2(17.0,110.0)],[pygame.Vector2(74.0,445.0),pygame.Vector2(146.0,379.0),pygame.Vector2(147.0,377.0),pygame.Vector2(266.0,296.0),pygame.Vector2(193.0,323.0),pygame.Vector2(321.0,237.0),pygame.Vector2(321.0,235.0),pygame.Vector2(389.0,205.0),pygame.Vector2(430.0,138.0),pygame.Vector2(482.0,94.0),pygame.Vector2(483.0,93.0),pygame.Vector2(20.0,467.0)],[3,4,2,1,2,1,1,1,3,4,3,6,4,4,6,3,3,3,4,6,4,4,4,0],pygame.Vector2(391.0,432.0),1,[[pygame.Vector2(368.0,107.0),pygame.Vector2(493.0,51.0)],[pygame.Vector2(349.0,169.0),pygame.Vector2(358.0,111.0)],[pygame.Vector2(225.0,203.0),pygame.Vector2(330.0,192.0)],[pygame.Vector2(195.0,279.0),pygame.Vector2(226.0,218.0)],[pygame.Vector2(81.0,295.0),pygame.Vector2(179.0,279.0)],[pygame.Vector2(62.0,372.0),pygame.Vector2(91.0,315.0)],[pygame.Vector2(2.0,390.0),pygame.Vector2(47.0,383.0)],[pygame.Vector2(91.0,350.0),pygame.Vector2(34.0,403.0)],[pygame.Vector2(226.0,265.0),pygame.Vector2(153.0,292.0)],[pygame.Vector2(247.0,176.0),pygame.Vector2(225.0,238.0)],[pygame.Vector2(371.0,161.0),pygame.Vector2(308.0,204.0)],[pygame.Vector2(410.0,92.0),pygame.Vector2(367.0,134.0)],[pygame.Vector2(498.0,39.0),pygame.Vector2(473.0,70.0)],[pygame.Vector2(415.0,348.0),pygame.Vector2(300.0,374.0)],[pygame.Vector2(492.0,278.0),pygame.Vector2(400.0,297.0)],[pygame.Vector2(196.0,386.0),pygame.Vector2(287.0,334.0)],[pygame.Vector2(226.0,497.0),pygame.Vector2(319.0,410.0)],[pygame.Vector2(211.0,434.0),pygame.Vector2(100.0,496.0)]],[],[]]#Barge
            ,[[pygame.Vector2(2000,1000)],[pygame.Vector2(5000,1000)],[1,1],pygame.Vector2(5000,5000),100,[],[],[]]]#en
        '''
        levelset = [[[pygame.Vector2(109.0,194.0)],[pygame.Vector2(97.0,268.0)],[10,4,0],pygame.Vector2(297.0,408.0),1,[],[[pygame.Vector2(499.0,243.0),pygame.Vector2(1.0,239.0)]],[1,0]]
                    ,[[pygame.Vector2(2000,1000)],[pygame.Vector2(5000,1000)],[1,1],pygame.Vector2(5000,5000),100,[],[],[]]]
        '''
        levelnums = len(levelset)-1
        for lev in range(1,levelnums+1):
            makelevel(levelset[lev-1])
        makelevel(levelset[lev])
        armies = []
        wires = []
        c = 0
        for g in range(1,len(levels[why.levelnum].playerpos)+1):
            makearmyg(levels[why.levelnum].playerpos[g-1],levels[why.levelnum].counts[c])
            c+=1
        for g in range(1,len(levels[why.levelnum].enemypos)+1):
            makearmye(levels[why.levelnum].enemypos[g-1],levels[why.levelnum].counts[c])
            c+=1
        if len(levels[why.levelnum].wirepos) != 0:
            for g in range(1,len(levels[why.levelnum].wirepos)+1):
                makewire(levels[why.levelnum].wirepos[g-1][0],levels[why.levelnum].wirepos[g-1][1])
        if len(levels[why.levelnum].wallpos) != 0:
            for g in range(1,len(levels[why.levelnum].wallpos)+1):
                makewall(levels[why.levelnum].wallpos[g-1][0],levels[why.levelnum].wallpos[g-1][1],levels[why.levelnum].lives[g-1])
        FlagsRCool = flag(levels[why.levelnum].endpos,levels[why.levelnum].flags)
        reset = False
    j = why.levelnum
    FlagsRCool.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mx, my = pygame.mouse.get_pos()
    if click == True and why.action == False:
        for army1 in range(1,len(armies)+1):
            if armies[army1-1] != None:
                if armies[army1-1].side == 0:
                    if armies[army1-1].sel == True and armies[army1-1].dest == None:
                        armies[army1-1].dest = pygame.Vector2(mx,my)
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None:
            if armies[army1-1].dest != None and armies[army1-1].side == 0:
                pygame.draw.rect(surface, (255,0,0), pygame.Rect(armies[army1-1].dest.x, armies[army1-1].dest.y, 3, 3))
    if pygame.mouse.get_pressed()[0]:
        click = True
    else:
        why.action = False
        click = False
    if pygame.mouse.get_pressed()[2]:
        for army1 in range(1,len(armies)+1):
            if armies[army1-1] != None and armies[army1-1].side == 0:
                armies[army1-1].sel = False
                armies[army1-1].dest =None
        click2 = True
    else:
        why.action2 = False
        click2 = False
    hi = 0
    for wr in wires:
        wr.update()
    for army1 in range(1,len(walls)+1):
        if walls[army1-1] != None:
            walls[army1-1].update()
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None:
            armies[army1-1].update()
            if armies[army1-1] != None:
                armies[army1-1].hurtbuf += 1
                if armies[army1-1].side == 0:
                    armies[army1-1].breakbuf += 1
                if armies[army1-1].hurtbuf > 2500:
                    armies[army1-1].hurt = False
                    armies[army1-1].hurtbuf = 0
                if armies[army1-1].side == 0:
                    if armies[army1-1].breakbuf > 1000:
                        armies[army1-1].breaking = False
                        armies[army1-1].breakbuf = 0
                if armies[army1-1].side == 0:
                    hi += 1
    if hi <= 0:
        reset = True
    speedcount = 0
    for army1 in range(1,len(armies)+1):
        if armies[army1-1] != None:
            speedcount += 1
    for army1 in range(1,len(wires)+1):
        if wires[army1-1] != None:
            speedcount += 1
    for army1 in range(1,len(walls)+1):
        if walls[army1-1] != None:
            speedcount += 2
    speedcount += 1
    speed = speedcount/3*0.01

    if why.levelnum == levelnums:
        b = True
        if b == True:
            surface.fill((30,30,30))
            text_surface_start = myFont2.render(str("You Win!"),True,(255,255,255))
            surface.blit(text_surface_start, (0,height/2-100))
            text_surface_start = myFont3.render(str("This Program Will Now Go Boom"),True,(255,255,255))
            surface.blit(text_surface_start, (0,height/2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    b = False
            pygame.display.flip()
            time.sleep(4)
            why.running = False

    pygame.display.flip()