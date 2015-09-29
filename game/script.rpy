# You can place the script of your game in this file.
# Declare characters used by this game.
#get rid of menu options??? after weapon pickup, event happens, objective complete, enemy is killed, etc.
define j = Character('John Doe', color="#c8ffc8")
define n = Character (' ', color = "#c8ffc8")
image road = im.Scale("road1.jpg",900,600)
image car = im.Scale("car2.png",150,80)
image hallway = im.Scale("hallway2.png",900,600)
image garage = im.Scale("garage.png",900,600)
image ballroom = im.Scale("ballroom_reg.jpg",900,600)
image mainhall = im.Scale("mainhall.png",900,600)
image mansion = im.Scale("Mansion.jpg",900,600)
image mechnest = im.Scale("mech-nest-filler.jpg",900,600)
image Lab = im.Scale("lab-filler.jpg",900,600)
image Dungeon = im.Scale("dungeon.png",900,600)
image Library = im.Scale("library.png",900,600)
image death = im.Scale("death.jpg",900,600)
image tunnel = im.Scale("tunnel-filler.jpg",900,600)

define diss = Dissolve(1.0)

# The game starts here.
label start:
    play sound "rain.mp3" fadeout 1.0 fadein 1.0 loop
    scene road
    with fade
    call setupItemSystem
    python:
        garageHuskIsAlive = True
        secretPassageActive = False
        playerName = renpy.input("What is your name?") #Take the players name
    play music "Private Reflection.mp3" fadein 1.0 loop
    scene road
    with fade
    n "You're driving down the road in your old beat up Chevy. It's raining pretty heavily and you don't recognize your surroudings."
    
    stop sound fadeout 1.0
    play sound "tree_fall.mp3" fadeout 1.0 
    play sound "screech_crash.mp3"
    show car at Position(xpos=335, ypos=350, xanchor=0, yanchor=0)
    with diss
    with hpunch
    
    n "Out of nowhere a tree falls into the road, causing you to swerve and crash."
    
    play sound "rain.mp3" fadein 2.0 loop
    
    n "It's raining hard and you need to find a place to go. You see a faint glow in the distance."
    
    menu: 
        with dissolve
        "Go towards the light...":
            jump choice_start
        
        "Stay in the car":
            jump choice_dead
        
            label choice_start:
                $ menu_flag = True
                stop sound fadeout 2.0
                play sound "car_door_close.mp3"
                hide car
                hide road
                play sound "woods_walking.mp3" fadein 1.0
                show mansion
                with dissolve
                stop sound fadeout 2.0
                play sound "rain.mp3" fadein 2.0 loop
                
                n "You see the source of the light, a large mansion at the end of the road."
                menu:      
                    with dissolve
                    "Go to the mansion":
                        jump choice_tothemansion
                    
                        label choice_tothemansion:
                            $ menu_flag = True
                            hide mansion
                            stop sound fadeout 2.0
                            play sound "door open.mp3" 
                            show mainhall
                            with fade
                            stop sound fadeout 1.0
                            
                            stop music
                            play sound "doorslam.mp3" 
                            queue sound "evillaugh.mp3" 
                    
                            "You have now entered the Malevolent Mansion."
                            
                           
                        
                            jump entrance_hall
                 
                
                label choice_dead:
                $ menu_flag = True
                hide car
                #hide road
                stop sound 
                stop music 
                play sound "car_explosion.mp3"
                
                n "You died in a fiery explosion."
                
    
                jump instant_death
                
#EVAN'S STUFF#
define h = Character('Harold', color="#c8ffc8")
define a = Character('Avidem', color="#c8ffc8")
define p = Character('Phoebe', color="#c8ffc8")
define b = Character('Archie', color="#c8ffc8")


