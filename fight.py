import random
char1  = input("Enter First Opponent: ")
char1str = int(input("Enter Stregnth Stat: "))
char1int = int(input("Enter Intellagence Stat: "))
char1spe = int(input("Enter Speed Stat: "))
char2 = input("Enter Second Opponent: ")
char2str = int(input("Enter Stregnth Stat: "))
char2int = int(input("Enter Intellagence Stat: "))
char2spe = int(input("Enter Speed Stat: "))
char1hp = 1000
char2hp = 1000
for x in range(1, 700):
    randatt1 = random.randint(1, 10)
    if randatt1 == 1:
        print(f"{char1} Goes in for the attack and Punches {char2} in the face!")
        char2hp -= (char1str * 10)
        if char1int > 5 and char1spe > 5:
            print(f"Than {char1} Procceds to swiftly punch {char2} in the chest!")
            char2hp -= 100
    if randatt1 == 2:
        print(f"{char1} trips {char2} and procceds to kick him in the knees!")
        if char2spe > 6:
            print(f"But, {char2} Dodges and Then Punches {char1} in the face!")
            char1hp -= 70
        else:
            char2hp -= 50
    if randatt1 == 3:
        print(f"{char1} uppercuts {char2} and slams {char2} down useing their elbow")
        char2hp -= 110
    if randatt1 == 4:
        print(f"{char1} Punches {char2}")
        char2hp -= (char1str * 10)
        if char1int > 7 and char1str > 5:
            print(f"{char1} then jumps and attemps to slam down on {char2}")
            if char2spe > 8:
                print(f"But {char2} rolls away just in time")
                if char2int > 6:
                    print(f"{char2} then jumps and dodges the attack completely")
                else:
                    print(f"")