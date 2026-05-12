
log = []
selfid = 0
for message in log:
    if message[0] != selfid:
        print()
        print(message[0])
        print(message[1])
