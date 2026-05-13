import os
import random
import time
def myMax(list1):
 
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = float('-inf')
# Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in list1:
        if x > max:
            max = x
 
    # after complete traversing the list
    # return the "max" value
    return max
money = 0
start = input("Enter Any Character To Start: ")
cakepos = ["eggs","flour","molasses","butter","sugar","vanilla","milk"]
burgerpos = ["cheese","bun","pickles","ketchup","mustard","onions"]
icepos = ["vanilla","strawberry","mango","chocolate","cherry","butter-pecan","rocky-road"]
saladpos = ["lettuce","spinach","croutons","ranch-dressing","hard-boiled-egg","chicken"]
typepos = ["cake","burger","ice-cream","salad"]
timed = time.time()
score = []
for x in range(1,10000000000000000):
    ingredent = {"Costomer Type":random.randint(1,3),"Type":None,"Ingredent 1":None,"Ingredent 2":None}
    ingredent["Type"] = random.choice(typepos)
    if typepos[0] == ingredent["Type"]:
        ingredent["Ingredent 1"] = random.choice(cakepos)
        ingredent["Ingredent 2"] = random.choice(cakepos)
    elif typepos[1] == ingredent["Type"]:
        ingredent["Ingredent 1"] = random.choice(burgerpos)
        ingredent["Ingredent 2"] = random.choice(burgerpos)
    elif typepos[2] == ingredent["Type"]:
        ingredent["Ingredent 1"] = random.choice(icepos)
        ingredent["Ingredent 2"] = random.choice(icepos)
    elif typepos[3] == ingredent["Type"]:
        ingredent["Ingredent 1"] = random.choice(saladpos)
        ingredent["Ingredent 2"] = random.choice(saladpos)
    for f in range(1,5):
        time.sleep(1)
        os.system("cls")
        print(f"Score: {money}$")
        print(ingredent)
        print(f)
    aws = [ingredent["Type"],ingredent["Ingredent 1"],ingredent["Ingredent 2"]]
    os.system("cls")
    print(f"Score: {money}")
    print(ingredent)
    first = time.time()
    imput = input("")
    next = time.time()
    imput = imput.split(" ")
    elap = next - first
    if elap > ingredent["Costomer Type"]*7 or aws != imput:
        print("Order Not Fulfilled In Time/Order Misspelled")
        time.sleep(1)
    else:
        print("Order Fulfilled!")
        time.sleep(1)
        money += 20
        money += (random.randint(10,700)/100)
        money = round(money,2)
    os.system("cls")
    timed2 = time.time()
    
        
    if timed2 - timed >= 120:
        print(f"Times Up!  Current Score {money}$")
        score.append(money)
        highscore = myMax(score)
        print(f"Your Highscore Is {highscore}$")
        
        imwot = input("Continue? ")
        if imwot == "yes" or imwot == "Yes":
            continue
        else:
            exit()