# The game starts here.
init python:
    style.tips_button.xminimum = 400
    #This part is for displaying sanity
    dead = False
    metAvidem = False
    metHarold = False
    metPhoebe = False
    metArchie = False
    def showInventory(n, b): #Show the inventory in a ui.frame on top of the current frame
        ui.frame()
        c = "'s inventory: "
        d = n + c
        ui.text(d + b.__str__())
        b.displaySanityAndHealth()

    class Item:
        def __init__(self, name, description, isWeapon, isHeavy):
            self.name = name
            self.isWeapon = isWeapon
            self.isHeavy = isHeavy
            self.description = description
        def __str__(self): #return the items name from the to string method
            return self.name

        def getDescription(self): #Return the description of the item
            return self.description
            

    class Inventory:
        def __init__(self):
            self.items = [Item("Backpack","Your old Backpack that you've had for many years",False,False)] #Adds a backpack to your inventory, you cant toss it. Might get rid of this code tho we don't really need to have the backpack in your inventory its just neat to have
            self.sanity = 100
            self.lives = 1

        def __contains__(self, item):
            return item in self.items

        def pickUpWeapon(self, item):
            if (item not in self.items):
                if (item.isWeapon): #TODO Ok now we need to see if we already have a heavy slash light weapon
                    self.items.append(item)#Well do that later, I'm working on ground work
                    roomItems.remove(item)
                else:
                    self.items.append(item)
                    lastPickup = item
                    roomItems.remove(item)
                return True
            return False

        def updateSanity(self, deltaS): #Change sanity by a positive or negative factor
            self.sanity += deltaS
            if self.sanity <= 0:
                dead = True
                ##!! TODO: Figure out how to end the game from a py script. Otherwise I can use a renpy helper method to call it and end it from there... Maybe? !!##

        def __str__(self): #To string
            ret = ""
            for item in self.items:
                ret += item.__str__() + ", " #Lists all the items in the bag separated by ", "
            ret = ret[:-2] #Chops the last ", " off of the string 
            return ret
 
        def displaySanityAndHealth(self):
            #if showSanity:   
                ui.frame(ypos = 50, xpos = 0) #This is optional. It adds a frame around the text.
                ui.text("Sanity: " + self.sanity.__str__() + "%")
                ui.bar(100,self.sanity,ypos = 100)
                ui.frame(ypos = 150, xpos = 0)
                ui.text("Lives Left: " + self.lives.__str__())
            #config.overlay_functions.append(displaySanityAndHealth())

        class Room:
            def __init__(self, name, items, obstacles, npcs):
                self.name = name               
                self.items = items
                self.obstacles = obstacles                
                self.npcs = npcs
            def __str__():
                return self.name

            def __contains__(item):
                if item in self.items:
                    return True
                else:
                    return False

            def getItems():
                return self.items

            def getNpcs():
                return self.npcs

            def getObstacles():
                return self.obstacles

label changeRoom (room):
    python:
        currentRoom = room
        currentRoomItems = room.getItems()
        currentRoomNPCs = room.getNpcs()
        currentRoomObstacles = room.getObstacles()

label goInsane:
    "You've lost all your sanity. You lose your mind and wander the halls of the Malevolent Mansion till the end of eternity."
    "Game Over"
    jump choice_end_game
    return

label die:
    "You've run out of medical supplies, and met your demise."
    "Game Over"
    jump choice_end_game
    return

label talkToHarold(attacking):
    if not attacking:
        if not metHarold:
            h "W-what? W-w-who's there? W-what do you want?"
            $metHarold = True
        else:
            h "W-what? W-w-who's there? Oh it's you a-again, what do you w-want?"
        menu:
            "Who are you?":
                h "M-My name is H-H-Harold. I-I am a historian from a-around here and I had h-heard some legends about this p-place."
                h "B-but I've seen such h-horrible things here! I-I will go n-no further"
            "How do I escape?":
                h "One of the l-legends I heard about t-this place told of a tunnel and a r-riddle."
                h "I-If you can find it and s-solve the puzzle then you mi-might escape."
            "Do you know anything about other people in the mansion?" if metAvidem or metPhoebe or metArchie:
                h "Y-yeah, I know Avidem, B-Basiltine, a-a-and Phoebe" 
                h "W-who do you w-want to h-hear about?"
                menu:
                    "Avidem" if metAvidem:
                        h "Hmm, the lady seems n-nice, but awfully c-calm."
                    "Basiltine" if metArchie:
                        h "That man is a few cards short of a d-deck. I-I'd be careful around h-him."
                    "Phoebe" if metPhoebe:
                        h "That young w-woman didn't h-have much to say to m-me. She just muttered about s-secrets."
    else:
        h "AHG MONSTER!"
        "Harold takes out a revolver from the pile of laundry and starts shooting"
        "One of the bullets pierces your lung and you die..."    
        call updateLives(1)
        "LUCKILY you have your first aid kit! Now you're alive again but you had to use some of your supplies"
    return

