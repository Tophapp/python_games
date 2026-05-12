import pygame
spaces = int(input("Trench Segments: ")) * 3
p1 = []
spacesize = 50
p2 = []
for b in range(spaces):
    p1.append(0)
    p2.append(0)
    p1.append(1)
    p2.append(0)

surface = pygame.display.set_mode((spacesize*5+10,spacesize*spaces+spaces*5))

# Drawing Rectangle
pygame.display.set_caption('Trenches')
turn = 0
turn +=2 
index = -1
movement = None
saved = -1
running = True
while running:
    if turn%2 == 0:
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)
            if mouse_x > spacesize*4+7.5+spacesize/2:
                    for h in range(0,spaces):
                        print(spacesize*h+h*5+spacesize)
                        if mouse_y > spacesize*h+h*5+spacesize:
                            index = h
                            mouse_y = -1
                            if movement == False and index != saved:
                                if p2[index] == 0:
                                    p2[index] = p2[saved]
                                    p2[saved] = 0
                                    movement = True
                            elif movement == None:
                                if p2[index] != 0:
                                    movement = False
                                    saved = index
                    
    surface.fill((200,200,200))
    for h in range(0,spaces):
        pygame.draw.rect(surface,(0,0,0),pygame.Rect(0,spacesize*h+h*5,spacesize+5,spacesize+5), 5)
        pygame.draw.rect(surface,(0,0,0),pygame.Rect(spacesize*4+5,spacesize*h+h*5,spacesize+5,spacesize+5), 5)
    for g in range(0,len(p1)):
        if p1[g] == 1:
            pygame.draw.circle(surface,(255,0,0),(spacesize*4+7.5+spacesize/2,spacesize*g+g*5+spacesize/2+2.5),round(spacesize/2-5))
        if p1[g] == 2:
            pygame.draw.circle(surface,(255,255,0),(spacesize*4+7.5+spacesize/2,spacesize*g+g*5+spacesize/2+2.5),round(spacesize/2-5))
    for g in range(0,len(p2)):
        if p2[g] == 1:
            pygame.draw.circle(surface,(255,0,0),(spacesize*4+7.5+spacesize/2,spacesize*g+g*5+spacesize/2+2.5),round(spacesize/2-5))
        if p2[g] == 2:
            pygame.draw.circle(surface,(255,255,0),(spacesize*4+7.5+spacesize/2,spacesize*g+g*5+spacesize/2+2.5),round(spacesize/2-5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
