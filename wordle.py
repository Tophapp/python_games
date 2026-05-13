import random
numofguess = int(input("Number of guesses: "))
words = [
"gold","main","view","flat","copy","acid","wild","tone","glue","hard","beam","what","cake","tool","mall","deal","soil""dice",
"play","food","done","flip","salt","best","back","even","knit","file","cube","fine","shut","knot","crab"]
word = random.choice(words)
word1 = [*word]
print("4 Letter Words Only")
print(f"Starting letter is {word1[0]}")
for m in range(1, numofguess +1):
    wordaws = input("")
    word1 = [*word]
    wordaws1 = [*wordaws]
    for g in range(1, len(wordaws1) + 1):
        if len(wordaws1) > 4:
            wordaws1.pop()
            print("4 LETTER WORD PLEASE!")
            break
        elif len(wordaws1) < 4:
            wordaws1.append("filler")
            wordaws1.append("filler")
            wordaws1.append("filler")
            wordaws1.append("filler")
    for x in range(1, len(word1) + 1):
        if word == wordaws and m == 1:
            print("YOU DID IT FIRST TRY!!!!!!!")
            exit()
        elif word == wordaws:
            print(f"yay you did it in {m} Tries")
            exit()
        elif wordaws1[x -1] in word1:
            print(word1[word1.index(wordaws1[x-1])])
print(f"You lost. The word was: {word}")
