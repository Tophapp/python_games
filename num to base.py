import math
try:
    num = int(input("Enter Number: "))
    base = int(input("Enter Base: "))
    baselist = []
    awnser = ""
    while True:
        baselist.insert(0,str(num % base))
        num = num / base
        num = math.floor(num)
        if num == 0:
            break
    for x in range(1,len(baselist)+1):
        awnser += baselist[x-1]
    print(awnser)
except:
    print("Something Went Wrong :P")