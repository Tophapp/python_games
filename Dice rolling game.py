import random

dicerolltotal = random.randint(2, 12)
print(f"The First Roll Was {dicerolltotal}")
decide = input("Do You Think The Next Roll Will Be Higher, Lower, Or The Same: ")
dicerolltotal2 = random.randint(2, 12)
print(f"The Next Roll Was {dicerolltotal2}")
if dicerolltotal2 > dicerolltotal and decide == "higher":
    print("Correct!")
    exit()
elif dicerolltotal2 < dicerolltotal and decide == "lower":
    print("Correct!")
elif dicerolltotal2 == dicerolltotal and decide == "same":
    print("Correct!")
else:
    print("Incorrect :(")

