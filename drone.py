import random
import os
types = ["Banana","Strawberry","Juice","Yogurt","Raspberries","Mango","Milk","Blueberry"]
ans = []
combo = []
count = 0
itera = int(input("Questions:"))
for que in range(itera):
    count +=1
    try:
       os.system("cls")
    except:
       print("Chromebook")
    typescopy = types.copy()
    inlist = []
    zeros=[]
    for h in range(len(types)):
       zeros.append(0)
    combo.append(zeros)
    for b in range(random.randint(2,6)):
      ingredient = typescopy.pop(random.randint(0,len(typescopy)-1))
      combo[que][types.index(ingredient)] = 1
      inlist.append(ingredient)
    
    print(f"Rate a smoothie with these ingredients:  {count}/{itera}")
    print(inlist)
    rating = int(input("Rating out of five: "))
    if rating == 1:
       ans.append([0.2])
    elif rating == 2:
       ans.append([0.4])
    elif rating == 3:
       ans.append([0.6])
    elif rating == 4:
       ans.append([0.8])
    elif rating == 5:
       ans.append([1])
print("Combination:")
print(combo)
print()
print("Answers:")
print(ans)
    