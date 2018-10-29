print("The adventures of Broughtly in Crultney Mansion")
loc = 1
import random
coins = 8
eqlist = list()
swicob = "0"
ask = "A"
alert = 0
window = 1
stairrobot = 1
towertext = "Your weapon successfully destroys the door and you walk in."
islandtext = "The island is small and the main feature is the mansion which looks majestic and intimidating. You can see a barbed wire fence surrounding this side of the mansion."
while  True:
    def inap():
        print("The item you have chosen is not appropriate for the current situation")
    def equip():
        print("You possess ", eqlist,)     
    def destroy(n):
        x = 0
        while n in eqlist:
            if eqlist[x] == n:
                del eqlist[x]
            x = x + 1
    def crystal():
        print("You reach for the crystal and observe that it is a rombohedron with one face being marked with a symbol in each corner.")
        print("In clockwise order, starting with the pentagon, these are a pentagon, a triangle, a square and a hexagon")
        print("Do you point the crystal at the target and strike one of the symbols (S) or do you throw the crystal at the target (T).")
        choice = str(input())
        if choice == "S":
            strike = str(input("Which symbol do you strike?   "))
            if strike == "HEXAGON":
                destroy("energy crystal (EC)")
                return "success"
            elif strike != "HEXAGON":
                return "failure"
        else:
            if random.randint(1, 4) == 4:
                print("The crystal strikes the target and releases a beam of energy which incinerates you")
                return "big failure"
            else:
                print("The crystal bounces off the target without releasing a beam of energy")
                return "failure"
    def endgame(n):
        print(eqlist)
        print("You have failed in your mission.")
        print("You completed ", n, " out of 5 major events successfully.")
        end = input() 
    def listweapons():
        print("You can attempt to use any of the folllowing:", eqlist)
    if loc == 1:
        print("The year is 1971 and Crultney, a famous architect and inventor has not been seen or heard from for several weeks. You are Broughtly, a skilled monkey ninja and your mission is to travel to his mansion and investigate. You should be aware that there are many traps and hidden rooms in the mansion.")
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
        print("The available items are a shortsword (SS, 2 coins), the shield of safety (SOS, 3 coins), a strength potion (SP, 3 coins), the warhammer (W, 4 coins), the golden blade (G, 5 coins) and the portable cannon (P, 6 coins)")
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
            elif choice  == "W":
                eqlist.append("warhammer (WH)")
                coins = coins - 4
            elif choice == "G":
                eqlist.append("golden blade (GB)")
                coins = coins - 5
            elif choice == "P":
                eqlist.append("portable cannon (PC)")
                coins = coins - 6
            if coins < 0:
                print("You could not afford that item")
                loc = 999
        loc = 5
    elif loc == 4:
        print("Geelophisis welcomes you into his lab but warns you that he has not invented many new items since you mission with the Robo Lion in 1963")
        print("Geelophisis first gives you a stone rod 300 mm long with symbols protruding from it at regular intervals along it. This was given to him by Crultney and which he believes willbe useful on your mission.")
        eqlist.append("stone rod (SR)")
        print("He shows you his inventions and says that you can choose two of them.")
        print("You can ask Geelophisis about an invention by typing the item code when prompted")
        print("The inventions are: complex brain destroyer (CBD), invisibility potion (IP), magic map (MM), strength potion (SP) and the energy crystal (E)")
        while ask != "NO":
            ask = str(input("Do you want to ask Geelophisis about an invention?   "))
            if ask == "CBD":
                print("Geelophisis tells you that the current version of the CBD is much safer than the prototype used in the 1960s. He says that it should only be used on intelligent opponents with larger brains as this makes it easier for the CBD to identify them.")
            elif ask == "IP":
                print("Geelophisis tells you that this is the standard invisibility potion used by the ninjas in Oland and it makes the user invisible for 2 minutes")
            elif ask == "SP":
                print("Geelophisis tells you that this invention grants a sudden burst of extreme strength to the user for a short period of time.")
            elif ask == "MM":
                print("Geelophisis tells you that this invention will allow you to find your way to any place but it can only be used once")
            elif ask == "E":
                print("Geelophisis tells you that the energy crystal is a highly dangerous weapon that will release a blast of energy from the end of the crystal marked with a triangle when the end marked with a hexagon is struck. It can only be used once as the crystal is consumed on use.")
        choice1 = str(input("choice 1   "))
        choice2 = str(input("choice 2   "))
        if choice1 == "CBD" or choice2 == "CBD":
            eqlist.append("CPD")
        if choice1 == "IP" or choice2 == "IP":
            eqlist.append("invisibility potion (IP)")
        if choice1 == "SP" or choice2 == "SP":
            eqlist.append("strength potion (SP)")
        if choice1 == "MM" or choice2== "MM":
            eqlist.append("magical map (MM)")
        if choice1 == "E" or choice2 == "E":
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
        print("Geelophisis tells you that Crultney Mansion is 3 storeys high and also has a set of underground rooms. He tells you that the easiest way to access the island is by first travelling to Ooville and then departing for the island in a smaller vessel")
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
        choice = str(input())
        if choice == "O":
            loc = 11
        elif choice == "C":
            coins = coins - 2
            loc = 12
    elif loc == 8:
        print("The ninja leaders tell you that there will likely be many robots in Crultney Mansion and these will be difficult to fight with conventional ninja weapons. Therefore they advise you to visit the Gaurilis army base in Ooville in order to obtain more suitable weapons.")
        print("The ninja leaders also show you a map of the islands and the surrounding area")
        #map#
        print("You now travel to the port.")
        loc = 7
    elif loc == 9:
        print("You arrive at Furfoot's Palace but he tells you that he does not have much advice to give you but he can tell you that Crultney's main living and work areas are on the irst floor of the mansion.")
        print("After the meeting with Furfoot, you find a banana coin on the ground near the palace and you put this in your pocket.")
        print("You now travel to the port.")
        loc = 7
    elif loc == 10:
        print("After travelling for a great length of time over the sea, you can see the island of Ooville.")
        print("You could land the helicopter in Ooville (O) or travel South to try to find Crultney's Island(C)")
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
        else:
            loc = 18
    elif loc == 13:
        print("As you approach the island, you can see the majestic mansion in front of you. Suddenly, a loud siren sounds from the mansion. You could try to land near the mansion (M) or fly back towards Ooville (O).")
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
        print("The gorillas welcome you into their base and give you the choice of either a sticky banana bomb (SBB) or a medical kit (MK) to use on your mission. They tell you to take a rowing boat to the island as this is cheaper than the ferry.")
        choice = str(input())
        if choice == "SBB":
            eqlist.append("sticky banana bomb (SBB)")
        elif choice == "MK":
            eqlist.append("medical kit (MK)")
        print("You return to the town centre.")
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
        print("You are approaching the island from the South and you can see a small pier directly ahead of you (P) and a sandy beach to the East (B). Alternatively, you could circle around the island to the North side (N)")
        choice = str(input())
        if choice == "P":
            loc = 24
        elif choice == "B":
            loc = 23
            print("You disembark from the boat and climb out onto the beach.")
        elif choice == "N":
            loc = 21
    elif loc == 18:
        print("You carry on through the stormy weather but some of your equipment is washed overboard by the waves.")
        text6 = random.choice(eqlist)
        print(text6, " is lost")
        destroy(text6)
        print("The storm has now ended and you continue on towards the island. ", islandtext)
        print("You are approaching the island from the South and you can see a small pier directly ahead of you (P) and a sandy beach to the East (B). Alternatively, you could circle around the island to the North side (N)")
        choice = str(input())
        if choice == "P":
            print("You dock at the pier and disembark.")
            loc = 24
        elif choice == "B":
            loc = 23
            print("You disembark from the boat and climb out onto the beach.")
        elif choice == "N":
            loc = 21
    elif loc == 19:
        print("You land at the airport in Ooville Town and arrange for a local pilot to return the helicopter to Geelophisis.")
        loc = 11
    elif loc == 20:
        print("You attempt to land the helicopter but you notice an armoured turret on the 2nd floor turning to face you. You are shot down before you can react.")
        print("You scramble out from the wreckage of the helicopter and notice that some of your equipment has beeen destroyed in the collision.")
        text7 = random.choice(eqlist)
        print(text7, " is lost")
        destroy(text7)
        alert = alert + 1
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
                window = 0
            elif choice == "SS":
                print("The window shatters and an alarm sounds. Unfortunately, the reinforced glass of the window has broken your shortsword. You enter the room.")
                alert = alert + 1
                destroy("short sword (SS)")
                loc = 26
                window = 0
            elif choice == "TS":
                print("Unfortunately, the glass of this window is reinforced so the throwing stars bounce off and fall into the sea.")
                destroy("throwing stars (TS)")
            elif choice == "TB":
                print("You place the bomb and duck back down into the boat. A few seconds later, a loud explosion occurs and an alarm sounds nside the mansion. You walk into the room through the large hole that has beeen created in the window.")
                destroy("time bomb (TB)")
                alert= alert + 1
                loc = 26
                window = 0
            elif choice == "PC":
                window = 0
                loc = 26
                print("You load the cannon and fire at the window. The window shatters and an alarm sounds. You enter the room.")
            elif choice == "EC":
                if  crystal() == "success":
                    print("The window is incinerated and an alarm sounds. You enter the room.")
                    loc = 26
                    window = 0
                elif crystal() == "failure":
                    destroy("energy crystal (EC)")
                    print("After the improper use, the crystal falls into the sea.")
                elif crystal() == "big failure":
                    endgame(1)
            elif choice == "CBD":
                inap()
            elif choice == "SBB":
                print("You pull the bomb out of your pocket and place it near the window but it explodes before you can take cover.")
                print("The window shatters and an alarm sounds. Unfortunately you are injured by the bomb and the broken glass.")
                if "medical kit (MK)" in eqlist:
                    print("Since you have a medical kit, you use it and after recovering, you enter the room.")
                    destroy(medical kit (MK))
                    loc = 26
                    window = 0
                else:
                    print("Your injuries are too great to continue. You return to Ooville and Crultney is never seen again")
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
            print("The gorillas overwhelm you and detain you. They take you to be questioned at their base in Gorillia Monkeyland.")
            endgame(0)
        elif choice == "S":
            print("The gorillas recognise your item and will allow you to continue your journey. They also give you a map of the nearby islands if you do not already have one.")
            loc = 17
    elif loc == 23:
        print("The mansion is to the North of you and there is a barbed wire fence ahead of you.")
        print("You can use a weapon to break the barbed wire (W), or you could go East to try to find another way to access the mansion (E).")
        choice = str(input())
        if choice == "W":
            place = C
            loc = 30
            #move to loc 30#
            listweapons()
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
            elif choice == "EC":
                if  crystal() == "success":
                    print("The barbed wire is destroyed and you walk towards the mansion.")
                    loc = 27
                elif crystal() == "failure":
                    destroy("energy crystal (EC)")
                    print("The crystal rolls away into the middle of the wire")
                elif crystal() == "big failure":
                    endgame(1)           
        elif choice == "E":
            print("The barbed wire continues on the Eastern side of the mansion until it reaches the sea on the North coast.")
            loc = 25
    elif loc == 24:
        print("There is a small path ahead which leads up to a gate in a barbed wire fence. You can see the mansion beyond the fence and to the West you can see a tower in the distance next to the fence.")
        print("You can attempt to breach the fence (F), attempt to open the gate (G) or go West towards the tower (W).")
        choice = str(input())
        if choice == "F":
            place = W
            loc = 30
        elif choice == "G":
            print("The gate looks very well armoured so only the most powerful weapons will be capable of breaching it.")
            print("The gate also has a handle which you could attempt to open (H), and there is also a box nearby with several switches (S).")
            listweapons()
            print("You may also retreat to the South (R).")
            choice = str(input())
            if choice == "H":
                swicobs = random.randint(0, 9999)
                if swicob != swicobs:
                    print("The gate will not open and an alarm sounds.")
                    alert = alert + 1
                elif swicob == swicobs and alert < 2:
                    print("The gate opens and you walk up to the front of the mansion.")
                    loc = 27
            elif choice == "S":
                print("There are four switches which can each be set to any position between 0 and 9. Currently they are all set to 0.")
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
                if crystal() == "success":
                    alert = alert + 1
                    print("The crystal destroys the gate. However, you hear an alarm sound so you advance cautiously towards the mansion.")
                    loc = 27
                elif crystal() == "failure":
                    print("After the improper use, you pick up the crystal.")
                elif crystal() == "big failure":
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
                    if crystal() == "success":
                        print(towertext)
                        loc = 28
                    elif crystal() == "failure":
                        print("You used the crystal improperly.")
                    elif crystal() == "big failure":
                        endgame(1)
                else:
                    inap()
    elif loc == 25:
        print("you are East of the mansion and a barbed wire fence separates you from the mansion. You notice a square garden area enclosed with hedges nearby.")
        print("You can try to breach the fence (F), enter the garden area (G) or go to the South West (SW).")
        choice = str(input())
        if choice == "F":
            place = E
            loc = 30
        elif choice == "SW":
            loc = 23
        elif choice == "G":
            print("You enter the garden. In the centre of the garden is a large cylindrical stone with a hole in the centre set into the ground.")
            print("In the North of the garden is a pool containing aquatic plants. there is a wooden bench in each of the other sides of the garden and these benches are surrounded by numerous plant species.")
            print("You can investigate the cylindrical stone (S) or withdraw from the garden (W).")
            choice = str(input())
            if choice == "S":
                print("The stone looks rather old and worn. There are some strange symbols on the stone but they are difficult to read and understand.")
                if "stonerod" in eqlist:
                    print("You immediatly notice that the symbols on the stone are similar to those on the stone rod given to you by Geelophisis.")
                    print("You can attempt to insert the rod into the hole in the stone (S) or abandon your examination of the stone (A).")
                    choice = str(input())
                    if choice == "S":
                        destroy("stonerod")
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
                                eqlist.append("woodenrod")
                                eqlist.append("metalrod")
                            elif choice == "B":
                                eqlist.append("information book")
                                print("You look in the book and find that it is about Crultney mansion. You decide to take the book with you but much of it is in a language you cannot understand.")
    elif loc == 26:
        print("You are in a circular room with bookshelves all the way along the wall except for a gap in the East where there is a fireplace.")
        if window == 1:
            print("There is also a large window in the North looking out towards the Sea.")
        print("The only door is to the South.")
        print("You can go through the door (S), investigate the bookshelf (B) or investigate the fireplace (F).")
        choice = str(input())
        if choice == "S":
            loc = 29
        elif choice == "B":
            print("Inserted into one of the books you find a map of the mansion.")
            #map#
        elif choice == "F":
            print("You crawl into the fireplace and find a narrow passage to the side. The passage leads up to a small black door with no handle.")
            print("There is a lever for opening the door but the handle is missing and it is too heavy to move without the handle.")
            print("You can withdraw into the room (W) or use an object in your possesion to stand in for the handle (H).")
            choice = str(input())
            if choice == "H":
                if "shortsword" in eqlist or "metalrod" in eqlist or "goldenblade" in eqlist or "stonerod" in eqlist:
                    print("You find a suitable item and open the door.")
                    print("The room is very small and you have to crouch down to get in.")
                    print("In the room is a low wooden table with a green candle and a set of rusted keys on it.")
                    print("You take the items and withdraw into the cylindrical room.")
                    eqlist.append("gcandle")
                    eqlist.append("rusted keys")
                else:
                    print("You have no suitable items so you withdraw into the cylindrical room.")
                    
    elif loc == 27:
        print("You are standing directly in front of the mansion and you can see a large metal door directly ahead of you. This is the main entrance to the mansion.")
        print("To the West is a shed which is connected directly to the mansion.")
        print("You can attempt to get in through the main door (M), investigate the shed (S) or walk around to the East side of the mansion (E).")
        choice = str(input())
        if choice == "M":
            print("The main door looks very well protected with an elaborate security system.")
            print("You may use a weapon to break down the door or you could try to scale the wall nearby and enter through a window on the 1st floor (SW).")
            choice = str(input())
            if choice == "SW":
                if "super strong rope (SSR)" in eqlist:
                    print("You use your super strong rope to successfully climb up to the window. However, an alarm sounds.")
                    alert = alert + 1
                    print("You hurriedly use an object from your equipment bag to smash the window and you climb inside. Unfortunately, you are forced to leave behind the rope since you cannot reach it through the window without alerting the CCTV camera again.")
                    destroy("super strong rope (SSR)")
                    
        elif choice == "S":
            print("You walk towards the shed and notice that this door is much flimsier and is made from wood.")
            print("To the West of the shed is an impassable rock formation. You can attempt to gain access to the shed using the door (D) or you can return to the front of the mansion (M).")
            choice = str(input())
            if choice == "S":
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
                    if crystal() == "success":
                        print("You destroy the door and enter the shed.")
                        loc = 39
                    elif crystal() == "big failure":
                        endgame(1)
                elif choice == "SP":
                    destroy("strength potion (SP)")
                    print("You destroy the door and enter the shed.")
                else:
                    inap()
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
            print("You climb the stairs into another room similar to the one below. Before you have a chance to look for clues, a bottle of green liquid suddenly shoots out from the room towards you.")
            print("You must hold up a piece of equipment to protect yourself.")
            tomrin = 1
            while tomrin == 1:
                eqloss = random.choice(eqlist)
                if eqloss == "timebomb" or eqloss == "stickybomb" or eqloss == "invisibility" or eqloss == "strengthp":
                    tomrin = 1
                else:
                    tomrin = 0
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
        print("30")
        #move to loc 30#
    elif loc == 31:
        print("You are in a corridor which runs from East to West. There is a junction with a North - South corridor to the West (W). There are two grey doors opposite each other in the Eastern side of the passage. (NED) and (SED). There is another door to the North in the WEstern side of the passage (WD).")
        choice = str(input())
        if choice == "W":
            loc = 29
        elif choice = "NED":
            loc = 34
        elif choice = "SED":
            loc = 35
        elif choice = "WD":
            loc = 33
    elif loc == 32:
        print("You are in a corridor which runs from North to South. To the South is the main door of the mansion. There are passages leading off to the East and West (E) and (W). You could also follow the corridor to the North (N).")
        choice = str(input())
        if choice == "E":
            loc = 36
        elif choice == "W":
            loc = 37
        elif choice == "N":
            loc = 29
    elif loc == 33:
        if rustdoor == 1:
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
                    if crystal() == "success":
                        print("Your crystal breaks the door and you advance into the room.")
                        loc = 38
                    elif crystal() == "failure":
                        print("You cannot remember the correct way to use the crystal.")
                    elif crystal() == "big failure":
                        endgame(2)
                else:
                    inap()
    elif loc == 34:
        print("The door is open and you walk out onto a spiral staircase which has stairs leading off upwards and downwards.")
        if stairrobot = 1:
            print("As you step out onto the stairs, you hear a sliding noise and you see a sharp blade mounted to the banister sliding down towards you.")
            print("You must use a piece of equipment to defend against the attack")
            listweapons()
            choice = str(input())
            if choice == "BD" or choice == "SS" or choice == "WH" or choice == "CBD":
                print("You parry the attack but your weapon is irrepairably damaged due to the impact.")
                stairrobot = 0
                if choice == "BD":
                    destroy("black dagger (BD)")
                elif choice == "SS":
                    destroy("shortsword (SS)")
                elif choice == "CBD":
                    destroy("CBD")
                else:
                    destroy("warhammer (WH)")
            elif choice == "GB" or choice == "SOS" or choice == "HOH":
                stairrobot = 0
                print("You successfully defend against the attack and your weapon is undamaged.")
            else:
                inap()
        else:
            Print("You can go upwards (U) or downwards (D) on the stairs or exit at this level (E).")
            choice = str(input())
            if choice == "U":
                loc = 40
            elif choice == "D":
                loc = 41
            elif choice == "E":
                loc = 31 
    elif loc == 35:
        print("You walk into an elaborately furnished dining room. A large table dominates the centre of the room. On the table are several empty plates, pieces of cutlery and candles.")
        print("There are doors to the North (N) and South (S). You could also stay in this room to investigate further (I).")
        choice = str(input())
        if choice == "N":
            loc = 31
        elif choice == "S":
            loc = 42
        elif choice == "I":
            print("You can investigate the plates and cutlery (P), the candles (C) or the lighting (L).")
            
        
               
                
                            
                            
                

                

                
                
                
                    
                

        
                

                    
                    
                    
            
        
 
        
        
                
                
        
            
        
        
        
            
        

        
        
        
              
    
        
        
        

            
        
                  
