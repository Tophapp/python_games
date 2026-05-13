import random
import time
import os
import math
import matplotlib.pyplot as plt
 

class company():
    def __init__(self):
        self.index = 0
        self.dayjoined = 0
        self.listpos = 0
        self.symbol = "UNK"
        self.name = "Unknown"
        self.price = random.randint(1200,5000)
        self.price /= 100
        self.product = "Unknown"
        self.stock = 0
        self.prices =[0]
        self.dire = 0
        self.priceslist = []
        self.lastprice = 0
        self.upordown = ""
        self.lastbought = 0
        self.upordown2 = ""
    
    def market(self):
        self.price = round(self.price,2)
        arrow = "="
        if self.upordown == "Up":
            arrow = "^"
        if self.upordown == "Down":
            arrow = "v"
        print(f"{self.name}({self.symbol}) Is Priced At {self.price}$ {arrow}.  You Can Buy {math.floor(money/self.price)} Shares.  It Is A {self.product} Company And You Have {self.stock} Shares Worth {round(self.price * self.stock,2)}$ ({self.symbol})")
    
    def buy(self,amount):
        self.stock += amount
        self.lastbought = self.price
        return money - round(amount * self.price,2)
    def sell(self,amount):
        self.stock -= amount
        return money + round(amount * self.price,2)

    def update(self):
        self.upordown = "The Same"
        self.upordown2 = "The Same"
        event = random.randint(1,80)
        if event == 10 and eventson == True:
            self.price -= (random.randint(400,1300)/100)
            events.append(f"{self.name}({self.symbol})'s Workers Demand Better Pay")
        elif event == 11 and eventson == True:
            self.price += (random.randint(400,1300)/100)
            events.append(f"{self.name}({self.symbol})'s Advertising Campaign Working Wonders As Customers Flood Stores")
        
        self.dire = random.randint(1,2)
        self.prices.append(self.dire)
        self.priceslist.append(self.price)
        total = random.randint(1,10)
        if len(self.prices) > 3:
            if total == 1:
                self.dire = self.prices[len(self.prices)-4]
            elif total > 6:
                self.dire = self.prices[len(self.prices)-3]
        
        if self.dire == 1:
            self.price += random.randint(0,200) / 100
        elif self.dire == 2:
            self.price -= random.randint(0,200) / 100
        self.price = round(self.price,2)

        if self.price < 4 and random.randint(1,20) == 10 and len(companies) > 3 and eventson == True:
            events.append(f"{self.name} Has Filed For Bankruptcy.  You Had {self.stock} Stocks Of It Worth {round(self.price * self.stock,2)}$ At The Time.  So Very Sad For You")
            listcompanies.append((self.name,self.symbol,self.product))
            companies.remove(self)
        if self.price > self.lastprice:
            self.upordown = "Up"
        elif self.price < self.lastprice:
            self.upordown = "Down"
        if self.price > self.lastbought:
            self.upordown2 = "Up"
        elif self.price < self.lastbought:
            self.upordown2 = "Down"

        if self.stock > 0:
            print(f"You Have {self.stock} Shares Of {self.name}({self.symbol}) Worth {round(self.price * self.stock,2)}$  The Price Is {self.upordown2} {str(round(abs(self.price - self.lastbought),2))}$ From When Last Bought.  It Is A {self.product} Company")
        self.price = abs(self.price)
        if self.price > 65:
            self.price -= (random.randint(700,1700)/100)
            events.append(f"{self.name}({self.symbol})'s Customers Moving To Local Buisnesses")