label talkToAvidem(attacking):
    if not attacking:
        if not metAvidem:
            a "Hm? Ah hello, who are you? Do you need any advice?"
            $metAvidem = True
        else:
            a "Hello again %(playerName)s, what would you like advice on now?"
        menu:
            "Who are you?":
                a "I'm Avidem"
                a "I'm trapped in this place like many of it's occupants."
                a "I was driving past one night when my vehicle broke down and I was forced to take shelter here."
                a "It seems like I've been here forever..."
            "How do I get out of here?":
                if PlainKey1 not in bag:
                    a "I've heard of an escape route, but its a precious secret of mine. If I tell you, you'll have to fetch me something even more valuable."
                    a "I hid it away long ago to keep it safe, but now I yearn for it..."
                    a "Retrieve it and I'll tell you the secret. You'll need this to find it"
                    $bag.items.append(PlainKey1)
                    $lastPickup = PlainKey1
                    "%(playerName)s got a Plain Key!"
                else:
                    a "Do you have what I sent you for?"
                    menu:
                        "Yes":
                            b "Really?"#IS THIS SUPPOSED TO BE B OR A? -JACK
                            call giveAvidemTheGem()
                        "No":
                            b "Well hurry up and find it. I really need it back soon."
            "Do you know anything about other people in the mansion?" if metHarold or metPhoebe or metArchie:#SHOULD THE IF GO BEFORE THE OPTION? -JACK
                menu:
                    "Harold" if metHarold:
                        h "The laundry-pile man?"#SAME HERE-JACK
                        h "He may seem meek and harmless, but fear can make men do strange things."
                    "Basiltine" if metArchie:
                        h "Poor soul, he's been here so long he had to create a whole other world to live in, to keep from becoming a gibbering Husk."
                    "Phoebe" if metPhoebe:
                        h "That girl was our latest addition before you. I don't think she's a fan of the weather."


    else:
        a "Fool, you would attack the master of this house?"
        a "BEGONE!"
        #push out of room
        call updateSanity(-50)
        #orangeRoom.items.append(PlainKey1)
    return

label giveAvidemTheGem():
    a "Do you have it? The sanguine rose? GIVE IT TO ME!"
    if Gem in bag:
        label back:
            menu: 
                "Ok":
                    $bag.items.remove(Gem)
                    a "Ah, my beauty! It's been much too long, my power has waned so. Courier, you may leave."
                    a "For your service, if you are still sane..."
                    call updateSanity(-50)
                    "%(playerName)s's sanity fell by 50" #IDK 50 is a lot, we might want to lower this
                    #kicks out of the room
                    #door locks
                "No":
                    a "WHAT, HOW DARE YOU DEFY ME! Give me that gem!!!"
                    jump back
    else:
        menu:
            "Yes":
                a "No you don't! Go and find it!"
            "No":
                a "Well go find it!"
    return

label talkToPhoebe(attacking):
    if not attacking:
        if not metPhoebe:
            p "You have arrived. Phoebe thinks you are late."
            $metPhoebe = True
        else:
            p "You return, what do you want from Phoebe?"
        menu:
            "Who are you?":
                p "Phoebe's name is Phoebe. She was drawn here by its aura."
                p "Such emotion... Such darkness..."
                p"But now Phoebe is trapped, she does not like the storm"
            "How do I get out of here?":
                p "The storm of madness releases no-one."
                p "Phoebe tried, and now Phoebe is dead."
            "Do you know anything about other people in the mansion?" if metArchie or metAvidem or metHarold:
                p "Sure, Phoebe knows about Avidem, Basiltine, and Harold" 
                p "Who would you like Phoebe to tell you about?"
                menu:
                    "Avidem" if metAvidem:
                        p "Unnerving, calm in the storm"
                    "Basiltine" if metArchie:
                        p "Funny man, lives in his own world. Phoebe wonders if hes foolish or fortunate..."
                    "Harold" if metHarold:
                        p "Does he hide from the world, or hide something from the world"

    else:
        p "That was unwise of you"
        "Phoebe has a knife! She stabs you right in the heart."
        "LUCKILY you have your first aid kit! Now you're alive again but you had to use some of your supplies"
        call updateLives(1)
    return

label talkToBasiltine:
    $attacking = False
    if not attacking:
        if not metArchie:
            b "You desire an audience with the emperor? Very well, ask away"
            $metArchie = True
        else:
            b "You return to the emperor, what do you wish from him now"
        menu:
            "Who are you?":
                b "You don't know who I am?!? But I am his Glorious Highness Basiltine von Ludwig XIII, appointed by the Heavens, Long May He Reign!"
                b "But you may call me Archie"
            "How do I get out of here?":
                if GoldNugget not in bag:
                    b "I can not see why you would wish to leave my Empire, but if that is truly so I can help you if you help me"
                    b "I have misplaced my crown, find it and I will grant you the keys to the empire"
                    b "However, impostor crowns lurk about. Use this to determine the true crown"
                    "%(playerName)s got a gold nugget"
                    $bag.items.append(GoldNugget)
                else:
                    b "Have you found my crown yet?"
                    menu:
                        "Yes":
                            b "Really?"
                            jump giveBasiltineCrown
                        "No":
                            b "Well hurry up and find it. The emperor grows impatient!"
            "Do you know anything about other people in the mansion?" if metHarold or metPhoebe or metAvidem:
                menu:
                    "Harold" if metHarold:
                        h "The record keeper has intellect, but lacks backbone."
                        h "I don't think I've ever seen him leave his Tower of Antiquity."
                    "Avidem" if metAvidem:
                        h "Queen Avidem? She is a calm advisor, and a potent force."
                        h "Sometimes I feel like she has more power than me..."
                        h "But that is nonsense, I'm the Emperor!" 
                    "Phoebe" if metPhoebe:
                        h "Ahh, the soothsayer. She is useful, but sometimes gives ominous predictions."

    else:
        b "Who dares assault them emperor?!"
        "Basiltine takes a wrench from behind him and beats you over the head with it"
        "You black out"
        "LUCKILY you have your first aid kit! Now you're alive again but you had to use some of your supplies"
        call updateLives(1)

    jump to_mech_nest

