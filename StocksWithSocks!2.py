import random
import time
import os
import math
nor = "normal"
spe = "speedrun"
userin = ""
over = False
comach = []
loan = 0
loanamount = 0
act = ["Sleeping","Eating","Gaming","Pooping","Waiting","Sitting","Watching TV","Playing On Your Phone","Working","Mowing","Barbecueing","Celebrateing","Partying","Sleeping","Sleeping","Playing With Your Pets","Crafting","Sculpting","Reading","writeing","Bakeing","Cooking","Painting","Scrolling Down Reddit","Walking","Drawing","Legoing","Exerciseing","Working Out","Shopping","Driveing","Petting Your Dog","Petting Your Cat","Sleeping","Swinging","Jumping In A Pool","Going Outside","Knitting"]
totalmoney = 0
print("Welcolm To Stocks With Socks!2 The Weird And Unrealistic Game About The Stock Market And Getting 17 Qintillion Dollars In 10 Minutes.  Plz Awnser The Questions Below To Start")
print("A Remake Of A Remake By Rand Tophapp")
print("----------------------------------------------------------")
totachspeed = {"Nice":"Not Done",
               "Alright":"Not Done",
               "Good":"Not Done",
               "Better":"Not Done",
               "Best":"Not Done",
               "Super Ultra Mega Ultimate Power Magic Stonks":"Not Done",
               "How?":"Not Done",}
totachnorm = {"Starter":"Not Done",
              "Well Off":"Not Done",
              "Alright!":"Not Done",
              "Stonks":"Not Done",
              "Richest In The World(By A Long Shot)":"Not Done",
              "17 Qintillion!!!":"Not Done",
              "Stocks Galore":"Not Done",
              "All The Stocks":"Not Done",
              "This Becomes Small":"Not Done",
              "17 Quintillion!!! Again?":"Not Done",
              "Pi":"Not Done",
              "Oh COME ON!":"Not Done",
              "Wow, You Actually Did It!":"Not Done"

              }
day = 0
slow = 0
intrest = 0.04
money = 400
mode = input("Enter Mode normal Or speedrun: ")
if mode == "n":
    mode = "normal"
if mode == "s":
    mode = "speedrun"
if mode == "speedrun":
    maxday = 40
if mode == "normal":
    slow = float(input("Enter The Multiplier For The Slow Money Loss.  0 Disables It: "))
event = input("Do You Want Events on Or off: ")
componies = []
posnames = {"HWI":"Hello World Inc",
        "TPB":"Tasty Pie Bakery",
        "GTD":"Garbage Truck Disposal",# Disposes Of Garbage Trucks 
        "CLE":"Chesters Lobtar Emporeium",#Lobtar
        "APL":"Apple",
        "TAR":"Target",
        "AIR":"Airplay",
        "WAL":"Walmart",
        "MAR": "Marvel",
        "UNS": "Universal Studios",
        "KRS": "Krispy Kreme",
        "TCO": "Taco Bell",
        "PET": "Petco",
        "MIC": "Microsoft",
        "SON": "Sony",
        "PIZ": "Pizza Ranch",# (:
        "WEL": "Wells Fargo",
        "HYV": "Hy-Vee",
        "DIS": "Disney",
        "BTX":"Betrix Shoes",
        "ESM":"Eins Squrrel Museum",
        "RBK":"Rubiks",
        "FFB":"Fourteen Foot Busses Incorperated",
        "FRD":"Ford",
        "FMI":"Feed Me Incorperated",
        "MFD":"Meh Foods",# Its Okay Food
        "UPS":"Ups",
        "AMZ":"Amazon",
        "SPX":"SpaceX",
        "TCS":"The Container Store",# Apropreatly Named
        "FBK":"Facebook",
        "TWR":"Twitter",
        "COS":"Costco",#Bulk
        "LAY":"Lays",
        "GOG":"Google",
        "SCC":"Satern Construction Compony",
        "HDT":"Home Depot",
        "TCF":"The Cheesecake Factory",# Good Cheesecake
        "PEP":"PepsiCo",
        "INT":"Intel",
        "TES":"Tesla",
        "PIE":"Pie",# Is Tasty
        "NKE":"Nike",
        "COC":"Coca-Cola",
        "DRG":"Dollar General",
        "NFX":"Netflix",# Today I Did Poorly
        "STR":"Starbucks",
        "DRT":"Dollar Tree",
        "MCD":"McDonald's",
        "KEL":"Kellogg",
        "EBY":"eBay",# Home Of ALL The Broken XBox Contollers Selling For 999.99$
        "PZH":"Pizza Hut",
        "GNM":"General Motors",
        "VER":"Verizon",
        "SNP":"Snapchat",
        "KOL":"Kohl's",
        "TRU":"Toys “R” Us",# Bring It Back!
        "GST":"Game Stop",
        "CAM":"Campbell Soup",
        "HER":"Hershey",
        "JMJ":"Jimmy John's",
        "COX":"Clorox",
        "STF":"State Farm",
        "JIM":"Jimmy Dean",# Good Breakfast Food
        "PIN":"Pinterest"
        
        
        }
