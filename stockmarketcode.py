import random
import os
import time
pl = [None,None,None,None,None,None,None,None]
componies = ["target","airplay","google","lays","costco","apple","amazon","walmart"]
diff = int(input("Select The Difficulty Level From 1 To 10,  0 Disables The Slow Money Loss: "))
name = input("Enter Your Name: ")
rt,rai,rg,rl,rc,ra,ram,rw = random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)
'''
class company:
    currentprice = 0
    name = "None"
    ownedshares = 0


    def __init__(self, name, startprice):
        self.name = name
        self.currentprice = startprice
        self.ownedshares = 0

    def AdjustPrice(self):
        decide = random.randint(1,2)
        newincrease = random.randint(1, 50)
        if decide == 1:
            newprice += (newincrease/100)
        else:
            newprice -= (newincrease/100)
        newprice = abs(newprice)
        self.currentprice = round(newprice,2)



def AdjustPrice(currentprice):
    decide = random.randint(1,2)
    newincrease = random.randint(1, 50)
    if decide == 1:
        newprice += (newincrease/100)
    else:
        newprice -= (newincrease/100)
    newprice = abs(newprice)
    currentprice = round(newprice,2)

    return currentprice



TargetCopmany = company("Target",5)
TargetCopmany.AdjustPrice()


GoogleCompany = company("Google", 10)


Companies = [TargetCopmany, GoogleCompany]


for SingleCompany in Companies:
    SingleCompany.AdjustPrice()
    print(f"You Have {SingleCompany.ownedshares} Shares Of {SingleCompany.name} ")
    print(f"Target: You Can Buy {round((money / SingleCompany.currentprice))-1} Shares. The Price Of A Share Is {SingleCompany.currentprice}$")

    if (SingleCompany.name == playertypedname):
        SingleCompany.owned += playersharecount

        Foundit = True

'''
def adjustprice(newprice):
    decide = random.randint(1,2)
    newincrease = random.randint(1, 50)
    if decide == 1:
        newprice += (newincrease/100)
    else:
        newprice -= (newincrease/100)
    newprice = abs(newprice)
    targetprice = round(newprice,2)

    return targetprice
targetprice1 = random.randint(1, 200)/ 100
targetprice = 0
targetstock = 0
airplayprice1 = random.randint(1, 200)/ 100
airplayprice = 0
airplaystock = 0
googleprice1 = random.randint(1, 200)/ 100
googleprice = 0
googlestock = 0
laysprice1 = random.randint(1, 200)/ 100
laysprice = 0
laysstock = 0
costcoprice1 = random.randint(1, 200)/ 100
costcoprice = 0
costcostock = 0
appleprice1 = random.randint(1, 200)/ 100
appleprice = 0
applestock = 0
amprice1 = random.randint(1, 200)/ 100
amprice = 0
amstock = 0
wallprice1 = random.randint(1, 200)/ 100
wallprice = 0
wallstock = 0
if diff > 0:
    money = 100
else:
    money = 50
