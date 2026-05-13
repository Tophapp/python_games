num1 = 17
rang1, rang2 = int(input("From Range ")), int(input("To "))
numedit = (num1 / 2 + 1)
numedit2 = int(numedit)
printer = 0
for l in range(rang1, rang2):
    for x in range(2, int(l/2)+1):
        if l % x == 0:
            #print(f"{l} is not prime. It can be made with {x}")
            printer = 0
            break

        else:
            printer += 1
            if printer == int(l/2)-1:
                print(f"{l} is Prime!")
                printer = 0
def aoc(b):
    return 3.14 * b * b
