import random
import os
import time
for a in range(1,100):
    wordpos = ["quartz","chair","owner","arrow","holder","winter","pillow","scramble","dialogue","string","orange","beautiful","explode","chance","tough","music","benefit","mayor","relief","avenue","broken","relax","sitter","canine","pants","board","computer","westward","concentration"]
    word = random.choice(wordpos)
    word1 = [*word]
    scram = []
    printed = ""

    print("Unscramble The Word. You Get Seven Guesses")
    print(f"Starting Letter Of The Unscrambled Word Is {word1[0]}")
    for x in range(1, len(word1) + 1):
        scram.append((random.choice(word1)))
        word1.pop(word1.index(scram[x-1]))
    for y in scram:
        printed += y
    print(printed)
    for d in range(1, 8):
        awser = input("Unscrambled Word: ")
        if awser == word:
            print("Correct!")
            time.sleep(2)
            break
        elif d == 7:
            print(f"You Lost, The Word Was {word}")
            time.sleep(2)
            break
        else:
            print("Incorrect")
    os.system('cls')
    


