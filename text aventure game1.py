roomnumber = 1
userinput = input("")

def room(roomnum, imput):
        roomnumeer = roomnum
        if roomnumeer == 1 and imput != "w":
            print("You are in the Starting Room")
            return roomnumeer
        if imput == "w" and roomnumeer == 1:
            print("welcolm to The Herbitoreum")
            roomnumeer = 2
            return roomnumeer
        elif imput == "w" and roomnumeer == 2:
            print("There is nothing there")
            roomnumeer = 2
            return roomnumeer
        elif imput == "e" and roomnumeer == 2:
            roomnumeer = 1
            print("Back to the Start")
            return roomnumeer


roomnumber = room(roomnumber, userinput)
for x in range(1, 100):
    room(roomnumber, input(""))