label giveBasiltineCrown():
    if Crown in bag:
        b "Do you bring me my crown?"
        menu:
            "Yes, here it is":
                b "Ahh yes, my precious. Thank you peasant, for your work you may have this"
                "Archie gave you the keys to the front door" #SHOULD WE GET RID OF THIS, SINCE THE ALPHAS OVER? -JACK
                "You make a b-line for the exit and you finally escape"
                jump escape
                #"%(playerName)s got a ring of keys"
                #$bag.items.append(Item("Ring of Keys", "A ring of assorted keys that look like they most likely belong to some old cars", False, False))
            "No":
                b "Well hurry up, the emperor is growing impatient"
    elif FakeCrown in bag:
        b "Do you bring me my crown?"
        menu:
            "Yes, here it is":
                b "This is not the real crown! This is but an impostor!"
                b "GET OUT!"
                call updateSanity(-10)
                #Kick out of room
            "No":
                b "Well hurry up, the emperor is growing impatient"
    else:
        b "You don't have it! Come back when you have it"
    jump to_mech_nest

label inventory:
    $showInventory(playerName,bag)
    "%(playerName)s's Inventory"
    return

label updateSanity(num):
    $bag.updateSanity(num)
    if bag.sanity <= 0:
        jump goInsane
    return

label updateLives(num):
    $bag.lives -= num
    if bag.lives <= 0:
        jump die
    return

label pickItems (roomItems = []): #BOOM Modular code
    python:
        roomItemsLength = len(roomItems) #Tell the script what items are in the room
    if roomItemsLength > 0:
        "There are %(roomItemsLength)d items in this room. Which would you like?"
        menu:
            "Chainsaw" if Chainsaw in roomItems:
                $justPickedUpAnItem = bag.pickUpWeapon(Chainsaw)
                $if justPickedUpAnItem: lastPickup = Chainsaw
            "Knife" if Knife in roomItems:
                $justPickedUpAnItem = bag.pickUpWeapon(Knife)
                $if justPickedUpAnItem: lastPickup = Knife
            "Crow Bar" if CrowBar in roomItems:
                $justPickedUpAnItem = bag.pickUpWeapon(CrowBar)         #We Will need extra if statements for weapons regarding their weight so I will do that later
                $if justPickedUpAnItem: lastPickup = CrowBar
            "Idol" if Idol in roomItems:
                $justPickedUpAnItem = bag.pickUpWeapon(Idol)
                $if justPickedUpAnItem: lastPickup = Idol
        python:
            desc = lastPickup.getDescription()
        if justPickedUpAnItem:
            "%(playerName)s picked up a %(lastPickup)s: %(desc)s"
        else: 
            "%(playerName)s couldn't pick that up..."
    else:
        "There are no items in this room..."
    return

label setupItemSystem:
    python:
        ###DEFINE ALL ITEMS HERE!!!###
        bag = Inventory()
        Chainsaw = Item("Chainsaw","You know whats good",True,True)
        CrowBar = Item("Crow Bar", "Take Dr. Freidman's advice, use the vents.", True,True)
        Knife = Item("Knife", "An old bloody kitchen knife.", True,False)
        Idol = Item("Idol", "Some random idol that just happens to be here next to these weapons.", False, False)
        Gem = Item("Gem", "A glittering red gem, it must be expensive. It has a mysterious aura about it...",False,False)
        GoldNugget = Item("Gold Nugget", "A small lump of shiny gold, it weighs about as much as you would expect the crown to weigh",False,False)
        Crown = Item("Crown", "A shiny gold crown, I wonder if its the real one or an impostor",False,False)
        FakeCrown = Item("Crown", "A shiny gold crown, I wonder if its the real one or an impostor ",False,False)
        PlainKey1 = Item("Plain Key", "A plain old key, I wonder what it goes to...",False, False)
        Hammer = Item("Hammer", "A lightly rusted hammer with a wooden handle. It looks like it's seen years of use",False,False)
        SpareParts = Item("Spare Parts", "Some old parts that look like they go to an engine", False,False)
        BasementKey = Item("Basement Key", "An old tarnished key.", False, False)
        Flask = Item("Flask", "", False, False)
        ###MAKE SURE YOU ALSO ADD A MENU STATEMENT FOR EACH ITEM YOU ADD HERE^^^### 

        lastPickup = Item("Backpack","Your old Backpack that you've had for many years",False,False) #Lets define all the items we need for this alpha
    return