os.system("cls")
print("Initalizing.")
time.sleep(1)
os.system("cls")
print("Initalizing..")
time.sleep(1)
os.system("cls")
print("Initalizing...")
time.sleep(1)
os.system("cls")
print("Initalizing.")
time.sleep(1)
os.system("cls")
print("Initalizing..")
time.sleep(1)
os.system("cls")
print("Initalizing...")
time.sleep(1.5)
os.system("cls")
gamerunning = True
while gamerunning:
    code = ""
    act = ["Sleeping","Eating","Gaming","Pooping","Waiting","Sitting","Watching TV","Playing On Your Phone","Working","Mowing","Barbecueing","Celebrateing","Partying","Sleeping","Sleeping","Playing With Your Pets","Crafting","Sculpting","Reading","writeing","Bakeing","Cooking","Painting","Scrolling Down Reddit","Walking","Drawing","Legoing","Exerciseing","Working Out","Shopping","Driveing","Petting Your Dog","Petting Your Cat","Sleeping","Swinging","Jumping In A Pool","Going Outside","Knitting"]
    poscompanies = [("Apple", "APL","Tech"),("Microsoft", "MIC","Tech"),("Mc Donalds", "MCD","Food"),("Arby's", "ARB","Food"),
                    ("Amazon","AMZ","Goods"),("Ebay","EBY","Goods"),("Walmart","WAL","Goods"),("Costco","CST","Goods"),("Home Depot","HDP","Home Improvement"),
                    ("Fourteen Foot Busses Incorperated","FFB","Transportation"),("SpaceX","SPX","Tech"),("Electronic Arts","EA","Tech"),("Airplay","AIR","Food"),
                    ("ToysRUs","TRU","Goods"),("Walgreens","WGN","Goods"),("Target","TAR","Home Improvement"),("Verizon","VER","Services"),("Wells Fargo","WFG","Services"),
                    ("Tuft Love","TFT","Tech"),("State Farm","SFM","Services"),("Bayerische Motoren Werke","BMW","Transportation"),("Lamborghini","LAM","Transportation"),
                    ("Ein's Squrrel Emporium","ESE","Goods"),("Twitter","TWR","Services"),("The Container Store","TCS","Goods"),("Lays","LAY","Food"),("Kellogs","KEL","Food"),
                    ("PepsiCo","PEP","Food"),("Pizza Hut","PZH","Food"),("United Parcel Service","UPS","Transportation"),("Hy-Vee","HIV","Food"),("Rubiks","RBK","Goods"),
                    ("Menards","MEN","Home Improvement"),("Netflix","NET","Entertainment"),("Pie","PI","Pi"),("General Motors","GMR","Transportation"),("Clorox","COX","Home Improvement"),
                    ("Starbucks","STB","Food"),("Dollar Tree","DRT","Goods"),("Satern Construction Company","SCC","Home Improvement"),("Google","GOG","Tech"),
                    ("Ford","FRD","Transportation"),("Marvel","MAR","Entertainment"),("DC Comics","DC","Entertainment"),("Taco Bell","TCO","Food"),("AMC Theaters","AMC","Entertainment"),
                    ("Flix Brewhouse","FLX","Entertainment"),("Youtube","YOU","Entertainment"),("Caseys","CAY","Food"),("Domino's","DOM","Food"),("Kohl's","KOL","Goods"),
                    ("Roblox","RBX","Entertainment"),("American Airlines","ALN","Transportation"),("Old Navy","OLD","Goods"),("Best Buy","BST","Goods"),("Couch.inc","SLP","Services"),
                    ("Dollar General","DRG","Goods"),("Future Furniture","FF","Home Improvement"),("Coca Cola","COC","Food"),("Snapchat","SNP","Services"),("Tesla","TES","Transportation"),
                    ("Intel","INT","Tech"),("The Cheesecake Factory","TCF","Food"),("Petco","PET","Goods"),("Krispy Kreme","KRS","Food"),("Universal Studios","UVS","Transportation"),
                    ("Game Stop","GSP","Tech"),("Pinterest","PIN","Services"),("Sony","SON","Tech"),("Ace Hardwere","ACE","Home Improvement")]
    listcompanies = poscompanies.copy()
    companies = []
    banish = []
    events = []
    day = 0
    start = True
    days = True
    money = 600
    bills = True
    searched = 0
    dayslist = [0]
    maxdays = -1
    loandue = -1
    loancost = -1
    borrowdue = -1
    borrowcost = -1
    borrowtype = ""
    eventson = True
    numofcomp = random.randint(15,len(poscompanies)-30)
    def createcompany():
        currcomp = company()
        currcomp.listpos = len(companies)
        currcomp.dayjoined = day
        companies.append(currcomp)
        compused = listcompanies.pop(random.randint(0,len(listcompanies)-1))
        currcomp.index = poscompanies.index(compused)
        currcomp.name = compused[0]
        currcomp.symbol = compused[1]
        currcomp.product = compused[2]

    def createsavecomp(ind,stock,price,lastprice):
        currcomp = company()
        currcomp.listpos = len(companies)
        currcomp.dayjoined = day
        companies.append(currcomp)
        currcomp.index = int(ind)
        currcomp.stock = int(stock)
        currcomp.price = float(price)
        currcomp.lastprice = float(lastprice)
        currcomp.name = poscompanies[int(ind)][0]
        currcomp.symbol = poscompanies[int(ind)][1]
        currcomp.product = poscompanies[int(ind)][2]
    print("Tophapp Games Presents...")
    time.sleep(0.2)
    print("Stocks With Socks V3.2!  The Game About Getting 17 Quintillion Dollars, In Less Than 10 Minutes!")
    time.sleep(0.1)
    print("A Remake Of A Remake Of A Remake Of A Game By Rand Tophapp")
    print("----------------------------------------------------------")
    print()
    bob = True
    while bob:
        indexhitlist = []
        save = input("Enter Your Save Code Or Type 'New' To Start A New Game: ")
        if save.lower() == "new":
            saves = "new"
            break
        else:
            try:
                save = save.split("#")
                day = int(save.pop(0))
                money = float(save.pop(0))
                maxdays = int(save.pop(0))
                eventson = bool(save.pop(0))
                bills = bool(save.pop(0))
                loandue = int(save.pop(0))
                loancost =float(save.pop(0))
                borrowdue = int(save.pop(0))
                borrowcost = int(save.pop(0))
                borrowtype = str(save.pop(0))
                for x in range(1,int((len(save)/4 )+1)):
                    createsavecomp(save[x*4-4],save[x*4-3],save[x*4-2],save[x*4-1])
                    indexhitlist.append(int(save[x*4-4]))
                
                listcompany = listcompanies.copy()
                for h in indexhitlist:
                    listcompanies.remove(listcompany[h])
                saves = "old"
                break
            except:
                print("That Is Not A Valid Save Code")
    if saves == "new":
        print(f"Change Your Settings Here To Modify The Game, Type 'Done' To Skip, Type The Part In Quotation Marks And Its New Value To Change It, T Means A Boolean Value, N Means A Intager, And Max Is The Max Amount The Value Can Be, The Settings Avalible Are Starting 'Money' ({str(money)}) N, 'Events' ({str(eventson)}) T, Max 'Days' ({str(maxdays)}) N, 'Bills' ({str(bills)}) B , And Number Of 'Companies'({str(numofcomp)}) N Max: {len(poscompanies)}")
        while True:
            set = input("")
            set = set.lower()
            set = set.split(" ")
            if set[0] == "money" and len(set) > 1:
                if set[1].isnumeric():
                    money = int(set[1])
                    print(f"Successfully Changed Money To {set[1]}")
                else:
                    print("That Is Not A Value Accepted By This Field")
            elif set[0] == "days" and len(set) > 1:
                if set[1].isnumeric():
                    maxdays = int(set[1])
                    print(f"Successfully Changed Days To {set[1]}")
                else:
                    print("That Is Not A Value Accepted By This Field")
            elif set[0] == "companies" and len(set) > 1:
                if set[1].isnumeric():
                    numofcomp = int(set[1])
                    print(f"Successfully Changed Companies To {set[1]}")
                else:
                    print("That Is Not A Value Accepted By This Field")
            elif set[0] == "bills" and len(set) > 1:
                if set[1] == "true":
                    numofcomp = True
                    print(f"Successfully Changed Bills To {set[1]}")
                if set[1] == "true":
                    numofcomp = False
                    print(f"Successfully Changed Bills To {set[1]}")
                else:
                    print("That Is Not A Value Accepted By This Field")
            elif set[0] == "done":
                break
            elif set[0] == "events" and len(set) > 1:
                if set[1] == "true":
                    eventson = True
                    print(f"Successfully Changed Events To {set[1]}")
                if set[1] == "true":
                    eventson = False
                    print(f"Successfully Changed Events To {set[1]}")
                else:
                    print("That Is Not A Value Accepted By This Field")
            else:
                print("That Is Not A Setting-Value pair")

        for x in range(1,numofcomp+1):
            createcompany()

    while days:
        os.system("cls")
        events = []
        print("Day " + str(day+1))
        print("? For Controls")
        if borrowdue >= 0:
            p=0
            for le in companies:
                if le.name != borrowtype:
                    p+=1
            if p >= len(companies):
                print("Lend Ended Due To Bankruptcy")
                borrowcost = -1
                borrowdue = -1
                borrowtype = ""
        if loandue >= 0:
            loandue -=1
            loancost *= 1.08
        if borrowdue >= 0:
            borrowdue -=1
            borrowcost *= 1.08
        if loandue > 0 and round(money-loancost,2) < 0:
                print(f"You have a loan out for {str(loancost)}, It Is Due In {str(loandue)} Days And You Need ${str(round(abs(money-loancost),2))} To Pay It Back")
        elif loandue > 0 and round(money-loancost,2) >= 0:
                print(f"You have a loan out for {str(loancost)}, It Is Due In {str(loandue)} Days And You Currently Can Pay It Off With ${str(round(abs(money-loancost),2))} Remaining")
        elif loandue == 0:
                print(f"Your Loan Has Been Automatically Paid.")
                money -= loancost
        if borrowdue > 0:
                print(f"You have a lend out for {str(borrowcost)} stocks of {borrowtype}, It Is Due In {str(borrowdue)} Days")
        elif borrowdue == 0:
                print(f"Your Lend Has Been Automatically Paid.")
                for le in companies:
                    if le.name == borrowtype:
                        if le.stock >= borrowcost:
                            le.stock -= borrowcost
                            borrowcost = -1
                            borrowdue = -1
                            borrowtype=""
                        else:
                            borrowcost -= le.stock
                            le.stock = 0
                            money -= borrowcost*le.price
                            borrowcost = -1
                            borrowdue = -1
                            borrowtype=""
        day += 1
        if day % 5 == 0:
            for g in companies:
                if g.stock > 0:
                    money += g.stock* (g.price / 20)
        if day % 10 == 0 and bills == True:
            money -= day *7
            print(f"Bills Are Due And Have Been Automatically Paid For ${day*7}")
        elif bills == True:
            print(f"Bills Are Due In {10- day % 10} Days For ${math.ceil(day/10)*70}")

        dayslist.append(day)
        for h in companies:
            h.update()
        money = round(money,2)
        
        if random.randint(1,10) == 1 and eventson == True:
            if len(listcompanies) > 0:
                createcompany()
                events.append(f"{companies[len(companies)-1].name}({companies[len(companies)-1].symbol}) Has Joined The Market At A Price Of {companies[len(companies)-1].price}$ Per Share")
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Massive Gold Shortage")
            for x in companies:
                if x.product == "Tech":
                    x.price -= random.randint(100,300) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("LOCUSTS")
            for x in companies:
                if x.product == "Food":
                    x.price -= random.randint(700,1200) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("New VR Headsets Are Released")
            for x in companies:
                if x.product == "Tech":
                    x.price += random.randint(300,500) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Train Derailment")
            for x in companies:
                if x.product == "Transportation":
                    x.price -= random.randint(300,500) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("World Newspapers Aprove Of New Movies")
            for x in companies:
                if x.product == "Entertainment":
                    x.price += random.randint(200,300) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Lumber Prices Skyrocket After Group Of Civillians Take To The Streets In Protest Against Climate Change")
            for x in companies:
                if x.product == "Home Improvement":
                    x.price -= random.randint(300,500) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Sheep Go On Strike")
            for x in companies:
                if x.product == "Goods":
                    x.price -= random.randint(100,500) /100
                if x.product == "Home Improvement":
                    x.price -= random.randint(100,500) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Large Auto-Repair Shop To Close Its Doors")
            for x in companies:
                if x.product == "Transportation":
                    x.price -= random.randint(200,400) /100
                if x.product == "Goods":
                    x.price -= random.randint(200,400) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Group Of Hakers Infiltrarte Popular Social Media Apps")
            for x in companies:
                if x.product == "Services":
                    x.price -= random.randint(300,500) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Large Nickel Vein Found In Canada")
            for x in companies:
                if x.product == "Tech":
                    x.price += random.randint(300,500) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("New Fruit Has Customers Baffled At Great Taste")
            for x in companies:
                if x.product == "Food":
                    x.price += random.randint(100,300) /100
        if random.randint(1,60) == 1 and eventson == True:
            events.append("Intrest Is Slowing Down!  Companies Are Not")
            for x in companies:
                x.price += random.randint(300,600) /100
        if money <= 0:
            print("Your Wallet Seems To Have Gone Bankrupt")
            break
        while start:
            money = round(money,2)
            code = str(day) + "#" + str(money)+ "#" + str(maxdays) + "#" + str(eventson) + "#" + str(bills) + "#" + str(loandue) + "#" + str(loancost) + "#" + str(borrowdue) + "#" + str(borrowcost) + "#" + str(borrowtype)
            for x in companies:
                code += "#" + str(x.index)
                code += "#" + str(x.stock)
                code += "#" + str(x.price)
                code += "#" + str(x.lastprice)
            print("Money: " + str(money) + "$")
            wante = input("")
            wante = wante.lower()
            want = wante.split(" ")
            searcher = False
            for v in companies:
                if v.symbol.lower() == want[0] or v.name.lower() == want[0] or v.product.lower() == want[0]:
                    v.market()
                    searcher = True
            if want[0] == "m" or want[0] == "market":
                print("Market:")
                for x in companies:
                    x.market()
            elif want[0] == "f" or want[0] == "fund":
                b2 = 0
                for x in companies:
                    cost = round(x.price * int(want[1]),2)
                    if cost < money:
                        money = x.buy(int(want[1]))
                        b2+=1
            elif want[0] == "l" or want[0] == "loan":
                if len(want) > 1:
                    if want[1].isnumeric():
                        if float(want[1]) <= 500000:
                            loancost = float(want[1])
                            loandue = 15
                            money += float(want[1])
                            print(f"We Successfully Loaned You ${str(float(want[1]))}")
                        else:
                            print("The Number You Entered Was Too High")
                    else:
                        print("Thats Not A Number, Please Learn What A Number Is")
                else:
                    if loandue > 0 and round(money-loancost,2) > 0:
                        print(f"You have a loan out for {str(loancost)}, It Is Due In {str(loandue)} Days And You Need ${str(round(money-loancost,2))} To Pay It Back")
                    elif loandue > 0 and round(money-loancost,2) <= 0:
                        print(f"You have a loan out for {str(loancost)}, It Is Due In {str(loandue)} Days And You Currently Can Pay It Off With ${str(round(abs(money-loancost),2))} Remaining")
            elif want[0] == "b" or want[0] == "borrow" or want[0] == "s" or want[0] == "short":
                k = 0
                if len(want) > 2:
                    if want[2].isnumeric():
                        if float( want[2]) == round(float(want[2])):
                            if int(want[2]) <money:
                                for b in companies:
                                    if b.symbol.lower() == want[1] or b.name.lower() == want[1]:
                                        borrowcost = int(want[2])
                                        borrowdue = round(15 - round(int(want[2])/12000,2))
                                        b.stock += int(want[2])
                                        print(f"We Successfully Lended You {str(int(want[2]))} Stocks In {b.name}")
                                        borrowtype = b.name
                                        money -= int(want[2])
                                    else:
                                        k+=1
                                if k >= len(companies):
                                    print("That Company Does Not Exist")
                            else:
                                print("The Number You Entered Was Too High For Your Current Balance")
                        else:
                            print("Thats Not An Integer, Please Learn What An Integer Is")
                    else:
                        print("Thats Not A Number, Please Learn What A Number Is")

            elif want[0] == "pay" and len(want) > 1:
                if want[1] == "loan" or want[1] == "lo":
                    if loandue >0:
                        money-=loancost
                        print("Thank You For Paying Your Loan")
                        loandue = -1
                        loancost = 0
                    else:
                        print("You Dont Have A Loan Out...  I Mean I Would Be Happy To Take Your Money, But I Am Sadly Not Allowed To Do That")
                if want[1] == "lend" or want[1] == "le" or want[1] == "short" or want[1] == "s":
                    if borrowdue >0:
                        for le in companies:
                            if le.name == borrowtype:
                                if le.stock >= borrowcost:
                                    le.stock -= borrowcost
                                    borrowcost = -1
                                    borrowdue = -1
                                    borrowtype=""
                                else:
                                    borrowcost -= le.stock
                                    le.stock = 0
                                    money -= borrowcost*le.price
                                    borrowcost = -1
                                    borrowdue = -1
                                    borrowtype=""
                        print("Thank You For Returning Your Stocks")
                    else:
                        print("You Dont Have A Lend Out...  I Mean I Would Be Happy To Take Your Money, But I Am Sadly Not Allowed To Do That")
            elif want[0] == "wait" or want[0] == "w":
                print(random.choice(act))
                time.sleep(2)
                break
            elif want[0] == "?":
                print("Buy: Buy a stock.  Syntax: Buy [Company] [Amount/Max]")
                print("Sell: Sell a stock you have.  Syntax: Sell [Company] [Amount/Max]  or  Sell All")
                print("(N)ewspaper: Dispay all events that day.  Syntax: Newspaper")
                print("(P)lot: Plot a Stock's Growth And Falls.  Syntax: Plot [Company] ")
                print("End: Ends the game  Syntax: End")
                print("Reset: Ends the run.  Syntax: Reset")
                print("Code: Displays the save code for that save.  Syntax: Code")
                print("(W)ait: Skip to next day.  Syntax: Wait")
                print("(B)orrow: Borrow stocks in a company.  Syntax: Borrow [Company] [Amount]")
                print("(M)arket: List the prices and other information about each of the companies.  Syntax: Market")
                print("Pay: Pay loans and lends.  Syntax: Pay [Type]")
                print("(F)und: Spread your money equally between stocks.  Syntax: Fund [Amount]")
                print("(L)oan: Loan money from us with an intrest rate of 8% per day.  Maxes out at $500,000.  Syntax: Loan [Amount]")
            elif want[0] == "buy" and len(want) >= 3:
                cost = 0
                searched = 0
                if want[2].isnumeric():
                    for v in companies:
                        if v.symbol.lower() == want[1] or v.name.lower() == want[1]:
                            cost = round(v.price * int(want[2]),2)
                            if cost > money:
                                print("YOU My Sir, Are Broke.  (You Cannot Aford The Cost Of The Stocks Your Trying To Buy)")
                            else:
                                v.lastprice = v.price
                                money = v.buy(int(want[2]))
                                print(f"{want[2]} Shares Of {v.name} ({v.symbol}) Have Been Bought Successfully For {cost}$")
                        else:
                            searched += 1
                    if searched >= len(companies):
                        print(f"HEY!  {want[1]} Is Not A Company!  I Can't Generate Companies Folks!")
                elif want[2] == "max":
                        for v in companies:
                            if v.name.lower() == want[1] or v.symbol.lower() == want[1]:
                                cost = round(v.price * math.floor(money/v.price),2)
                                print(f"{math.floor(money/v.price)} Shares Of {v.name} ({v.symbol}) Have Been Bought Successfully For {cost}$")
                                v.lastprice = v.price
                                money = v.buy(math.floor(money/v.price))
                            else:
                                searched += 1
                        if searched >= len(companies):
                            print(f"HEY!  {want[1]} Is Not A Company!  Thats A Dumb Name For A Company Anyway!")
                else:
                        print(f"Just To Let You Know, {want[2]} Is NOT A Valid Number.")
                
            elif want[0] == "sell" and len(want) >= 3:
                cost = 0
                searched = 0
                if want[2].isnumeric():
                    for v in companies:
                        if v.name.lower() == want[1] or v.symbol.lower() == want[1]:
                            cost = round(v.price * int(want[2]),2)
                            if v.stock < int(want[2]):
                                print(f"YOU My Sir, Do Not In Fact Own {round((int(str(want[2])[:4]) / 100),2)}% Of {v.name}")
                            else:
                                money = v.sell(int(want[2]))
                                print(f"{want[2]} Shares Of {v.name} ({v.symbol}) Have Been Sold Successfully For {cost}$")
                        else:
                            searched += 1
                    if searched >= len(companies):
                        print(f"HEY!  {want[1]} Is Not A Company!  I Can't Generate Money Folks!")
        
                elif want[2] == "max":
                        for v in companies:
                            if v.name.lower() == want[1] or v.symbol.lower() == want[1]:
                                cost = round(v.price * v.stock,2)
                                print(f"{v.stock} Shares Of {v.name} ({v.symbol}) Have Been Sold Successfully For {cost}$")
                                money = v.sell(v.stock)
                            else:
                                searched += 1
                        if searched >= len(companies):
                            print(f"HEY!  {want[1]} Is Not A Company!  I Cant Go Off Nothing!")
                else:
                    print(f"Just To Let You Know, {want[2]} Is NOT A Valid Number.")
            elif want[0] == "sell" and want[1] == "all":
                    for v in companies:
                        if v.stock > 0:
                            cost = round(v.price * v.stock,2)
                            print(f"{v.stock} Shares Of {v.name} ({v.symbol}) Have Been Sold Successfully For {cost}$")
                            money = v.sell(v.stock)
            elif want[0] == "plot" or want[0] == "p" :
                if len(want) >= 2:
                    for v in companies:
                        if v.name.lower() == want[1] or v.symbol.lower() == want[1]:
                            daylistedit = []
                            for x in range(1,len(v.priceslist) + 1):
                                daylistedit.append(dayslist[len(dayslist)-x])
                            print("And Its Somewhat Accurate!   Will Not Update Naturally And You MUST Delete It To Type Again")
                            plt.plot(daylistedit, v.priceslist)
                            # naming the x axis
                            plt.xlabel('Days')
                            # naming the y axis
                            plt.ylabel('Cost')
                            # giving a title to my graph
                            plt.title('StockViewer V.73000000  Viewing: ' + v.name) 
                            # function to show the plot
                            plt.show()
            elif want[0] == "newspaper" or want[0] == "n" or want[0] == "paper" or want[0] == "np" or want[0] == "news":
                print("---------------------- Newspaper -----------------------")
                if len(events) > 0:
                    for l in events:
                        print(l)
                else:
                    print()
                    print()
                    print("Nothing For Today")
                    print()
                    print()
                print("--------------------------------------------------------")
            elif want[0] == "skipofcool" and len(want) >= 2:
                for g in range(1,int(want[1])+1):
                    day += 1
                    dayslist.append(day)
                    for h in companies:
                        h.update()
                    money = round(money,2)
                dayslist.pop(len(dayslist)-1)
            elif want[0] == "end":
                gamerunning = False
            elif want[0] == "reset":
                bob = False
            elif want[0] == "code":
                print(code)
            elif searcher != True:
                if wante in banish:
                    print("That Command Has Been Banished To The Shadow Realm.")
                else:
                    banish.append(wante)
                    print(f'Whatever This "{wante}" Is, Its Not A Command And Therefore Does Not Belong Here.  We Have Banished It.')
            money = round(money,2)
            if day == maxdays:
                gamerunning = False
print(f"Farewell, I Hope You Enjoyed.")
print()
print(f"Totally Copywrited: Tophapp Productions, 2025")
print(f"Made By Rand Tophapp")