for x in range(1, 1200000000):
    money -= (x*diff)
    if money <= 0:
        os.system("cls")
        print("You Ran Out Of Money!  You Lost :(")
        exit()
    print(f"Day {x}")
    targetprice1 = adjustprice(targetprice1)

    targetprice = round(targetprice1,2)
    googleprice1 = adjustprice(googleprice1)
    googleprice = round(googleprice1,2)
    airplayprice1 = adjustprice(airplayprice1)
    airplayprice = round(targetprice1,2)
    laysprice1 = adjustprice(laysprice1)
    laysprice = round(laysprice1,2)
    costcoprice1 = adjustprice(costcoprice1)
    costcoprice = round(costcoprice1,2)
    appleprice1 = adjustprice(appleprice1)
    appleprice = round(appleprice1,2)
    amprice1 = adjustprice(amprice1)
    amprice = round(amprice1,2)
    wallprice1 = adjustprice(wallprice1)
    wallprice = round(wallprice1,2)
    for t in range(1, 5):
        money = round(money,2)
        targetcost = targetprice * rt
        targetcost = round(targetcost,2)
        airplaycost = airplayprice * rai
        airplaycost = round(airplaycost,2)
        googlecost = googleprice * rg
        googlecost = round(googlecost,2)
        layscost = laysprice * rl
        layscost = round(layscost,2)
        costcocost = costcoprice * rc
        costcocost = round(costcocost,2)
        applecost = appleprice * ra
        applecost = round(applecost,2)
        amcost = amprice * ram
        amcost = round(amcost,2)
        wallcost = wallprice * rw
        wallcost = round(wallcost,2)
        prices = [targetcost,airplaycost,googlecost,layscost,costcocost,applecost,amcost,wallcost]
        targetcost += 0.01
        airplaycost += 0.01
        googlecost += 0.01
        layscost += 0.01
        costcocost += 0.01
        applecost += 0.01
        amcost += 0.01
        wallcost += 0.01
        wallcost = round(wallcost,2)
        amcost = round(amcost,2)
        applecost = round(applecost,2)
        costcocost = round(costcocost,2)
        layscost = round(layscost,2)
        googlecost = round(googlecost,2)
        airplaycost = round(airplaycost,2)
        targetcost = round(targetcost,2)
        os.system('cls')
        print(f"Day {x}  Name: {name}")
        print(f"You Have {money}$")
        print(f"You Have {targetstock} Shares Of Target")
        print(f"You Have {airplaystock} Shares Of Airplay")
        print(f"You Have {googlestock} Shares Of Google")
        print(f"You Have {laysstock} Shares Of Lays")
        print(f"You Have {costcostock} Shares Of Costco")
        print(f"You Have {applestock} Shares Of Apple")
        print(f"You Have {amstock} Shares Of Amazon")
        print(f"You Have {wallstock} Shares Of Walmart")
        print(f"Target: You Can Buy {round(((money - (x*diff)) / targetcost))-1} Shares. Price: {targetcost}$.       Price When Last Bought: {pl[0]}")
        print(f"Airplay: You Can Buy {round(((money - (x*diff)) / airplaycost))-1} Shares. Price: {airplaycost}$.      Price When Last Bought: {pl[1]}")
        print(f"Google: You Can Buy {round(((money - (x*diff)) / googlecost))-1} Shares. Price: {googlecost}$.      Price When Last Bought: {pl[2]}")
        print(f"Lays: You Can Buy {round(((money - (x*diff)) / layscost))-1} Shares. Price: {layscost}$.       Price When Last Bought: {pl[3]}")
        print(f"Costco: You Can Buy {round(((money - (x*diff)) / costcocost))-1} Shares. Price: {costcocost}$.       Price When Last Bought: {pl[4]}")
        print(f"Apple: You Can Buy {round(((money - (x*diff)) / applecost))-1} Shares. Price: {applecost}$.        Price When Last Bought: {pl[5]}")
        print(f"Amazon: You Can Buy {round(((money - (x*diff)) / amcost))-1} Shares. Price: {amcost}$.        Price When Last Bought: {pl[6]}")
        print(f"Walmart: You Can Buy {round(((money - (x*diff)) / wallcost))-1} Shares.  Price: {wallcost}$.        Price When Last Bought: {pl[7]}")
        imput = input()
        split = imput.split(" ")
        if "buy" in split and "target" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * targetcost) <= money:
                        money -= (int(split[y-1]) * targetcost)
                        targetstock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "target" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if targetstock >= int(split[y-1]):
                        money += (int(split[y-1]) * targetcost)
                        targetstock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)
        elif "buy" in split and "airplay" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * airplaycost) <= money:
                        money -= (int(split[y-1]) * airplaycost)
                        airplaystock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "airplay" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if airplaystock >= int(split[y-1]):
                        money += (int(split[y-1]) * airplaycost)
                        airplaystock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)

        elif "buy" in split and "google" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * googlecost) <= money:
                        money -= (int(split[y-1]) * googlecost)
                        googlestock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "google" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if googlestock >= int(split[y-1]):
                        money += (int(split[y-1]) * googlecost)
                        googlestock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)
        elif "buy" in split and "lays" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * layscost) <= money:
                        money -= (int(split[y-1]) * layscost)
                        laysstock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "lays" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if laysstock >= int(split[y-1]):
                        money += (int(split[y-1]) * layscost)
                        laysstock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)
        elif "buy" in split and "costco" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * costcocost) <= money:
                        money -= (int(split[y-1]) * costcocost)
                        costcostock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "costco" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if costcostock >= int(split[y-1]):
                        money += (int(split[y-1]) * costcocost)
                        costcostock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)
        elif "buy" in split and "apple" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * applecost) <= money:
                        money -= (int(split[y-1]) * applecost)
                        applestock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "apple" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if applestock >= int(split[y-1]):
                        money += (int(split[y-1]) * applecost)
                        applestock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)
        elif "buy" in split and "amazon" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * amcost) <= money:
                        money -= (int(split[y-1]) * amcost)
                        amstock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "amazon" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if amstock >= int(split[y-1]):
                        money += (int(split[y-1]) * amcost)
                        amstock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)
        elif "buy" in split and "walmart" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * wallcost) <= money:
                        money -= (int(split[y-1]) * wallcost)
                        wallstock += int(split[y-1])
                    else:
                        print("You Dont Have Enough Money")
                        time.sleep(1)
        elif "sell" in split and "walmart" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if wallstock >= int(split[y-1]):
                        money += (int(split[y-1]) * wallcost)
                        wallstock -= int(split[y-1])
                    else:
                        print("You Dont Have Enough Shares To Sell That Much")
                        time.sleep(1)
        elif "wait" in split or "w" in split:
            print("Waiting")
            time.sleep(2)
            break
        else:
            print("Thats Not A Company")
            time.sleep(1)
        if "buy" in split:
            for v in range(1,len(componies)+1):
                if componies[v-1] in split:
                    pl[v-1] = prices[v-1]