#BAILEY'S STUFF#

label entrance_hall:
menu:
    "Go down the left hall":
        jump to_garage
        
    "Go down the right hall":
        jump to_basement_door_from_mainhall
        
label to_garage:
    $ menu_flag = True
    "You're at the garage door."
    
    jump garage_door_choices
    
label to_basement_door_from_mainhall:
    $ menu_flag = True
    "You're at the basement door"
    
    jump basement_door_choices
    
label garage_door_choices:
    "You hear heavy breathing from somewhere within the garage..."
menu:
    "Keep Going":
         jump into_the_garage
   
    "Turn Back":
        jump entrance_hall
        
label basement_door_choices:
    "You see a closed door in front of you."
menu:
    "Attempt to open the door":
        jump missing_basement_key
    
    "Turn Back":
        jump entrance_hall
    
label into_the_garage:
      $ menu_flag = True
      "You step into the garage and see a crazed husk charging at you."
      "It tackles you and you attempt to fight back,  but before you can retaliate it hits you over the head with a wrench."
      hide mainhall
      show mechnest #SHOULD THIS BE BLACK? -JACK
      with fade
      "Everything fades to black."
        
      jump to_mech_nest
     
# label wake_up_basement:
#      $  menu_flag = True
#      "You wake up in what looks to be some kind of mechanic's nest."
#      "There are wires strewn about and tools scattered on the floor."
#      "The husk that attacked you earlier is sleeping in the corner, there is a work-bench, toolbox and an old chest in the room." #can kill with certain weapon
#      menu:
#          #"Attack the husk":
#         # jump choice_injured
#          "Search the work-bench":
#              jump search_workbench
#          "Search the toolbox":
#              jump search_toolbox
#          "Search the old chest":
#              jump search_oldchest
#          "Leave the room":
#              jump lab_mainhall
             
#when player doesn't have the basement key in their bag (**this is for the first time entering the mansion on the main floor only**)
label missing_basement_key:
      $ menu_flag = True
      "You attempt to open the door but it won't budge, it looks as if you may need a key to get in."  #only way to get to basement thorugh mechanic? (unlocked_basement jump after play has unlocked the door)   
      jump basement_door_choices
      #basement_door_unlocked
      
#player needs to lose health-pack here   
label choice_injured:
    $ menu_flag = True
    "You have been injured and must retreat."
  #change this so that the player goes back to the last room before they died or something
    jump choice_end_game

#Instant_death call    
label instant_death:
    $ menu_flag = True
    show death
    "You have died."
    jump choice_end_game

 #Basement Mechanic's Nest room           
label to_mech_nest:
    $ menu_flag = True
    show mechnest
    if garageHuskIsAlive:
        "The husk that attacked you earlier is sleeping in the corner, there is a work-bench, toolbox and an old chest in the room. There is also another man in in the back of the room behind a car who seems to be awake" #can kill with certain weapon
    else:
        "The husk no longer needs to be worried about, there is a work-bench, toolbox and an old chest in the room. The other man seems to barely have noticed that you're there"
    menu:
        "Attack the husk" if garageHuskIsAlive:
            "You attack the husk with desperate force." #get rid of option if husk is killed
            "After a bit of struggling the husk stops moving. You're safe, for now..."
            $garageHuskIsAlive = False
            call updateSanity(-5)
        "Talk to other man":
            jump talkToBasiltine
        "Search the work-bench" if CrowBar not in bag:
            jump search_workbench
        "Search the toolbox" if Hammer not in bag:
            jump search_toolbox
        "Search the old chest" if SpareParts not in bag:
            jump search_oldchest
        "Leave the room":
            jump lab_mainhall
    jump to_mech_nest
            
#basement mechanic's nest take_item calls             
label take_hammer:
     $ menu_flag = True
     "You take the hammer and put it in your bag."
     $bag.items.append(Hammer)
     jump to_mech_nest   
label take_crowbar:
     $ menu_flag = True
     "You take the crowbar and put it in your bag."
     $bag.items.append(CrowBar)
     jump to_mech_nest
