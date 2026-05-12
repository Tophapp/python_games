import random
dif = input("Difficulty Either Hard Medium Or Easy: ")
if dif == "easy":
    playerhp = 150
    enemyhp = 100
elif dif == "medium":
    playerhp = 100
    enemyhp = 100
elif dif == "hard":
    playerhp = 100
    enemyhp = 150
else:
    playerhp = 100
    enemyhp = 100
block = False
cooldownthr = 1
enemystun = 0
cooldownstu = 1

print("The Attacks Are: hammer, throw, stun, and slash")
print("You Can Also block And Only Take Half Of The Damage")
for x in range(1, 501):
    clock = False
    crit = random.randint(1, 2)
    enemydamage = random.randint(1, 4)
    halfdamage = 0
    cooldownstu -= 1
    enemystun -= 1
    cooldownthr -= 1
    block == False
    imput = input("Attack: ")
    prop = imput.split(' ')
    if enemydamage == 1:
        enhit = random.randint(10, 20)
    elif enemydamage == 2:
        enhit = random.randint(20, 30)
    elif enemydamage == 3:
        enhit = random.randint(30, 40)
    elif enemydamage == 4:
        enhit = random.randint(40, 50)
    if "slash" in prop:
        randomattack = random.randint(20, 30)
        enemyhp -= randomattack
        print(f"You Did {randomattack} Damage!  The Enemy Has {enemyhp} HP Left")
    elif "throw" in prop and cooldownthr <= 0:
        randomattack = random.randint(30, 50)
        enemyhp -= randomattack
        print(f"You Did {randomattack} Damage!  The Enemy Has {enemyhp} HP Left")
        cooldownthr = 2
    elif "hammer" in prop:
        if crit == 1:
            randomattack = random.randint(30, 50)
        else:
            randomattack = random.randint(0, 20)
        enemyhp -= randomattack
        print(f"You Did {randomattack} Damage!  The Enemy Has {enemyhp} HP Left")
    elif "block" in prop:
        clock = True
        halfdamage = round(enhit/2)
        playerhp -= halfdamage
        print(f"You Blocked The Enemy Attack But You Still Took Half The Damage. Your Health Is Now {playerhp}")
    elif "stun" in prop and cooldownstu <= 0:
        block = True
        enemystun = 2
        cooldownstu = 4
    else:
        print("Not An Action/Action Not Avalible Right Now")
        block = True
    if block == True:
        print("Enemy Attack Missed You/You Blocked Its Attack")
        block = False
    elif enemystun > 0:
        enemystun = 0
        print("Enemy Attack Missed You/You Blocked Its Attack") 
    elif clock == True:
        clock = False
    else:
        playerhp -= enhit
        print(f"You Were Hit For {enhit} Damage.  Your Health Is Now At {playerhp} HP")
    if playerhp <= 0:
        print("You Lost!")
        exit()
    elif enemyhp <= 0:
        print("You Win!!!")
        exit()
    

