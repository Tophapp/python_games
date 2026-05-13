print("Collatz Conjecture Genarator")

num2 = int(input("Input Number: "))
num3 = int(input("Input Number: "))

listthing = []
for n in range (num2,num3+1):
    num = n
    listthing = []
    while True:
    
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        listthing.append(num)
        num = round(num)
        if num == 1:
            print(f"Starting Number: {n}  Steps: {len(listthing)}")
            print(f"Numbers Visited: {listthing}")
            
            print()
            num = n
            break
        continue