class comp():
    def __init__(self):
        self.name = "Unknown"
        self.symbol = "UNK"
        self.price = random.randint(526,2486)/100
        self.adrate = 0
        self.stock = 0
        self.addorsub = 0
        self.max = 0
        self.lastprice = 0
        self.upordown = ""
        self.preprice = self.price
        self.upper = ""
        self.isevent = False
    def ad(self):
        if self.isevent != True:
            self.adrate = random.randint(148,279)/100
            self.addorsub = random.randint(1,2)
            if self.addorsub == 1:
                self.price += self.adrate
            else:
                self.price -= self.adrate
        self.price = round(self.price,2)
        self.price = abs(self.price)
        if self.price > self.preprice:
            self.upordown = "^"
        elif self.price < self.preprice:
            self.upordown = "v"
        self.preprice = self.price
        if  self.price < self.lastprice :
            self.upper = (f" The Price Is Down {abs(round(self.price - self.lastprice ,2))}$ From When Last Bought")
        elif self.price > self.lastprice :
            self.upper = (f" The Price Is Up {abs(round(self.price - self.lastprice ,2))}$ From When Last Bought")
        self.isevent = False
    def do(self,money,totalmoney,split):

        
        if self.price == 0:
            self.price += 1
        if self.price >= 55:
            self.price = 15
        self.max = math.floor(money / self.price) -1
        if "buy" in split and self.symbol in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if (int(split[y-1]) * self.price) <= money:
                        money -= (int(split[y-1]) * self.price)
                        totalmoney += (int(split[y-1]) * self.price)
                        self.stock += int(split[y-1])
                        self.lastprice = self.price
                        print(f"You Succeded In Buying {int(split[y-1])} Shares Of ({self.symbol}) {self.name}")
                    else:
                        print("You Dont Have Enough Money To Buy That Many Shares")
                        time.sleep(1)
        elif "sell" in split and self.symbol in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    if self.stock >= int(split[y-1]):
                        money += (int(split[y-1]) * self.price)
                        self.stock -= int(split[y-1])
                        print(f"You Succeded In Selling {int(split[y-1])} Shares Of ({self.symbol}) {self.name}")
                    else:
                        print("You Dont Have Enough Shares To Sell That Many")
                        time.sleep(1)
        if "buy" in split and self.symbol in split and "max" in split:
            print(f"You Succeded In Buying {self.max} Shares Of ({self.symbol}) {self.name}")
            money -= (self.max * self.price)
            totalmoney += (self.max * self.price)
            self.stock += self.max
            self.lastprice = self.price
            
        if "sell" in split and self.symbol in split and "max" in split:
            money += (self.stock * self.price)
            print(f"You Succeded In Selling {self.stock} Shares Of ({self.symbol}) {self.name}")
            self.stock -= self.stock
            
        elif "market" in split or "m" in split:
            print(f"({self.symbol}) {self.name}  You Have {self.stock} Stocks  Current Price: {self.price}${self.upordown}  Price When Last Bought: {self.lastprice}$  Max Shares You Can Buy: {self.max}  {self.symbol}")
        money = round(money,2)
        totalmoney = round(totalmoney,2)
        
        return money,totalmoney
    

