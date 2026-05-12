import random
import time
import os
pr1 = [8,8,8,8,8,8,8,8]
pr2 = [0,0,0,0,0,0,0,0]
pr3 = [0,0,0,0,0,0,0,0]
pr4 = [0,0,0,0,0,0,0,0]
pr5 = [0,0,0,0,0,0,0,0]
pr6 = [0,0,0,0,0,0,0,0]

for x in range(1,70000):
    time.sleep(0.1)
    os.system("cls")
    print(pr1)
    print(pr2)
    print(pr3)
    print(pr4)
    print(pr5)
    print(pr6)
    pr6 = pr5
    pr5 = pr4
    pr4 = pr3
    pr3 = pr2
    pr2 = pr1
    if pr6 == [8,8,8,8,8,8,8,8]:

        pr1 = [0,0,0,0,0,0,0,0]
    elif pr6 == [0,0,0,0,0,0,0,0] and pr5 == [0,0,0,0,0,0,0,0] and pr4 == [0,0,0,0,0,0,0,0] and pr3 == [0,0,0,0,0,0,0,0] and pr2 == [0,0,0,0,0,0,0,0]:
        pr1 = [8,8,8,8,8,8,8,8]
    else:
        pr1 = [0,0,0,0,0,0,0,0]
    


    