label take_spareparts:
     $ menu_flag = True
     "You take the spare parts and put them in your bag."
     $bag.items.append(SpareParts)
     jump to_mech_nest
     
#search_locations for mechanic's nest 
label search_workbench:
     $ menu_flag = True   
     "Inside the workbench you see a crowbar."
     menu:
         "Take the crowbar":
             jump take_crowbar
         "Leave the crowbar":
             jump to_mech_nest
             
label escape:
    play sound "rain.mp3" fadeout 1.0 fadein 1.0 loop
    play music "Private Reflection.mp3" fadein 1.0 loop
    scene road
    with fade
    "After a long night in the Malevolent Mansion, you finally escape."
    "What happens next..."
    "Is up to you"
    jump choice_end_game

label search_toolbox:
     $ menu_flag = True
     "Inside the toolbox you see a hammer."
     menu:
         "Take the hammer":
             jump take_hammer
         "Leave the hammer":
             jump to_mech_nest
             
label search_oldchest:
     $ menu_flag = True
     "Inside the old chest you see a bag of spare parts."
     menu:
         "Take the spare parts":
             jump take_spareparts
         "Leave the spare parts":
             jump to_mech_nest
             
#hall between mechanic's nest and the lab
label lab_mainhall:
     $ menu_flag = True
     hide mechnest
     show hallway
     with fade
     "You've entered the main lab hallway."
     menu:
         "Go to the Mechanic's Nest":
             jump to_mech_nest
         "Go to the Lab":
             jump to_Lab
         "Go to basement landing":
             jump to_basement
             
label to_basement:
    $ menu_flag = True
    show hallway
    with fade
    "At the bottom of the stairway you see three doorways."
    menu:
        "Go to the dungeon":
            jump to_Dungeon
        "Go to the library":
            jump to_Library
        "Go to the Lab and Mechanic's Nest":
            jump lab_mainhall
        "Go upstairs":
            jump from_basement
            
#Basement Lab room
label to_Lab:
    hide hallway
    hide Library
    hide tunnel
    show Lab
    with fade
    $ menu_flag = True
    "You're now in the Lab, you see a locker, a desk and table."
    menu:
        "Search the locker":
            jump search_locker
        "Search the desk" if Crown not in bag:
            jump search_desk
        "Search the table" if Flask not in bag:
            jump search_table
        "Leave the Lab":
            jump lab_mainhall
             
     
#basement lab search_locations calls
label search_locker:
     $ menu_flag = True
     $secretPassageActive = True
     "You approach the locker, and open it."
     "To your surprise, on the other side you see a long cave-like passage."
     show tunnel
     with fade
     hide Lab
     menu:
         "Go down the passage":
             "When you enter the library a bookshelf slides blocking the secret passage"
             jump secret_pass_to_library
         "Step away from the locker":
             jump to_Lab
             
label search_desk:
    #"You see a key with the label 'Basement' on it"
    "You see a golden band with carvings on it. Perhaps its a crown"
    menu:
        "Take the crown":
            $bag.items.append(Crown)
            jump to_Lab
        "Leave it":
            jump to_Lab
        #"Take the key":
            #jump take_basement_key
        #"Leave the key":
        #    jump to_Lab
label search_table:
    "You see a flask on the table with a mysterious glowing liquid inside."
    menu:
        "Chug the liquid":
            call updateLives(1)
            "Turns out the liquid is poisonous. Good thing you have your first aid kit."
            "You are still alive but you had to use some of your medical supplies"
        "Take the flask":
            jump take_flask
        "Leave the table":
            jump to_Lab
       
#these calls add items to the player's bag
label take_basement_key:
     $ menu_flag = True
     "You put the key into your backpack"
     $bag.items.append(BasementKey)
     jump to_Lab

label take_flask:
     $ menu_flag = True
     "You put the flask of glowing liquid into your backpack."
     $bag.items.append(Flask)
     jump to_Lab
            
#this goes to the library        
label secret_pass_to_library:
     $ menu_flag = True
     "You walk down the small cavern path and see a light at the end."
     #maybe add a switch
     "As you get closer to the light you see an opening at the end of the tunnel."
     "The opening leads into what looks like a library."
     menu:
         "Continue into the library":
             $secretPassageActive = True
             jump to_Library
         "Go back to the lab":
             jump to_Lab
             
#add a  way of entry exclusive for secret passage
#to_Library_pass
label to_Library:
    $menu_flag = True
    hide tunnel
    hide hallway
    show Library
    with fade
    "You enter the library and see five bookcases."
    "The shelves  are labeled as follows: 'Mythology', 'Riddles', 'Self-Help', 'Medical' and 'Cooking'."
    label bookChoices:
        menu:
            "Examine Mythology":
                jump mythology_bookcase
            "Examine Riddles":
                jump riddles_bookcase
            "Examine Self-Help":
                jump selfhelp_bookcase
            "Examine Medical":
                jump medical_bookcase
            "Examine Cooking":
                jump cooking_bookcase
            
