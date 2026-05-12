decimalsystem = int(input("Choose The Number Of Digits (Decimal System) (Max 10): "))
startingrow = input("Enter Starting Row: ")
startrow = [*startingrow]
firstrow = [*startingrow]
for q in range(1, len(firstrow)+1):
    firstrow[q-1] = int(firstrow[q-1])
for q in range(1, len(startrow)+1):
    startrow[q-1] = int(startrow[q-1])
Speashelrow = []
memory = []
memory.append(startrow)
currentrow = []
currentsum = 0
for l in startrow:
    if firstrow.index(l) != (len(firstrow)-1):
        currentsum = (int(l) + int(firstrow[firstrow.index(l) + 1]))
        firstrow.pop(0)
        if currentsum >= decimalsystem:
            currentrow.append(currentsum - decimalsystem)
        else:
            currentrow.append(currentsum)
for z in range(1, len(currentrow)+1):
    Speashelrow.append(currentrow[z-1])
for x in range(1,len(startrow)-1):
    firstrow = currentrow
    Speashelrow = []
    for z in range(1, len(firstrow)+1):
        Speashelrow.append(firstrow[z-1])
    memory.append(Speashelrow)
    firstrow = currentrow
    Speashelrow = []
    for z in range(1, len(firstrow)+1):
        Speashelrow.append(firstrow[z-1])
    currentrow = []
    

    for l in Speashelrow:
        if firstrow.index(l) != (len(firstrow)-1):
            currentsum = int(l) + int(firstrow[firstrow.index(l) + 1])
            firstrow.pop(0)
            if currentsum >= decimalsystem:
                currentrow.append(currentsum - decimalsystem)
            else:
                currentrow.append(currentsum)
currentsum = int(Speashelrow[0]) + int(Speashelrow[1])

if currentsum >= decimalsystem:
    memory.append(currentsum - decimalsystem)
else:
    memory.append(currentsum)
haha = len(startrow)
row = []
add = ""
for p in range(1, haha+1):
    add += "  "
    haha -= 1
    print(add,row)
    row = []
    row.append(memory[0])
    memory.pop(0)
add += "   "
print(add,row)