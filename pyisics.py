import pygame
import random
import math

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
objects = []
class metal():
    def __init__(self):
        self.speed = 0.5
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.angle = 270
        self.width = random.randint(10,60)
        self.hight = random.randint(10,60)
        self.mass = ((self.width + self.hight) / 40)
        self.speed -= (self.mass/4)
        if self.speed <= 0:
            self.speed = 0.1
        self.rect = pygame.Rect(self.pos.x,self.pos.y, self.width, self.hight)

        
        

    def exist(self):

        pygame.draw.rect(screen, "grey", self.rect)

    def move(self):
        
        self.pos.x += math.sin(self.angle * 0.0174533) * self.speed
        self.pos.y += math.cos(self.angle * 0.0174533) * self.speed
        self.rect = pygame.Rect(int(self.pos.x),int(self.pos.y), self.width, self.hight)
    def gravity(self):
         h = 2


def makemetal():
    curr = metal()
    objects.append(curr)
makemetal()
running = True
tick = 0
while running:
    screen.fill((255,255,255))
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    for apples in objects:
        if tick >= 10:
            apples.move()
            tick = 0
        apples.exist()

    pygame.display.flip()