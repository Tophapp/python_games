import os

dex = 525004424
mal = 525005423
mom = float('inf')
rand = 1007031
while True:
    os.system("cls")
    print("dex = "+str(dex))
    print("mal = "+str(mal))
    print("rand = "+str(rand))
    print("mom = Infinite")

    inp = input("")
    inp = inp.split(" ")

    if inp[0] == "rand":
        rand += int(inp[1])
    elif inp[0] == "dex":
        dex += int(inp[1])
    elif inp[0] == "mal":
        mal += int(inp[1])
    elif inp[0] == "mom":
        mom += int(inp[1])
    elif inp[0] == "all":
        mom += int(inp[1])
        mal += int(inp[1])
        dex += int(inp[1])
        rand += int(inp[1])

