import os
outfin = []
ans = []
for x in range(int(input("Iterations: "))):
    os.system("cls")
    
    inp = input("")
    inp = inp.split(" ")
    inp.append(".")
    inp.insert(0,".")
    for b in range(1,len(inp)):
        out2 = []
        out2.append(inp[b-1])
        outfin.append(out2)
        ans.append([inp[b]])
    
print()
print("Questions")
print(outfin)
print()
print("Answers")
print(ans)