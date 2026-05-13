import pygame
import random
import time
pygame.init()
# Edit These Variables

font = "Comic San MS"
increse = 0.1 # Increse Of Red Value Every Fraction Of A Second, Adds Encouragement, 0 Is Fine
timebetween = 0 # Time Between Flashcards (Seconds), 0 Is Fine
maincolor = (255,0,255) # RGB Values
secondarycolor = (51,255,255) # RGB Values

# Question Sets
queposs1 = ["5x1","5","5x20","100","5x2","10","5x19","95","5x3","15","5x18","90","5x4","20","5x17","85","5x5","25","5x16","80","5x6","30","5x15","75","5x7","35","5x14","70","5x8","40","5x13","65","5x9","45","5x12","60","5x10","50","5x11","55"]
title1 = "x5"

queposs2 = []
title2 = "BLANK"

queposs3 = []
title3 = "BLANK"

queposs4 = []
title4 = "BLANK"

# Not These
myFont = pygame.font.SysFont(font, 500)
myFont2 = pygame.font.SysFont(font, 300)
myFont3 = pygame.font.SysFont(font, 200)
myFont4 = pygame.font.SysFont(font, 100)
myFont5 = pygame.font.SysFont(font, 150)
screen = pygame.display.set_mode((1500, 900))
timerun = False
inputing = ""
response = ""
fontcolor = (0,0,0)
queposs = []
questions = []
tal = True
selection = True
while selection:
    screen.fill(maincolor)
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                queposs = queposs1
                selection = False
            if event.key == pygame.K_2:
                queposs = queposs2
                selection = False
            if event.key == pygame.K_3:
                queposs = queposs3
                selection = False
            if event.key == pygame.K_4:
                queposs = queposs4
                selection = False
    
    pygame.draw.rect(screen, secondarycolor, pygame.Rect(30, 30, 650, 350))
    pygame.draw.rect(screen, secondarycolor, pygame.Rect(820, 30, 650, 350))
    pygame.draw.rect(screen, secondarycolor, pygame.Rect(820, 520, 650, 350))
    pygame.draw.rect(screen, secondarycolor, pygame.Rect(30, 520, 650, 350))
    text_surface_start = myFont4.render(title1,True,fontcolor)
    screen.blit(text_surface_start, (40,130))
    text_surface_start = myFont4.render(title2,True,fontcolor)
    screen.blit(text_surface_start, (830,130))
    text_surface_start = myFont4.render(title3,True,fontcolor)
    screen.blit(text_surface_start, (40,620))
    text_surface_start = myFont4.render(title4,True,fontcolor)
    screen.blit(text_surface_start, (830,620))
    text_surface_start = myFont4.render("Set #1",True,fontcolor)
    screen.blit(text_surface_start, (40,40))
    text_surface_start = myFont4.render("Set #2",True,fontcolor)
    screen.blit(text_surface_start, (830,40))
    text_surface_start = myFont4.render("Set #3",True,fontcolor)
    screen.blit(text_surface_start, (40,530))
    text_surface_start = myFont4.render("Set #4",True,fontcolor)
    screen.blit(text_surface_start, (830,530))
    text_surface_start = myFont4.render("To Check Your Answer, Press Tab.",True,fontcolor)
    screen.blit(text_surface_start, (30,385))
    text_surface_start = myFont4.render("Press The # Of The Set You Want.",True,fontcolor)
    screen.blit(text_surface_start, (30,450))
    pygame.display.flip()
    
while tal:
    number = random.randint(0,len(queposs)-1)
    if number % 2 != 1:
        questions.append(queposs[number])
        questions.append(queposs[number+1])
        queposs.pop(number)
        queposs.pop(number)
    if len(queposs) == 0:
        tal = False
for x in range(1, (len(questions) +1)):
    response = ""
    inputing = ""
    fontcolor = (0,0,0)
    if (x -1) % 2 != 1:
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        curr = questions[x-1]
        answer = questions[x]
        correct = True
        # Main Loop
        while correct:
            if timerun != True:
                color = (color[0]+increse,color[1],color[2])
                if color[0] > 255:
                    color = (255,color[1]-increse,color[2]-increse)
                if color[1] < 0:
                    color = (color[0],0,color[2])
                if color[2] < 0:
                    color = (color[0],color[1],0)
            if color == (255,0,0) or timerun == True:
                timerun = True
                color = (color[0]-increse,0,0)
            if timerun == True:
                fontcolor = (255,255,255)
            if color == (0,0,0):
                fontcolor = (255,255,255)
            if color[0] < 0:
                color = (0,0,0)
                #Input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key != pygame.K_BACKSPACE:
                        if event.key == pygame.K_0:
                            inputing += "0"
                        elif event.key == pygame.K_1:
                            inputing += "1"
                        elif event.key == pygame.K_2:
                            inputing += "2"
                        elif event.key == pygame.K_3:
                            inputing += "3"
                        elif event.key == pygame.K_4:
                            inputing += "4"
                        elif event.key == pygame.K_5:
                            inputing += "5"
                        elif event.key == pygame.K_6:
                            inputing += "6"
                        elif event.key == pygame.K_7:
                            inputing += "7"
                        elif event.key == pygame.K_8:
                            inputing += "8"
                        elif event.key == pygame.K_9:
                            inputing += "9"
                        elif event.key == pygame.K_PERIOD:
                            inputing += "."
                        elif event.key == pygame.K_TAB:
                            if answer == inputing:
                                response = "Correct"
                                correct = False
                                pygame.display.flip()
                                time.sleep(timebetween)
                                break
                            else:
                                response = "Incorrect, Try Again"
                                inputing = ""
                    else:
                        inputing = inputing[:-1]
            
            # Changing surface color
            screen.fill(color)
            text_surface = myFont.render(curr,True,fontcolor)
            screen.blit(text_surface, (350, 100))
            text_surface2 = myFont2.render(inputing,True,fontcolor)
            screen.blit(text_surface2, (50, 600))
            text_surface3 = myFont3.render(response,True,fontcolor)
            screen.blit(text_surface3, (50, 400))
            pygame.display.flip()
screen.fill(maincolor)
text_surface_end = myFont5.render("CONGRATSULATIONS!!!",True,fontcolor)
screen.blit(text_surface_end, (50, 100))
text_surface_end = myFont4.render("You Are Done With Flash Cards For Today!",True,fontcolor)
screen.blit(text_surface_end, (50, 300))
text_surface_end = myFont4.render("This Program Will Now Self-destruct,",True,fontcolor)
screen.blit(text_surface_end, (50, 500))
text_surface_end = myFont4.render("You May Go On With Your Day.",True,fontcolor)
screen.blit(text_surface_end, (50, 700))
pygame.display.flip()
time.sleep(2.5) 