#library bookcases            
label mythology_bookcase:
     $ menu_flag = True
     "You see a book with a title that's written in some unrecognizable cryptic language."
     menu:
         "Examine the book":
             jump read_mythology
         "Back away from the shelf":
#have a way to jump straight to the options
             jump bookChoices
             
label riddles_bookcase:
    $ menu_flag = True
    "You see a book titled 'See a Page's Crest'."
    menu:
        "Examine the book":
            jump read_riddles
        "Back away from the shelf":
#have a way to jump straight to the options
             jump bookChoices
             
label selfhelp_bookcase:
     $ menu_flag = True
     "You see a book titled 'How to Die'."
     menu:
         "Examine the book":
             jump read_selfhelp
         "Back away from the shelf":
#have a way to jump straight to the options
             jump bookChoices
             
label medical_bookcase:
     $ menu_flag = True
     "You see a book titled 'On Madness and Phobias'."
     menu:
         "Examine the book":
             jump read_medical
         "Back away from the shelf":
#have a way to jump straight to the options
             jump bookChoices
             
label cooking_bookcase:
     $ menu_flag = True
     "You see a book titled '42 Comfort Foods'."
     menu:
         "Examine the book":
             jump read_cooking
         "Back away from the shelf":
#have a way to jump straight to the options
             jump bookChoices

#bookcase actions
label read_mythology:
    $ menu_flag = True
    "You pick up the strange book and see that the contents of the book are written in the same cryptic language as the title."
    "You put the book back into place and back away from the shelf."#THE MYTHOLOGY BOOK IS WHAT YOU GIVE TO HAROLD, IT NEEDS TO GO INTO INVENTORY- JACK
    jump to_Library
            
label read_riddles:
    $ menu_flag = True
    "You grab the book and attempt to pull it of the shelf."
    "To your surprise the book rotates about 45 degrees and then locks with a click."

    "The bookshelf then begins to slide to the left to reveal a secret passage."
    if secretPassageActive:
        "This must be the passage back to the lab that was covered by the bookshelf when you entered"
    hide Library
    show tunnel with fade
    menu:
        "Follow the passage.":
            jump secret_pass_to_lab
        "Push the book back into place and back away.":
            jump to_Library#_return
    
label read_selfhelp:
    $ menu_flag = True
    "You pick up the book and hear a something approaching quickly from the hallway."
    "Before you know it a man in a ragged suit with a crazed look in his eyes bursts into the library wielding a shotgun."
    "The man locks his gaze onto you and pumps the shotgun."
    menu:
        "Dive for cover":
            "Sadly you don't get to cover in time. The man shoots you square in the chest"
            call updateLives(1) #attempt to dive for cover but the crazed man shoots you before you can (self_help_death)
            "Thankfully you have your first aid kit. You save yourself using some of your medical supplies."
            "In an adrenaline fueled rage you run to the man as hes reloading his shotgun, grab the gun and beat him upside the head with it."
            "He's dead, so you're safe again, for now..."
        "Run for the secret passage" if secretPassageActive:
            jump  secret_pass_to_lab#_escape (if the player has previously discovered the passage this option should be available)
        #possibly a shoot first or fight option depending on what weapon(s) the player has
        #decrese sanity?
    
label read_medical:
    $ menu_flag = True
    "You pick up the book, and skim over a paragraph that reads:" 
    "'Near death experiences can cause great stress and decrease a person's sanity."
    "Performing normal actions, like eating good food and conversing with other sane individuals, have been suspected to help recover one's nerves...'"
    "You put the book back into place and step away from the bookcase."
    jump to_Library
     
label read_cooking:
    $ menu_flag = True
    "You pick up the book, and flip through all the images of delicious looking foods."
    "You feel more relaxed and refreshed after viewing the book." # if sanity < 100 +10 sanity, else no change
    if bag.sanity <= 90:
        call updateSanity(10)
    else:
        $bag.sanity = 100
    "You put the book back into place and step away from the bookcase."

#this goes to the lab        
label secret_pass_to_lab:
     $ menu_flag = True
     hide Library
     show tunnel with fade
     "You walk down the small cavern path and see a light at the end."
     #maybe add a switch
     "As you get closer to the light you see an opening at the end of the tunnel."
     "The opening leads into what looks like a laboratory."
     menu:
         "Continue into the lab":
             jump to_Lab
         "Go back to the library":
             jump to_Library
             
