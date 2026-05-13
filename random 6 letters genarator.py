import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for c in range(1, 5):
    for x in range(1, 7):
        randomint = random.randint(1, 6)
        letter = random.choice(letters)
        sent = ""
        for s in range(1, 7):
            if s == randomint:
                sent += "{word}"
            letter = random.choice(letters)
            sent += letter
        print(sent)
