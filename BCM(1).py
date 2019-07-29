import random
print("The adventures of Broughtly in Crultney Mansion")
loc = 1
coins = 8
eqlist = list()
dlist = list()
ulist = list()
swicob = "0"
ask = "A"
alert = 0
observe = 1
ncode = 0
fcode = random.randint(0, 999)
screen = [4, 4] #SN
candlelist = ["", "", ""]
lcandlelist = [0, 0, 0] #NCS
loclog = list()
bathwater = [0, 3] #lever, water (water on = 2)
stairrobot = 1
wunlock = 0
craneunlock = 0
towerpos = "G"
towertext = "Your weapon successfully destroys the door and you walk in."
islandtext = "The island is small and the main feature is the mansion which looks majestic and intimidating. You can see a barbed wire fence surrounding this side of the mansion."
def inap():
    print("The item you have chosen is not appropriate for the current situation.")
def equip():
    print("You possess ", eqlist,)     
def destroy(n):
    dlist.append(n)
    x = 0
    while n in eqlist:
        if eqlist[x] == n:
            del eqlist[x]
        x = x + 1
def udestroy(n):
    ulist.append(n)
    destroy(n)
def poswheel(n): #S=0, N=1
    poslist = ["top", "right", "down", "left"]
    if n == 3:
        return poslist[2*stairrobot]
    else:
        return poslist[screen[n]-1]
def lastloc():
    oriid = len(loclog) - 2
    return loclog[oriid]
def findconnect(a):
    conreport = list()
    for i in range(len(loclog)):
        if loclog[i] == a:
            conreport.append(loclog[i-1])
    return conreport
def crystal():
    print("You reach for the crystal and observe that it is a rombohedron with one face being marked with a symbol in each corner.")
    print("In clockwise order, starting with the pentagon, these are a pentagon (P), a triangle (T), a square (S) and a hexagon (H)")
    print("Do you point the crystal at the target and strike one of the symbols (S) or do you throw the crystal at the target (T).")
    choice = str(input())
    if choice == "S":
        strike = str(input("Which symbol do you strike?  (P/T/S/H) "))
        if strike == "H":
            print("The crystal releases a beam which strikes your target.") 
            destroy("energy crystal (EC)")
            return "success"
        else:
            return "failure"
    else:
        if random.randint(1, 4) == 4:
            print("The crystal strikes the target and releases a beam of energy which incinerates you.")
            return "big failure"
        else:
            print("The crystal bounces off the target without releasing a beam of energy.")
            return "failure"
def candle(n):
    if "green candle" in eqlist or "red candle" in eqlist or "blue candle" in eqlist or len(candlelist[n]) > 3:
        scs = "You may place a candle from your inventory into the holder (P). "
        if len(candlelist[n]) > 3:
            scs = "You may retrieve the ", candlelist[n], "from the candle holder (R). "
            if "matches" in eqlist:
                print("You may use the matches in your possesion to light the ", candlelist[n], " in the candle holder (L).")
        print(scs, " or you may discontinue your investigation of the candle holder (D).")
        return 1
    else:
        print("You notice nothing unusual about the candle holder.")    
        return 0                        
def endgame(n):
    print("You have failed in your mission.")
    print("You collected: ", eqlist+dlist)
    endtext = ["You failed to even reach the island that Crultney lives on.", "You reached Crultney's island but were unable to gain access to the mansion.", "You entered the mansion but were unable to complete your mission."]
    print(endtext[n])
    end = input() 
def listweapons():
    print("You can attempt to use any of the folllowing: ", eqlist)
def screencheck(a, d, p):  #p=1 if N, p=0 if S, d = direction, a = desired location
    if d == screen[p]:
        return 54
    else:
        return a
