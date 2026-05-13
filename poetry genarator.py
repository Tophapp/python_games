import random
print("How Many Poems Would You Like To Generate?")
imput = int(input(""))
poem = ""
nouns = ["apple","dog","song","memory","topic","sword","friendship","initiative","owner","silence"]
verbs = ["jumps","eats","returns","tightens","guides","condemns","defies","shapes","constructs","drives"]
adjectives = ["fuzzy","gullable","undesirable","unwieldy","profuse","steadfast","unkempt","ragged","ubiquitous","trite","droll","ablaze","ajoining","makeshift","accidental","fumbling","feeble","murky","coherent"]
for x in range(1, imput + 1):
    poem = ""
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    poem += noun
    poem += " "
    poem += verb
    poem += " "
    poem += adjective
    print(poem)

