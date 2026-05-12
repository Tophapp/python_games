import random
print()
crimepos = ["Theft", "Assult","Breaking And Entering","Tresspassing","Barging Into Someones Home And Eating Their Pie"]
namepos = ["Bob Smukleham","Briant Tukerman","Mint Quartler","Emanuel Forge","Pieton Gorfin","Freddie Consatamion","Tommy Kholb","Jarv Mintorlm","Victor Fold","Cherry Qwaltz","Nixton Dorm","Kole Trenton"]
crime = random.choice(crimepos)
name = random.choice(namepos)
print("Guilty or Not Guilty")
print(f"Name: {name}")
print(f"The Crime Is: {crime}")
print()
total = 0
evfor = []
evaga = []
forev = ["1 Witness","2 Witnesses","Fingerprints At Crime Scene","Recently Bought Tool/weapon Used In Crime"]
agaev = ["At Home Says Neighbor","No witnesses","Lived Far Away","Car Still In Driveway"]
for x in range(1, random.randint(1, 3) + 1):
    evfor.append(random.choice(forev))
for z in range(1, random.randint(1, 3)+1):
    evaga.append(random.choice(agaev))
print(f"Evedence For the Crime")
print(evfor)
print()
print(f"Evedence Against the Crime")
print(evaga)
if "1 Witness" in evfor:
    total += 2
if "2 Witnesses" in evfor:
    total += 4
if "Recently Bought Tool/weapon Used In Crime" in evfor:
    total += 5
if "Fingerprints At Crime Scene" in evfor:
    total += 7
if "At Home Says Neighbor" in evaga:
    total -= 3
if "No witnesses" in evaga:
    total -= 3
if "Car Still In Driveway" in evaga:
    total -= 4
if "Lived Far Away" in evaga:
    total -= 6
if total < 0:
    desaws = "Not Guilty"
else:
    desaws = "Guilty"
print()
userinput = input("Your Desision: ")
if userinput == "Guilty" and desaws == "Guilty" or userinput == "Not Guilty" and desaws == "Not Guilty":
    print("Correct! :)")
elif userinput == "Guilty" and desaws == "Not Guilty" or userinput == "Not Guilty" and desaws == "Guilty":
    print("Incorrect :(")