while  True:
    if loc == 1:
        print("The date is 8th October 1971 and Crultney, a famous architect and inventor has not been seen or heard from for several weeks. You are Broughtly, a skilled monkey ninja and your mission is to travel to his mansion and investigate. You should be aware that there are many traps and hidden rooms in the mansion.")
        print("You now have a choice of where to go to get supplies or the mission")
        print("You can go to the Ninja Armoury (N), Royal Weaponary Supply Company (R) or Geelophisis' Lab (G)")
        choice = str(input())
        if choice == "N":
            loc = 2
        elif choice == "R":
            loc = 3
        elif choice == "G":
            loc = 4
        else:
            loc = 999
    elif loc == 2:
        print("You have arrived at the Ninja Armoury. A monkey wearing white robes walks in and offers you the black dagger, a powerful weapon which is the symbol of the ninjas of Oland.")
        print("He also shows you a wooden table with an assortment of objects on it and tells you that you may choose two of them")
        print("You can choose from the throwing stars (T), invisibility potion (I), golden blade, (G), time bomb (B) or super strong rope (S)")
        choice1 = str(input("choice 1   "))
        choice2 = str(input("choice 2   "))
        eqlist.append("black dagger (BD)")
        if choice1 == "T" or choice2 == "T":
            eqlist.append("throwing stars (TS)")
        if choice1 == "I" or choice2 == "I":
            eqlist.append("invisibility potion (IP)")
        if choice1 == "G" or choice2 == "G":
            eqlist.append("golden blade (GB)")
        if choice1 == "B" or choice2== "B":
            eqlist.append("time bomb (TB)")
        if choice1 == "S" or choice2 == "S":
            eqlist.append("super strong rope (SSR)")
        loc = 5
    elif loc == 3:
        print("The chairmonkey of the Royal Weaponary Supply Company welcomes you into his office and tells you that you may use any of his equipment so long as you can pay for it.")
        print("You have 8 banana coins to spend")
        print("The available items are a shortsword (SS, 2 coins), the shield of safety (SOS, 3 coins), a strength potion (SP, 3 coins), the warhammer (WH, 4 coins), the golden blade (GB, 5 coins) and the portable cannon (PC, 6 coins).")
        while choice != "E":
            choice = str(input("Type in an item code or type E to exit the office.   "))
            if choice == "SS":
                eqlist.append("shortsword (SS)")
                coins = coins - 2
            elif choice == "SOS":
                eqlist.append("shield of safety (SOS)")
                coins = coins - 3
            elif choice == "SP":
                eqlist.append("strength potion (SP)")
                coins = coins - 3
            elif choice  == "WH":
                eqlist.append("warhammer (WH)")
                coins = coins - 4
            elif choice == "GB":
                eqlist.append("golden blade (GB)")
                coins = coins - 5
            elif choice == "PC":
                eqlist.append("portable cannon (PC)")
                coins = coins - 6
            if coins < 0:
                print("You could not afford that item.")
                del eqlist[len(eqlist) - 1]
                coins = 0
        loc = 5
    elif loc == 4:
        print("Geelophisis welcomes you into his lab but warns you that he has not invented many new items since your mission with the Robo Lion in 1963")
        print("Geelophisis first gives you a stone rod 300 mm long with symbols protruding from it at regular intervals along it. This was given to him by Crultney and which he believes willbe useful on your mission.")
        eqlist.append("stone rod")
        print("He shows you his inventions and says that you can choose two of them.")
        print("You can ask Geelophisis about an invention by typing the item code when prompted. Type NO to proceed without asking.")
        print("The inventions are: complex brain destroyer (CBD), invisibility potion (IP), magical map (MM), strength potion (SP) and the energy crystal (EC)")
        while ask != "NO":
            ask = str(input("Do you want to ask Geelophisis about an invention?   "))
            if ask == "CBD":
                print("Geelophisis tells you that the current version of the CBD is much safer than the prototype used in the 1960s. He says that it should only be used on intelligent opponents with larger brains as this makes it easier for the CBD to identify them.")
            elif ask == "IP":
                print("Geelophisis tells you that this is the standard invisibility potion used by the ninjas in Oland and it makes the user invisible for 2 minutes.")
            elif ask == "SP":
                print("Geelophisis tells you that this invention grants a sudden burst of extreme strength to the user for a short period of time.")
            elif ask == "MM":
                print("Geelophisis tells you that this invention will allow you to find your way to any place.")
            elif ask == "EC":
                print("Geelophisis tells you that the energy crystal is a highly dangerous weapon that will release a blast of energy from the end of the crystal marked with a triangle when the end marked with a hexagon is struck. It can only be used once as the crystal is consumed on use.")
        choice1 = str(input("choice 1   "))
        choice2 = str(input("choice 2   "))
        if choice1 == "CBD" or choice2 == "CBD":
            eqlist.append("complex brain destroyer (CBD)")
        if choice1 == "IP" or choice2 == "IP":
            eqlist.append("invisibility potion (IP)")
        if choice1 == "SP" or choice2 == "SP":
            eqlist.append("strength potion (SP)")
        if choice1 == "MM" or choice2== "MM":
            eqlist.append("magical map (MM)")
        if choice1 == "EC" or choice2 == "EC":
            eqlist.append("energy crystal (EC)")
        print("You were just about to leave when Geelophisis offers to give you some advice for the mission.")
        print("Type 'S' if you stay to listen to his advice or type 'P' if you go straight to the port.")
        choice = str(input())
        if choice == "S":
            loc = 6
        else:
            loc = 7
    elif loc == 5:
        print("Would you like to attend the ninja strategy meeting to discuss the mission before you leave or would you rather seek advice from other sources?")
        print("Type 'M' to attend the meeting, type 'G' to seek advice from Geelophisis, type 'F' to seek advice from Furfoot or type 'L' to leave without seeking advice.")
        choice = str(input())
        if choice == "M":
            loc = 8
        elif choice == "G":
            loc = 6
        elif choice == "F":
            loc = 9
        elif choice == "L":
            loc = 7
    elif loc == 6:
        print("Geelophisis tells you that Crultney Mansion is 3 storeys high and also has a set of underground rooms. He tells you that the easiest way to access the island is by first travelling to Ooville and then departing for the island in a smaller vessel. He warns you also that Crultney is paranoid and will have made it difficult to gain access to his mansion.")
        print("Geelophisis also offers for you to travel in his helicopter to the mansion if you do not want to follow this advice. However, Geelophisis is a very busy monkey at the moment so you would have to fly the helicopter yourself.")
        choice = str(input("Type 'H' if you travel in the helicopter or type 'P' if you go to the port to find the ship to Ooville.   "))
        if choice == "H":
            loc = 10
        elif choice == "P":
            loc = 7
    elif loc == 7:
        print("You arrive at the port and see many ships which you could use to get to Crultney Mansion.")
        print("You could travel for free on the ship to Ooville (O) or you could travel for 2 banana coins on a boat going directly to Crultney's Island (C).")
        print("You have ", coins, "banana coins")
        if "magical map (MM)" in eqlist:
            print("You may also consult the magical map (MM).")
        choice = str(input())
        if choice == "O":
            loc = 11
        elif choice == "C":
            coins = coins - 2
            loc = 12
        elif choice == "MM" and "magical map (MM)" in eqlist:
            print("The magical map appears to suggest that the wisest course of action would be to take the ship to Ooville.")
    elif loc == 8:
        print("The ninja leaders tell you that there will likely be many robots in Crultney Mansion and these will be difficult to fight with conventional ninja weapons. Therefore they advise you to visit the Gaurilis army base in Ooville in order to obtain more suitable weapons.")
        print("You now travel to the port.")
        loc = 7
    elif loc == 9:
        print("You arrive at Furfoot's Palace but he tells you that he does not have much advice to give you. However, he can tell you that Crultney's main living and work areas are on the second floor of the mansion.")
        print("After the meeting with Furfoot, you find a banana coin on the ground near the palace and you put this in your pocket.")
        coins = coins + 1
        print("You now travel to the port.")
        loc = 7
    elif loc == 10:
        print("After travelling for a great length of time over the sea, you can see the island of Ooville.")
        print("You could land the helicopter in Ooville (O) or travel South to try to find Crultney's Island(C).")
        choice = str(input())
        if choice == "O":
            loc = 19
        elif choice == "C":
            loc = 13
    elif loc == 11:
        print("You arrive in Ooville and you go to the town centre. You may now try to find a ship going to Crultney Island (C) or you could go to the nearby Gaurilis army base (G) or to the local shops (S).")
        choice = str(input())
        if choice == "C":
            loc = 14
        elif choice == "G":
            loc = 15
        elif choice == "S":
            loc = 16
    elif loc == 12:
        print("The monkey takes your banana coins and you depart from the port. However, you soon enter stormy weather. You could go into the port at Ooville to seek shelter for the duration of the storm (O) or you could continue your journey (C).")
        choice = str(input())
        if choice == "O":
            print("You arrive in Ooville and wait for the storm to end. Eventually it does and you are able to go out in the ship to Crultney Island.")
            loc = 17
        elif choice =="C":
            loc = 18
    elif loc == 13:
        print("As you approach the island, you can see the majestic mansion in front of you. Suddenly, a loud siren sounds from the mansion. You could try to land near the mansion (M) or fly back towards Ooville (O).")
        alert = alert + 1
        choice = str(input())
        if choice == "M":
            loc = 20
        elif choice == "O":
            loc = 19
    elif loc == 14:
        print("There is a ferry which will take you to the island for 1 banana coin (F) or there is a small rowing boat which is free (R). You could also return to the town centre (T).")
        print("You have ", coins, "banana coins.")
        choice = str(input())
        if choice == "F":
            coins = coins - 1
            print("The monkey operating the ferry takes your coin and delivers you to the island.")
            loc = 17
        elif choice == "R":
            loc = 22
        elif choice == "T":
            loc = 11
    elif loc == 15:
        if "sticky banana bomb (SBB)" not in eqlist and "sticky banana bomb (SBB)" not in dlist and "medical kit (MK)" not in eqlist and "medical kit (MK)" not in dlist:
            print("The gorillas welcome you into their base and give you the choice of either a sticky banana bomb (SBB) or a medical kit (MK) to use on your mission. They tell you to take a rowing boat to the island as this is cheaper than the ferry.")
            choice = str(input())
            if choice == "SBB":
                eqlist.append("sticky banana bomb (SBB)")
            elif choice == "MK":
                eqlist.append("medical kit (MK)")
            print("You return to the town centre.")
        else:
            print("The gorillas tell you that they will be unable to help you any further so you leave the base.")
        loc = 11
    elif loc == 16:
        print("You see many local shops selling a wide range of products.")
        if "golden blade (GB)" in eqlist:
            print("Before you have a chance to enter the shops, a monkey walks up to you and offers you 11 banana coins for your golden blade.")
            print("Do you accept the offer")
            choice = str(input())
            if choice == "YES":
                destroy("golden blade (GB)")
                coins = coins + 11
        print("You enter the shops and you find some super strong rope (S) costing 3 coins and the helm of horror (H) which costs 6 coins")
        print("You have ", coins, "banana coins.")
        while choice != "E":
            choice = str(input("Type in an item code or type E to exit the shop.   "))
            if choice == "S":
                eqlist.append("super strong rope (SSR)")
                coins = coins - 3
            elif choice == "H":
                eqlist.append("helm of horror (HOH)")
                coins = coins - 6
        print("You now return to the town centre.")
        loc = 11
    elif loc == 17:
        print(islandtext)
        print("You are approaching the island from the South and you can see a small pier directly ahead of you (P) and a sandy beach to the East (B). Alternatively, you could circle around the island to the North side (N).")
        if "magical map (MM)" in eqlist:
            print("You may also consult the magical map (MM).")
        choice = str(input())
        if choice == "P":
            loc = 24
        elif choice == "B":
            loc = 23
            print("You disembark from the boat and climb out onto the beach.")
        elif choice == "N":
            loc = 21
        elif choice == "MM" and "magical map (MM)" in eqlist:
            print("The magical map appears to suggest that circling around to the North would be the most direct way to gain access to the mansion.")
    elif loc == 18:
        print("You carry on through the stormy weather but some of your equipment is washed overboard by the waves.")
        text6 = random.choice(eqlist)
        print(text6, " is lost")
        destroy(text6)
        print("The storm has now ended and you continue on towards the island. ", islandtext)
        loc = 17
    elif loc == 19:
        print("You land at the airport in Ooville Town and arrange for a local pilot to return the helicopter to Geelophisis.")
        loc = 11
    elif loc == 20:
        print("You attempt to land the helicopter but you notice an arcane looking device on the 2nd floor turning to face you. You suddenly lose control of the helicopter and it crashes near the mansion.")
        print("You scramble out from the wreckage of the helicopter and notice that some of your equipment has beeen destroyed in the collision.")
        text7 = random.choice(eqlist)
        print(text7, " is lost")
        destroy(text7)
        alert = alert + 1
        loc = 27
    elif loc == 21:
        print("On the North side of the mansion, there is a tower 3 storeys high with a large window on the ground floor looking out to Sea. To the East and West of the mansion, there are steep cliffs which would be impossible to land on.")
        print("You can break the window using a weapon (W) or turn back to the South side of the island (S).")
        if "super strong rope (SSR)" in eqlist:
            print("Since you have a super strong rope in your possesion, you may also attempt to climb the cliff using this item (R).")
        choice = str(input())
        if choice == "W":
            listweapons()
            choice = str(input())
            if choice == "BD" or choice == "GB" or choice == "WH":
                print("The window shatters and an alarm sounds. You enter the room.")
                alert = alert + 1
                loc = 26
            elif choice == "SS":
                print("The window shatters and an alarm sounds. Unfortunately, the reinforced glass of the window has broken your shortsword. You enter the room.")
                alert = alert + 1
                destroy("short sword (SS)")
                loc = 26
            elif choice == "TS":
                print("Unfortunately, the glass of this window is reinforced so the throwing stars bounce off and fall into the sea.")
                destroy("throwing stars (TS)")
            elif choice == "TB":
                print("You place the bomb and duck back down into the boat. A few seconds later, a loud explosion occurs and an alarm sounds nside the mansion. You walk into the room through the large hole that has beeen created in the window.")
                destroy("time bomb (TB)")
                alert= alert + 1
                loc = 26
            elif choice == "PC":
                loc = 26
                print("You load the cannon and fire at the window. The window shatters and an alarm sounds. You enter the room.")
            elif choice == "EC":
                crystsample = crystal()
                if  crystsample == "success":
                    print("The window is incinerated and an alarm sounds. You enter the room.")
                    loc = 26
                elif crystsample == "failure":
                    destroy("energy crystal (EC)")
                    print("After the improper use, the crystal falls into the sea.")
                elif crystsample == "big failure":
                    endgame(1)
            elif choice == "CBD":
                inap()
            elif choice == "SBB":
                print("You pull the bomb out of your pocket and place it near the window but it explodes before you can take cover.")
                print("The window shatters and an alarm sounds. Unfortunately you are injured by the bomb and the broken glass.")
                if "medical kit (MK)" in eqlist:
                    print("Since you have a medical kit, you use it and after recovering, you enter the room.")
                    destroy("medical kit (MK)")
                    loc = 26
                else:
                    print("Your injuries are too great to continue. You return to Ooville and Crultney is never seen again.")
                    endgame(1)
            else:
                inap()
        elif choice == "S":
            loc = 17
        elif choice == "R":
            print("Do you climb the cliffs to the West (W) or the East (E)?")
            choice = str(input())
            print("You create a loop in the rope and throw it so that it wraps around a large stone at the top of the cliff.")
            print("You succeed in climbing the cliff and you retrieve the rope.")
            if choice == "W":
                Print("There are no doors on the Western side of the mansion and the walls are too high to climb. Using your rope,you climb over a steep rock formation to arrive near the front of the mansion.")
                loc = 24
            elif choice == "E":
                loc = 25
    elif loc == 22:
        print("You row the boat towards the island and the voyage seems to be going well. Suddenly, a Gaurilis submarine surfaces nearby.")
        print("The gorillas are displeased with your presence interrupting their naval excersise so they demand payment of 3 banana coins for you to continue your voyage (P) and otherwise you must return to Ooville (O).")
        print("You have ", coins, " banana coins.")
        print("You can also pay using equipment (E) or try to fight the gorillas (F).")
        if "medical kit (MK)" in eqlist or "sticky banana bomb (SBB)" in eqlist:
             print("Since you posess a Gorilla made item, you can show this to the gorillas (S) to convince them that you are friendly.")
        choice = str(input())
        if choice == "P":
            coins = coins - 3
            print("The gorillas allow you to continue your journey.")
            loc = 17
        elif choice == "O":
            loc = 11
        elif choice == "E":
            print(eqlist)
            print("Enter the position on the list for the item to be sacrificed.")
            kkjj = int(input())
            print(eqlist[kkjj], " was given to the gorillas. They allow you to continue your journey.")
            destroy(eqlist[kkjj])
            loc = 17
        elif choice == "F":
            print("The gorillas overwhelm you and detain you. They take you to be questioned at their base in Gorillia Monkeyland. Your mission is over.")
            endgame(0)
        elif choice == "S":
            print("The gorillas recognise your item and will allow you to continue your journey. They also give you a map of the nearby islands if you do not already have one.")
            loc = 17
    elif loc == 23:
        print("You are standing on a beach on the island's South coast. The mansion is to the North of you and there is a barbed wire fence ahead of you. To the West is a small pier. ")
        print("You can use a weapon to break the barbed wire (W), you can walk towards the pier (P) or you can go East to try to find another way to access the mansion (E).")
        choice = str(input())
        if choice == "W":
            loc = 30
        elif choice == "P":
            loc = 24
        elif choice == "E":
            print("The barbed wire continues on the Eastern side of the mansion until it reaches the sea on the North coast.")
            loc = 25
    elif loc == 24:
        print("You are standing on the South coast of the island near a small pier. There is a sandy beach to the East. There is a small path ahead which leads up to a gate in a barbed wire fence. You can see the mansion beyond the fence and to the West you can see a tower in the distance next to the fence.")
        print("You can attempt to breach the fence (F), attempt to open the gate (G), go East towards the beach (E) or go West towards the tower (W).")
        choice = str(input())
        if choice == "F":
            loc = 30
        elif choice == "G":
            print("The gate looks very well armoured so only the most powerful weapons will be capable of breaching it.")
            print("The gate also has a handle which you could attempt to open (H), and there is also a box nearby with several switches (S).")
            listweapons()
            print("You may also retreat to the South (R).")
            choice = str(input())
            if choice == "H":
                swicobs = random.randint(1000, 9999)
                if swicob != swicobs:
                    print("The gate will not open and an alarm sounds.")
                    alert = alert + 1
                elif swicob == swicobs and alert < 2:
                    print("The gate opens and you walk up to the front of the mansion.")
                    loc = 27
            elif choice == "S":
                print("There are four switches which can each be set to any position between 0 and 9. Currently they are all set to 0, but the first from the left which is set to 1.")
                print("You can set the switches by typing their positions from left to right or you can withdraw (W).")
                choice = input()
                if choice == "W":
                    print("You withdraw.")
                else:
                    swicob = choice
            elif choice == "PC":
                print("The cannon destroys the gate. However, you hear an alarm sound from inside the mansion so you advance towards the mansion cautiously.")
                alert = alert + 1
                loc = 27
            elif choice == "TB":
                print("The bomb destroys the gate. However, you hear an alarm sound so you advance cautiously towards the mansion.")
                destroy("time bomb (TB)")
                alert = alert + 1
                loc = 27
            elif choice == "EC":
                crystsample = crystal()
                if crystsample == "success":
                    alert = alert + 1
                    print("The crystal destroys the gate. However, you hear an alarm sound so you advance cautiously towards the mansion.")
                    loc = 27
                elif crystsample == "failure":
                    print("After the improper use, you pick up the crystal.")
                elif crystsample == "big failure":
                    endgame(1)
            elif choice == "HOH":
                print("You put on the helmet and charge towards the gate. It collapses, but the helmet is also damaged beyond repair.")
                print("An alarm sounds nearby so you advance cautiously towards the mansion.")
                destroy("helmet of horror (HOH)")
                alert = alert + 1
                loc = 27
        elif choice == "W":
            print("The tower is two storeys high and to the West of the tower is an impassable rock formation.")
            print("The door to the tower is old and wooden with a rusty keyhole. You could try the handle (H), try to force the door open with a weapon (W) or go to the East (E).")
            choice = str(input())
            if choice == "H":
                print("The door opens with a loud creaking noise.")
                loc = 28
            elif choice == "W":
                listweapons()
                choice = str(input())
                if choice == "SS" or choice == "GB" or choice == "WH" or choice == "PC" or choice == "HOH":
                    print(towertext)
                    loc = 28
                elif choice == "TB" or choice == "SBB" :
                    if choice == "TB":
                        destroy("time bomb (TB)")
                    elif choice == "SBB":
                        destroy("sticky banana bomb (SBB)")
                    print(towertext)
                    loc = 28
                elif choice == "SP":
                    destroy("strength potion (SP)")
                    print("You feel a sudden rush of strength and you force the door open. You enter the tower.")
                    loc = 28
                elif choice == "EC":
                    crystsample = crystal()
                    if crystsample == "success":
                        print(towertext)
                        loc = 28
                    elif crystsample == "failure":
                        print("You used the crystal improperly.")
                    elif crystsample == "big failure":
                        endgame(1)
                else:
                    inap()
        elif choice == "E":
            loc = 23
    elif loc == 25:
        print("You are East of the mansion and a barbed wire fence separates you from the mansion. You notice a square garden area enclosed with hedges nearby.")
        print("You can try to breach the fence (F), enter the garden area (G) or go to the South West (SW).")
        choice = str(input())
        if choice == "F":
            loc = 30
        elif choice == "SW":
            loc = 23
        elif choice == "G":
            if "stone rod" in ulist:
                print("You have already accomplished all there is to do in the garden so you withdraw.")
            else:
                print("You enter the garden. In the centre of the garden is a large cylindrical stone with a hole in the centre set into the ground.")
                print("In the North of the garden is a pool containing aquatic plants. there is a wooden bench in each of the other sides of the garden and these benches are surrounded by numerous plant species.")
                print("You can investigate the cylindrical stone (S) or withdraw from the garden (W).")
                choice = str(input())
                if choice == "S":
                    print("The stone looks rather old and worn. There are some strange symbols on the stone but they are difficult to read and understand.")
                    if "stone rod" in eqlist:
                        print("You immediatly notice that the symbols on the stone are similar to those on the stone rod given to you by Geelophisis.")
                        print("You can attempt to insert the rod into the hole in the stone (S) or abandon your examination of the stone (A).")
                        choice = str(input())
                        if choice == "S":
                            udestroy("stone rod")
                            print("By pushing and turning the rod, you are able to get two thirds of it to go into the hole.")
                            print("You now try to force the rod completely into the hole. This is hard to do, but eventually you succeed and the remainder of the rod descends into the hole. A loud mechanical noise occurs and you notice with surprise that one of the stone tiles in the garden has moved aside to reveal a hidden ladder leading underground.")
                            print("You can descend the ladder (L) or withdraw from the garden (W).")
                            choice = str(input())
                            if choice == "L":
                                print("You descend into a small chamber of stone. The only furniture is a wooden table with a large book upon it and a cabinet mounted to the wall.")
                                print("You can look in the cabinet (C), look in the book (B) or withdraw (W).")
                                choice = str(input())
                                if choice == "C":
                                    print("you look in the cabinet and find 2 rods, similar to the stone one you used to possess, hanging on hooks. These rods are of metal and wood. but there are two more hooks with no rods hanging on them.")
                                    print("You take the rods.")
                                    eqlist.append("wooden rod")
                                    eqlist.append("metal rod")
                                elif choice == "B":
                                    eqlist.append("information book")
                                    print("You look in the book and find that it is about Crultney mansion. You decide to take the book with you but much of it is in a language you cannot understand.")
    elif loc == 26:
        print("You are in a circular room with bookshelves all the way along the wall except for a gap in the East where there is a fireplace.")
        if 21 in findconnect(26):
            print("There are also several shards of glass on the floor, probably because the large window looking out towards the sea has been shattered.")
        else:
            print("There is also a large window in the North looking out towards the sea.")
        print("The only door is to the South.")
        print("You can go through the door (S), investigate the bookshelf (B) or investigate the fireplace (F).")
        choice = str(input())
        if choice == "S":
            loc = 29
        elif choice == "B":
            print("Inserted into one of the books you find a note which you read:")
            print("'Never did I think before that such a mode of transportation would be possible, yet upon building the device as described I found that it works, under certain circumstances. However, the consequences of its use could be grave so I have dismantled it and am storing the parts in the astronomy tower.'")
            print("The book into which this is inserted is very old and the text makes little sense to you.")
        elif choice == "F":
            print("You crawl into the fireplace and find a narrow passage to the side. The passage leads up to a small black door with no handle.")
            print("There is a lever for opening the door but the handle is missing and it is too heavy to move without the handle.")
            print("You can withdraw into the room (W) or use an object in your possesion to stand in for the handle (H).")
            choice = str(input())
            if choice == "H":
                if "shortsword (SS)" in eqlist or "metal rod" in eqlist or "large knife (LK)" in eqlist or "golden blade (GB)" in eqlist or "stone rod" in eqlist or "wooden rod" in eqlist:
                    print("You find a suitable item and open the door.")
                    print("The room is very small and you have to crouch down to get in.")
                    if "rusted keys" not in eqlist and "rusted keys" not in dlist:
                        print("In the room is a low wooden table with a green candle and a set of rusted keys on it.")
                        print("You take the items and withdraw into the cylindrical room.")
                        eqlist.append("green candle")
                        eqlist.append("rusted keys")
                    else: 
                        print("There are no items of interest in the room.")
                else:
                    print("You have no suitable items so you withdraw into the cylindrical room.")
                    
    elif loc == 27:
        if lastloc == 32:
            if 27 in findconnect(32):
                print("You step outside, passing the destroyed door.")
            else:
                print("You unlock the door and step outside.")
        print("You are standing directly in front of the mansion and you can see a large metal door directly ahead of you. This is the main entrance to the mansion. You can also see a small pier to the South.")
        print("To the West is a shed which is connected directly to the mansion.")
        print("You can attempt to get in through the main door (M), investigate the shed (S), walk towards the pier (P), walk towards the fence (F), or walk around to the East side of the mansion (E).")
        choice = str(input())
        if choice == "M":
            print("The main door looks very well protected with an elaborate security system.")
            if 32 in loclog():
                print("You may enter through the door (D) or you could try to scale the wall nearby and enter through a window on the 1st floor (SW).")
            else:
                print("You may use a weapon to break down the door (W) or you could try to scale the wall nearby and enter through a window on the 1st floor (SW).")
            choice = str(input())
            if choice == "SW":
                if "super strong rope (SSR)" in eqlist:
                    print("You use your super strong rope to successfully climb up to the window. You hurriedly use an object from your equipment bag to smash the window and you climb inside. ")
                    print("It will be difficult to pull up the rope through the window without alerting the nearby security cameras. You can try to pull up the rope (SSR) or abandon it and climb inside (C).")
                    choice = str(input())
                    if choice == "SSR":
                        print("You pull up the rope but an alarm sounds as you do so.")
                        alert = alert + 1
                    else:
                        destroy("super strong rope (SSR)")
                    loc = 72
                else:
                    print("You have no equipment for climbing so you abandon your attempt to scale the wall while halfway up. However, as you climb down, an alarm sounds.")
                    alert = alert + 1
            elif choice == "W":
                listweapons()
                choice = str(input())
                if choice == "BD" or choice == "SS" or choice == "HOH":
                    print("The weapon you have chosen is not powerful to do anything more than scratch the door.")
                elif choice == "TS":
                    print("The throwing stars bounce off the door and are bent out of shape by the impact so cannot be used again.")
                    destroy("throwing stars (TS)")
                elif choice == "GB":
                    print("The golden blade is able to break down the main door of the mansion but is broken in the process of doing so. An alarm sounds from within the mansion. You walk through the door into a corridor.")
                    destroy("golden blade (GB)")
                    alert = alert +1
                    loc = 32
                elif choice == "TB":
                    print("You set up the bomb and take cover. You look up after the explosion and find the door destroyed. You walk in while an alarm sounds from within the mansion.")
                    destroy("time bomb (TB)")
                    alert = alert + 1
                    loc = 32
                elif choice == "SP":
                    print("With the strength granted to you by the potion, you are able to pull the door from its hinges. You walk in while an alarm sounds from within the mansion.")
                    destroy("strength potion (SP)")
                    alert = alert + 1
                    loc = 32
                elif choice == "WH" or choice == "PC":
                    print("Your weapon succesfully destroys the door and you walk inside, while an alarm sounds from within the mansion.")
                    alert = alert + 1
                    loc = 32
                elif choice == "EC":
                    crystsample = crystal()
                    if  crystsample == "success":
                        print("The door is destroyed by the energy blast and an alarm sounds. You enter the mansion.")
                        alert = alert + 1
                        loc = 32
                    elif crystsample == "failure":
                        print("The crystal has no effect on the door.")
                    elif crystsample == "big failure":
                        endgame(1)
                elif choice == "SBB":
                    print("The sticky banana bomb is ineffective in breaking down the door.")
                    destroy("sticky banana bomb (SBB)")
                else:
                    inap()
        elif choice == "D" and 32 in loclog:
            print("You walk through the door into the main corridor.")
            loc = 32
        elif choice == "S":
            print("You walk towards the shed and notice that this door is much flimsier and is made from wood.")
            print("To the West of the shed is an impassable rock formation. You can attempt to gain access to the shed using the door (D) or you can return to the front of the mansion (M).")
            choice = str(input())
            if choice == "D":
                if 39 in loclog:
                    print("The shed door is unlocked and you step inside")
                    loc = 39
                else:
                    print("The shed door is locked so you may use a weapon against it.")
                    listweapons()
                    choice = str(input)
                    if choice == "SS":
                        destroy("shortsword (SS)")
                        print("Your weapon is destroyed on contact with the door but it does damage the door enough for you to be able to enter the shed.")
                        loc = 39
                    elif choice == "GB" or choice == "WH" or choice == "HOH" or choice == "PC":
                        print("your weapon succeeds in breaking down the door and you enter the shed.")
                        loc = 39
                    elif choice == "TB":
                        destoy("time bomb (TB)")
                        print("The bomb works and you enter the shed.")
                        loc = 39
                    elif choice == "EC":
                        crystsample = crystal() 
                        if crystsample == "success":
                            print("You destroy the door and enter the shed.")
                            loc = 39
                        elif crystsample == "failure":
                            print("The crystal is ineffective.")
                        elif crystsample == "big failure":
                            endgame(1)
                    elif choice == "SP":
                        destroy("strength potion (SP)")
                        print("You destroy the door and enter the shed.")
                    else:
                        inap()
        elif choice == "P":
            loc = 24
        elif choice == "F":
            if 30 in findconnect(27):
                print("You walk back following the path you cleared earlier.")
        elif choice == "E":
            print("There are no entrances on the East side of the mansion. As you are walking you notice a monitoring camera on the wall near you so you head back to the front of the mansion to avoid being detected.")
    elif loc == 28:
        print("In the ground floor of the tower, there is a table in the centre of the room with no interesting objects on it. There is also a staircase leading up to the first floor.")
        print("You can withdraw from the tower (W) or climb the stairs to the first floor (S).")
        choice = str(input())
        if choice == "W":
            print("You return to the path near the fence.")
            loc = 24
        elif choice == "S": 
            if "brass key" in eqlist or "brass key" in dlist:
                print("You ascend the stairs into a room similar to the one below. There are no items of interest in the room.")
            else:
                print("You climb the stairs into another room similar to the one below. Before you have a chance to look for clues, a bottle of green liquid suddenly shoots out from the room towards you.")
                print("You must hold up a piece of equipment to protect yourself.")
                tomrin = 1
                tomrino = 0
                while tomrin == 1:
                    eqloss = random.choice(eqlist)
                    if eqloss == "time bomb (TB)" or eqloss == "sticky banana bomb (SBB)" or eqloss == "invisibility potion (IP)" or eqloss == "strength potion (SP)":
                        tomrin = 1
                    else:
                        tomrin = 0
                    tomrino = tomrino + 1
                    if tomrino >= 1000:
                        print("You have no appropriate equipment. The bottle contained acid and dealt you a severe injury.")
                        endgame(1)
                destroy(eqloss)
                print(eqloss, " is lost")
                print("The bottle contained acid and your equipment was destroyed. The bottle was launched from a spring powered mechanism that detected the opening of the door into the room.")
                print("You look around the room and see that it is very similar to the downstairs room. However, you do notice a small brass key hanging from the wall. You take the key and exit the tower.")
                eqlist.append("brass key")
                print("You return to the path near the fence.")
            loc = 24
    elif loc == 29:
        print("You are in a corridor which runs from North to South. To the North, there is a grey door leading into a room (GD). To the South, there is a junction with two passages leading off it, one to the East (E) and one to the South (S).")
        print("There is also an old, brown door in the West wall of the corridor (BD).")
        choice = str(input())
        if choice == "GD":
            loc = 26
        elif choice == "E":
            loc = 31
        elif choice == "S":
            loc = 32
        elif choice == "BD":
            loc = 33
    elif loc == 30:
        listweapons()
        print("You may also withdraw (W).")
        choice = str(input())
        if choice == "GB" or choice == "SS" or choice == "SOS":
            print("Your weapon is successful in clearing a path through the barbed wire.")
            loc = 27
        elif choice == "BD":
            print("The blade of the weapon is not long enough to be particularly effective in cutting through the barbed wire. Hence, you make a blunder and drop the weapon but you are able to stumble on to the other side of the wire.")
            destroy("black dagger (BD)")
            loc = 27
        elif choice == "TB" or choice == "PC":
            print("You are able to blast a path through the barbed wire.")
            if choice == "TB":
                destroy("time bomb (TB)")
            loc = 27
        elif choice == "WH":
            print("This weapon is not effective in cutting a path through the barbed wire.")
        elif choice == "SBB":
            print("The bomb explodes but does not help and leaves a mass of tangled barbed wire covered in sticky banana juices.")
            destroy("sticky banana bomb (SBB)")
        elif choice == "EC":
            crystsample = crystal()
            if  crystsample == "success":
                print("The barbed wire is destroyed and you walk towards the mansion.")
                loc = 27
            elif crystsample() == "failure":
                destroy("energy crystal (EC)")
                print("The crystal rolls away into the middle of the wire.")
            elif crystsample() == "big failure":
                endgame(1)
        elif choice == "W":
            loc = lastloc()
        else:
            inap()
    elif loc == 31:
        print("You are in a corridor which runs from East to West. There is a junction with a North - South corridor to the West (W). There are two grey doors opposite each other in the Eastern side of the passage. (NED) and (SED). There is another door to the North in the WEstern side of the passage (WD).")
        choice = str(input())
        if choice == "W":
            loc = 29
        elif choice == "NED":
            loc = 34
        elif choice == "SED":
            loc = 35
        elif choice == "WD":
            loc = 33
    elif loc == 32:
        print("You are in a corridor which runs from North to South. To the South is the main door of the mansion (S). There are passages leading off to the East and West (E) and (W). You could also follow the corridor to the North (N).")
        choice = str(input())
        if choice == "E":
            loc = 36
        elif choice == "W":
            loc = 37
        elif choice == "N":
            loc = 29
        elif choice == "S":
            loc = 27
    elif loc == 33:
        if 38 in loclog:
            print("You walk back into the control room.")
        else:
            if "rusted keys" in eqlist:
                print("You find the key to the door amongst your items and you open the door.")
                loc = 38
            else:
                print("The door is locked. You may retreat (R) or use weapons.")
                listweapons()
                choice = str(input())
                if choice == "WH":
                    destroy("warhammer (WH)")
                    print("Your warhammer is successful in breaking the door but is destroyed by the impact.")
                    loc = 38
                elif choice == "PC":
                    print("Your portable cannon is successful in breaking the door and you advance into the room.")
                    loc = 38
                elif choice == "TB":
                    print("Your time bomb is successful in breaking the door and you advance into the room.")
                    destroy("time bomb (TB)")
                    loc = 38
                elif choice == "EC":
                    crystsample = crystal()
                    if crystsample == "success":
                        print("Your crystal breaks the door and you advance into the room.")
                        loc = 38
                    elif crystsample == "failure":
                        print("You cannot remember the correct way to use the crystal.")
                    elif crystsample == "big failure":
                        endgame(2)
                elif choice == "R":
                    loc = lastloc()
                else:
                    inap()
        
    elif loc == 34:
        print("You walk out onto a spiral staircase which has stairs leading off upwards and downwards and an exit to the South at this level.")
        if 34 in loclog or stairrobot == 0:
            Print("You can go upwards (U) or downwards (D) on the stairs or exit to the South at this level (E).")
            choice = str(input())
            if choice == "U":
                loc = 40
            elif choice == "D":
                loc = 41
            elif choice == "E":
                loc = 31 
        else:
            print("As you step out onto the stairs, you hear a sliding noise and you see a sharp blade mounted to the banister sliding down towards you.")
            print("You must use a piece of equipment to defend against the attack")
            listweapons()
            choice = str(input())
            if choice == "BD" or choice == "SS" or choice == "WH" or choice == "CBD" or choice == "LK":
                print("You parry the attack but your weapon is irrepairably damaged due to the impact.")
                stairrobot = 0
                if choice == "BD":
                    destroy("black dagger (BD)")
                elif choice == "SS":
                    destroy("shortsword (SS)")
                elif choice == "CBD":
                    destroy("CBD")
                elif choice == "WH":
                    destroy("warhammer (WH)")
                elif choice == "LK":
                    destroy("large knife (LK)")
            elif choice == "GB" or choice == "SOS" or choice == "HOH":
                stairrobot = 0
                print("You successfully defend against the attack and your weapon is undamaged.")
            else:
                inap()
                print("The sharp blades strikes you and you fall unconscious. Your mission is over.")
                endgame(2)                
    elif loc == 35:
        print("You walk into an elaborately furnished dining room. A large table dominates the centre of the room. On the table are several empty plates, pieces of cutlery and candles.")
        print("There are doors to the North (N) and South (S). You could also stay in this room to investigate further (I).")
        choice = str(input())
        if choice == "N":
            loc = 31
        elif choice == "S":
            loc = 42
        elif choice == "I":
            print("You can investigate the plates and cutlery (P), the candles (C) or the underside of the table (T).")
            choice = str(input())
            if choice == "P":
                if "magnetic fork (MF)" in eqlist or "magnetic fork (MF)" in dlist:
                    print("You notice nothing interesting about the plates and cutlery.")
                else:
                    print("you notice that one of the forks has been magnetised. You take it with you. You notice nothing remarkable about any of the other cutlery or plates.")
                    eqlist.append("magnetic fork (MF)")
            elif choice == "T":
                print("You notice nothing remarkable about the table.")
            elif choice == "C":
                if "blue candle" in eqlist or "blue candle" in dlist:
                    print("You notice nothing interesting about the candles.")
                else: 
                    print("You notice that while all other candles in the room are white or yellow, one is a vibrant shade of blue. You decide to take it with you.")
                    eqlist.append("blue candle")
    elif loc == 36:
        print("You are in a corridor which runs from East to West. There is a junction with a North-South corridor to the West (W), a dirty wooden door leading to the North (N), a solid metal door to the East(E) and a colourfully painted door to the South (S).")
        choice = str(input())
        if choice == "N":
            loc = 42
        elif choice == "E":
            loc = 43
        elif choice == "S":
            loc = 44
        elif choice == "W":
            loc = 32
    elif loc == 37:
        if lastloc() == 47 and 37 not in findconnect(47) and 47 not in findconnect(37):
                print("As you walk up the short passageway to the door, a pit trap opens up beneath your feet and you fall in.")
                print("You are able to escape from the trap unharmed and you open the door to the North.")
                alert = alert + 1
        print("You are in a sparsely furnished corridor running from East to West. There are two doors leading to the South (SE) and (SW), a junction with another corridor to the East (E) and to the North, a short passageway leading up to another door (N).")
        choice = str(input())
        if choice == "SE":
            loc = 45
        elif choice == "SW":
            loc = 46
        elif choice == "E":
            loc = 32
        elif choice == "N":
            if 37 in findconnect(47) or 47 in findconnect(37):
                print("Avoiding the pit, you make your way into the cylindrical room.")
            elif "magical map (MM)" in eqlist:
                print("You feel uneasy about this passageway so you consult the magical map. It shows that there is a pit trap. You carefully move around the trap and you open the door to the North.")
            else:
                print("As you walk up the short passageway to the door, a pit trap opens up beneath your feet and you fall in.")
                print("You are able to escape from the trap unharmed and you open the door to the North.")
                alert = alert + 1
            loc = 47
    elif loc == 38:
        print("You walk into the room and notice a bank of switches in the far corner of the room. In the centre of the room is a small, round hole in the floor surrounded by inscriptions from a language you do not recognise. To one side of the room is a desk with various papers and tools on it. There are doors to the South and to the West.")
        print("You can investigate the switches (SW), the hole (H), or the desk (D) or you may leave through the doors to the South (S) or West (W).")    
        choice = str(input())
        if choice == "SW":
            print("On the right of the panel there are two circular wheels, one above the other. To the right is a small lever which is hidden behind a glass screen. You could investigate the wheels (W), investigate the lever (L) or withdraw into the room (R).")
            choice = str(input())
            if choice == "W":
                print("Each wheel has four spokes with a marker attached to one of these.")
                print("Currently, the marker of the upper wheel is in the ", poswheel(1), " position and that of the lower wheel is in the ", poswheel(0), "position.")
                print("Let the positions of each wheel be numbered clockwise from 1 to 4, starting with the upper position.")
                screen[1] = int(input("Set position of upper wheel (1/2/3/4).   "))
                screen[0] = int(input("Set position of lower wheel (1/2/3/4).   "))
            elif choice == "L":
                if "metal rod" in ulist:
                    print("You lift the glass cover. The lever can be in two positions, up (0) or down (1), and is currently in the ", poswheel(3), "position.")
                    stairrobot = int(input("Set position of lever (0/1).   "))
                else:
                    print("Unfortunately, you are unable to lift the glass screen so you must withdraw into the room.")
        elif choice == "H":
            if "metal rod" in eqlist:
                print("You notice that the symbols around the hole are similar to those engraved on the metal rod.")
                print("You can attempt to insert the metal rod (MR) or you can withdraw (W)")
                choice = str(input())
                if choice == "MR":
                    print("You insert the metal rod and twist it until it descends until it descends into the hole, with only around 150 mm protruding. You here a noise from the corner of the room and you believe that something has changed about the panel of switches.")   
                    udestroy("metal rod")
            else:
                print("You do not recognise the symbols and do not understand the purpose of the hole. You withdraw from the hole.")
        elif choice == "D":
            print("You find a note which you believe corresponds to the switches you saw in the corner of the room.")
            print("You read the note: 'West wing - cylindrical room rotation screens. The positions marked on the wheels are the positions of the blocking screens of the two Northern cylindrical rooms. These extend to all floors.'")
        elif choice == "S":
            loc = 31
        elif choice == "W":
            loc = 29
    elif loc == 39: 
        print("You are in a large shed with various pieces of garden related machinery. To the North and South are wooden doors (N) and (S). You could remain in the shed and investigate it further (I).")
        choice = str(input())
        if choice == "S":
            print("You leave the shed by the Southern door.")
            loc = 27
        elif choice == "N":
            loc = 48
        elif choice == "I":
            print("You find a diary on a shelf at the back of the shed and you read the most recent entry. You notice that some pages are missing.")
            print("'September 16th, 1971")
            print("Today I made another attempt to clear the rubble in the collapsed chamber. However, the lawnmower engine broke again. I am now moving all operations to the North side of the chamber and hope to find a substitute for the lawnmower engine soon. Since I am not currently capable of operating the crane, I have taken three gears from its gearbox and hidden them in the mansion, to prevent malignant use of the crane by my enemies. Records of their location can be found in the study. I have recently been distracted from the project by the mysterious antics of one of the robotic wardens, 0066A12. It seems to be slow to obey orders and has a strange tendency to walk around the astronomy tower at night, so I am now tring to '")
            print("A significant fragment of the page has been torn off so you do not know how the sentence finishes.")
    elif loc == 40:
        print("You are on the first floor landing, you can go up (U) or down (D) on the spiral staircase or exit to the South at this level (E)")
        choice = str(input())
        if choice == "U":
            loc = 49
        elif choice == "D":
            loc = 34
        elif choice == "E":
            loc = 50
    elif loc == 41:
        print("You are standing at the bottom of the spiral staircase. You can go up (U) or exit to the South at this level (E)")
        choice = str(input())
        if choice == "U":
            loc = 34
        elif choice == "E":
            loc = 51
    elif loc == 42:
        print("You are in a large kitchen with many utensils arranged neatly on top of work surfaces. There is a small elevator shaft in the corner of the room, presumably for the transportation of cooking supplies. You could investigate the elevator (E) or the kitchen utensils (U). There are doors to the North and South (N and S).")
        choice = str(input())
        if choice == "E":
            print("You examine the elevator shaft and discover that the elevator is not in working order.")
            if "super strong rope (SSR)" in eqlist:
                print("You look up the shaft and at first you can see nothing. However, as your eyes become accustomed to the darkness, you notice a thin rod sticking out of the wall about halfway up the shaft. Using your super strong rope, you may attempt to climb up the shaft to this point (C) or you may withdraw into the kitchen (W).")
                choice = str(input())
                if choice == "C":
                    print("You throw the rope up the shaft and it catches on the rod. you then ascend the elavator shaft. You find that the rod is securely fastened to the wall and that there is a small ledge just above it.")
                    print("You can pull yourself up onto the ledge (L) or go back down the shaft to the kitchen (D).")
                    choice = str(input())
                    if choice == "L":
                        if "brass key" in ulist:
                            print("You have already opened the chest so you feel no need to climb back up to the ledge.")
                        else:
                            print("You climb up to the ledge and discover that a locked chest sits upon it.")
                        if "brass key" in eqlist:
                            print("You notice that the brass key you found in the tower fits the chest and you excitedly open it.")
                            print("You find that the chest contains a ")
                            udestroy("brass key")
                        else:
                            print("You do not have the key for the chest. You may use a weapon to attempt to force the chest to open (W) or you can leave the chest and go back to the kitchen (D).")    
                            choice = str(input())
                            if choice == "W":
                                listweapons()
                                if choice == "BD" or choice == "GB" or choice == "SS" or choice == "WH" or choice == "HOH":
                                    print("You break open the chest and find a mysterious electronic device that you do not recognise. You take this with you.")
                                    eqlist.append("strange device")
                                elif choice == "SP":
                                    print("You break open the chest and find a mysterious electronic device that you do not recognise. You take this with you.")
                                    destroy("strength potion (SP)")
                                    eqlist.append("strange device")
                                elif choice == "PC":
                                    print("The portable cannon succeeds in destroying the chest but also destroys whatever was inside.")
                                elif choice == "TB":
                                    destroy("time bomb (TB)")
                                    print("The time bomb succeeds in destroying the chest but also destroys whatever was inside.")
                                elif choice == "LK":
                                    print("You are able to open the chest but you break the knife in the process of doing so. Inside the chest you find a mysterious electronic device that you do not recognise. You take this with you.")
                                    eqlist.append("strange device")
                                elif choice == "SBB":
                                    print("The sticky banana bomb fails to break open the chest.")
                                    destroy("sticky banana bomb (SBB)")
                                elif choice == "EC":
                                    crystsample = crystal()
                                    if crystsample == "success":
                                        print("You break open the chest and find a mysterious electronic device that you do not recognise. You take this with you.")
                                        eqlist.append("strange device")
                                    elif crystsample == "failure":
                                        print("The crystal has no effect on the chest.")
                                    elif crystsample == "big failure":
                                        endgame(2)
        elif choice == "U":
            print("You find a large knife that you may carry with you as a weapon (W) or leave behind (L).")
            if choice == "W":
                eqlist.append("large knife (LK)")
        elif choice == "N":
            loc = 35
        elif choice == "S":
            loc = 36
    elif loc == 43:
        print("You are in a small circular room with a narrow ascending staircase. There are no other objects of interest in the room. You can ascend the staircase (A) or exit the room to the West (W).")
        choice = str(input())
        if choice == "A":
            loc = 52
        elif choice == "W":
            loc = 36
    elif loc == 44:
        print("You are in a very spacious living room. Finely decorated rugs cover the floor and the walls have expensive paintings mounted upon them. There are two large sofas and several comfortable chairs and nearby is a small yet magnificent woodwn table")
        print("you can leave the room through the door to the North (N). You could also investigate the paintings (P), the table (T) or the floor (F).")
        choice = str(input())
        if choice == "N":
            loc = 36
        elif coice == "P":
            print("You investigate the paintings. You believe they correspond to notable members of the Glass Of Water family. You find nothing hidden behind the paintings and no hidden clues within them.")
        elif choice == "F":
            print("You pull up the rug near the sofa and discover a trapdoor in the floor. You find nothing else of interest. You can open the trapdoor (O) or ignore it (I).")
            choice = str(input())
            if choice == "O":
                print("You open the trapdoor and find a box of matches which you decide to take with you.")
                eqlist.append("matches")
        elif choice == "T":
            print("The top of the table is bare but there is a small drawer at the side of the table. you open the drawer and find some papers and an iron key. You take these with you.")  
    elif loc == 45:
        print("You are in a courtyard which is enclosed on all sides by walls. In the centre is a medium sized tree surrounded by various other plants and benches. Above you is a large balcony which you cannot access from below.")        
        print("The only door out of the courtyard is to the North (N). You could observe the balcony in greater detail (B) or observe the tree in the centre of the courtyard (T).")
        choice = str(input())
        if choice == "N":
            loc = 37
        elif choice == "B":
            print("The balcony looks down on the courtyard from 3 sides. You observe that while two of these sides have only wooden railings, the other has a stone wall with only a small gap above it.")
        elif choice == "T":
            print("You notice nothing unusual about the tree, nor do you find anything of interest amongst the plants and benches nearby. You climb the tree for a better view of the 1st floor balcony. You can observe from this position that there are two security cameras mounted on the balcony.")
            if "super strong rope (SSR)" in eqlist:
                print("You could attempt to climb up to the balcony using your super strong rope (SSR).")
                choice = str(input())
                if choice == "SSR":
                    if observe == 1:  
                        print("You are able to climb up to the balcony, but not before an alarm sounds. You notice a security camera on the balcony. It must have noticed you and sounded the alarm.") 
                    else:
                        print("You successfully climb up to the balcony.")
                    loc = 53
            else:
                print("Due to the presence of the security cameras and your lack of suitable climbing equipment, you climb down from the tree.")
    elif loc == 46:
        print("Inner collapsed room.")
        #collapsed room#
    elif loc == 47:
        print("You are standing in a small, cylindrical room with a low ceiling and doors leading off towards each of the cardinal compass directions (N, E, S, W). There is also a small depression in the centre of the room which you could examine (D).")
        choice = str(input())
        if choice == "N":
            acloc = 47
            loc = screencheck(55, 3, 0)
        elif choice == "E":
            loc = 56
        elif choice == "S":
            loc = 37
        elif choice == "W":
            loc = 57
        elif choice == "D":
            print("At the bottom of the depression, you find a small plate with the number ", fcode[0], " written upon it.")
    elif loc == 48:
        print("You are standing in a room with a collapsed ceiling. Rubble blocks your way to the North, but you can see that the room continues beyond the rubble and that there is a small structure in the North side of the room. To the South is a wooden door (S).")
        if craneunlock == 0:
            print("There is a temporary panel near the rubble with wires connecting this device to the distant structure. On the panel is a single switch which you may press (P).")
        choice = str(input())
        if choice == "S":
            loc = 39
        elif choice == "P":
            print("You notice no immediate effect.")
            craneunlock = 1
    elif loc == 49:
        print("You are standing on the second floor landing, at the top of the spiral staircase. You can go down to the first floor (D) or exit to the corridor in the South.")
        choice = str(input())
        if choice == "D":
            loc = 40
        elif choice == "E":
            loc = 58
    elif loc == 50:
        print("You are in a corridor which runs from East to West. The corridor borders a North-South corridor to the West (W). There are two doors to the North (NW and NE) there is also a door to the South (S).")
        choice = str(input())
        if choice == "NW":
            loc = 73
        elif choice == "NE":
            loc = 40
        elif choice == "S":
            if 59 in loclog:
                loc = 59
            else:
                print("The door is locked.")
                if "silver key" in eqlist:
                    print("You find the key to the door amongst your items (the silver key) and you open the door.")
                    udestroy("silver key")
                    loc = 59 
                else:
                    print("You may use weapons (W) or withdraw (I).")
                    choice = str(input())
                    if choice == "W":
                        listweapons()
                        choice = str(input())
                        if choice == "GB" or choice == "WH"  or choice == "HOH" or choice == "PC":
                            print("You succesfully break down the door and enter the room but an alarm sounds.")
                            alert = alert + 1
                            loc = 59
                        elif choice == "SBB":
                            print("The sticky banana bomb is ineffective in breaking down the door.")
                            destroy("sticky banana bomb (SBB)")
                        elif choice == "TB":
                            print("The time bomb successfully breaks down the door and you enter the room. However, an alarm sounds.")
                            destroy("time bomb (TB)")
                            loc = 59
                        elif choice == "EC":
                            crystsample = crystal()
                            if crystsample == "success":
                                print("You destroy the door and walk into the room but an alarm sounds as you do so.")
                                alert = alert + 1
                                loc = 59
                            elif crystsample == "failure":
                                print("The crystal is ineffective.")
                            elif crystsample == "big failure":
                                endgame(2)
                        else:
                            inap()   
        elif choice == "W":
            loc = 66
    elif loc == 51:
        print("You are in a passageway in the basement of the mansion. There are doors to the North and South (N and S) and there is also a short passageway leading off towards a spiral staircase to the North (SS).") 
        choice = str(input())
        if choice == "N":
            loc = 60
        elif choice == "S":
            loc = 61
        elif choice == "SS":
            loc = 41
    elif loc == 52:
        print("You are in a small room with no doors and a narrow descending staircase (D). There is a small window facing East and you can see the gardens of the mansion through this. In the centre of the room is a turntable with a marker on it. You can turn the table so that the marker points towards the Garden (G), Astronomy Tower (A) or West Tower (W).")
        print("The turntable is currently in the ", towerpos, " position.")
        choice = str(input())
        if choice == "D":
            loc = 43
        else:
            towerpos = choice
    elif loc == 53:
        print("You are standing on the Southern side of  a balcony which overlooks a courtyard below. To the East, the balcony turns to the North (N). A cyan tile is set into the wall on the corner between the East-West part of the balcony, which you are currently standing on, and the North-South part of the balcony. On the part of the balcony upon which you stand, there is a small bench and an elaborate candle holder as well as several potted plants.")
        print("You can go North (N), investigate the candle holder (C), investigate the plants (P) or climb down into the courtyard (D).")
        choice = str(input())
        if choice == "N":
            loc = 62
        elif choice == "C":
            if "green candle" in eqlist or "red candle" in eqlist or "blue candle" in eqlist or len(candlelist[2]) > 3:
                if candle(2) == 1:
                    choice = str(input())
                    if choice == "P":
                        print(eqlist)
                        candleid = input("Which candle should be placed here?   ")
                        if candleid in eqlist:
                            destroy(candleid)
                            candlelist[2] = candleid
                    elif choice == "R":
                        eqlist.append(candlelist[2])
                        lcandlelist[2] = 0
                        candlelist[2] = ""
                    elif choice == "L":
                        if "matches" in eqlist:
                            print("You light the candle.")
                            lcandlelist[2] = 1
        elif choice == "P":
            if observe == 1:
                print("You notice that one of the plants is obscuring a hidden security camera, yet no alarm sounds when you uncover it. You wonder what the purpose of this camera is.")
            else:
                print("You notice nothing unusual about the plants.")
        elif choice == "D":
            loc = 45
    elif loc == 54:
        print("You open the door but find your way blocked by a metal screen so you return to the room.")
        loc = acloc
    elif loc == 55:
        print("You are standing in a small, cylindrical room with a low ceiling and doors leading off towards each of the cardinal compass directions (N, E, S, W). The room has no features worthy of further investigation.")
        choice = str(input())
        acloc = 55
        if choice == "N":
            loc = screencheck(68, 1, 0)
        elif choice == "E":
            loc = screencheck(64, 2, 0)
        elif choice == "S":
            loc = screencheck(47, 3, 0)
        elif choice == "W":
            loc = screencheck(65, 4, 0)
    elif loc == 56:
        print("Tou are standing by the side of a pool containing water.")
    elif loc == 57:
        print("You are in a dimly lit room with many wooden boxes piled up along the western wall. There is a door to the East (E). You could search through the boxes (B).")
        choice = str(input())
        if choice == "E":
            loc = 47
        elif choice == "B":
            print("You find that the boxes contain a small metal wheel which you take with you. The boxes also contain many uninteresting items.")
            smallwheels = smallwheels + 1
    elif loc == 58:
        print("You are in a corridor running from East to West. There are doors to the North and South (N and S) and there is a junction with a North-South corridor to the West (W).")
        choice = str(input())
        if choice == "N":
            loc = 49
        elif choice == "S":
            print("The door is locked.")
            print("You may withdraw into the corridor (I) or use weapons (W)")
            choice = str(input())
            if choice == "W":
                listweapons()
                choice = str(input())
                if choice == "GB" or choice == "WH"  or choice == "HOH" or choice == "PC":
                    print("You succesfully break down the door and enter the room but an alarm sounds.")
                    alert = alert + 1
                    loc = 98
                elif choice == "SBB":
                    print("The sticky banana bomb is ineffective in breaking down the door.")
                    destroy("sticky banana bomb (SBB)")
                elif choice == "TB":
                    print("The time bomb successfully breaks down the door and you enter the room. However, an alarm sounds.")
                    destroy("time bomb (TB)")
                    loc = 98
                elif choice == "EC":
                    crystsample = crystal()
                    if crystsample == "success":
                        print("You destroy the door and walk into the room but an alarm sounds as you do so.")
                        alert = alert + 1
                        loc = 98
                    elif crystsample == "failure":
                        print("The crystal is ineffective.")
                    elif crystsample == "big failure":
                        endgame(2)
                else:
                    inap()   
        elif choice == "W":
            loc = 74
    elif loc == 59:
        print("You are in a large bedroom.")
    elif loc == 60:
        print("You are in a long rectangular room with a narrow staircase occupying around half the space in the room at the top of which is a door to the North (D). There is a door to the South (S) and there are no other objects of interest in the room.")
        choice = str(input())
        if choice == "N":
            loc = 65
        elif choice == "S":
            loc = 51
    elif loc == 61:
        print("You are in a musty room with a low ceiling. There are a few boxes piled up against the far wall and nearby there is an interesting looking panel on the wall. You could investigate the contents of the boxes (B), investigate the panel (P) or withdraw from the room (W).")
        choice = str(input())
        if choice == "B":
            print("You check the boxes and find that they contain scientific and electrical equipment. These items are all too heavy to add to your baggage apart from a selection of fuses which you notice near the top of the box.")
            eqlist.append("fuses")
        elif choice == "P":
            print("Implanted into the panel are two large iron discs and above these is a symbol of a trident. You may attempt to interact with the panel using an item in your possesion (I), you may try to remove the iron discs using a weapon (R) or you may end your investigation into the panel (E).")
            choice = str(input())
            if choice == "I":
                listweapons()
                choice = str(input("Which item do you want to use?   "))
                if choice == "MF" and "magnetic fork (MF) in eqlist":
                    print("You attach the ends of the magnetic fork to the two discs and the panel slides upwards, revealing a small hollow containing a metal wheel. You decide to take this with you as it looks to be of significance.") 
                    destroy("magnetic fork (MF)")
                    smallwheels = smallwheels + 1
            elif choice == "R":
                listweapons()
                choice = str(input())
                if random.randint(1,6) <=2:
                    print("Unfortunately, you were unable to remove the discs and the weapon you were using was destroyed.")
                    dindex = 0
                    while choice not in eqlist[dindex]:
                        dindex = dindex + 1
                    destroy(eqlist[dindex])
            else:
                print("Unfortunately, you were unable to remove the discs.")
        elif choice == "W":
            loc = 51
    elif loc == 62:
        ccs = ""
        if len(candlelist[1]) > 3:
            ccs = ""
        print("You are standing in the centre of a balcony which overlooks a courtyard to the West. To the North and South (N and S), the balcony turns such that it becomes perpendicular to the part on which you currently stand. In the centre of the North-South part of the balcony is a large stone cuboid upon which stands an elaborate candle holder (C). You could attempt to climb down into the courtyard below (D) but there may be safer places nearby to do this. There is also a door to the East (E).") 
        if candlelist == ["red candle", "green candle", "blue candle"] and lcandlelist == [1, 1, 1]:
            print("You notice that a hidden door in the stone cube has swung aside to reveal a small chamber. Inside the chamber is a silver key which you take with you.")
            eqlist.append("silver key")
        choice = str(input())
        if choice == "N":
            loc = 67
        elif choice == "S":
            loc = 53
        elif choice == "C":
            if candle(1) == 1:
                choice = str(input())
                if choice == "P":
                    print(eqlist)
                    candleid = input("Which candle should be placed here?   ")
                    if candleid in eqlist:
                        destroy(candleid)
                        candlelist[1] = candleid
                elif choice == "R":
                    eqlist.append(candlelist[1])
                    lcandlelist[1] = 0
                    candlelist[1] = ""
                elif choice == "L":
                    if "matches" in eqlist:
                        print("You light the candle.")
                        lcandlelist[1] = 1
        elif choice == "D":
            luck = random.randint(1,5)
            if luck == 1: 
                print("You climb down but are injured in the process.")
                if "medical kit (MK)" in eqlist:
                      print("Since you have a medical kit you use it and are able to continue with your investigation of the mansion.")
                      destroy("medical kit (MK)")
                else:
                    print("You are so severely injured that you must abort your mission")
                    endgame(2)
            elif luck == 2:
                print("You climb down but an alarm sounds as you do so.")
                alert = alert + 1
            else:
                print("You climb down successfully.")
            loc = 45
        elif choice == "E":
            loc = 76
    elif loc == 63:
        print("You are in a small, cylindrical room with doors leading off towards the East, South and West (E, S and W). The room has no other noteworthy features.")
        choice = str(input())
        acloc = 63
        if choice == "E":      
            loc = screencheck(69, 2, 1)
        elif choice == "S":
            loc = screencheck(70, 3, 1)
        elif choice == "W":
            loc = screencheck(71, 4, 1)
    elif loc == 64:
        print("Puzzle room")
    elif loc == 65:
        print("You are in a very small room with no features worthy of investigation. There are doors to the East and South (E and S).")
        choice = str(input())
        if choice == "E":
            loc = screencheck(55, 4, 0)
        elif choice == "S":
            print("You open the door and descend a narrow staircase.")
            loc = 60
    elif loc == 66:
        print("You are in a corridor which runs from North to South. To the North there is a white door (WD). To the East there is a brown door (BD) and South of this is another corridor leading off to the East (E). To the South there is a junction with passages leading to the South (S) and West (W).") 
        choice = str(input())
        if choice == "WD":
            loc = 75
        elif choice == "BD":
            loc = 73
        elif choice == "E":
            loc = 50
        elif choice == "S":
            loc = 76
        elif choice == "W":
            loc = 77
    elif loc == 67:
        print("You are standing on the Northern side of  a balcony which overlooks a courtyard below. To the East, the balcony turns to the South (S). A yellow tile is set into the wall on the corner between the East-West part of the balcony, which you are currently standing on, and the North-South part of the balcony. On the part of the balcony upon which you stand, there is a small bench and an elaborate candle holder. There is also a door to the North.")
        print("You can go South along the balcony (S), investigate the candle holder (C), climb down into the coutyard (D) or go through the door to the North (N).")
        choice = str(input())
        if choice == "S":
            loc = 62
        elif choice == "C":
            if "green candle" in eqlist or "red candle" in eqlist or "blue candle" in eqlist or len(candlelist[2]) > 3:
                if candle(0) == 1:
                    choice = str(input())
                    if choice == "P":
                        print(eqlist)
                        candleid = input("Which candle should be placed here?   ")
                        if candleid in eqlist:
                            destroy(candleid)
                            candlelist[0] = candleid
                    elif choice == "R":
                        eqlist.append(candlelist[0])
                        lcandlelist[0] = 0
                        candlelist[0] = ""
                    elif choice == "L":
                        if "matches" in eqlist:
                            print("You light the candle.")
                            lcandlelist[0] = 1
        elif choice == "D":
            loc = 45
        elif choice == "N":
            loc = 77
    elif loc == 68:
        loc = screencheck(63, 3, 1)
    elif loc == 69:
        print("You are standing in an extremely small room whose only notable features are a number input device affixed to the wall (N) and a door to the West (W).")        
        choice = str(input())
        if choice == "N":
            print("The device consists of three wheels with the numbers 0-9 enscribed upon them. These are arranged from left to right. Above the leftmost wheel is written the number 0. Above the centre wheel is written the number 1. Above the rightmost wheel is written the number 2. Below the wheels is a button. You can adjust the positions of the wheels (A), press the button (B) or withdraw (W).")
            choice = str(input())
            if choice == "A":
                ncode = input("Type the numbers to which you set the wheels, from left to right.   ")
            elif choice == "B":
                if ncode == fcode:
                    print("You here a mechanical noise from above you.")
                    wunlock = 1
                else:
                    print("An alarm sounds.")
                    alert = alert + 1
        elif choice == "W":
            loc = screencheck(63, 2, 1)
    elif loc == 70:
        loc = screencheck(55, 1, 0)
    elif loc == 71:
        print("You are standing in a short hallway with a door to the East (E) and an ascending staircase to the West (W).")
        choice = str(input())
        if choice == "E":
            loc = screencheck(63, 4 , 1)
        elif choice == "W":
            loc = 78
    elif loc == 72:
        print("You are in a bathroom containing a large bathtub (B), a sink (S) and a toilet (T). The only door is to the North (N). ")
        choice = str(input())
        bwlist = ["left", "right", "on", "off"]
        if choice == "B":
            print("You notice a strange lever attached to the wall above the bath. It can be in two positions, left and right and is currently in the ", bwlist[bathwater[0]], " position. The bathtap is currently ", bwlist[bathwater[1]], " .")
            print("You may move the lever (L), turn the tap (T) or discontinue your investigation into the bath (D).")
            choice = str(input())
            if choice == "L":
                bathwater[0] = input("You may move the lever to the left (0) or to the right (1).   ")
            elif choice == "T":
                bathwater[1] = input("You may turn the tap on (2) or off (3).   ")
        elif choice == "S":
            print("Above the sink is a collection of soaps. One bar of soap is bright orange and has a strange odour. You may take this with you (T) or leave it (L).")
            choice = str(input())
            if choice == "T":
                eqlist.append("soap")
        elif choice == "T":
            print("You notice nothing unusual about the toilet.")
        elif choice == "N":
            loc = 81
    elif loc == 73:
        print("Guardroom")
    elif loc == 74:
        print("You are in a corridor which runs from North to South. There is an iron door to the North with a painting of the Moon on a wall nearby (N), and two other corridors leading off to the East which are a large distance apart (EN and ES).")
        choice = str(input())
        if choice == "N":
            print("You find that the door is locked.") 
            if "iron key" in eqlist:
                print("You find the key to the door amongst your items and you walk through the doorway having opened the door.")
                udestroy("iron key")
                loc = 79
            elif 74 in findconnect(79) or 79 in findconnect(74) or "iron key" in ulist:
                print("You go North into the cylindrical room.")
            else:
                print("The key to the door is not in your possesion. You may withdraw (I) or use weapons against the door (W).") 
                choice = str(input())
                if choice == "W":
                    listweapons()
                    choice = str(input())
                    if choice == "WH":
                        print("You successfully break down the door and enter the room but the warhammer is irreparably damaged and an alarm sounds.")
                        destroy("warhammer (WH)")
                        alert = alert + 1
                    elif choice == "PC":
                        print("You successfully break down the door and an alarm sounds. You enter the room.")
                        alert = alert + 1
                        loc = 79
                    elif choice == "TB":
                        print("The time bomb is successful in breaking down the door. An alarm sounds and you enter the room.")
                        destroy("time bomb (TB)")
                        alert = alert + 1
                        loc = 79
                    elif choice == "SBB":
                        print("The sticky banana bomb is ineffective in breaking down the door.")
                        destroy("sticky banana bomb (SBB)")
                    elif choice == "EC":
                        crystsample = crystal()
                        if crystsample == "success":
                            print("An alarm sounds as you walk past the destroyed door.")
                            alert = alert + 1
                            loc = 79
                        elif crystsample == "failure":
                            print("The crystal is ineffective against the door")
                        elif crystsample == "bigfailure":
                            endgame(2)
                    else:
                        print("The weapon you chose is incapable of breaking down the door.")
        elif choice == "EN":
            loc = 58
        elif choice == "ES":
            loc = 80
    elif loc == 75:
        print("You are in a cylindrical room with a door to the South (S) and an ascending staircase (A).")
        choice = str(input())   
            if choice == "S":
                loc = 66
            elif choice == "A":
                if 79 in loclog():
                    print("You ascend the staircase.")
                else:
                    print("The staircase is barred so you may not ascend.")
    elif loc == 76:
        print("You are in a corridor which runs from North to South. To the North is a junction, with passages leading off to the North (N) and West (W). Another corridor branches off further South in an Easterly direction (E). South of this there is a door to the West (D).")
        choice = str(input())
        if choice == "N":
            loc = 66
        elif choice == "W":
            loc = 77
        elif choice == "E":
            loc = 81
        elif choice == "D":
            loc = 62
    elif loc == 77:
        print("You are in a corridor which runs from East to West. To the East is a junction with passages leading off to the North (N) and South (S). There are two doors to the South (SE and SW) and one to the North (ND). To the West, the corridor terminates in a wall with a small window in it.")
        choice = str(input())
        if choice == "N":
            loc = 66
        elif choice == "S":
            loc = 76
        elif choice == "SE":
            loc = 67
        elif choice == "SW":
            loc = 82
        elif choice == "ND":
            loc = 83
    elif loc == 78:
        print("You are standing in a corridor which runs from East to West. To the West is a descending staircase (W). To the East is a door (E).")
        choice = str(input())
        if choice == "W":
            loc = 71
        elif choice == "E":
            loc = screencheck(84, 4, 1)
    elif loc == 79:
        print("You are in a cylindrical room with a staircase and a door to the South. There are many star charts and astronomical instruments on the wall. You notice that the staircase below is shut off by a door which you can pull up from this side so you decide to do that in order to enable you to travel on this staircase. You may ascend (A) or descend (D) the staircase or leave through the door to the South (S).")
        choice = str(input())
        if choice == "A":
            loc = 85
        elif choice == "D":
            loc = 75
        elif choice == "S":
            loc = 74
    elif loc == 80:
        print("You are in a corridor which runs from East to West. There is a junction with a North-South corridor to the West (W). There are two doors on this corridor, one to the North (N) and one to the South (S).")
        choice = str(input())
        if choice == "W":
            loc = 74
        elif choice == "N":
            loc = 86
        elif choice == "S":
            loc = 87
    elif loc == 81:
        print("You are in a corridor which runs from East to West. There are doors to the North and South (N and S). There is also a junction with a North-South corridor to the West (W).")
        choice = str(input())
        if choice == "N":
            loc = 88
        elif choice == "S":
            loc = 72
        elif choice == "W":
            loc = 76
    elif loc == 82:
        print("You open the door but notice immediatly that the room has no stable floor to walk upon. Therefore, you decide that it would be wise to withdraw from the room.")
        loc = 77    
    elif loc == 83:
        print("You are standing in a small, cylindrical room with a low ceiling and doors leading off towards the North, South and West (N, S and W). There is also a small depression in the centre of the room which you could examine (D).")
        choice = str(input())
        if choice == "N":
            loc = screencheck(89, 3, 0)
        elif choice == "S":
            loc = 77
        elif choice == "W":
            loc = 91
        elif choice == "D":
            print("At the bottom of the depression, you find a small plate with the number ", fcode[1], " written upon it.")
    elif loc == 84:
        acloc = 84
        print("You are standing in a cylindrical room with no interesting features. There are doors to the South and to the West (S and W).")
        choice = str(input())
        if choice == "S":
            loc = screencheck(92, 3, 1)
        elif choice == "W":
            loc = 78
    elif loc == 85:
        print("Astronomy tower")
    elif loc == 86:
        print("You are in a rather untidy room with an elaborate wooden desk and a cabinet mounted to the wall. Many pieces of paper are scattered over both the desk and the floor. You believe this is Crultney's study. There is a door to the South.")
        print("You could investigate the desk (D), investigate the cabinet (C) or leave through the door to the South (S).")
        choice = str(input())
        if choice == "D":
            print("You cannot make sense of most of the papers on the desk.")
            if 39 in loclog:
                print("You notice a small scrap of paper recording the location of three small wheels in the mansion. The locations are described as 'basement panel', 'West wing storeroom - ground floor' and 'primary bedroom - first floor'")
        elif choice == "C":
            if "water wheel" not in eqlist and "water wheel" not in dlist:
                print("Inside the cabinet you find a water wheel. Next to it is a note explaining that it is to be used as an alternative method of propulsion for the crane. You take it with you, despite its high mass, as you feel it will be important.")
                eqlist.append("water wheel")
            else:
                print("You find nothing interesting inside the cabinet.")
        elif choice == "S":
            loc = 80
    elif loc == 87:
        print("You are standing in a small bedroom which looks as though it is not currently being used for that purpose, since there are several architechtural plans and scientific instruments piled on top of the bed.")
        print("You could investigate the instruments (I) or withdraw from the room using the door to the North (N).")
        choice = str(input())
        if choice == "I":
            print("You investigate the instruments and find nothing that you think will help you on your mission. You are about to leave when a robotic arm hiding amongst the instruments lunges out at you. You must parry the strike.")
            listweapons()
            choice = str(input())
            if choice == "BD" or choice == "GB" or choice == "SS" or choice == "SOS" or choice == "HOH":
                print("You succesfully parry the strike and the robot arm falls back down onto the bed. You do not think it was intending to strike at you.")
            elif choice == "IP":
                destroy("invisibility potion (IP)")
                print("The robotic arm strikes you despite your use of the invisibility potion. You do not think it was deliberately trying to strike you.")
                print("You are injured but not severely enough to end your mission.")
            elif choice == "LK":
                destroy("large knife (LK)")
                print("You parry the attack but the large knife was destroyed in the process of doing so.")
            elif choice == "WH":
                print("The robotic arm strikes the handle of the warhammer and destroys it.")
                destroy("warhammer (WH)")
            elif choice == "CC":
                print("The arm does not appear to be responding to the control card. It strikes you, but your injuries are minor.")
            elif choice == "CBD":
                print("The robotic arm destroys the complex brain destroyer but you are unharmed.")
                destroy("complex brain destroyer (CBD)")
            else:
                inap()
                print("You have no suitable items with which to parry the attack so you are struck by the robotic arm. It injures you but not severely enough to end your mission.")
        elif choice == "N":
            loc = 80
    elif loc == 88:
        print("bedroom 2")
    elif loc == 89:
        acloc = 89
        print("You are in a cylindrical room with doors to the North, East and South (N, E and S) and an ascending staircase (A).")
        choice = str(input())
        if choice == "N":
            loc = screencheck(90, 1, 0)
        elif choice == "E":
            loc = screencheck(93, 2, 0)
        elif choice == "S":
            loc = screencheck(83, 3, 0)
        elif choice == "A":
            loc = 94
    elif loc == 90:
        loc = screencheck(84, 3, 1)
    elif loc == 91:
        print("You are in a spacious room with a small circular hole in the wall. Near the hole is a wooden panel with indecipherable glyphs written upon it. You can investigate the hole (H) or withdraw from the room using the door to the East (E).")
        choice = str(input())
        if choice == "H":
            if "wooden rod" in ulist:
                print("You have already inserted the wooden rod into the hole so you don not need to investigate it again.")
            elif "wooden rod" in eqlist:
                print("You notice that the glyphs match those on the wooden rod. You may insert the wooden rod into the hole (I) or discontinue your investigation into the hole (D).")
                choice = str(input())
                if choice == "I":
                    udestroy("wooden rod")
                    print("You insert the wooden rod into the hole and rotate it. You do not notice any immediate effect.")
                    alert = 0
            else:
                print("You notice no useful function of the hole.")
    elif loc == 92:
        loc = screencheck(89, 1, 0)
    elif loc == 93:
        print("small room")
    elif loc == 94:
        print("You are in a cylindrical room with doors to the East and South (E and S). There is also a descending staircase (D).")
        choice = str(input())
        if choice == "E":
            if wunlock == 1:
                loc = screencheck(95, 2, 0)
            else:
                print("The door is locked. You may withdraw (I) or use weapons (W).")
                choice = str(input())
                if choice == "W":
                    listweapons()
                    choice = str(input())
                    if choice == "WH":
                        destroy("warhammer(WH)")
                        print("Your warhammer is successful in breaking the door but is destroyed by the impact.")
                        loc = screencheck(95, 2, 0)
                    elif choice == "PC":
                        print("Your portable cannon is successful in breaking the door and you advance into the room.")
                        loc = screencheck(95, 2, 0)
                    elif choice == "TB":
                        print("Your time bomb is successful in breaking the door and you advance into the room.")
                        destroy("time bomb (TB)")
                        loc = screencheck(95, 2, 0)
                    elif choice == "EC":
                        crystsample = crystal()
                        if crystsample == "success":
                            print("Your crystal breaks the door and you advance into the room.")
                            loc = screencheck(95, 2, 0)
                        elif crystsample == "failure":
                            print("You cannot remember the correct way to use the crystal.")
                        elif crystsample == "big failure":
                            endgame(2)
                    else:
                        inap()
                    if loc == 95 or loc == 54:
                        print("An alarm sounds as you break down the door.")
                        alert = alert + 1
        elif choice == "S":
            loc = screencheck(96, 3, 0)
        elif choice == "D":
            loc = 89          
    elif loc == 95:
        print("You are in a small room near the top of the West tower of the mansion. There is an ascending staircase (A) and a door to the West (W).")
        choice = str(input())
        if choice == "A":
            if towerpos == "W":
                loc = 97
            else:
                print("Unfortunately, the staircase is barred and you cannot ascend it.")
        elif choice == "W":
            loc = 94
    elif loc == 96:
        print("You are in a cylindrical room with a small depression in the centre (D) and a door to the North (N).")
        choice = str(input())
        if choice == "D":
            print("At the bottom of the depression, you find a small plate with the number ", fcode[2], " written upon it.")
        elif choice == "N":
            loc = 94
    elif loc == 97:
        if "iron key" in eqlist or "iron key" in dlist:
            iktext = "."
        else:
            iktext = " or pick up an iron key from a hook on the wall (IK)."
        print("you are at the top of the West Tower and have a great view of the mansion. You can descend the staircase (D)", iktext.)
        choice = str(input())
        if choice == "IK" and "iron key" not in eqlist and "iron key" not in dlist:
            print("You pick up the iron key")
            eqlist.append("iron key")
        elif choice == "D":
            loc = 95
    elif loc == 98:
        print("You are in an extremely large bedroom with a mirror mounted on the wall that you could investigate (M) and a door to the North (N).")
        choice = str(input())
        if choice == "M":
            print("You notice nothing interesting about the mirror.")
        elif choice == "N":
            loc = 58
    
        
        
        
        
        
        
        
        
    loclog.append(loc)
    if alert >= 4 and observe == 1:
        print("You hear a long continuous alarm and notice that all doors have locked and that your passage throught the mansion has become impossible.")
        endgame(2)
    if alert == 3:
        if randint(1, 5) == 1:
            
    if alert == 2:
        if randint(1, 10) == 1:
            
              
              
              
                          
