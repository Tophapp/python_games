import random
posname = ["Tim Lork","Alexander Harch","Bob Smukleham","Briant Tukerman","Mint Quartler","Emanuel Forge","Pieton Gorfin","Freddie Consatamion","Tommy Kholb","Jarv Mintorlm","Victor Fold","Cherry Qwaltz","Nixton Dorm","Kole Trenton"] 
print("Welcome To Court Knox, The Game Where The Same People Do Crime Over And Over Again And Sometimes Get Away With It Because The Game Says So")
while True:
    mode = input("Choose A Gamemode: fun mode, career mode, And bad day mode: ")

    if mode == "f" or mode == "fun mode" or mode == "Fun Mode":
        mode = 1
        break
    elif mode == "c" or mode == "career mode" or mode == "Career Mode":
        mode = 2
        break
    elif mode == "b" or mode == "bad day mode" or mode == " Bad Day Mode":
        mode = 3
        break
    else:
        print("That Is Not One Of The Selected Options, If You Cant Read The Options Than You Should Go Back To Preschool.  If You Are Already in Preschool Than You Should Wait A Year Before You Play This Game")
        continue
evfors = {"1 Witness":2,"2 Witnesses":4,"Fingerprints At Crime Scene":6,"Recently Bought Tool/weapon Used In Crime":4,"Video Evedence":7}
evagansts = {"At Home Says Neighbor":-2,"Lived Far Away":-5,"Car Still In Driveway":-3,"Shopping At Time Of Crime":-6}
evforskeys = list(evfors.keys())
    
evaganstskeys = list(evagansts.keys())
class case():
    def __init__(self):
        self.evforss = evfors
        self.evagainstss = evagansts
        self.evfor = {}
        self.evagainst = {}
        self.combinedev = {}
        self.combinedev.update(self.evfor)
        self.combinedev.update(self.evagainst)
        self.name = random.choice(posname)
        self.evforskeyss = list(evfors.keys())
    
        self.evaganstskeyss = list(evagansts.keys())
        self. eat = None

    

        for windoweater in range(1,random.randint(2,3)+1):
            self.eat = random.choice(self.evforskeyss)
            self.evfor.update(self.eat,self.evforss[self.evforskeyss.index(self.eat)])
            self.evforss.pop(self.evforss.index(self.evfor[len(self.evfor-1)]))
        for windoweater in range(1,random.randint(2,3)+1):
            self.eat = random.choice(self.evaganstskeyss)
            self.evfor.update(self.eat,self.evagainstss[self.evaganstskeyss.index(self.eat)])
            self.evagainstss.pop(self.evagainstss.index(self.evagainst[len(self.evagainst-1)]))

        self.combinedev.update(self.evfor)
        self.combinedev.update(self.evagainst)
        self.score = 0
                
        self.val = list(self.combinedev.keys())
    
        self.val_list = list(self.combinedev.values())
        for self.totalwowsocoolahhhh in self.combinedev:
            self.score += self.totalwowsocoolahhhh
dog = case()