number = 0



numofcomp = int(input(f"Enter The Starting Number Of Componies You Want In Your Game (Max Is {len(posnames)}): "))


def makecomp():
    
    val = list(posnames.keys())
    
    val_list = list(posnames.values())
    compname = random.choice(val_list)
    
    
    pos = val_list.index(compname)
    compsymbol = val[pos]
    componie = comp()
    componie.name = compname
    componie.symbol = compsymbol
    componies.append(componie)
    posnames.pop(compsymbol)
    
for g in range(1,numofcomp +1):
    makecomp()
slow = abs(slow)
run = True
start = time.time()
while run:
    



    loan -=1 

    if mode == "speedrun":
        if day == maxday:
            run = False
            break
    money -= slow * day
    day += 1
    if money <= 0:
        run = False
        break


            
    os.system("cls")

    if mode == "normal":
        print("Controls: wait Or w To End The Day, buy (Company Symbol) (Number) To Buy Shares, Same With Selling Shares Except With sell Instead, q To Quit,  market Or m To See The Current Prices And Stocks,  And loan Followed By A Number To Take Out A Loan Due In 15 Days At An Intrest Of 0.125% (Max Money That Can Be Borrowed At A Time Is 900,000$), You Can Pay The Loan Early By Typeing pay loan")
    if mode == "speedrun":
        print("Controls: wait Or w To End The Day, buy (Company Symbol) (Number) To Buy Shares, Same With Selling Shares Except With sell Instead, q To Quit, And market Or m To See The Current Prices And Stocks")
    print(f"Day {day}")
    money = round(money, 2)
    
    if loan > 0:
        loanamount += (loanamount * intrest)
        loanamount = abs(loanamount)
        loanamount = round(loanamount, 2)
        amo = loanamount - money
        if amo <= 0:
            amo = 0
        print(f"Loan Due In {loan} Days For {loanamount}$ Amount Needed {amo}$")
    if loan == 0:
        print("Loan Due Today")
    if loan == 0 and loanamount > 0:
        money -= loanamount
        loanamount = 0
    if event == "on":
        for h in componies:
            if h.price <= 4:
                bank = random.randint(1,5)
                if bank == 5:

                    print(f"{h.name} ({h.symbol}) Went Bankrupt!")
                    componies.pop(componies.index(h))
    if event == "on":
        for j in range(1,len(componies)-1):
            if random.randint(1,10) == 1:
                rand = random.randint(1,33)
                if rand == 9 and len(componies) > 1:
                    compbank = random.choice(componies)
                    
                    if mode == nor and compbank.stock >= 10000 and not "Oh COME ON!"in comach:
                        comach.append("Oh COME ON!")
                        totachnorm["Oh COME ON!"] = "Done"
                        print("You Got The Oh COME ON! Achevment!")
                    print(f"{compbank.name} ({compbank.symbol}) Went Bankrupt!")
                    componies.pop(componies.index(compbank))
                elif rand == 17 and len(componies) < len(posnames):
                    makecomp()
                    compbank = componies[len(componies)-1]
                    print(f"{compbank.name} ({compbank.symbol}) Has Become A Companey!")
                    compbank.price = round(compbank.price,2)
                    compbank.price = abs(compbank.price)
                else:
                    if random.randint(1,2) == 1:
                        compbank = random.choice(componies)
                        print(f"{compbank.name} ({compbank.symbol}) Is Doing Great!  Stock Prices Have Risen Significently!")
                        compbank.price += random.randint(746, 1592)/100
                        compbank.price = round(compbank.price,2)
                        compbank.price = abs(compbank.price)
                    else:
                        compbank = random.choice(componies)
                        print(f"{compbank.name} ({compbank.symbol}) Is Doing Horrible!  Stock Prices Have Fallen Significently!")
                        compbank.price -= random.randint(746, 1592)/100
                        compbank.price = round(compbank.price,2)
                        compbank.price = abs(compbank.price)
                compbank.isevent = True
    if day != 1:
        for c in componies:
            c.ad()
    for g in componies:
        if g.stock > 0:
            print(f"You Have {g.stock} Stocks Of ({g.symbol}) {g.name} Eqivelent To {round(g.stock * g.price)}${g.upper}")
    while True:

        if slow > 0 and (slow * day) > money:
            print(f"You Dont Have Enough Money To Account For The Slow Money Loss.  You Have To Earn {((slow * day)+ 1) - money}$ To Keep Playing Next Turn")
        ten = time.time() - start
        number =0
        over = False
        if mode == nor and money >= 1000 and not "Starter"in comach:
            comach.append("Starter")
            totachnorm["Starter"] = "Done"
            print("You Got The Starter Achevment!")
        if mode == nor and money >= 100000 and not "Well Off"in comach:
            comach.append("Well Off")
            totachnorm["Well Off"] = "Done"
            print("You Got The Well Off Achevment!")
        if mode == nor and money >= 10000000 and not "Alright!"in comach:
            comach.append("Alright!")
            totachnorm["Alright!"] = "Done"
            print("You Got The Alright! Achevment!")
        if mode == nor and money >= 10000000000 and not "Stonks"in comach:
            comach.append("Stonks")
            totachnorm["Stonks"] = "Done"
            print("You Got The Stonks Achevment!")
        if mode == nor and money >= 1_000_000_000_000 and not "Richest In The World(By A Long Shot)"in comach:
            comach.append("Richest In The World(By A Long Shot)")
            totachnorm["Richest In The World(By A Long Shot)"] = "Done"
            print("You Got The Richest In The World(By A Long Shot) Achevment!")
        if mode == nor and money >= 17_000000000000000000 and not "17 Qintillion!!!"in comach:
            comach.append("17 Qintillion!!!")
            totachnorm["17 Qintillion!!!"] = "Done"
            print("You Got The 17 Qintillion!!! Achevment!")
        if mode == nor and money >= 17_000000000000000000 and not "Wow, You Actually Did It!"in comach and ten < 600:
            comach.append("Wow, You Actually Did It!")
            totachnorm["Wow, You Actually Did It!"] = "Done"
            print("You Got The Wow, You Actually Did It! Achevment!")
        for g in componies:
            if g.stock >= 1000:
            
                over = True
        if mode == nor and over == True and not "Stocks Galore"in comach:
            comach.append("Stocks Galore")
            totachnorm["Stocks Galore"] = "Done"
            print("You Got The Stocks Galore Achevment!")
        for g in componies:
            if g.stock >= 1000:
                number+=1
        if number == len(componies):

            over = True
        else:
            over = False
        if mode == nor and over == True and not "All The Stocks"in comach:
            comach.append("All The Stocks")
            totachnorm["All The Stocks"] = "Done"
            print("You Got The All The Stocks Achevment!")
        over = False
        for g in componies:
            if g.stock >= 1000000000:
                over = True
        
        if mode == nor and over == True and not "This Becomes Small"in comach:
            comach.append("This Becomes Small")
            totachnorm["This Becomes Small"] = "Done"
            print("You Got The This Becomes Small Achevment!")
        over = False
        for g in componies:
            if g.stock >= 17_000000000000000000:
                over = True
        if mode == nor and over == True and not "17 Quintillion!!! Again?"in comach:
            comach.append("17 Quintillion!!! Again?")
            totachnorm["17 Quintillion!!! Again?"] = "Done"
            print("You Got The 17 Quintillion!!! Again? Achevment!")
        over = False
        if mode == spe and money >= 1000 and not "Nice"in comach:
            comach.append("Nice")
            totachspeed["Nice"] = "Done"
            print("You Got The Nice Achevment!")
        if mode == spe and money >= 10000 and not "Alright"in comach:
            comach.append("Alright")
            totachspeed["Alright"] = "Done"
            print("You Got The Alright Achevment!")
        if mode == spe and money >= 100000 and not "Good"in comach:
            comach.append("Good")
            totachspeed["Good"] = "Done"
            print("You Got The Good Achevment!")
        if mode == spe and money >= 1000000 and not "Better"in comach:
            comach.append("Better")
            totachspeed["Better"] = "Done"
            print("You Got The Better Achevment!")
        if mode == spe and money >= 10000000 and not "Best"in comach:
            comach.append("Best")
            totachspeed["Best"] = "Done"
            print("You Got The Best Achevment!")
        if mode == spe and money >= 100000000 and not "Super Ultra Mega Ultimate Power Magic Stonks"in comach:
            comach.append("Super Ultra Mega Ultimate Power Magic Stonks")
            totachspeed["Super Ultra Mega Ultimate Power Magic Stonks"] = "Done"
            print("You Got The Super Ultra Mega Ultimate Power Magic Stonks Achevment!")
        if mode == spe and money >= 1000000000 and not "How?"in comach:
            comach.append("How?")
            totachspeed["How?"] = "Done"
            print("You Got The How? Achevment!")
        print(f"Money: {money}$")
        userin = input("")
        split = userin.split(" ")
        if mode == "normal":
            if "loan" in split and loan <= 0:
                for y in range(1, len(split) + 1):
                    if split[y-1].isnumeric():
                        if not int(split[y-1]) > 900_000:
                            loan = 15
                            money += int(split[y-1])
                            loanamount = int(split[y-1]) + (int(split[y-1]) * intrest)
                        else:
                            print("You Cant Take Out A Loan For That Much")
            if userin == "pay loan":
                money -= loanamount
                loanamount = 0
                loan = 0
        

            

        if userin == "wait" or userin == "w":
            print(random.choice(act))
            time.sleep(2)
            break
        if userin == "q":
            run = False
            break
        if money == 3.14:
            totachnorm["Pi"] = "Done"

        if money <= 0 and slow > 0:
            run = False
        if userin == "DoEvent":
            if random.randint(1,1) == 1:
                rand = random.randint(1,33)

                if rand == 17 and len(componies) < len(posnames):
                    makecomp()
                    compbank = componies[len(componies)-1]
                    print(f"{compbank.name} ({compbank.symbol}) Has Become A Companey!")
                    round(compbank.price,2)
                else:
                    if random.randint(1,2) == 1:
                        compbank = random.choice(componies)
                        print(f"{compbank.name} ({compbank.symbol}) Is Doing Great!  Stock Prices Have Risen Significently!")
                        compbank.price += random.randint(746, 1592)/100
                        round(compbank.price,2)
                    else:
                        compbank = random.choice(componies)
                        print(f"{compbank.name} ({compbank.symbol}) Is Doing Horrible!  Stock Prices Have Fallen Significently!")
                        compbank.price -= random.randint(746, 1592)/100
                        round(compbank.price,2)
        if "StocksInABox" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    for g in componies:
                        if g.symbol in split or "ALL" in split:
                            g.stock += int(split[y-1])
        if "GiveMeTheStonks" in split:
            for y in range(1, len(split) + 1):
                if split[y-1].isnumeric():
                    money += float(split[y-1])
        for d in componies:
            money,totalmoney = d.do(money,totalmoney,split)
        if money <= 0:
            run = False
            break

            


print("Thanks For Playing")
print(f"Current Money: {money}$  Total Money Spent: {totalmoney}")
print(f"Total Amount Of Time Waiting: {day * 2 -2} Seconds")
if mode == "normal" and slow != 0:
    print(f"Achevments: {totachnorm}")
if mode == "speedrun":
    print(f"Achevments: {totachspeed}")