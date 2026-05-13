import random
print("Find The 4 Four Letter Words")
choices = ["worn","make","grow","gold","form","main","view","flat","copy","acid","wild","tone","glue","hard","beam","what","cake","tool","mall","deal","soil""dice",
"play","food","done","flip","salt","best","back","even","knit","file","cube","fine","shut","knot","crab"]
list = []
for x in range(1, 5):
    word1 = ""
    word = random.choice(choices)
    choices.remove(word)
    wordsplit = [*word]
    randomint = random.randint(1, 2)
    rint = random.randint(1, 7)
    if randomint == 1:
        for y in range(1, len(wordsplit)+1):
            word1 += wordsplit[len(wordsplit) - y]
    else:
        word1 = word
    list.append(word)
    if rint == 1:
        print(f"dfd{word1}soq")
    elif rint == 2:
        print(f"foqnch{word1}")
    elif rint == 3:
        print(f"g{word1}dfnya")
    elif rint == 4:
        print(f"mtei{word1}br")
    elif rint == 5:
        print(f"fdkm{word}xa")
    elif rint == 6:
        print(f"zlr{word}rmv")
    elif rint == 7:
        print(f"citp{word}bz")
    elif rint == 8:
        print(f"i{word}dcywq")
    elif rint == 9:
        print(f"gxqf{word}wa")
    elif rint == 10:
        print(f"zenk{word}wg")
for n in range(1, 10):
    imput = input("1 Word: ")
    if imput in list:
        print("Found One! :)")
        list.remove(imput)
    elif n == 9:
        print("You Failed :(")
    else:
        print("Not A Word! :(")
    if len(list) == 0:
        print("You Won!!!!")

