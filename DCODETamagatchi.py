import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import math
import winsound
import time
from tkinter import messagebox
#c:\users\kyled\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\scripts\pyinstaller.exe --onefile --clean DCODETamagatchi.py

def main():
    #make player window
    player = tk.Tk()

    #loading sprites
    global imagey1

    path = os.path.dirname(os.path.realpath(__file__))
    try:
        walk1 = Image.open(path + "\\sprites\\walk1.png").resize((200,200))
        walk1 = ImageTk.PhotoImage(walk1)
    except:
        try:
            path = os.getcwd() 
            walk1 = Image.open(path + "\\sprites\\walk1.png").resize((200,200))
            walk1 = ImageTk.PhotoImage(walk1)
        except:
            print("Sprites Not Found, Place in folder with a subfolder called 'sprites' with reqired sprites. Self Destructing Soon in 3 seconds")
            time.sleep(3)
            quit()
    imagey1 = walk1
    
    harddrive = Image.open(path + "\\sprites\\harddrive.png").resize((100,100))
    harddrive = ImageTk.PhotoImage(harddrive)

    deadsprite =ImageTk.PhotoImage(Image.open(path + "\\sprites\\die.png").resize((200,200)))
    asleep1 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\asleep1.png").resize((200,200)))
    asleep2 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\asleep2.png").resize((200,200)))
    asleep3 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\asleep3.png").resize((200,200)))
    asleep4 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\asleep4.png").resize((200,200)))

    wifi1 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\wifi1.png").resize((100,100)))
    wifi2 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\wifi2.png").resize((100,100)))
    wifi3 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\wifi3.png").resize((100,100)))
    wifi4 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\wifi4.png").resize((100,100)))

    walk2 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\walk2.png").resize((200,200)))
    walk3 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\walk3.png").resize((200,200)))
    walk4 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\walk4.png").resize((200,200)))

    sick1 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\sick1.png").resize((200,200)))
    sick2 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\sick2.png").resize((200,200)))
    sick3 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\sick3.png").resize((200,200)))
    sick4 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\sick4.png").resize((200,200)))
    tired1 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\tired1.png").resize((200,200)))
    tired2 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\tired2.png").resize((200,200)))
    tired3 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\tired3.png").resize((200,200)))
    tired4 =ImageTk.PhotoImage(Image.open(path + "\\sprites\\tired4.png").resize((200,200)))
    bench =ImageTk.PhotoImage(Image.open(path + "\\sprites\\bench.png"))

    playfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\playfile.png").resize((100,100)))
    cleancasefile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\cleancase.png").resize((100,100)))
    cleandrivefile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\cleandrive.png").resize((100,100)))
    doctorfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\doctor.png").resize((100,100)))
    mealfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\feedmeal.png").resize((100,100)))
    treatfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\feedtreat.png").resize((100,100)))
    gamefile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\game.png").resize((100,100)))
    shutofffile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\shutoff.png").resize((100,100)))
    wakefile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\wake.png").resize((100,100)))
    taxesfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\taxes.png").resize((100,100)))
    trainfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\train.png").resize((100,100)))
    walkfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\walk.png").resize((100,100)))
    wordfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\word.png").resize((100,100)))
    savefile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\save.png").resize((100,100)))
    loadfile = ImageTk.PhotoImage(Image.open(path + "\\sprites\\load.png").resize((100,100)))


    #setup for player window
    player.title("Tamagotchi DCODE.cool")
    dimensions = str(imagey1.width())  + "x" + str(imagey1.height())
    width, height = imagey1.width(), imagey1.height()
    image_label = tk.Label(player, bg="white",width=width, height=height, image=imagey1)
    image_label.pack()
    player.geometry(dimensions)
    player.wm_attributes('-transparentcolor', 'white')
    player.overrideredirect(True)

    #Console Information
    print("This Console Is The Life Of The Game, Close It If You Want To Stop Playing")
    print()
    print("Welcome to Tech-Pets™!")
    print("-----------------------------------------------")
    print("If you would like the instructions for this game, type '?', otherwise press enter.")
    messagebox.showinfo("Alert", "Look at the Console")
    instruction = input()
    if instruction =="?":
        print("""Welcome to Tech-Pets™!
In this game you take care of a device by doing actions.  The computer has 5 statistics that you need to monitor.  
1:Health, this is the health of the computer, if it gets too low, it dies.  You can find this statistic as physical deterioration of the pet or by right clicking the pet and finding the label:HP.  
2:Weight, the weight, or storage taken up, of the pet.  If it gets too high or low then your pet dies.  It is found by right clicking the pet and finding the hard drive symbol.  
3:Hunger, this statistic shows how hungry the Tech-Pet™ is.  If it gets too low, your pet starts to degrade and other stats are lowered.  This statistic periodically goes down.  It is found by right clicking the pet and finding the battery symbol.  
4:Happiness, the happiness of the pet.  This statistic will go down over time, similar to hunger.  If it gets too low, then your pet gets depressed and starts losing energy. It is denoted by right clicking the pet and finding the wifi section (because happiness is directly correlated by how much you use the internet).  
5:Energy, the amount of energy the pet has to do tasks.  This decides your pet's ability to do a task or not.  Different tasks require different amounts of energy.  If it gets too low, you cannot do anything.  This statistic is found by right clicking the pet, and clicking the “Task Manager” button and finding the % used section. 
To control these statistics, you must provide your Tech-Pet™ with actions to do that differently affect the statistics.  These actions are found by right clicking the pet and selecting the “File Explorer” button.  Each action also has a minigame in which you do a task a certain number of times (normally clicking buttons) to successfully do the action.  WARNING: If you click the X then the action will not be performed.  The actions and their games are as follows.
Clean case: This action is simply cleaning the case of your Tech-Pet™ and involves clicking the dust to remove it from the pet.
Clean Hard Drive: This action is simply cleaning the hard drive of the pet by removing unwanted folders and files.  Click the files to remove them (does not actually affect the action files).
Feed Meal: Feed the Tech-Pet™ a meal, simply press the squares to “eat” that part of the food
Feed Treat: Ibid
GAMING!: You do some EXTREME GAMING on your Tech-Pet™, this is a harder minigame where you have to click the square as it rapidly teleports around, if you click it enough times, you win.
Play: You play with your Tech-Pet™, different from gaming.  In this game you must press the button when the background turns gold.  No spamming is allowed.
Load and Save: Tech-Pet™’s exclusive software allows for users to store their Tech-Pet™ in a permanent digitized format and then recall the pet at any moment as if the pet was never stopped in the first place.  WARNING: it will be like time has passed so if you save and then wait 5 days and then load, your pet will have died.  If you press the save button, your pet is saved to a digitized format located in the DATA folder of the game files.  You can then recall the pet when you press the load button.  
Wake and Sleep: you may wake your pet and put them to sleep at your will.  WARNING: You cannot wake up a Tech-Pet™ between the hours of 8:30 pm to 8:30 am as they are in shutdown mode.
Taxes: you do your taxes on your Tech-Pet™.  Nothing good comes from taxes.  Simply sign the papers 50 times to finish it.  (yes, it is the US constitution, it technically talks about taxes.)
Training/Get buff: Your Tech-Pet™ trains to become the best of them all.  Simply beat the other square in a race by pressing the “RUN!” button enough times.  (second hardest one but “Challenge is a necessity to become the best, such as I -Rand Tophapp”)
Take on a Walk: Your pet takes a walk to a park and sits down to relax.  Simply press the “Sit on Bench” button and relax for 15 seconds whilst relaxing rain sounds play in the background.  WARNING: You cannot close this window, you are relaxing or you are relaxing, pick your choice.
WORD: Write a great novel in Microsoft Word, simply type the 20 letters out using the buttons above and if you mess up, you restart, if you don't get it when you press submit, you restart.
Take to Doctor: Take your Tech-Pet™ to a doctor, which will heal him from illness if they have any.  Simply choose the best option to fix the medical problems shown.
Some actions may control the states of the Tech-Pet™ or they may happen on their own.  Each state shows a different ailment the Tech-Pet™ is experiencing.  They may be good, neutral, or bad.  They are as follows:
Asleep: your Tech-Pet™ is asleep.  Can be affected by the wake and go to sleep buttons or if the time is between 8:30 pm and 8:30 am.  In that time, your pet will fall asleep and you may not perform actions while it is in this state.  You can make it eat, as it still loses hunger whilst in this state (Less so) but that's all.  WARNING: You cannot wake your pet up in this state, only when you tell them to sleep can you do that.  If you were to set it to sleep by using the go to sleep button then it will have normal hunger loss and you can wake it up.  Whilst asleep, your pet will randomly lose an action from the task manager menu every once in a while, causing you to regain the lost energy and be able to do more tasks.  This will not affect your Tech-Pet™’s statistics except the energy one.
Sick: your Tech-Pet™ may randomly become infected with a virus and start to deteriorate.  You must take him to a doctor or he may die from health loss.  
Depressed: caused by a lack of happiness, will cause your Tech-Pet™ to lose energy over time.  
Deterioration: Your Tech-Pet™ may start to crack and this is a sign of a lack of health, the more cracks, the more health loss your pet has experienced.  This is a cosmetic change but shows the amount of remaining health your Tech-Pet™ has.  
DEAD: Your Tech-Pet™ may die.  If this happens, they appear very cracked and from that point onward, no statistics will deteriorate and nothing will happen.  You may still interact with the pet but it will not affect them in any meaningful way.  They are dead by your hand.
That covers the main features of Tech-Pets™.  For any questions, email Rand Tophapp at magmoslime@gmail.com.
Have a Nice Day!
    Rand Tophapp, Miles Moser, Tyler Ramirez, Tophapp Industries
""")
    global name
    name = input("Please select a name for your pet: ")

    print("Name Sucessfully Confrmed, Look on the background of your computer screen by minimizing this console to find your Tech-Pet™")
    
    #if I reference this variable it wont give me an error and it is also now global
    global interface
    interface = None
    global fileexplore
    fileexplore = None
    global health
    global taxes
    taxes = ["We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.","All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives.  The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature.","No Person shall be a Representative who shall not have attained to the Age of twenty five Years, and been seven Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State in which he shall be chosen.","Representatives and direct Taxes shall be apportioned among the several States which may be included within this Union, according to their respective Numbers, which shall be determined by adding to the whole Number of free Persons, including those bound to Service for a Term of Years, and excluding Indians not taxed, three fifths of all other Persons. The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to chuse three, Massachusetts eight, Rhode-Island and Providence Plantations one, Connecticut five, New-York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five, and Georgia three.","When vacancies happen in the Representation from any State, the Executive Authority thereof shall issue Writs of Election to fill such Vacancies.  The House of Representatives shall chuse their Speaker and other Officers; and shall have the sole Power of Impeachment.","The Senate of the United States shall be composed of two Senators from each State, chosen by the Legislature thereof, for six Years; and each Senator shall have one Vote.  Immediately after they shall be assembled in Consequence of the first Election, they shall be divided as equally as may be into three Classes. The Seats of the Senators of the first Class shall be vacated at the Expiration of the second Year, of the second Class at the Expiration of the fourth Year, and of the third Class at the Expiration of the sixth Year, so that one third may be chosen every second Year; and if Vacancies happen by Resignation, or otherwise, during the Recess of the Legislature of any State, the Executive thereof may make temporary Appointments until the next Meeting of the Legislature, which shall then fill such Vacancies.","No Person shall be a Senator who shall not have attained to the Age of thirty Years, and been nine Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State for which he shall be chosen.  The Vice President of the United States shall be President of the Senate, but shall have no Vote, unless they be equally divided.  The Senate shall chuse their other Officers, and also a President pro tempore, in the Absence of the Vice President, or when he shall exercise the Office of President of the United States.","The Senate shall have the sole Power to try all Impeachments. When sitting for that Purpose, they shall be on Oath or Affirmation. When the President of the United States is tried, the Chief Justice shall preside: And no Person shall be convicted without the Concurrence of two thirds of the Members present.  Judgment in Cases of Impeachment shall not extend further than to removal from Office, and disqualification to hold and enjoy any Office of honor, Trust or Profit under the United States: but the Party convicted shall nevertheless be liable and subject to Indictment, Trial, Judgment and Punishment, according to Law.","The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators.  The Congress shall assemble at least once in every Year, and such Meeting shall be on the first Monday in December, unless they shall by Law appoint a different Day.","Each House shall be the Judge of the Elections, Returns and Qualifications of its own Members, and a Majority of each shall constitute a Quorum to do Business; but a smaller Number may adjourn from day to day, and may be authorized to compel the Attendance of absent Members, in such Manner, and under such Penalties as each House may provide.  Each House may determine the Rules of its Proceedings, punish its Members for disorderly Behaviour, and, with the Concurrence of two thirds, expel a Member.","Each House shall keep a Journal of its Proceedings, and from time to time publish the same, excepting such Parts as may in their Judgment require Secrecy; and the Yeas and Nays of the Members of either House on any question shall, at the Desire of one fifth of those Present, be entered on the Journal.  Neither House, during the Session of Congress, shall, without the Consent of the other, adjourn for more than three days, nor to any other Place than that in which the two Houses shall be sitting.","The Senators and Representatives shall receive a Compensation for their Services, to be ascertained by Law, and paid out of the Treasury of the United States. They shall in all Cases, except Treason, Felony and Breach of the Peace, be privileged from Arrest during their Attendance at the Session of their respective Houses, and in going to and returning from the same; and for any Speech or Debate in either House, they shall not be questioned in any other Place.  No Senator or Representative shall, during the Time for which he was elected, be appointed to any civil Office under the Authority of the United States, which shall have been created, or the Emoluments whereof shall have been encreased during such time; and no Person holding any Office under the United States, shall be a Member of either House during his Continuance in Office.","All Bills for raising Revenue shall originate in the House of Representatives; but the Senate may propose or concur with Amendments as on other Bills.","Every Bill which shall have passed the House of Representatives and the Senate, shall, before it become a Law, be presented to the President of the United States; If he approve he shall sign it, but if not he shall return it, with his Objections to that House in which it shall have originated, who shall enter the Objections at large on their Journal, and proceed to reconsider it. If after such Reconsideration two thirds of that House shall agree to pass the Bill, it shall be sent, together with the Objections, to the other House, by which it shall likewise be reconsidered, and if approved by two thirds of that House, it shall become a Law. But in all such Cases the Votes of both Houses shall be determined by yeas and Nays, and the Names of the Persons voting for and against the Bill shall be entered on the Journal of each House respectively. If any Bill shall not be returned by the President within ten Days (Sundays excepted) after it shall have been presented to him, the Same shall be a Law, in like Manner as if he had signed it, unless the Congress by their Adjournment prevent its Return, in which Case it shall not be a Law.","Every Order, Resolution, or Vote to which the Concurrence of the Senate and House of Representatives may be necessary (except on a question of Adjournment) shall be presented to the President of the United States; and before the Same shall take Effect, shall be approved by him, or being disapproved by him, shall be repassed by two thirds of the Senate and House of Representatives, according to the Rules and Limitations prescribed in the Case of a Bill.","""The Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and provide for the common Defence and general Welfare of the United States; but all Duties, Imposts and Excises shall be uniform throughout the United States;

To borrow Money on the credit of the United States;

To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes;

To establish an uniform Rule of Naturalization, and uniform Laws on the subject of Bankruptcies throughout the United States;

To coin Money, regulate the Value thereof, and of foreign Coin, and fix the Standard of Weights and Measures;

To provide for the Punishment of counterfeiting the Securities and current Coin of the United States;

To establish Post Offices and post Roads;

To promote the Progress of Science and useful Arts, by securing for limited Times to Authors and Inventors the exclusive Right to their respective Writings and Discoveries;

To constitute Tribunals inferior to the supreme Court;

To define and punish Piracies and Felonies committed on the high Seas, and Offences against the Law of Nations;

To declare War, grant Letters of Marque and Reprisal, and make Rules concerning Captures on Land and Water;

To raise and support Armies, but no Appropriation of Money to that Use shall be for a longer Term than two Years;

To provide and maintain a Navy;

To make Rules for the Government and Regulation of the land and naval Forces;

To provide for calling forth the Militia to execute the Laws of the Union, suppress Insurrections and repel Invasions;""","To provide for organizing, arming, and disciplining, the Militia, and for governing such Part of them as may be employed in the Service of the United States, reserving to the States respectively, the Appointment of the Officers, and the Authority of training the Militia according to the discipline prescribed by Congress;  To exercise exclusive Legislation in all Cases whatsoever, over such District (not exceeding ten Miles square) as may, by Cession of particular States, and the Acceptance of Congress, become the Seat of the Government of the United States, and to exercise like Authority over all Places purchased by the Consent of the Legislature of the State in which the Same shall be, for the Erection of Forts, Magazines, Arsenals, dock-Yards, and other needful Buildings;—And","To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.","The Migration or Importation of such Persons as any of the States now existing shall think proper to admit, shall not be prohibited by the Congress prior to the Year one thousand eight hundred and eight, but a Tax or duty may be imposed on such Importation, not exceeding ten dollars for each Person.","The Privilege of the Writ of Habeas Corpus shall not be suspended, unless when in Cases of Rebellion or Invasion the public Safety may require it.  No Bill of Attainder or ex post facto Law shall be passed.  No Capitation, or other direct, Tax shall be laid, unless in Proportion to the Census or enumeration herein before directed to be taken.","No Tax or Duty shall be laid on Articles exported from any State.  No Preference shall be given by any Regulation of Commerce or Revenue to the Ports of one State over those of another: nor shall Vessels bound to, or from, one State, be obliged to enter, clear, or pay Duties in another.  No Money shall be drawn from the Treasury, but in Consequence of Appropriations made by Law; and a regular Statement and Account of the Receipts and Expenditures of all public Money shall be published from time to time.","No Title of Nobility shall be granted by the United States: And no Person holding any Office of Profit or Trust under them, shall, without the Consent of the Congress, accept of any present, Emolument, Office, or Title, of any kind whatever, from any King, Prince, or foreign State.","No State shall enter into any Treaty, Alliance, or Confederation; grant Letters of Marque and Reprisal; coin Money; emit Bills of Credit; make any Thing but gold and silver Coin a Tender in Payment of Debts; pass any Bill of Attainder, ex post facto Law, or Law impairing the Obligation of Contracts, or grant any Title of Nobility.","No State shall, without the Consent of the Congress, lay any Imposts or Duties on Imports or Exports, except what may be absolutely necessary for executing it's inspection Laws: and the net Produce of all Duties and Imposts, laid by any State on Imports or Exports, shall be for the Use of the Treasury of the United States; and all such Laws shall be subject to the Revision and Controul of the Congress.","No State shall, without the Consent of Congress, lay any Duty of Tonnage, keep Troops, or Ships of War in time of Peace, enter into any Agreement or Compact with another State, or with a foreign Power, or engage in War, unless actually invaded, or in such imminent Danger as will not admit of delay."]
    health = 100
    global hunger
    hunger = 100
    global energy
    global cases
    cases = {"Paitient describes having a window open without their action.":1,"Patient describes their computer crashing frequently without a reason.":1,"Patient describes their computer not being able to run games it could run only a few months ago.":1,"Patient describes having their computer not booting.":3,"Patient describes their computer charger is bitten all the way through.":3,"Patient describes their display having a baseball forcefully shoved through it":3,"Patient describes their computer being frozen":2,"Patient describes their computer not connecting to the internet properly":2,"THE BLUE SCREEN OF DEATH!":2}
    energy = 100
    global happy
    happy = 100
    global weight
    weight = 5
    global x
    x = 500
    global y
    global dead
    global taskmgr
    taskmgr = None
    global asleep
    global tasks
    tasks = {}
    asleep = False
    dead = False
    y = 500
    global cycles
    global sick
    sick = False
    cycles = 0
    global canvas
    canvas = None
    batterycolors = ["red" ,"yellow","green"]
    global hungerdeg
    hungerdeg = 0.01
    global lastrecordedtime
    lastrecordedtime = time.time()
    global lastsprite
    lastsprite = None
    global playerdata
    global loaded
    loaded = False
    playerdata = {"tasks":tasks, "sick":sick,"dead":dead,"health":health,"hunger":hunger,"energy":energy,"happy":happy,"weight":weight,"lastrecordedtime":lastrecordedtime}

    #main loop
    def loop():
        #declare variables
        global y 
        global imagey1
        global x 
        global health
        global hunger
        global energy
        global happy
        global weight
        global lastrecordedtime
        global asleep
        global cycles
        global hungerdeg
        global sick
        global lastsprite
        global tasks
        global dead
        global loaded
        global name

        #player stats
        global playerdata
        if not loaded:
            playerdata = {"tasks":tasks, "sick":sick,"dead":dead,"health":health,"hunger":hunger,"energy":energy,"happy":happy,"weight":weight,"lastrecordedtime":lastrecordedtime,"name":name}
        else:
            try:
                tasks = playerdata["tasks"]
                sick = playerdata["sick"]
                dead = playerdata["dead"]
                health = playerdata["health"]
                hunger = playerdata["hunger"]
                energy = playerdata["energy"]
                happy = playerdata["happy"]
                weight = playerdata["weight"]
                name= playerdata["name"]
                lastrecordedtime = playerdata["lastrecordedtime"]
            except:
                messagebox.showinfo("Alert", "Incorrect File Contents")
            loaded = False

        #reset image
        imagey1 = walk1
        
        #cycle counter
        for updates in range(math.floor((time.time()-lastrecordedtime) /0.01)):
            cycles += 1
            if cycles % 99 == 0:
                hunger -= hungerdeg
                happy -= hungerdeg/2

            #sleeping effects
            if asleep:
                if cycles%90000 == 0:  
                    if len(list(tasks)) > 0:
                        keytasks = random.choice(list(tasks))
                        if not tasks[keytasks] < 0:
                            energy += tasks.pop(keytasks)
                            if len(list(tasks)) ==0:
                                energy = 100

            #sick effects
            if sick and not asleep:
                if cycles%20000 == 0:
                    health -=1

        if energy<=20:
            imagey1 = None
            if health <= 100 and not dead:
                    imagey1 = tired1    
            if health <= 75 and not dead: 
                    imagey1 = tired2                                                                                                                   
            if health <= 50 and not dead: 
                    imagey1 = tired3                                                                                                                     
            if health <= 25 and not dead: 
                    imagey1 = tired4   

        if asleep:
            imagey1 = None
            if health <= 100 and not dead:
                    imagey1 = asleep1    
            if health <= 75 and not dead: 
                    imagey1 = asleep2                                                                                                                   
            if health <= 50 and not dead: 
                    imagey1 = asleep3                                                                                                                     
            if health <= 25 and not dead: 
                    imagey1 = asleep4   

        if sick:
            imagey1 = None
            if health <= 100 and not dead:
                    imagey1 = sick1    
            if health <= 75 and not dead: 
                    imagey1 = sick2                                                                                                                   
            if health <= 50 and not dead: 
                    imagey1 = sick3                                                                                                                     
            if health <= 25 and not dead: 
                    imagey1 = sick4   

        #if stats go too low, something happens
        if health <= 0 and not dead: 
            die()                                                                                                                     
            health = 0
        if (weight <= 0 or weight >= 200)and not dead: 
            die()                                                                                                                     
            weight = 0
        if health <= 100 and not dead and imagey1 == walk1: 
            imagey1 = walk1      
        if health <= 75 and not dead and imagey1 == walk1: 
            imagey1 = walk2                                                                                                                   
        if health <= 50 and not dead and imagey1 == walk1: 
            imagey1 = walk3                                                                                                                     
        if health <= 25 and not dead and imagey1 == walk1: 
            imagey1 = walk4                                                                                                                 
        if hunger <= 0:
            hunger = 0
            for updates in range(math.floor((time.time()-lastrecordedtime) /0.01)):
                if random.randint(1,2000) == 76:
                    health -= 1
                if random.randint(1,20000) == 76:
                    #being too hungry leads to unhapiness and less energy
                    action("Very Hungry",10,hundeg=0,hapdeg=20,lbdeg=0.2)
        if hunger <= 30:
            hunger = 0
            for updates in range(math.floor((time.time()-lastrecordedtime) /0.01)):
                if random.randint(1,90000) == 76:
                    action("Hungry",10,hundeg=0,hapdeg=10,lbdeg=0.2)
        if energy <= 0:
            energy = 0
            asleep = True
        if happy <= 0:
            happy = 0
            imagey1 = None
            for updates in range(math.floor((time.time()-lastrecordedtime) /0.01)):
                if random.randint(1,20000) == 76:
                    #Depression
                    action("Depressed",5,hundeg=0,hapdeg=0,lbdeg=0.1)
        
        #send window to back
        try:
            player.lower()
        except:
            pass

        #set position of player to (x,y)
        player.geometry(dimensions + '+{x}+{y}'.format(x=str(x),y=str(y)))

        #sleepy time
        if time.localtime()[3] > 20 or time.localtime()[3] < 8:
            asleep = True
            hungerdeg = 0.001
        else:
            hungerdeg = 0.008

        #oh no! he got sick!
        if not time.localtime()[3] > 20 or time.localtime()[3] < 8:
            for updates in range(math.floor((time.time()-lastrecordedtime) /0.01)):
                if random.randint(1,6500000) == 37:
                    sick = True

        #loop the main loop every 10 miliseconds unless dead
        if not dead:
            player.after(10,loop)
        else:
            imagey1 = deadsprite

        #refresh images
        if lastsprite != imagey1:
            for image5 in player.winfo_children():
                if not isinstance(image5, tk.Toplevel):
                    image5.destroy()
            image_label = tk.Label(player, bg="white",width=width, height=height, image=imagey1)
            image_label.pack()
        
        #rounding values
        hunger = round(hunger,3)
        happy = round(happy,2)
        health = round(health,2)
        energy = round(energy,2)
        weight = round(weight,2)
        
        #cap stats at 100
        if health > 100:
            health = 100
        if hunger > 100:
            hunger = 100
        if energy > 100:
            energy = 100
        if happy > 100:
            happy = 100

        lastsprite = imagey1
        lastrecordedtime = time.time()

    #if right click function
    def right(event):
        #wifi symbol calculation (which symbol to use based off happy)
        wifi = None
        if happy >= 70:
            wifi = wifi1
        elif happy >= 40:
            wifi = wifi2
        elif happy >= 10:
            wifi = wifi3
        else:
            wifi = wifi4

        #make subwindow
        global interface
        interface = tk.Toplevel(player)

        #set variables of subwindow
        interface.title("Tamagotchi DCODE Important Stats.cool")
        dimensions = str(500)  + "x" + str(300)
        global canvas
        canvas = tk.Canvas(interface)
        canvas.pack()
    
        #display name
        text_label = tk.Label(interface,text=f"{name}'s Interface",font=('helvetica','15'))
        text_label.place(x=20,y=0)

        #task manager button for energy
        taskbutton = tk.Button(interface, text="Task Manager", command=taskmanagerfunc)
        taskbutton.place(x=50,y=40)

        #file explorer button for actions
        filebutton = tk.Button(interface, text="File Explorer", command=middle)
        filebutton.place(x=200,y=40)
        
        #images for stats
        image_label = tk.Label(interface, image=harddrive)
        image_label.place(x=50,y=150)
        image_label3 = tk.Label(interface, image=wifi)
        image_label3.place(x=350,y=150)

        #hard drive/weight
        text_label = tk.Label(interface,text=f"{200-weight} GB free of 500 GB")
        text_label.place(x=50,y=100)
    
        #health label
        text_label = tk.Label(interface,text=f"{health} HP Left")
        text_label.place(x=350,y=20)

        #battery/hunger (higher the hunger, the less hungry it is)
        text_label = tk.Label(interface,text=f"{hunger}%")
        text_label.place(x=230,y=100)
        canvas.create_rectangle(165,155,195,165,width=5)
        canvas.create_rectangle(155,165,205,245,width=5)
        canvas.create_rectangle(155,-round(hunger/1.25)+245,205,245,fill = batterycolors[math.floor(hunger/34)])

        #wifi/happy
        text_label = tk.Label(interface,text=f"{round(happy/25,1)} Bars")
        text_label.place(x=370,y=100)
        
        interface.geometry(dimensions + f'+{x}+{y}'.format(x=str(event.x),y=str(event.y)))
        mainwindowidle()
    
    global lastsp
    lastsp = None
    global wifi
    wifi = None

    #rightclick window loop
    def mainwindowidle():
        global lastsp
        lastsp = False
        global wifi
        images = 0

        for image5 in interface.winfo_children():
            if isinstance(image5, tk.Label):
                if image5['image'] != '':
                    images+=1
                
        #wifi symbol calculation (which symbol to use based off happy)
        if happy >= 70:
            if wifi != wifi1:
                wifi = wifi1
                lastsp=True
        elif happy >= 40:
            if wifi != wifi2:
                wifi = wifi2
                lastsp=True
        elif happy >= 20:
            if wifi != wifi3:
                wifi = wifi3
                lastsp=True
        else:
            if wifi != wifi4:
                wifi = wifi4
                lastsp=True
        
        #clear text
        for image5 in interface.winfo_children():
                if isinstance(image5, tk.Label):
                    if image5['image'] == '':
                        image5.destroy()
    
        #display name
        text_label = tk.Label(interface,text=f"{name}'s Interface",font=('helvetica','15'))
        text_label.place(x=20,y=0)

        #task manager button for energy
        taskbutton = tk.Button(interface, text="Task Manager", command=taskmanagerfunc)
        taskbutton.place(x=50,y=40)

        #file explorer button for actions
        filebutton = tk.Button(interface, text="File Explorer", command=middle)
        filebutton.place(x=200,y=40)
        
        #images for stats
        if images <= 0:
            image_label = tk.Label(interface, image=harddrive)
            image_label.place(x=50,y=150)
            image_label3 = tk.Label(interface, image=wifi)
            image_label3.place(x=350,y=150)

        #hard drive/weight
        text_label = tk.Label(interface,text=f"{200-weight} GB free of 200 GB")
        text_label.place(x=50,y=100)

        #health label
        text_label = tk.Label(interface,text=f"{health} HP Left")
        text_label.place(x=350,y=20)

        #battery/hunger (higher the hunger, the less hungry it is)
        text_label = tk.Label(interface,text=f"{hunger}%")
        text_label.place(x=230,y=100)
        canvas.create_rectangle(165,155,195,165,width=5)
        canvas.create_rectangle(155,165,205,245,width=5)
        canvas.create_rectangle(155,-round(hunger/1.25)+245,205,245,fill = batterycolors[math.floor(hunger/34)])

        #wifi/happy
        text_label = tk.Label(interface,text=f"{round(happy/25,1)} Bars")
        text_label.place(x=370,y=100)
    
        #refresh images
        if lastsp:
            for image5 in interface.winfo_children():
                if isinstance(image5, tk.Label):
                    if image5['image'] != '':
                        image5.destroy()
            #clear canvas
            canvas.delete("all")

        dimensions = str(500)  + "x" + str(300)
        interface.geometry(dimensions)
        interface.iconbitmap(path + "\\sprites\\TophappIcon.ico")
        interface.after(1000,mainwindowidle)


    #file explorer fuction
    def middle():
        #make subwindow
        global fileexplore
        try:
            fileexplore = tk.Toplevel(interface)
        except:
            pass

        #set variables of subwindow
        fileexplore.iconbitmap(path + "\\sprites\\TophappIcon.ico")
        fileexplore.title("Tamagotchi DCODE File Explorer.cool")
        dimensions = str(550)  + "x" + str(350)
        
        #files
        playbutton = tk.Button(fileexplore, command= lambda:action("Playing",20,hundeg=20,hapdeg=-30,lbdeg=0.3,hpdeg=-5),image=playfile)
        playbutton.grid()
        playbutton2 = tk.Button(fileexplore, command= lambda:action("Clean Case",10,hapdeg=10,hpdeg=-10),image=cleancasefile)
        playbutton2.grid(column=1,row=0)
        playbutton3 = tk.Button(fileexplore, command= lambda:action("Clean Hard Drive",5,hapdeg=10,lbdeg=0.5,hpdeg=-20),image=cleandrivefile)
        playbutton3.grid(column=2,row=0)
        playbutton4 = tk.Button(fileexplore, command= lambda:action("Take To Doctor",30,hapdeg=30,hpdeg=-60,doc=False),image=doctorfile)
        playbutton4.grid(column=3,row=0)
        playbutton5 = tk.Button(fileexplore, command= lambda:action("Feed Meal",-5,hundeg=-20,lbdeg=-0.2,hpdeg=-5,hapdeg=10),image=mealfile)
        playbutton5.grid(column=4,row=0)
        playbutton6 = tk.Button(fileexplore, command= lambda:action("Feed Treat",-10,hundeg=-10,hapdeg=-20,lbdeg=-0.5,hpdeg=10),image=treatfile)
        playbutton6.grid(column=0,row=1)
        playbutton7 = tk.Button(fileexplore, command= lambda:action("EXTREME GAMING!!!!",40,hundeg=30,hapdeg=-30,hpdeg=5),image=gamefile)
        playbutton7.grid(column=1,row=1)
        playbutton8 = tk.Button(fileexplore, command= lambda:asleepchange(True),image=shutofffile)
        playbutton8.grid(column=2,row=1)
        playbutton9 = tk.Button(fileexplore, command= lambda:asleepchange(False),image=wakefile)
        playbutton9.grid(column=3,row=1)
        playbutton10 = tk.Button(fileexplore, command= lambda:[action("Do Taxes",50,hundeg=20,hapdeg=40,lbdeg=-0.2)],image=taxesfile)
        playbutton10.grid(column=4,row=1)
        playbutton11 = tk.Button(fileexplore, command= lambda:action("TRAINING!!",20,hundeg=20,hapdeg=-20,lbdeg=0.5),image=trainfile)
        playbutton11.grid(column=0,row=2)
        playbutton12 = tk.Button(fileexplore, command= lambda:action("Take a Walk",20,hundeg=20,hapdeg=-15,lbdeg=0.3,hpdeg=-10),image=walkfile)
        playbutton12.grid(column=1,row=2)
        playbutton13 = tk.Button(fileexplore, command= lambda:action("Writing in Word",5,hundeg=5,hapdeg=10,lbdeg=-0.3),image=wordfile)
        playbutton122 = tk.Button(fileexplore, command= load,image=loadfile)
        playbutton122.grid(column=3,row=2)
        playbutton132 = tk.Button(fileexplore, command= save,image=savefile)
        playbutton132.grid(column=4,row=2)
        playbutton13.grid(column=2,row=2)

        fileexplore.geometry(dimensions)

    #action functions
    def asleepchange(value):
        global lastsp
        global asleep
        asleep = value

        for image5 in interface.winfo_children():
                if isinstance(image5, tk.Label):
                    if image5['image'] != '':
                        image5.destroy()
        #clear canvas
        canvas.delete("all")
    
    global game
    game = None
    global done
    done=False
    global actionim1
    global actionim2
    global actionim3
    global actionim4
    global actionim5
    global actionim6
    global actionim7
    global actionim8
    global cyclestrain
    actionim1 = None
    cyclestrain = 0
    actionim2 = None
    actionim3 = None
    actionim4 = None
    actionim5 = None
    actionim6 = None
    actionim7 = None
    global word
    word = ""
    global word2
    word2 = ""
    actionim8 = None
    global countaction
    countaction = 0

    #actions/minigames
    def action(task,value,hundeg=0,hpdeg=0,lbdeg=0,hapdeg=0,doc=None):
        #initialize vars
        global lastsp
        global energy
        global hunger
        global cyclestrain
        global health
        global weight
        global happy
        global game
        global word
        global sick
        global done
        global actionim1
        global actionim2
        global actionim3
        global actionim4
        global actionim5
        global actionim6
        global actionim7
        global actionim8
        global countaction
        global word2

        #if enough energy
        if energy >= value:
            dimensions = str(width)  + "x" + str(height)

            #alll minigames
            if task == "Clean Case":
                if actionim1 == None:
                    done = False
                    game = tk.Toplevel(fileexplore)
                    image_label3 = tk.Label(game, image=imagey1)
                    image_label3.place(x=0,y=0)
                    actionim1 = tk.Button(game,width=2, background="#BBA37B",command=lambda:[actionim1.destroy(),addcount()])
                    actionim1.place(x=random.randrange(1,width-20),y=random.randrange(1,height-20))
                    actionim2 = tk.Button(game,width=2, background="#BBA37B",command=lambda:[actionim2.destroy(),addcount()])
                    actionim2.place(x=random.randrange(1,width-20),y=random.randrange(1,height-20))
                    actionim3 = tk.Button(game,width=2, background="#BBA37B",command=lambda:[actionim3.destroy(),addcount()])
                    actionim3.place(x=random.randrange(1,width-20),y=random.randrange(1,height-20))
                    actionim4 = tk.Button(game,width=2, background="#BBA37B",command=lambda:[actionim4.destroy(),addcount()])
                    actionim4.place(x=random.randrange(1,width-20),y=random.randrange(1,height-20))    
                    game.geometry(dimensions)
                else:
                    if countaction == 4:
                        done = True      

            elif task == "Clean Hard Drive":
                if actionim1 == None:
                    dimensions = str(500)  + "x" + str(300)
                    done = False
                    game = tk.Toplevel(fileexplore)
                    actionim1 = tk.Button(game, image=playfile,command=lambda:[actionim1.destroy(),addcount()])
                    actionim1.place(x=0,y=0)
                    actionim2 = tk.Button(game, image= gamefile,command=lambda:[actionim2.destroy(),addcount()])
                    actionim2.place(x=0,y=70)
                    actionim3 = tk.Button(game, image=walkfile,command=lambda:[actionim3.destroy(),addcount()])
                    actionim3.place(x=0,y=140)
                    actionim4 = tk.Button(game, image=taxesfile,command=lambda:[actionim4.destroy(),addcount()])
                    actionim4.place(x=0,y=210)
                    actionim5 = tk.Button(game, image=trainfile,command=lambda:[actionim5.destroy(),addcount()])
                    actionim5.place(x=70,y=0)
                    actionim6 = tk.Button(game, image=doctorfile,command=lambda:[actionim6.destroy(),addcount()])
                    actionim6.place(x=70,y=70)
                    game.geometry(dimensions)
                else:
                    if countaction == 6:
                        done = True              

            elif task == "Take To Doctor":
                if actionim1 == None:
                    done = False
                    dimensions = str(700)  + "x" + str(700)
                    game = tk.Toplevel(fileexplore)
                    actionim2 = tk.Label(game,wraplength=590,text=random.choice(list(cases)))
                    actionim2.place(x=10,y=10)
                    actionim1 = tk.Button(game,text="Install AntiVirus",command=lambda:[addcount()])
                    actionim1.place(x=530,y=650)
                    actionim3 = tk.Button(game,text="Reboot",command=lambda:[addcount(),addcount()])
                    actionim3.place(x=430,y=650)
                    actionim4 = tk.Button(game,text="Replace Parts",command=lambda:[addcount(),addcount(),addcount()])
                    actionim4.place(x=330,y=650)
                    game.geometry(dimensions)
                else:
                    try:
                        actionim1.destroy()
                        actionim3.destroy()
                        actionim4.destroy()
                        actionim1 = tk.Button(game,text="Install AntiVirus",command=lambda:[addcount()])
                        actionim1.place(x=530,y=650)
                        actionim3 = tk.Button(game,text="Reboot",command=lambda:[addcount(),addcount()])
                        actionim3.place(x=430,y=650)
                        actionim4 = tk.Button(game,text="Replace Parts",command=lambda:[addcount(),addcount(),addcount()])
                        actionim4.place(x=330,y=650)

                        if countaction == 1:
                            if cases[actionim2["text"]] == 1:
                                done = True   
                            else:
                                actionim2.destroy()
                                actionim2 = tk.Label(game,wraplength=590,text=random.choice(list(cases)))
                                actionim2.place(x=10,y=10)
                        elif countaction == 2:
                            if cases[actionim2["text"]] == 2:
                                done = True   
                            else:
                                actionim2.destroy()
                                actionim2 = tk.Label(game,wraplength=590,text=random.choice(list(cases)))
                                actionim2.place(x=10,y=10)
                        elif countaction >= 3:
                            if cases[actionim2["text"]] == 3:
                                done = True   
                            else:
                                actionim2.destroy()
                                actionim2 = tk.Label(game,wraplength=590,text=random.choice(list(cases)))
                                actionim2.place(x=10,y=10)
                    except:
                        pass

            elif task == "Feed Meal":
                if actionim1 == None:
                    done = False
                    game = tk.Toplevel(fileexplore)
                    actionim1 = tk.Button(game,width=2, background="#E2DAC9",command=lambda:[actionim1.destroy(),addcount()])
                    actionim1.place(x=60,y=60)
                    actionim2 = tk.Button(game,width=2, background="#E2DAC9",command=lambda:[actionim2.destroy(),addcount()])
                    actionim2.place(x=80,y=60)
                    actionim3 = tk.Button(game,width=2, background="#E2DAC9",command=lambda:[actionim3.destroy(),addcount()])
                    actionim3.place(x=100,y=70)
                    actionim4 = tk.Button(game,width=2, background="#E2DAC9",command=lambda:[actionim4.destroy(),addcount()])
                    actionim4.place(x=100,y=50)    
                    actionim5 = tk.Button(game,width=2, background="#CB6004",command=lambda:[actionim5.destroy(),addcount()])
                    actionim5.place(x=50,y=50)
                    actionim6 = tk.Button(game,width=2, background="#CB6004",command=lambda:[actionim6.destroy(),addcount()])
                    actionim6.place(x=70,y=50)
                    actionim7 = tk.Button(game,width=2, background="#CB6004",command=lambda:[actionim7.destroy(),addcount()])
                    actionim7.place(x=50,y=70)
                    actionim8 = tk.Button(game,width=2, background="#CB6004",command=lambda:[actionim8.destroy(),addcount()])
                    actionim8.place(x=70,y=70)    
                    game.geometry(dimensions)
                else:
                    if countaction == 8:
                        done = True      
            
            elif task == "Feed Treat":
                if actionim1 == None:
                    done = False
                    game = tk.Toplevel(fileexplore)
                    actionim1 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim1.destroy(),addcount()])
                    actionim1.place(x=40,y=40)
                    actionim2 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim2.destroy(),addcount()])
                    actionim2.place(x=60,y=40)
                    actionim3 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim3.destroy(),addcount()])
                    actionim3.place(x=80,y=40)
                    actionim4 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim4.destroy(),addcount()])
                    actionim4.place(x=40,y=60)    
                    actionim5 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim5.destroy(),addcount()])
                    actionim5.place(x=80,y=60)
                    actionim6 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim6.destroy(),addcount()])
                    actionim6.place(x=40,y=80)
                    actionim7 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim7.destroy(),addcount()])
                    actionim7.place(x=60,y=80)
                    actionim8 = tk.Button(game,width=2, background="#AA7733",command=lambda:[actionim8.destroy(),addcount()])
                    actionim8.place(x=80,y=80)    
                    game.geometry(dimensions)
                else:
                    if countaction == 8:
                        done = True      

            elif task == "EXTREME GAMING!!!!":
                if actionim1 == None:
                    done = False
                    game = tk.Toplevel(fileexplore)
                    actionim1 = tk.Button(game,width=4, background="#FF0000",command=lambda:[actionim1.destroy(),addcount()],height=2)
                    actionim1.place(x=random.randrange(1,width-20),y=random.randrange(1,height-20))
                    game.geometry(dimensions)
                else:
                    try:
                        actionim1.destroy()
                        actionim1 = tk.Button(game,width=4,height=2, background="#FF0000",command=lambda:[actionim1.destroy(),addcount()])
                        actionim1.place(x=random.randrange(1,width-20),y=random.randrange(1,height-20))
                        if countaction >= 5:
                            done = True      
                    except:
                        pass
            
            elif task == "Playing":
                if actionim1 == None:

                    done = False
                    game = tk.Toplevel(fileexplore)
                    actionim1 = tk.Button(game,width=2, background="#FF0000",command=lambda:[actionim1.destroy(),addcount()])
                    actionim1.place(x=width/2,y=height/2)
                    game.geometry(dimensions)
                else:
                    try:
                        game.configure(background=random.choice(["red","green","purple2","gold"]))
                        if countaction >= 1:
                            actionim1.destroy()
                            actionim1 = tk.Button(game,width=2, background="#FF0000",command=lambda:[actionim1.destroy(),addcount()])
                            actionim1.place(x=random.randrange(1,width-20),y=random.randrange(1,height-20))
                            countaction = 0
                            if game['bg'] == "gold":
                                done = True      
                    except:
                        pass

            elif task == "Do Taxes":
                if actionim1 == None:
                    done = False
                    dimensions = str(700)  + "x" + str(700)
                    game = tk.Toplevel(fileexplore)
                    actionim2 = tk.Label(game,wraplength=590,text=random.choice(taxes))
                    actionim2.place(x=10,y=10)
                    actionim1 = tk.Button(game,text="Sign",width = 20,command=lambda:[actionim2.destroy(),addcount()])
                    actionim1.place(x=530,y=650)
                    game.geometry(dimensions)
                else:
                    try:
                        actionim1.destroy()
                        if not actionim2.winfo_exists():
                            actionim2 = tk.Label(game,wraplength=590,text=random.choice(taxes))
                            actionim2.place(x=10,y=10)
                        actionim1 = tk.Button(game,text="Sign",width = 20,command=lambda:[actionim2.destroy(),addcount()])
                        actionim1.place(x=530,y=650)
                        if countaction >= 30:
                            done = True   
                    except:
                        pass
            
            elif task == "TRAINING!!":
                if actionim1 == None:
                    cyclestrain = 0
                    dimensions = str(500)  + "x" + str(200)
                    done = False
                    game = tk.Toplevel(fileexplore)
                    actionim1 = tk.Label(game,width=2, background="#00FF00")
                    actionim1.place(x=countaction*10,y=50)
                    actionim2 = tk.Label(game,width=2, background="#FF0000")
                    actionim2.place(x=actionim2.winfo_x()+20,y=100)
                    game.geometry(dimensions)
                    actionim3 = tk.Button(game,text="RUN!",command=addcount)
                    actionim3.place(x=0,y=0)
                else:
                    try:
                        cyclestrain+=1
                        actionim1.destroy()
                        actionim2.destroy()
                        actionim1 = tk.Label(game,width=2, background="#00FF00")
                        actionim1.place(x=countaction*10,y=50)
                        actionim2 = tk.Label(game,width=2, background="#FF0000")
                        actionim2.place(x=cyclestrain*15,y=100)

                        if countaction*10 >=500:
                            done=True
                        if cyclestrain*18 >=500:
                            countaction = 0
                            actionim2.destroy()
                            cyclestrain =0

                    except:
                        pass
            
            elif task == "Take a Walk":
                if actionim1 == None:
                    cyclestrain = 0
                    dimensions = str(550)  + "x" + str(550)
                    done = False
                    game = tk.Toplevel(fileexplore)
                    actionim3 = tk.Label(game,text="Take 15 Seconds to Relax on a Bench with your Tech-Pet™, Dont try to escape, its meditation time")
                    actionim3.place(x=0,y=0)
                    actionim1 = tk.Button(game,text="Listen to the Rain",command=lambda:[actionim1.destroy(),addcount()])
                    actionim1.place(x=0,y=20)
                    game.geometry(dimensions)
                    actionim6 = tk.Label(game,image=bench)
                    actionim6.place(x=width/2-20,y=height/2+100)
                    actionim2 = tk.Label(game,image=walk1)
                    actionim2.place(x=width/2,y=height/2)
                    actionim4 = tk.Label(game,bg="green",width =100,height=100)
                    actionim4.place(x=0,y=height/2+250)
                else:
                    if countaction >= 1:
                        winsound.PlaySound(path + "\\sprites\\rainsounds.wav", winsound.SND_FILENAME)
                        game.after(15000,doneupdate)

            elif task == "Writing in Word":
                if actionim1 == None:
                    word = ""
                    word2 = ""
                    for letter in range(1,20):
                        word2+=random.choice(["A","B","C","D","E","F"])
                    dimensions = str(500)  + "x" + str(500)
                    done = False
                    game = tk.Toplevel(fileexplore)
                    game.geometry(dimensions)
                    actionim1 = tk.Button(game,text="A",command=lambda: addletter("A"),width=2)
                    actionim1.grid(row=0,column=0)
                    actionim2 = tk.Button(game,text="B",command=lambda: addletter("B"),width=2)
                    actionim2.grid(row=0,column=1)
                    actionim3 = tk.Button(game,text="C",command=lambda: addletter("C"),width=2)
                    actionim3.grid(row=0,column=2)
                    actionim4 = tk.Button(game,text="D",command=lambda: addletter("D"),width=2)
                    actionim4.grid(row=0,column=3)
                    actionim5 = tk.Button(game,text="E",command=lambda: addletter("E"),width=2)
                    actionim5.grid(row=0,column=4)
                    actionim6 = tk.Button(game,text="F",command=lambda: addletter("F"),width=2)
                    actionim6.grid(row=0,column=5)
                    actionim7 = tk.Button(game,text="Enter",command=lambda: addcount(),width=5)
                    actionim7.place(x=0,y=30)
                    actionim8 = tk.Label(game,text=word2 + "\n"+word)
                    actionim8.place(x=20,y=100)
                else:
                    try:
                        actionim8.destroy()
                        actionim8 = tk.Label(game,text=word2 + "\n"+word)
                        actionim8.place(x=20,y=100)
                        if countaction >= 1:
                            if word == word2:
                                word = ""
                                word2 = ""
                                done=True
                            else:
                                word = ""
                                countaction = 0
                    except:
                        pass

            #when closing window by force
            game.protocol("WM_DELETE_WINDOW", closegame)
            
            #if done and a normal action
            if abs(value) == value and done:
                done = False
                actionim1 = None
                actionim2 = None
                actionim3 = None
                actionim4 = None
                actionim5 = None
                actionim6 = None
                actionim7 = None
                actionim8 = None    
                game.destroy()
                countaction = 0
                for image5 in interface.winfo_children():
                    if isinstance(image5, tk.Label):
                        if image5['image'] != '':
                            image5.destroy()
                #clear canvas
                canvas.delete("all")
                if not asleep:
                    tasks[task] = value
                    energy -= value
                    hunger -= hundeg
                    health -= hpdeg
                    happy -= hapdeg
                    weight -= lbdeg
                    if doc != None:
                        sick = doc
                else:
                    messagebox.showinfo("Alert", "Your Pet is Simply Far Too Tired to Preform This Task")
            #if food action
            elif not hunger + abs(hundeg) > 100 and done:
                done = False
                actionim1 = None
                actionim2 = None
                actionim3 = None
                actionim4 = None
                actionim5 = None
                actionim6 = None
                actionim7 = None
                actionim8 = None   
                for image5 in interface.winfo_children():
                    if isinstance(image5, tk.Label):
                        if image5['image'] != '':
                            image5.destroy()
                #clear canvas
                canvas.delete("all") 
                tasks[task] = value
                energy -= value
                hunger -= hundeg
                health -= hpdeg
                happy -= hapdeg
                weight -= lbdeg
                countaction = 0
                game.destroy()
            
            #if too full for food
            elif done:
                for image5 in interface.winfo_children():
                    if isinstance(image5, tk.Label):
                        if image5['image'] != '':
                            image5.destroy()
                #clear canvas
                canvas.delete("all")
                actionim1 = None
                actionim2 = None
                actionim3 = None
                actionim4 = None
                actionim5 = None
                actionim6 = None
                actionim7 = None
                actionim8 = None    
                done = False
                countaction = 0
                game.destroy()
                messagebox.showinfo("Alert", "Your pet is too full")

            elif not done:
                #loop
                game.after(300,action,task,value,hundeg,hpdeg,lbdeg,hapdeg,doc)

        else:
            messagebox.showinfo("Alert", "Your Pet is Simply Far Too Tired to Preform This Task")
    
    #when close function
    def closegame():
        global actionim1
        global actionim2
        global actionim3
        global actionim4
        global actionim5
        global actionim6
        global actionim7
        global actionim8
        global countaction
        global game
        game.destroy()
        countaction = 0
        actionim1 = None
        actionim2 = None
        actionim3 = None
        actionim4 = None
        actionim5 = None
        actionim6 = None
        actionim7 = None
        actionim8 = None  
        game = None
        
    def addcount():
        global countaction
        countaction +=1

    def addletter(letter):
        global word
        word += letter
    
    def doneupdate():
        global done
        done = True

    #save and load
    def save():
        #open file
        file = open(path + "\\Data\\data.txt","w")

        #write data to file
        file.write(f"{playerdata}")

        #close file
        file.close()
    
    def load():
        #decleare variables
        global loaded
        global playerdata

        #open file
        file = open(path + "\\Data\\data.txt","r")
        try:
            #read file
            data =file.read()
        except:
            data = ""

        #if empty file
        if data !="":
            try:
                #set contents of file to playerdata
                playerdata = eval(data)
                loaded = True
            except:
                messagebox.showinfo("Alert", f"Incorrect File Contents: {data}")
        else:
            messagebox.showinfo("Alert", "No Save Data")
            
        #close file
        file.close()

    #task manager function
    def taskmanagerfunc():
        #make subwindow
        global taskmgr
        taskmgr = tk.Toplevel(interface)

        #set variables of subwindow
        taskmgr.title("Tamagotchi DCODE Task Manager.cool")
        dimensions = str(500)  + "x" + str(300)
        
        #start loop
        taskmgr.geometry(dimensions)
        taskmanageridle()

    #task manager loop
    def taskmanageridle():
        #tasks        
        for image5 in taskmgr.winfo_children():
            if isinstance(image5, tk.Label):
                        image5.destroy()
        textlabel = tk.Label(taskmgr,text=f"                                                 {energy}% Total" if len(list(tasks)) ==0 else f"{energy}% Total",font=('helvetica','15'))
        textlabel.place(x=20,y=20)
        for task, percent in tasks.items():
            textlabel = tk.Label(taskmgr,text=f"{task}                    {-percent}%",font=('helvetica','15'))
            textlabel.place(x=20,y=60+(50*list(tasks).index(task)))
        
        if len(tasks) < 1:
            textlabel2 = tk.Label(taskmgr,text=f"No Tasks Currently",font=('helvetica','20'))
            textlabel2.place(x=20,y=20)

        taskmgr.iconbitmap(path + "\\sprites\\TophappIcon.ico")
        taskmgr.after(1000,taskmanageridle)

    #die function
    def die():
        print("Your Pet Has Died")
        global dead
        global imagey1
        imagey1 =deadsprite
        messagebox.showinfo("Alert", "Your Pet Died, Look at the Consolde")
        print("""What have you done.  This helpless being has been slayed because of your ignorance.  Your inability to keep even a computer program alive for more than a few days is dissapointing.  Your excuses are meaningless, simply desprate attempts to deny the blunt murder.  You were given the life of a being beyond your comprehension and you threw it away, letting it rot in an endless sea of regret and pain.  This creature's death was entirely in your hands.  It can't die without neglagence.  Old age and desease don't exist in this digitized world, you are the sole hand responislbe for this outright atrocity.  You disgust me with your pure and unbridled neglagence for life, your lack of care for a living, breathing entity.  You have failed.""")
        print("You May Now Close The Console")
        dead = True

    #mouse click detection
    player.bind("<Button-3>", right)

    #start tkinter mainloop(updates) and start loop function looping
    loop()
    player.mainloop()
    if interface != None:
        interface.mainloop()

#call main function
if __name__ == "__main__":
    main()

#shrine to housefire of 3/20/2025 (not my house but a neighbor's)
