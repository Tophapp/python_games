import tkinter as tk
from PIL import Image, ImageTk
import random 
import base64
import os

action = random.randrange(1,4)
timer = 0
direction = 0
frame = 0
mode = False
picture = None
popups = []
pull = False
timeframe = 300
speed = 1
side = 2
window = tk.Tk()
window.title("FRIEDRICH The XXXXII.exe")
dir_path = os.path.dirname(os.path.realpath(__file__))
#dir_path = os.getcwd() 


try:
    walk1 = Image.open(dir_path + "\\pixil-frame-0 (13).png")
    walk1 = ImageTk.PhotoImage(walk1)
except:
    dir_path = os.getcwd() 
    walk1 = Image.open(dir_path + "\\pixil-frame-0 (13).png")
    walk1 = ImageTk.PhotoImage(walk1)

walk2 = Image.open(dir_path + "\\pixil-frame-0 (12).png")
walk2 = ImageTk.PhotoImage(walk2)
pull1 = Image.open(dir_path + "/PetRockMove1.png")
pull1 = ImageTk.PhotoImage(pull1)
pull2 = Image.open(dir_path + "/PetRockMove2.png")
pull2 = ImageTk.PhotoImage(pull2)
sit = Image.open(dir_path + "/PetRockSitting.png")
sit= ImageTk.PhotoImage(sit)
pullother1 = Image.open(dir_path + "/PetRockMoveOther2.png")
pullother1 = ImageTk.PhotoImage(pullother1)
pullother2 = Image.open(dir_path + "/PetRockMoveOther1.png")
pullother2= ImageTk.PhotoImage(pullother2)
imagey1,imagey2 = walk1, walk2
y = random.randint(5,window.winfo_screenheight() - 5 - imagey1.height())
x = random.randint(5,window.winfo_screenwidth() - 5 - imagey1.width())
dimensions = str(imagey1.width())  + "x" + str(imagey1.height())
width, height = imagey1.width(), imagey1.height()
image_label = tk.Label(window, bg="white",width=width, height=height, image=imagey1)
image_label.pack()
window.geometry(dimensions)
window.wm_attributes('-transparentcolor', 'white')
window.attributes('-topmost', True)
window.overrideredirect(True)

class annoy():
    def __init__(self):
        self.index = 0
        self.die = False
        if side == 1:
            self.pos = [x+ imagey1.width(),y]
        else:
            self.pos = [x- imagey1.width(),y]
        self.targetx = random.randint(305,window.winfo_screenwidth() - 305)

        if picture == 1:
            self.pic = Image.open(dir_path + "/BAD.png")
        elif picture == 2:
            self.pic = Image.open(dir_path + "/CHEETOBIRB.png")
        elif picture == 3:
            self.pic = Image.open(dir_path + "/CORNBUN.png")
        elif picture == 4:
            self.pic = Image.open(dir_path + "/DERP.png")
        elif picture == 5:
            self.pic = Image.open(dir_path + "/DRAWING1.png")
        elif picture == 6:
            self.pic = Image.open(dir_path + "/DRAWING2.png")
        elif picture == 7:
            self.pic = Image.open(dir_path + "/DRAWING3.png")
        elif picture == 8:
            self.pic = Image.open(dir_path + "/DRAWING4.png")
        elif picture == 9:
            self.pic = Image.open(dir_path + "/LOGIC.png")
        elif picture == 10:
            self.pic = Image.open(dir_path + "/MAIL.png")
        elif picture == 11:
            self.pic = Image.open(dir_path + "/MUD.png")
        elif picture == 12:
            self.pic = Image.open(dir_path + "/No way.png")
        elif picture == 13:
            self.pic = Image.open(dir_path + "/SIGN.png")
        elif picture == 14:
            self.pic = Image.open(dir_path + "/StonksGoose.png")
        elif picture == 15:
            self.pic = Image.open(dir_path + "/TASKS.png")

        self.pic = ImageTk.PhotoImage(self.pic)
        self.imagewindow = tk.Toplevel()
        self.moveable = True
        self.die2 = False
        self.imagewindow.geometry(str(self.pic.width())  + "x" + str(self.pic.height()) + "+" + str(self.pos[0]) + "+" + str(self.pos[1]))
        self.timage_label = tk.Label(self.imagewindow, bg="white",width=self.pic.width(), height=self.pic.height(), image=self.pic)
        self.timage_label.pack()
        self.imagewindow.attributes('-topmost', True)

    def otherupdate(self):
        self.imagewindow.protocol("WM_DELETE_WINDOW", self.on_closingother)
    def update(self):
        self.imagewindow.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        self.die = True
    def on_closingother(self):
        self.die2 = True


