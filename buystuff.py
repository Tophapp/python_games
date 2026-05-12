import random
#Unfinished
names = ["Monicle","Top Hat","Necklace",""]
class player():
    def __init__(self):
        self.money = 0
        self.items = {}
        self.score = 0
        self.index = 0
numofplayers = int(input("Enter The Number Of Players(Max Is 4 And Least Is 2): "))
class card():
    def __init__(self):
        self.worth = 0
        self.name = ""
        self.score = 0
cards = []
def makecard():
    currcard = card()
    cards.append(currcard)
    currcard.score = random.randint(1,10)*10
    currcard.name = random.choice(names)
                                  


players = [1]
def playermake():
    currplayer = player()
    players.append(currplayer)
    currplayer.index = len(players)-1

for g in range(1,numofplayers +1):

    playermake()

