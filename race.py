import keyboard
import turtle
import time
import random
turt = turtle.Turtle()
top = turtle.Turtle()
combo = turtle.Turtle()
combo.ht()
turtle.back(350)
turt.back(350)
top.back(350)
turtle.sety(100)
turt.sety(-100)
top.sety(0)
turtle.clear()
turt.clear()
top.clear()
w = 1
while True:
    choose = random.randint(1,6)
    if choose == 1:
        if keyboard.is_pressed("a"):
            w +=1
        else:
            if keyboard.is_pressed("a"):
                turtle.fd(random.randint(11,20))
            
    
        
        if keyboard.is_pressed("g"):
            w += 1
        else:
            if keyboard.is_pressed("g"):
                top.fd(random.randint(11,20))
                
    
        if keyboard.is_pressed("l"):
            w += 1
        else:
            if keyboard.is_pressed("l"):
                turt.fd(random.randint(11,20))
    elif choose == 2:

            

        
        if keyboard.is_pressed("g"):
            w += 1
        else:
            if keyboard.is_pressed("g"):
                top.fd(random.randint(11,20))
        if keyboard.is_pressed("a"):
            w +=1
        else:
            if keyboard.is_pressed("a"):
                turtle.fd(random.randint(11,20))
        if keyboard.is_pressed("l"):
            w += 1
        else:
            if keyboard.is_pressed("l"):
                turt.fd(random.randint(11,20))
    elif choose == 3:
        if keyboard.is_pressed("a"):
            w +=1
        else:
            if keyboard.is_pressed("a"):
                turtle.fd(random.randint(11,20))
        if keyboard.is_pressed("l"):
            w += 1
        else:
            if keyboard.is_pressed("l"):
                turt.fd(random.randint(11,20))
        if keyboard.is_pressed("g"):
            w += 1
        else:
            if keyboard.is_pressed("g"):
                top.fd(random.randint(11,20))
    elif choose == 4:

            

        
        if keyboard.is_pressed("g"):
            w += 1
        else:
            if keyboard.is_pressed("g"):
                top.fd(random.randint(11,20))
        if keyboard.is_pressed("l"):
            w += 1
        else:
            if keyboard.is_pressed("l"):
                turt.fd(random.randint(11,20))
        if keyboard.is_pressed("a"):
            w +=1
        else:
            if keyboard.is_pressed("a"):
                turtle.fd(random.randint(11,20))
    elif choose == 5:

            
        if keyboard.is_pressed("l"):
            w += 1
        else:
            if keyboard.is_pressed("l"):
                turt.fd(random.randint(11,20))

        if keyboard.is_pressed("g"):
            w += 1
        else:
            if keyboard.is_pressed("g"):
                top.fd(random.randint(11,20))
        if keyboard.is_pressed("a"):
            w +=1
        else:
            if keyboard.is_pressed("a"):
                turtle.fd(random.randint(11,20))
    elif choose == 6:

            
        if keyboard.is_pressed("l"):
            w += 1
        else:
            if keyboard.is_pressed("l"):
                turt.fd(random.randint(11,20))
        if keyboard.is_pressed("a"):
            w +=1
        else:
            if keyboard.is_pressed("a"):
                turtle.fd(random.randint(11,20))

        if keyboard.is_pressed("g"):
            w += 1
        else:
            if keyboard.is_pressed("g"):
                top.fd(random.randint(11,20))



    
    

                

    if top.xcor() >= 350:
        combo.st()
        combo.write("Player 2 Wins")
        time.sleep(4)
        exit()
        
    if turt.xcor() >= 350:
        combo.st()
        combo.write("Player 3 Wins")
        time.sleep(4)
        exit()
    if turtle.xcor() >= 350:
        combo.st()
        combo.write("Player 1 Wins")
        time.sleep(4)
        exit()
        
                