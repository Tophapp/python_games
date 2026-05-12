import turtle
import keyboard
import time
import random
color = input("Drawing Mode On Or Off.  Awnser In lowercase. ")
w = 1

diacir = 20
speed = 4
turnangle = 4.5
turtwith = 15
currenttoggledraw = 1
currenttogglecolor = 1
currenttoggleerase = 0
currenttogglefill = 1
turtle.back(1)
while True:
    try:
        if keyboard.is_pressed("D"):
            turtle.right(turnangle)
        if keyboard.is_pressed("A"):
            turtle.left(turnangle)   
        if keyboard.is_pressed("S"):
            turtle.back(speed)
        if keyboard.is_pressed("W"):
            turtle.forward(speed)
        if color == "on":
            turtle.width(turtwith)
            if keyboard.is_pressed("E") and keyboard.is_pressed("Q"):
                turtwith = 15
            if keyboard.is_pressed("R"):
                turtle.reset()
                turtwith = 15
                currenttogglecolor = 1
                currenttoggleerase = 0
            if keyboard.is_pressed("F"):
                time.sleep(0.3)
                if currenttoggledraw == 2:
                    currenttoggledraw = 0
                currenttoggledraw += 1
            if currenttoggledraw == 1:
                turtle.pd()
            else:
                turtle.pu()

            if keyboard.is_pressed("V"):
                time.sleep(0.3)
                if currenttoggleerase == 2:
                    currenttoggleerase = 0
                currenttoggleerase += 1

            if currenttoggleerase == 1:
                turtle.pencolor("white")
            if currenttoggleerase != 1:
                
                if keyboard.is_pressed("C"):
                    time.sleep(0.3)

                    if currenttogglecolor == 5:
                        currenttogglecolor = 0
                    currenttogglecolor += 1
                if currenttogglecolor == 1:
                    turtle.color("black")
                if currenttogglecolor == 2:
                    turtle.color("lime green")
                elif currenttogglecolor == 3:
                    turtle.color("blue")
                elif currenttogglecolor == 4:
                    turtle.color("red")
                elif currenttogglecolor == 5:
                    turtle.color("yellow")
            if keyboard.is_pressed("E"):
                turtwith += 0.5
            if keyboard.is_pressed("Q"):
                turtwith -= 0.5
            if keyboard.is_pressed("P"):
                exit()
        else:
            turtle.clear()
            if keyboard.is_pressed("P"):
                exit()
            if keyboard.is_pressed("E"):
                speed += 0.5
            if keyboard.is_pressed("Q"):
                speed -= 0.5

    except:
        continue    
