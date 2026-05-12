import random
import os
import time
diff = int(input("Enter The Difficuilty Level From 1 To 5: "))
last = {"wood":0,"glass":0,"steel":0,"brick":0}
money = 100
woodbaseprice = 1
woodprice = woodbaseprice
woodstock = 0
steelbaseprice = 1.7
steelprice = steelbaseprice
steelstock = 0
brickbaseprice = 1.3
brickprice = brickbaseprice
brickstock = 0
glassbaseprice = 2
glassprice = glassbaseprice
glassstock = 0
job1 = {"wood":0, "glass":0, "brick":0,"steel":0,  "money":0}
job2 = {"wood":0, "glass":0, "brick":0,"steel":0,  "money":0}
job3 = {"wood":0, "glass":0, "brick":0,"steel":0,  "money":0}
for x in range(1,12000000000):
    money -= (x*diff)
    if money <= 0:
        os.system("cls")
        print("You Ran Out Of Money!  You Lost :(")
        exit()
    if woodprice > woodbaseprice:
        woodprice -= (random.randint(1,60)/100)
    elif woodprice < woodbaseprice:
        woodprice += (random.randint(1,60)/100)
    if steelprice > steelbaseprice:
        steelprice -= (random.randint(1,60)/100)
    elif steelprice < steelbaseprice:
        steelprice += (random.randint(1,60)/100)
    if brickprice > brickbaseprice:
        brickprice -= (random.randint(1,60)/100)
    elif brickprice < brickbaseprice:
        brickprice += (random.randint(1,60)/100)
    if glassprice > glassbaseprice:
        glassprice -= (random.randint(1,60)/100)
    elif glassprice < glassbaseprice:
        glassprice += (random.randint(1,60)/100)
    job1['wood'] = (random.randint(0,8)*5)
    job1['brick'] = (random.randint(0,8)*5)
    job1['steel'] = (random.randint(0,8)*5)
    job1['glass'] = (random.randint(0,8)*5)
    job1['money'] = (random.randint(10,40)*5)
    job2['wood'] = (random.randint(0,8)*5)
    job2['brick'] = (random.randint(0,8)*5)
    job2['steel'] = (random.randint(0,8)*5)
    job2['glass'] = (random.randint(0,8)*5)
    job2['money'] = (random.randint(10,40)*5)
    job3['wood'] = (random.randint(0,8)*5)
    job3['brick'] = (random.randint(0,8)*5)
    job3['steel'] = (random.randint(0,8)*5)
    job3['glass'] = (random.randint(0,8)*5)
    job3['money'] = (random.randint(10,40)*5)
    if woodprice > woodbaseprice:
        woodprice -= (random.randint(1,50)/100)
    elif woodprice < woodbaseprice:
        woodprice += (random.randint(1,50)/100)
    elif steelprice > steelbaseprice:
        steelprice -= (random.randint(1,50)/100)
    elif steelprice < steelbaseprice:
        steelprice += (random.randint(1,50)/100)
    elif glassprice < glassbaseprice:
        glassprice += (random.randint(1,50)/100)
    elif glassprice > glassbaseprice:
        glassprice -= (random.randint(1,50)/100)
    elif brickprice > brickbaseprice:
        brickprice -= (random.randint(1,50)/100)
    elif brickprice < brickbaseprice:
        brickprice += (random.randint(1,50)/100)
    for c in range(1,21):
        abs(glassprice)
        abs(steelprice)
        abs(brickprice)
        abs(woodprice)
        steelprice = round(steelprice,2)
        woodprice = round(woodprice,2)
        glassprice = round(glassprice,2)
        brickprice = round(brickprice,2)
        money = round(money,2)
        os.system('cls')
        print(f"Day {x}")
        print(f"Money: {money}$")
        print(f"Wood: {woodstock}")
        print(f"Glass: {glassstock}")
        print(f"Brick: {brickstock}")
        print(f"Steel: {steelstock}")
        print(f"Price Of Wood: {woodprice}$")
        print(f"Price Of Glass: {glassprice}$")
        print(f"Price Of Brick: {brickprice}$")
        print(f"Price Of Steel: {steelprice}$")
        print(f"Job1: {job1}")
        print(f"Job2: {job2}")
        print(f"Job3: {job3}")
        imput = input("")
        split = imput.split(" ")
        if "buy" in split and "wood" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if money >= (woodprice*int(split[y-1])):
                        last['wood'] = woodprice
                        money -= woodprice * int(split[y-1])
                        woodstock += int(split[y-1])
                        woodprice += ((random.randint(1,10)/100) * (int(split[y-1])/2))
                        woodprice = round(woodprice,2)
        elif "sell" in split and "wood" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if woodstock >= int(split[y-1]):
                        money += last['wood'] * int(split[y-1])
                        woodstock -= int(split[y-1])
                        woodprice -= ((random.randint(0,10)/100) * (int(split[y-1])/2))
                        woodprice = round(woodprice,2)
        elif "buy" in split and "glass" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if money >= (glassprice*int(split[y-1])):
                        last['glass'] = glassprice
                        money -= glassprice * int(split[y-1])
                        glassstock += int(split[y-1])
                        glassprice += ((random.randint(1,10)/100) * (int(split[y-1])/2))
                        glassprice = round(glassprice,2)
        elif "sell" in split and "glass" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if glassstock >= int(split[y-1]):
                        money += last['glass'] * int(split[y-1])
                        glassstock -= int(split[y-1])
                        glassprice -= ((random.randint(0,10)/100) * (int(split[y-1])/2))
                        glassprice = round(glassprice,2)
        elif "buy" in split and "brick" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if money >= (brickprice*int(split[y-1])):
                        last['brick'] = brickprice
                        money -= brickprice * int(split[y-1])
                        brickstock += int(split[y-1])
                        brickprice += ((random.randint(1,10)/100) * (int(split[y-1])/2))
                        brickprice = round(brickprice,2)
        elif "sell" in split and "brick" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if brickstock >= int(split[y-1]):
                        money += last['brick'] * int(split[y-1])
                        brickstock -= int(split[y-1])
                        brickprice -= ((random.randint(0,10)/100) * (int(split[y-1])/2))
                        brickprice = round(brickprice,2)
        elif "buy" in split and "steel" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if money >= (steelprice*int(split[y-1])):
                        last['steel'] = steelprice
                        money -= steelprice * int(split[y-1])
                        steelstock += int(split[y-1])
                        steelprice += ((random.randint(1,10)/100) * (int(split[y-1])/2))
                        steelprice = round(steelprice,2)
        elif "sell" in split and "steel" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if steelstock >= int(split[y-1]):
                        money += last['steel'] * int(split[y-1])
                        steelstock -= int(split[y-1])
                        steelprice -= ((random.randint(0,10)/100) * (int(split[y-1])/2))
                        steelprice = round(steelprice,2)
            
        elif "fulfill" in split and "job1" in split:
            if woodstock >= job1['wood'] and brickstock >= job1['brick'] and glassstock >= job1['glass'] and steelstock >= job1['steel']:
                money += job1['money']
                woodstock -= job1['wood']
                brickstock -= job1['brick']
                glassstock -= job1['glass']
                steelstock -= job1['steel']
                job1['wood'] = 0
                job1['brick'] = 0
                job1['glass'] = 0
                job1['steel'] = 0
                job1['money'] = 0
        elif "fulfill" in split and "job2" in split:
            if woodstock >= job2['wood'] and brickstock >= job2['brick'] and glassstock >= job2['glass'] and steelstock >= job2['steel']:
                money += job2['money']
                woodstock -= job2['wood']
                brickstock -= job2['brick']
                glassstock -= job2['glass']
                steelstock -= job2['steel']
                job2['wood'] = 0
                job2['brick'] = 0
                job2['glass'] = 0
                job2['steel'] = 0
                job2['money'] = 0
        elif "fulfill" in split and "job3" in split:
            if woodstock >= job3['wood'] and brickstock >= job3['brick'] and glassstock >= job3['glass'] and steelstock >= job3['steel']:
                money += job3['money']
                woodstock -= job3['wood']
                brickstock -= job3['brick']
                glassstock -= job3['glass']
                steelstock -= job3['steel']
                job3['wood'] = 0
                job3['brick'] = 0
                job3['glass'] = 0
                job3['steel'] = 0
                job3['money'] = 0
        elif "wait" in split or "w" in split:
            print("Waiting")
            time.sleep(2)
            break