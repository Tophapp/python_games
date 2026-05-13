import random
print("How Many Dog Breed Combo's Would You Like To Generate?")
imput = int(input(""))
for d in range(1, imput+1):
    part1 = ""
    part2 = ""
    dogbreed12 = ""
    dogbreed22= ""
    dogbreeds = ["Shih-tzu","Cor-gi","Bull-dog","Poo-odle","Chihu-ahua","Dachs-hund","Malt-ese","Poma-ranian","Hava-nese","Samo-yed","Dober-mann","Yor-kie"]
    dogbreed1 = random.choice(dogbreeds)
    dogbreed2 = random.choice(dogbreeds)
    dog1split = [*dogbreed1]
    dog2split = [*dogbreed2]
    split1 = dogbreed1.split("-")
    part1 = split1[0]
    split2 = dogbreed2.split("-")
    part2 = split2[1]
    part3 = part1 + "-" + part2
    parts = part1 + part2
    dog1split.remove("-")
    dog2split.remove("-")
    for c in range(1, len(dog1split) + 1):
        dogbreed12 += dog1split[c-1]
    for b in range(1, len(dog2split) + 1):
        dogbreed22 += dog2split[b-1]
    print(f"{part3} = {dogbreed12} + {dogbreed22}")
    print(f"{parts} = {dogbreed12} + {dogbreed22}")