def loop():
    global x
    global y
    global timer
    global direction
    global mode
    global picture
    global popups 
    global pull
    global imagey1
    global imagey2
    global timeframe
    global speed
    global side

    if action == 2:
        if popups != []:
            for h in popups:
                if h != "DELETED, GO AWAY":
                    if h.moveable == True:
                        if side == 1:
                            h.pos = [x+ imagey1.width(),y]
                        else:
                            h.pos = [x - h.pic.width(),y]
                        h.update()
                        
                        h.imagewindow.geometry(str(h.pic.width())  + "x" + str(h.pic.height()) + "+" + str(h.pos[0]) + "+" + str(h.pos[1]))
                        if h.pos[0] <= h.targetx + 4 and h.pos[0] >= h.targetx - 4:
                            h.moveable = False
                            pull = False
                            imagey1,imagey2 = walk1, walk2
        if x > window.winfo_screenwidth()- imagey1.width():
            mode = True
            timeframe = 500
            imagey1 = pull1
            imagey2 = pull2
            x = window.winfo_screenwidth() - imagey1.width() - 2
        elif x < 0:
            mode = True
            timeframe = 500
            imagey1 = pullother1
            imagey2 = pullother2
            x = imagey1.width() + 2
    
        else:
            imagey1,imagey2 = walk1, walk2
            mode = False
        if pull == False:
            timeframe = 300
            if mode == True:
                pull = True
                picture = random.randint(1,15)
                popup = annoy()
                popups.append(popup)
                popup.index = len(popups) - 1
            if x >= round(window.winfo_screenwidth()/2):
                x += 2
                side = 1
            else:
                x -= 2
                side = 2
        else:
            if side == 1:
                imagey1 = pull1
                imagey2 = pull2
                x -= 1
            else:
                imagey1 = pullother1
                imagey2 = pullother2
                x += 1
    elif action == 1:
        if popups != []:
            for h in popups:
                if h != "DELETED, GO AWAY":
                    if h.moveable == True:
                        h.moveable = False
        pull = False
        timeframe = 300
        imagey1,imagey2 = walk1, walk2
        timer -= 0.01

        if timer <= 0:
            direction = random.randint(1,5)
            speed = random.randint(1,3)
            timer = 3
        else:
            if direction == 1:
                x += speed
            elif direction == 2:
                x -= speed
            elif direction == 3:
                y += speed
            elif direction == 4:
                y -= speed
            elif direction == 5:
                if y >= (round(window.winfo_screenheight()/2 - 4)) and y <= (round(window.winfo_screenheight()/2 + 4)) and x >= (round(window.winfo_screenwidth()/2) -144) and x <= (round(window.winfo_screenwidth()/2) -136):
                    imagey1 = sit
                    imagey2 = sit
                else:
                    if x > round(window.winfo_screenwidth()/2) -140:
                        x -= speed
                    elif x < round(window.winfo_screenwidth()/2) - 140:
                        x += speed
                    if y > round(window.winfo_screenheight()/2):
                        y -= speed
                    elif y < round(window.winfo_screenheight()/2):
                        y += speed
                    imagey1 = walk1
                    imagey2 = walk2
            if x < 0:
                direction = 1
                x = 0
            elif x > window.winfo_screenwidth()- imagey1.width():
                direction = 2
                x = window.winfo_screenwidth() - imagey1.width() - 2
            if y < 0:
                direction = 3
                y = 0
            elif y > window.winfo_screenheight()- imagey1.height():
                direction = 4
                y = window.winfo_screenheight() - imagey1.height() - 2
    elif action == 3:
        if popups != []:
            for h in popups:
                if h != "DELETED, GO AWAY":
                    if h.moveable == True:
                        h.moveable = False
        pull = False
        imagey1 = sit
        imagey2 = sit
    elif action == 4:
        if popups != []:
            for h in popups:
                if h != "DELETED, GO AWAY":
                    if h.moveable == True:
                        h.moveable = False
        pull = False
        if y >= (round(window.winfo_screenheight()/2 - 4)) and y <= (round(window.winfo_screenheight()/2 + 4)) and x >= (round(window.winfo_screenwidth()/2) -144) and x <= (round(window.winfo_screenwidth()/2) -136):
            imagey1 = sit
            imagey2 = sit
        else:
            if x > round(window.winfo_screenwidth()/2) -140:
                x -= speed
            elif x < round(window.winfo_screenwidth()/2) - 140:
                x += speed
            if y > round(window.winfo_screenheight()/2):
                y -= speed
            elif y < round(window.winfo_screenheight()/2):
                y += speed
            imagey1,imagey2 = walk1, walk2
    window.geometry(dimensions + '+{x}+{y}'.format(x=str(x),y=str(y)))
    
    if popups != []:
        for l in popups:
            if l != "DELETED, GO AWAY":
                if l.moveable != True:
                    l.otherupdate()
                if l.die == True:
                    popups[l.index] = "DELETED, GO AWAY"
                    l.imagewindow.destroy()
                    pull = False
                if l.die2 == True:
                    popups[l.index] = "DELETED, GO AWAY"
                    l.imagewindow.destroy()
    window.after(10, loop)


def actionnew():
    global action
    action = random.randint(1,4)
    window.after(10000,actionnew)

def fun(event):
    if event.keysym=='z':
       exit()

def frameadvance():
    global frame 
    frame += 1
    if frame == 2:
        frame = 0
    if frame == 0:
        image_label.configure(image=imagey1)
    else:
        image_label.configure(image=imagey2)
    window.after(timeframe,frameadvance)

window.bind("<Key>", fun)
window.after(10,loop)
window.after(0,actionnew)
window.after(0,frameadvance)
# Start the Tkinter event loop
window.mainloop()