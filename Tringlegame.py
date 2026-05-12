import math
import random
import os

#clear the screen
os.system("cls")

#player class
class Player():
    def __init__(self,health):
        self.health = health
        self.bet = 0
        self.roll = []
        self.total = 0
        self.hand = 0 #0 = highest total, 1 = three of a kind, 2 = two pair, 3 = straight, 4 = four of a kind
       
    def rolldice(self):
        self.bet = 0
        self.roll = []
        self.total = 0
        self.hand = 0
        #roll the dice and add the rolls up
        for die in range(4):
            self.roll.append(random.randrange(1,5))
            self.total += self.roll[die]
           
        #sort the list for easier hand selection
        self.roll.sort()
       
        #decide which hand you have
        if self.roll[0] == self.roll[1] and self.roll[1] == self.roll[2] and self.roll[2] == self.roll[3]:
            self.hand = 4
        elif self.roll[0] == self.roll[1] and self.roll[2] == self.roll[3]:
            self.hand = 2
        elif self.roll[0] == 1 and self.roll[1] ==2 and self.roll[2] == 3 and self.roll[3] == 4:
            self.hand = 3
        elif self.roll[0] == self.roll[1] and self.roll[1] == self.roll[2]:
            self.hand = 1
        elif self.roll[1] == self.roll[2] and self.roll[2] == self.roll[3]:
            self.hand = 1
        else:
            self.hand = 0
    
    def decidehand(self):
        self.roll.sort()
        if self.roll[0] == self.roll[1] and self.roll[1] == self.roll[2] and self.roll[2] == self.roll[3]:
            self.hand = 4
        elif self.roll[0] == self.roll[1] and self.roll[2] == self.roll[3]:
            self.hand = 2
        elif self.roll[0] == 1 and self.roll[1] ==2 and self.roll[2] == 3 and self.roll[3] == 4:
            self.hand = 3
        elif self.roll[0] == self.roll[1] and self.roll[1] == self.roll[2]:
            self.hand = 1
        elif self.roll[1] == self.roll[2] and self.roll[2] == self.roll[3]:
            self.hand = 1
        else:
            self.hand = 0
           
           
       
       
#define starting health and players and other vars
players = []
startinghp = int(input("Input starting points for both sides (Ten is reccomended): "))
boon = 0 #0 = none, 1 = fortune teller (see opponents hand), 2 = chancemaker (change one dice to a target number), 3 = assasian (make the enemy lose a point), 4 = artist (gain an extra reroll : passive), 5 = economist (add a 1 to a random dice less than four : passive), 6 = warrior (gain an extra point and the enemy loses a point : passive)
print("Select a boon:")
print("1) Nothing" )
print("2) The Fortune Teller (Active): Look at the opponents hand" )
print("3) The Chancemaker (Active): Change one of your dice to a target number" )
print("4) The Assasian (Active): Make the opponent lose 20% of their points" )
print("5) The Artist (Passive): Gain an extra reroll" )
print("6) The Economist (Passive): Change one random dice to the dice on its right" )
print('7) The Warrior (Passive): Start with 20% extra points')
print("8) The Joker (Passive): The minimum bet each round is randomized")
print("9) The Dancer (Passive): The maximum bet is raised from 40% to 50%")
boon = int(input(""))
if boon < 0:
    boon = 0
boonsleft = 1
player = Player(startinghp)
if boon == 9 or boon==42:
    maxbet = math.ceil(startinghp*0.5)
else:
    maxbet = math.ceil(startinghp*0.4)
players.append(player)
enemy = Player(startinghp)
players.append(enemy)
alive = True
winner = None
pot = 0
minbet = 1
rerolled = False
rounds = 0
enemyreroll = False
boonused = False
boonused2 = False
if boon == 7 or boon==42:
    player.health *= 1.2
    #enemy.health *= 0.8