label to_Dungeon:
     $ menu_flag = True
     hide hallway
     show dungeon
     with fade
     "You enter a dark and dank dungeon."
     menu:
         "Go into room 1":
             jump to_dungeon_1
         "Go into room 2":
             jump to_dungeon_2
         "Go into room 3":
             jump to_dungeon_3
         "Go into room 4":
             jump to_dungeon_4
         "Return to the basement landing":
             jump to_basement
         
label to_dungeon_1:
     $ menu_flag = True
     "You walk into the first dungeon cell to see a nest of sniveling and squeaking rats."
     "As you step into the room all the rats rush by you in a frenzy."
     "Physically, you suffer only minor scratches, but mentally you are wounded by the sight."
     call updateSanity(-10)
     jump to_Dungeon
     
label to_dungeon_2:
     $ menu_flag = True
     "You walk into the second dungeon cell to see a skeleton on the floor."
     menu:
         "Examine the skull":
             jump examine_skull
         "Examine the ribs":
             jump examine_ribs
         "Examine the hands":
             jump examine_hands
         "Back out of the cell":
             jump to_Dungeon
             
label examine_skull:
     $ menu_flag = True
     "You take a closer look at the skull and notice that it has become merged with the stone floor."
     "You also notice that there is a strange gaping hole that looks vaguely key-shaped in the center of the skull."
     jump to_dungeon_2#_options
     
label examine_ribs:
     $ menu_flag = True
     "You take a closer look at the ribs and notice a pair of eyes peering back at you."
     "All of a sudden a rat leaps from inside the skeleton and bites your arm."
     "You manage to bat it away and suffer no serious injuries, but you are shaken by the experience."
     jump to_dungeon_2#_options
label examine_hands:
     $ menu_flag = True
     "You take a closer look at the hands and notice that they're gripping a piece of bread."
     menu:
         "Eat the bread":
             jump eat_bread_dungeon
         "Back away from the skeleton":
             jump to_dungeon_2#_options
             
label eat_bread_dungeon:
     $ menu_flag = True
     "You take the bread from the skeleton's hands and eat it."
     "It's a bit dusty and stale but it helps settle your stomach, and calm your nerves."
     if bag.sanity <= 90:
        call updateSanity(10)
     else:
        $bag.sanity = 100
     jump to_dungeon_2#_options
     #restore sanity +10 if sanity<100, else no change
     
label to_dungeon_3:
     $ menu_flag = True
     "You enter the third dungeon cell and immediately stop when you hear the jingling of chains from within the cell."
     menu:
         "Investigate the noise":
             jump chained_husk
         "Back out of the cell":
             jump to_Dungeon
             
label chained_husk:
     $ menu_flag = True
     "You step forward slowly and as you get closer you find the source of the rattling chains."
     "Someone chained a husk up in this cell and you can see its silhouette, as it struggles uselessly against the chains."
     "You feel badly for the creature but you know that whoever it was their mind was lost long ago."
     "You back out of the cell as the husk continues to struggle to break free."
     jump to_Dungeon
     
label to_dungeon_4:
     $ menu_flag = True
     "There is a strange golden light emanating from the fourth cell as you approach it."
     "As you walk into the cell you see a room filled with treasures of gold and silver."
     "One particular piece catches your eye."
     menu:
         "Take a closer look":
             jump examine_gold_band
         "Back out of the room":
             jump to_Dungeon
         
label examine_gold_band:
     $ menu_flag = True
     "The piece that caught you eye is a particularly exquisite golden band."
     menu:
         "Take the golden band":
             jump take_golden_band
         "Leave the golden band":
             jump to_dungeon_4#_options
             
label take_golden_band:
     $ menu_flag = True
     "You pick up the golden band and put it into you bag."
     "You then back out of the fourth dungeon cell."
     jump to_Dungeon
     
label from_basement:
     $ menu_flag = True
     "You walk up the stairs towards the first floor."
     jump basement_door_to_first_floor

     label basement_door_to_first_floor:
     "You see a closed door in front of you."
menu:
    "Attempt to open the door":
        jump missing_basement_key_to_first_floor
    
    "Turn Back":
                  jump to_basement
                  
#when player doesn't have the basement key in their bag   
label missing_basement_key_to_first_floor:
      $ menu_flag = True
      "You attempt to open the door but it won't budge, it looks as if you may need a key to get in."  #only way to get to basement thorugh mechanic? (unlocked_basement jump after play has unlocked the door)   
      jump basement_door_to_first_floor
      #basement_door_unlocked
     #jump basement_door_unlocked_to_first floor
     #jump basement_door_unlocked_to_basement
 #to_Library_return and to_Lab_return jump calls to only display options upon returning to already visited locations  

label choice_end_game:  
    return