#main loop
while alive:
    #reset vars
    pot = 0
    if boon == 8 or boon==42:
        minbet = random.randint(1,maxbet)
   
    #roll all players dice
    for p in players:
        p.rolldice()
     
    #print information  
    print()
    print(f"Your score:")
    print(player.health)
    print()
    print(f"Opponents score:")
    print(enemy.health)
    print()
    print("Your roll:")
    print(player.roll)
    print()
    
        #enemy logic for rerolling
    if enemy.hand < 1:
            enemy.rolldice()
    while enemy.hand < 1 and enemy.health <= maxbet and enemy.health > 1:
            enemy.rolldice()
            if enemyreroll == True:
                enemy.health -=1
            elif enemyreroll == False:
                enemyreroll = True
        
    enemyreroll = False

    if boon == 2:
            if boonsleft > 0:
                print(f"You have {boonsleft} uses of your chosen boon left.  You regain one use every 3 rounds.")
                print("Would you like to use your chosen boon?")
                boonused = input().lower()
                if boonused == "y" or boonused == "yes":
                    boonsleft -=1
                    if boon == 2:
                        print("The opponents roll:")
                        print(enemy.roll)
    if boon==42:

                print(f"You have {boonsleft} uses of the Fortune Teller boon left.  You regain one use every 3 rounds.")
                print("Would you like to use your chosen boon?")
                boonused = input().lower()
                if boonused == "y" or boonused == "yes":

                    if boon==42:
                        print("The opponents roll:")
                        print(enemy.roll)

    #rerolling logic
    if rerolled == True:
        if (boon == 5 or boon==42) and boonused2 == False:
            print("Would you like to reroll?")
            reroll = input().lower()
        else:
            print(f"Would you like to reroll?  WARNING: You will use up {round(startinghp/10)} points, to do so")
            reroll = input().lower()
    else:
        print("Would you like to reroll?")
        reroll = input().lower()
   
    if reroll == "y" or reroll == "yes":
        if rerolled == False:
            rerolled = True
            
        elif (boon == 5 or boon==42) and boonused2 == False:
            boonused2 = True
        else:
            player.health-=round(startinghp/10)
           
    else:

        #boons
        if boon == 3 or boon == 4 or boon==42:
            if boonsleft > 0:
                print(f"You have {boonsleft} uses of your chosen boon left.  You regain one use every 3 rounds.")
                print("Would you like to use your chosen boon?")
                boonused = input().lower()
                if boonused == "y" or boonused == "yes":
                    boonsleft -=1
                    if boon == 3 or boon==42:
                        index = int(input("Choose which dice you would like to change: "))-1
                        number = int(input("To what: "))
                        player.roll[index] = number
                        player.decidehand()
                        print("Your new hand")
                        print(player.roll)
                    if boon == 4 or boon==42:
                        enemy.health -= round(enemy.health*0.2)
                        print("Opponent's new score:")
                        print(enemy.health)
                        
        
        if boon == 6 or boon==42:

                index = random.randrange(1,5)-1
                if index == 3:
                    player.roll[index]=player.roll[0]
                else:
                    player.roll[index]=player.roll[index+1]
                player.decidehand()
                print("Your new hand after the boon")
                print(player.roll)
                    
        print(f"Enter amount to bet, minimum bet: {minbet},  maximum bet: {maxbet}")
       
        #amount currently being bet
        betamount = int(input(""))
        print()
       
        if betamount < minbet:
            betamount = minbet
        elif betamount > maxbet:
            betamount = maxbet
       
        minbet = betamount
       
        pot += betamount*2
           
        #determining who wins
        if enemy.hand > player.hand:
            print(f"You have lost to a hand of:")
            print(enemy.roll)
            player.health-=betamount
            enemy.health+=betamount
        elif enemy.hand < player.hand:
            print(f"You have won against a hand of:")
            print(enemy.roll)
            player.health+=betamount
            enemy.health-=betamount
        elif enemy.hand == player.hand:
            if enemy.total > player.total:
                print(f"You have lost to a hand of:")
                print(enemy.roll)
                player.health-=betamount
                enemy.health+=betamount
            elif enemy.total < player.total:
                print(f"You have won against a hand of:")
                print(enemy.roll)
                player.health+=betamount
                enemy.health-=betamount
            else:
                print(f"You have tied with the opponent")
               
        rerolled = False
        boonused = False
        boonused2 = False
        rounds +=1
        if rounds % 3 == 0:
            boonsleft += 1
       
        print()
        #loose conditions:
        if player.health <= 0:
            print("You have lost")
            print(f"It was round {rounds}")
            print(f"The opponent had {enemy.health} points")
            alive = False
            
        elif enemy.health <= 0:
            print("You have won")
            print(f"It was round {rounds}")
            print(f"You had {player.health} points")
            alive = False