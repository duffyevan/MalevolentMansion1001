## MALEVOLENT MANSION ##
## A game where the player is dropped in a mansion after their car breaks down in a storm and must complete quests to escape ##
## TEAM:
## Story: Jack Riley
## CODE: Bailey Schmidt and Evan Duffy
## ART: Delores Jackson
## Beta as of 10/6/15
## Warning: Many froot loops and Ramen were consumed in the making of this game

#get rid of menu options??? after weapon pickup, event happens, objective complete, enemy is killed, etc.
define j = Character('John Doe', color="#c8ffc8")
image road = im.Scale("images/road1.jpg",900,600)
image car = im.Scale("images/car2.png",150,80)
image hallway = im.Scale("images/hallway2.png",900,600)
image garageBackground = im.Scale("images/garage.jpg",900,600)
image litBallroom = im.Scale("images/ballroom_reg.bmp",900,600)
image darkBallroom = im.Scale("images/Ballroom (Dim).png",900,600)
image mainhall = im.Scale("images/mainhall.png",900,600)
image mansion = im.Scale("images/Mansion.jpg",900,600)
image mechnest = im.Scale("images/mechNest.jpg",900,600)
image Lab = im.Scale("images/lab-filler.jpg",900,600)
image Dungeon = im.Scale("images/dungeon.png",900,600)
image Library = im.Scale("images/library.png",900,600)
image death = im.Scale("images/death.jpg",900,600)
image tunnel = im.Scale("images/tunnel-filler.jpg",900,600)
image kitchen = im.Scale("images/Kitchen Sane.png", 900, 600)
image laundryRoom = im.Scale("images/laundry sane.png", 900, 600)
image redRoom = im.Scale("images/Floor 2/Blue Beds.png", 900, 600)
image greenRoom = im.Scale("images/Floor 2/Green Beds.png", 900, 600)
image orangeRoom = im.Scale("images/Floor 2/Blue Beds Tentative Sanity.png", 900, 600)
image purpleRoom = im.Scale("images/Floor 2/Purple Beds.png", 900, 600)
image masterBedroom = im.Scale("images/Floor 2/2nd Floor Master Bedroom.png", 900, 600)
image Avidem = im.Scale("images/NPCs/Avidem.png", 900,600)
image Phoebe = im.Scale("images/NPCs/Phoebe.png", 900,600)
image Harold = im.Scale("images/NPCs/Harold.png", 900,600)
image litGarden = im.Scale("images/garden Sane.png", 900,600)
image darkGarden = im.Scale("images/garden (Dim).png", 900,600)
image gameroom = im.Scale("images/Floor 3/Game Room Sane.jpg", 900,600)
image burnedroom = im.Scale("images/Floor 3/burned-bedroom.jpg", 900,600)
image office = im.Scale("images/Floor 3/office sane.jpg", 900,600)
image emptybedroom = im.Scale("images/Floor 3/Sane Empty Room.jpg", 900,600)
image nursery = im.Scale("images/Floor 3/Nursery Sane.jpg", 900,600)
image TVroom = im.Scale("images/Floor 3/TV room Sane.jpg", 900,600)
image artroom = im.Scale("images/Floor 3/art studio Sane.jpg", 900,600)
image Bas = im.Scale("images/NPCs/Archie.png", 900,600)

image ballroomInsane = im.Scale("images/Ballroom Insane.png",900,600)
image mainhallInsane = im.Scale("images/Main Hall- Insane.png",900,600)
image LibraryInsane = im.Scale("images/library insane.png",900,600)
image kitchenInsane = im.Scale("images/Kitchen Insane.png", 900, 600)
image laundryRoomInsane = im.Scale("images/laundry insane.png", 900, 600)
image gardenInsane = im.Scale("images/garden Insane.png", 900,600)
image gameroomInsane = im.Scale("images/Floor 3/Game Room Insane.jpg", 900,600)
image officeInsane = im.Scale("images/Floor 3/Office Insane.jpg", 900,600)
image emptybedroomInsane = im.Scale("images/Floor 3/Insane Empty Room.jpg", 900,600)
image nurseryInsane = im.Scale("images/Floor 3/Nursery Insane.jpg", 900,600)
image TVroomInsane = im.Scale("images/Floor 3/TV room Insane.jpg", 900,600)
image artroomInsane = im.Scale("images/Floor 3/art studio Insane.jpg", 900,600)

define diss = Dissolve(1.0)

# The game starts here.
label start:
    play sound "audio/rain.mp3" fadeout 1.0 fadein 1.0 loop
    scene road
    with fade
    call setupItemSystem
    python:
        garageHuskIsAlive = True
        secretPassageActive = False
        playerName = renpy.input("What is your name?") #Take the players name
    play music "audio/Private Reflection.mp3" fadein 1.0 loop
    if playerName == "John Cena":
        play music "audio/Cena.mp3" loop

    scene road
    with fade
    "You're driving down the road in your old beat up Chevy. It's raining pretty heavily and you don't recognize your surroundings."
    
    stop sound fadeout 1.0
    play sound "audio/tree_fall.mp3" fadeout 1.0 
    play sound "audio/screech_crash.mp3"
    show car at Position(xpos=335, ypos=350, xanchor=0, yanchor=0)
    with diss
    with hpunch
    
    "Out of nowhere a tree falls into the road, causing you to swerve and crash."
    
    play sound "audio/rain.mp3" fadein 2.0 loop
    
    "It's raining hard and you need to find a place to go. You see a faint glow in the distance."
    
    menu: 
        with dissolve
        "Go towards the light...":
            jump choice_start
        
        "Stay in the car":
            jump choice_dead
        
            label choice_start:
                $ menu_flag = True
                stop sound fadeout 2.0
                play sound "audio/car_door_close.mp3"
                hide car
                hide road
                play sound "audio/woods_walking.mp3" fadein 1.0
                show mansion
                with dissolve
                stop sound fadeout 2.0
                play sound "audio/rain.mp3" fadein 2.0 loop
                
                "You run out of the car, grabbing the emergency first-aid kit in the glove compartment just before you leave."
                "You see the source of the light, a large mansion at the end of the road."
                menu:      
                    with dissolve
                    "Go to the mansion":
                        jump choice_tothemansion
                    
                        label choice_tothemansion:
                            $ menu_flag = True
                            hide mansion
                            stop sound fadeout 2.0
                            play sound "audio/door open.mp3" 
                            show mainhall
                            with fade
                            stop sound fadeout 1.0
                            
                            stop music
                            play sound "audio/doorslam.mp3" 
                            queue sound "audio/evillaugh.mp3" 
                            play music "audio/Epic Unease.mp3" fadein 1.0 loop

                    
                            "You have now entered the Malevolent Mansion."
                            
                           
                        
                            jump entrance_hall
                 
                
                label choice_dead:
                $ menu_flag = True
                hide car
                #hide road
                stop sound 
                stop music 
                play sound "audio/car_explosion.mp3"
                
                "You died in a fiery explosion."
                
    
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
    atePie = False
    huskInRedBed = True
    ballroomLightsOff = True
    attacking = False # TODO This breaks the attacking option for all NPCs, we can deal with that feature later
    firstTimeInGarage = True
    carFixed = False
    knightDead = False
    eatenBread = False
    ratsAttacked = False
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
            self.lives = 100

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
    "You've lost all of your sanity. You lose your mind and wander the halls of the Malevolent Mansion, forever."
    "Game Over"
    jump choice_end_game
    return

label die:
    "You've run out of medical supplies, and met your demise."
    "Game Over"
    jump choice_end_game
    return

label talkToHarold:
    show Harold
    with fade
    if not attacking:
        if not metHarold:
            h "W-what? W-w-who's there? W-what do you want?"
            $metHarold = True
        else:
            h "W-what? W-w-who's there? Oh it's you a-again. %(playerName)s, what do you w-want?"
        menu:
            "Who are you?":
                h "M-My name is H-H-Harold. I-I am a historian from a-around here and I had h-heard some legends about this p-place."
                h "B-but I've seen such h-horrible things here! I-I will go n-no further"
            "How do I escape?":
                h "One of the l-legends I heard about t-this place told of a tunnel and a r-riddle."
                h "I-If you can find it and s-solve the puzzle then you mi-might escape."
            "What is this place?":
                h "You mean you d-don't know about the M-M-Malevolent Mansion?!? I suppose you're n-not from around h-here."
                h "*Ahem* Originally owned by the Cupido family, this mansion had stayed in the possession of the wealthy banking family for generations."
                h "However, approximately 60 years ago the then owner of the house, Gerald Cupido, vanished along with his wife and the entire staff."
                h "When police, suspecting foul play, attempted to enter the mansion they encountered something so horrific they've banned any mention of the Mansion in public records."
                h "As an avid historian, I feel it is my duty to explore this place and restore the public record! However..."
                h "I... I-I'm afraid I c-c-cannot delve f-further..."
            "Do you know anything about other people in the mansion?" if metAvidem or metPhoebe or metArchie:
                menu:
                    "Avidem" if metAvidem:
                        h "Hmm, the lady seems n-nice, but awfully c-calm."
                    "Basiltine" if metArchie:
                        h "That man is a few cards short of a d-deck. I-I'd be careful around h-him."
                    "Phoebe" if metPhoebe:
                        h "That young w-woman didn't h-have much to say to m-me. She just muttered about s-secrets."
            "Can you tell me about this Mythology Book?" if MythologyBook in bag:
                h "Hmmm... Th-These symbols... They resemble a dialect of ancient Sumerian."
                h "Now that I think of if, Lord Cupido did entertain a fascination with Sumerian artifacts a little while before his disappearance."
                h "It's been a while, but I think... I... can...."
                h "Got it! I've deciphered the text. There's one passage in particular that might aid your escape, titled 'Riddle for Passage of Bone.'"
                h "It reads: 'Swim through the clouds, crawl along the ocean depths, fly silently through the grass.'"
                h "I'm not sure what that means, but it m-might be a clue to that underground escape t-tunnel."
    else:
        h "AHG MONSTER!"
        "Harold takes out a revolver from the pile of laundry and starts shooting"
        "One of the bullets pierces your lung and you are grievously wounded..."    
        call updateLives(1)
        "Luckily you have your first aid kit. You've recovered, but you had to use some of your supplies"
    hide Harold
    jump back1


label talkToAvidem:
    show Avidem
    with fade
    if not attacking:
        if not metAvidem:
            a "Hm? Ah hello, who are you? Do you need any advice?"
            $metAvidem = True
        else:
            a "Hello again %(playerName)s, what would you like advice on now?"
        menu:
            "Who are you?":
                a "I'm Avidem"
                a "I'm trapped in this place like many of its occupants."
                a "I was driving past one night when my vehicle broke down, and I was forced to take shelter here."
                a "It seems like I've been here forever..."
            "How do I get out of here?":
                if PlainKey1 not in bag:
                    a "I've heard of an escape route, but it's a precious secret of mine. If I tell you, you'll have to fetch me something even more valuable."
                    a "I hid it away long ago to keep it safe, but now I yearn for it..."
                    a "Retrieve it and I'll tell you the secret. You'll need this to find it:"
                    $bag.items.append(PlainKey1)
                    $lastPickup = PlainKey1
                    "%(playerName)s got a Plain Key!"
                else:
                    a "Do you have what I sent you for?"
                    menu:
                        "Yes":
                            a "Really?"
                            call giveAvidemTheGem()
                        "No":
                            a "Well hurry up and find it. I really need it back soon."
            "What is this place?":
                a "Hm? Well, it's a mansion. Besides that I cannot really say."
            "Do you know anything about other people in the mansion?" if metHarold or metPhoebe or metArchie:#SHOULD THE IF GO BEFORE THE OPTION? -JACK
                menu:
                    "Harold" if metHarold:
                        a "The laundry-pile man?" 
                        a "He may seem meek and harmless, but fear can make men do strange things."
                    "Basiltine" if metArchie:
                        a "Poor soul, he's been here so long he had to create a whole other world to live in, to keep from becoming a gibbering Husk."
                    "Phoebe" if metPhoebe:
                        a "That girl was our latest addition before you. I don't think she's a fan of the weather."


    else:
        a "Fool, you would attack the master of this house?"
        a "BEGONE!"
        #push out of room
        call updateSanity(-50)
        #orangeRoom.items.append(PlainKey1)
    hide Avidem
    return

label giveAvidemTheGem():
    a "Do you have it? The sanguine rose? GIVE IT TO ME!"
    if Gem in bag:
        label back:
            menu: 
                "Ok":
                    $bag.items.remove(Gem)
                    a "Ah, my beauty! It's been much too long, my power has waned so. Courier, for your service you may leave."
                    a "If you are still sane..."
                    call updateSanity(-50)
                    "%(playerName)s's sanity fell by 50" #IDK 50 is a lot, we might want to lower this
                    "You also hear a click from somewhere in the mansion... As if a door unlocked..."
                    $frontDoorLocked = False
                    #door locks
                "No":
                    a "WHAT?? HOW DARE YOU DEFY ME! Give me that gem!!!"
                    jump back
    else:
        menu:
            "Yes":
                a "No you don't! Go and find it!"
            "No":
                a "Well go find it!"
    return

label talkToPhoebe:
    show Phoebe
    with fade
    if not attacking:
        if not metPhoebe:
            p "You have arrived. Phoebe thinks you are late."
            $metPhoebe = True
        else:
            p "You return, what does %(playerName)s want from Phoebe?"
        menu:
            "Who are you?":
                p "Phoebe's name is Phoebe. She was drawn here by this place's aura."
                p "Such emotion... Such darkness..."
                p"But now Phoebe is trapped, she does not like the storm."
            "How do I get out of here?":
                p "Escape? Phoebe sees... four?... No, three exits."
                p "Phoebe only knows they exist, not where they are."
                p "Otherwise Phoebe would not be trapped."
            "What is this place?":
                p "Tainted..." 
                p "Always corrupted? No, Phoebe feels an event, an explosion of emotion."
                p "Everywhere reeks of hate and greed and madness. Whatever it was before, now it is only a nest of darkness."
            "Do you know anything about other people in the mansion?" if metArchie or metAvidem or metHarold:
                menu:
                    "Avidem" if metAvidem:
                        p "Unnerving, calm in the storm."
                    "Basiltine" if metArchie:
                        p "Funny man, lives in his own world. Phoebe wonders if he is foolish or fortunate..."
                    "Harold" if metHarold:
                        p "Does he hide from the world, or hide something from the world?"

    else:
        p "That was unwise of you."
        "Phoebe has a knife! She stabs you right in the heart."
        "Luckily you have your first aid kit. You've recovered, but you had to use some of your supplies."
        call updateLives(1)
    hide Phoebe
    return

label talkToBasiltine:
    show Bas
    $attacking = False
    if not attacking:
        if not metArchie:
            b "You desire an audience with the emperor? Very well, ask away"
            $metArchie = True
        else:
            b "%(playerName)s! You return to the emperor, what do you wish from him now?"
        menu:
            "Who are you?":
                b "You don't know who I am?!? But I am his Glorious Highness Basiltine von Ludwig XIII, Appointed by the Heavens, Long May He Reign etc. etc.!"
                b "But you may call me Archie."
            "How do I get out of here?":
                if GoldNugget not in bag:
                    b "I can not see why you would wish to leave my Empire, but if that is truly so I can help you. If you help me..."
                    b "I have misplaced my crown, find it and I will grant you the keys to the empire."
                    b "However, impostor crowns lurk about. Use this to determine the true crown:"
                    "%(playerName)s got a gold nugget"
                    $bag.items.append(GoldNugget)
                elif CarKeys not in bag:
                    b "Have you found my crown yet?"
                    menu:
                        "Yes":
                            b "Really?"
                            jump giveBasiltineCrown
                        "No":
                            b "Well hurry up and find it. The emperor grows impatient!"
                else:
                    "You must figure out how to use those keys, peasant!"
            "What is this place?":
                b "Why my Empire, of course! I am surprised you are unaware of it."
                b "Although... perhaps its beauty so dazzled you, you momentarily lost memory of all else? Yes, that must be it!" 
            "Do you know anything about other people in the mansion?" if metHarold or metPhoebe or metAvidem:
                menu:
                    "Harold" if metHarold:
                        b "The record keeper has intellect, but lacks backbone."
                        b "I don't think I've ever seen him leave his Tower of Antiquity."
                    "Avidem" if metAvidem:
                        b "Queen Avidem? She is a calm advisor, and a potent force."
                        b "Sometimes I feel like she has more power than me..."
                        b "But that is nonsense, I'm the Emperor!" 
                    "Phoebe" if metPhoebe:
                        b "Ahh, the soothsayer. She is useful, but sometimes gives ominous predictions."

    else:
        b "Who dares assault them emperor?!"
        "Basiltine takes a wrench from behind him and beats you over the head with it."
        "You black out..."
        "Luckily you have your first aid kit. You've recovered, but you had to use some of your supplies."
        call updateLives(1)
        hide Bas
    jump purple_room

label giveBasiltineCrown():
    if Crown in bag and FakeCrown not in bag:
        b "Do you bring me my crown?"
        menu:
            "Yes, here it is":
                b "Ahh yes, my precious. Thank you peasant, for your work you may have this: the keys to my kingdom."
                "Archie hands you a small ring of car keys."
                $bag.items.append(CarKeys)
                b "If you use these well, you just may be able to escape."
            "No":
                b "Well hurry up, the emperor is growing impatient."
    elif FakeCrown in bag and Crown not in bag:
        b "Do you bring me my crown?"
        menu:
            "Yes, here it is":
                b "This is not the real crown! This is but an impostor!"
                b "GET OUT!"
                call updateSanity(-10)
                #Kick out of room
            "No":
                b "Well hurry up, the emperor is growing impatient"
    elif FakeCrown in bag and Crown in bag:
        b "You have two! Which one is the real one? Come back when you've discovered the real one."
    else:
        b "You don't have it! Come back when you have it."
    jump purple_room 

label inventory:
    $showInventory(playerName,bag)
    "%(playerName)s's Inventory"
    return

label updateSanity(num):
    if bag.sanity > 50 and bag.sanity + num < 50:
        play music "audio/The Hive.mp3" fadein 1.0 loop
    elif  bag.sanity < 50 and bag.sanity + num > 50:
        play music "audio/Epic Unease.mp3" fadein 1.0 loop
    $bag.updateSanity(num)
    if bag.sanity <= 0:
        jump goInsane
    if bag.sanity > 100:
        $bag.sanity = 100
    return

label updateLives(num):
    python:
        holdingLightWeapon = False
        holdingHeavyWeapon = False
        for i in bag.items:
            if i.isWeapon:
                if i.isHeavy:
                    holdingHeavyWeapon = True
                else:
                    holdingLightWeapon = True
        if Chainsaw in bag:
            num = 0
        elif (holdingHeavyWeapon == True):
            num = num * 0.25
        elif holdingLightWeapon == True:
            num = num * 0.75
        bag.lives -= num
    if bag.lives <= 0:
        jump die
    return

label setupItemSystem:
    python:
        ###DEFINE ALL ITEMS HERE!!!###
        bag = Inventory()
        Chainsaw = Item("Chainsaw","You know what's good.",True,True)
        CrowBar = Item("Crow Bar", "Take Dr. Friedman's advice, use the vents.", True,True)
        Knife = Item("Knife", "An old bloody kitchen knife.", True,False)
        Gem = Item("Gem", "A glittering red gem, it must be expensive. It has a mysterious aura about it...",False,False)
        GoldNugget = Item("Gold Nugget", "A small lump of shiny gold, it weighs about as much as you would expect the crown to weigh.",False,False)
        Crown = Item("Gold Band", "A shiny gold band, I wonder if its real?",False,False)
        FakeCrown = Item("Toy Crown", "A glittering gold crown, I wonder if its real?",False,False)
        PlainKey1 = Item("Plain Key", "A plain old key.",False, False)
        Hammer = Item("Hammer", "A lightly rusted hammer with a wooden handle. It looks like it's seen years of use.",False,False)
        SpareParts = Item("Spare Parts", "Some old parts that look like they go to an engine.", False,False)
        BasementKey = Item("Basement Key", "An old tarnished key.", False, False)
        Flask = Item("Flask", "", False, False)
        Flashlight = Item("Flashlight", "", False, False)
        OrangeKey = Item("Orange Key", "", False, False)
        MythologyBook = Item("Mythology Book","",False,False)
        CarKeys = Item("Car Keys", "", False, False)
        Matches = Item("Matches", "", False, False)
        SkeletonKey = Item("Matches", "", False, False)
        Sword = Item("Queens Saber","", True, True)
        GlassKey = Item("Glass Key","",False, False)

        ###MAKE SURE YOU ALSO ADD A MENU STATEMENT FOR EACH ITEM YOU ADD HERE^^^### 
        #lastPickup = Item("Backpack","Your old Backpack that you've had for many years.",False,False) #Lets define all the items we need for this alpha
    return





#BAILEY'S STUFF#

label entrance_hall:
    hide kitchen
    if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
        scene mainhall
        with fade
    else:
        scene mainhallInsane
        with fade
    "You're in the entrance hall of the mansion."
    "Where do you want to go?"
    menu:
        "Go down the left hall":
            jump to_garage

        "Go up the stairs":
            jump up_level_2

        "Go straight into the main hallway":
            jump mainHallway

        "Go down the right hall":
            jump to_basement_door_from_mainhall
        "Go out the front door":
            "You try the front door and its open!"
            "Giving Avidem her gem must have triggered the supernatural lock!"
            "You walk out the front door of the mansion"
            jump escape
    jump entrance_hall

label mainHallway:
    scene hallway
    "You're in the first floor hallway, where do you want to go?"
    menu:
        "Go into the kitchen":
            "You enter a small, dark kitchen"
            jump kitchen
        
        "Go into the laundry room":
            "You enter a small room with cloths strewn about"
            jump laundryRoom

        "Go to the garden":
            if GlassKey in bag:
                "You go out the back door to find a fenced off garden"
                if Flashlight in bag:
                    "It's very dark. You take out your flashlight and turn it on."
                    "It easily illuminates the garden"
                    "There's a small flower bed with a dingy cement statue next to it."
                    if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                        scene gardenlit
                        with fade
                    else:
                        scene gardenInsane
                        with fade
                else:
                    "Its too dark to see..."
                    scene darkGarden
                jump garden
            else: 
                "The glass door to the garden is locked..."

        "Go into the ballroom":
            "You enter a large ballroom"
            jump ballroom

        "Go to the main entryway":
            jump entrance_hall
    jump mainHallway

label to_garage:
    $ menu_flag = True
    "You're at the garage door."
    
    jump garage_door_choices
    
label to_basement_door_from_mainhall:
    $ menu_flag = True
    "You're at the basement door"
    
    jump basement_door_choices
    
label garage_door_choices:
    if firstTimeInGarage:
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
        if BasementKey in bag:
            "You insert your Basement Key and the door opens with little effort."
            "There is a set of old wooden stairs that descend into a dark basement with dust and cobwebs floating in the air."
            jump to_basement
        else:    
            jump missing_basement_key

    "Turn Back":
        jump entrance_hall
    
label into_the_garage:
    if firstTimeInGarage:
        $ menu_flag = True
        $ firstTimeInGarage = False
        "You step into the garage and see a crazed husk charging at you."
        "It tackles you and you attempt to fight back,  but before you can retaliate it hits you over the head with a wrench."
        hide mainhall
        show mechnest #TODO should this be a black background? -Jack
        with fade
        "Everything fades to black."
        jump to_mech_nest
    else:
        jump garageScene
     
label garageScene:
    scene garageBackground
    with fade
    "You're in the garage, theres nothing but dust and an old car."
    "What would you like to do?"
    menu:
        "Inspect car":
            if SpareParts not in bag:
                "Maybe you could fix it with some spare parts, but where could you find them?"
                jump garageScene
            elif not carFixed and SpareParts in bag:
                "Upon closer examination, the car seems to be missing a few parts."
                "The spare parts in your bag could help, would you like to try and fix the car?"
                menu:
                    "Sure":
                        "You spend a few minutes fiddling with the spare parts that you put in the car."
                        $carFixed = True
                        "The car seems like it should work now with the spare parts, but you still need to turn it on."
                        if CarKeys in bag:
                            "Would you like to try to start the car with the keys that Archie gave you?"
                            menu:
                                "Yes":
                                    "You insert the key and the car roars to life."
                                    "You back the car up right through the rusted garage door and out into the storm!"
                                    jump escape
                                "No":
                                    "You back away from the car."
                        else:
                            "Looks like you'll need to find the keys to the car."
                    "No":
                        "You back away from the car."
                        jump garageScene
            elif CarKeys in bag and carFixed:
                "Would you like to try to start the car with the keys that Archie gave you?"
                menu:
                    "Yes":
                        "You insert the key and the car roars to life."
                        "You back the car up right through the rusted garage door and out into the storm!"
                        jump escape
                    "No":
                        "You back away from the car."
            elif CarKeys not in bag and carFixed:
                "The car is fixed, all you need are the keys now..."
        "Go Back":
            jump entrance_hall
    jump garageScene
             
#when player doesn't have the basement key in their bag (**this is for the first time entering the mansion on the main floor only**)
label missing_basement_key:
      $ menu_flag = True
      "You attempt to open the door but it won't budge, it looks as if you may need a key to get in."  #only way to get to basement through mechanic? (unlocked_basement jump after play has unlocked the door)   
      jump basement_door_choices
      #basement_door_unlocked

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
    if garageHuskIsAlive: #is there any way to change this if you haven't gone to the garage yet? The only way to get to the mech_nest before 
        if bag.sanity > 50:
            play music "audio/Dragon and Toast.mp3" fadein 1.0 loop
        else:
            play music "audio/Heart of the Beast.mp3" fadein 1.0 loop
        
        "The husk that attacked you earlier is sleeping in the corner, there is a work-bench, toolbox and an old chest in the room." #can kill with certain weapon
    else:
        "The husk no longer needs to be worried about, there is a work-bench, toolbox and an old chest in the room."
    menu:
        "Attack the husk" if garageHuskIsAlive:
            "You attack the husk with desperate force!" #get rid of option if husk is killed
            "After a bit of struggling the husk stops moving. You're safe, for now..."
            $garageHuskIsAlive = False
            call updateSanity(-5)
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
    play sound "audio/rain.mp3" fadeout 1.0 fadein 1.0 loop
    play music "audio/Private Reflection.mp3" fadein 1.0 loop
    if playerName == "John Cena":
        play music "audio/Spook.mp3" fadein 3.0 loop
    scene road
    with fade
    "After a long night in the Malevolent Mansion, you finally escape."
    "What happens next..."
    "Is up to you."
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
    if bag.sanity > 50:
        play music "audio/Dragon and Toast.mp3" fadein 1.0 loop
    else:
        play music "audio/Heart of the Beast.mp3" fadein 1.0 loop
        
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
        "Search the desk" if BasementKey not in bag:
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
    "You see a key with the label 'Basement' on it."
    menu:
        "Take the key":
            $bag.items.append(BasementKey)
            jump to_Lab
        "Leave it":
            jump to_Lab
label search_table:
    "You see a flask on the table with a mysterious glowing liquid inside."
    menu:
        "Chug the liquid":
            call updateLives(10)
            "Turns out the liquid is poisonous. Good thing you have your first aid kit."
            "You are still alive but you had to use some of your medical supplies."
        "Take the flask":
            jump take_flask
        "Leave the table":
            jump to_Lab
       
#these calls add items to the player's bag
label take_basement_key:
     $menu_flag = True
     "You put the key into your backpack"
     $bag.items.append(BasementKey)
     jump to_Lab

label take_flask:
     $ menu_flag = True
     "You put the flask of glowing liquid into your backpack."
     $bag.items.append(Flask)
     jump to_Lab
            

label kitchen:
    #show kitchen but i don't have the assets for kitchen yet...
    # hide mainhall
    if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
        scene kitchen
        with fade
    else:
        scene kitchenInsane
        with fade
    with fade
    label back:
    "What do you want to do?"
    menu:
        "Check sink":
            if ((GoldNugget in bag) and (Crown in bag) and (FakeCrown in bag)):
                "Would you like to check to see which one of the crowns is Archie's real crown?"
                menu:
                    "Yeah":
                        $bag.items.remove(FakeCrown)
                        "Using the principles of displacement and density, you find which crown is made of real gold, and you toss the other in the garbage."
                        jump back

                    "No": 
                        jump back
            else:
                "There's nothing but water here..."
                jump back
        "Check fridge":
            if not atePie:    
                "In the fridge there is nothing but a single pie. Do you want to eat it or leave it?"
                menu:
                    "Eat it":
                        "The pie is delicious! It makes you feel a lot better."
                        "Your sanity was completely restored"
                        call updateSanity(100)
                        $atePie = True
                        jump back
                    "Leave it":
                        "You close the fridge and back away"
                        jump back
            else:
                "There's nothing in here."
                "You close the fridge and back away."
                jump back
        "Check Counter" if Knife not in bag:
            "There is an old bloody kitchen knife on the counter, do you want to take it or leave it?"
            menu:
                "Take it":
                    "You put the knife in your bag."
                    $bag.items.append(Knife)
                    jump back

                "Leave it":
                    "You back away."
                    jump back

        "Leave":
            jump mainHallway

label ballroom:
    if not ballroomLightsOff:
        scene darkBallroom
        with fade
    else:
        scene 
    label back2:
    if ballroomLightsOff:
        "The room is dark, too dark to see."
        "Theres a light switch on the wall, do you want to flip it?"
    else:
        "The bodies still hang from the ceiling, but they seem to have finished kicking."
    menu:
        "Flip the switch" if ballroomLightsOff:
            $ballroomLightsOff = False
            if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                scene litBallroom
                with fade
            else:
                scene ballroomInsane
                with fade
            "You turn on the lights to the sight of many bodies hung from the ceiling, some of them still kicking."
            "The grisly sight disturbs you."
            call updateSanity(-20)
            jump back2

        "Leave":
            jump mainHallway
    jump back2

label laundryRoom:
    if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
        scene laundryRoom
        with fade
    else:
        scene laundryRoomInsane
        with fade
    with fade
    label back1:
    "What would you like to do?"
    menu:
        "Inspect the pile of clothes" if not metHarold:
            "After a bit of digging you feel something solid."
            "Removing some clothes reveals a small man huddled under the pile."
            jump talkToHarold
        "Talk to Harold" if metHarold:
            jump talkToHarold
        "Check the laundry chute":
            "There is a metal laundry chute in the wall."
            "It is too small and slippery to climb up."
            jump back1
        "Leave":
            "You back out into the main hall."
            jump mainHallway
    jump laundryRoom

label garden:
    "What do you want to do?"
    menu:
        "Inspect the statue" if Flashlight in bag:
            if Gem not in bag:
                "There's a notch in the statue next to its foot, do you want to investigate further?"
                menu:
                    "Yes":
                        "You slide the foot to the side and a click comes from inside the statue."
                        "A hole has opened up in the side of a statue. Inside is a beautiful red gem."
                        "It must be important so you put it in your bag and take it with you."
                        $bag.items.append(Gem)
                    "No":
                        "You back away from the statue"
            else:
                "The statue looks the same as when you left it"
        "Leave":
            jump mainHallway
    jump garden 
    #Avidem's key and stuff



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
    if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
        show Library
        with fade
    else:
        scene LibraryInsane
        with fade
    "You enter the library and see five bookcases."
    "The shelves  are labeled as follows: 'Mythology', 'Riddles', 'Self-Help', 'Medical' and 'Cooking'."
    label bookChoices:
        menu:
            "Examine Mythology" if MythologyBook not in bag:
                jump mythology_bookcase
            "Examine Riddles":
                jump riddles_bookcase
            "Examine Self-Help":
                jump selfhelp_bookcase
            "Examine Medical":
                jump medical_bookcase
            "Examine Cooking":
                jump cooking_bookcase
            "Leave to hallway":
                jump to_basement
            
#library bookcases            
label mythology_bookcase:
     $ menu_flag = True
     "You see a book with a title that's written in some unrecognizable, cryptic language."
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
    "You're pretty curious about this book, do you want to take it or put it back?"
    menu:
        "Take it":
            "%(playerName)s put the mythology book in their bag."
            $bag.items.append(MythologyBook)
        "Leave it":
            "You return the book to its shelf and back away."
    jump to_Library
            
label read_riddles:
    $ menu_flag = True
    "You grab the book and attempt to pull it of the shelf."
    "To your surprise the book rotates about 45 degrees and then locks with a click."

    "The bookshelf then begins to slide to the left, revealing a secret passage."
    if secretPassageActive:
        "This must be the secret passage to the lab."
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
            "Sadly you don't get to cover in time. The man shoots you square in the chest."
            call updateLives(10) #attempt to dive for cover but the crazed man shoots you before you can (self_help_death)
            "Thankfully you have your first aid kit. You save yourself using some of your medical supplies."
            "In an adrenaline fueled rage you run to the man as hes reloading his shotgun, grab the gun and beat him upside the head with it."
            "He's dead, so you're safe again, for now..."
            jump bookChoices
        "Run for the secret passage" if secretPassageActive:
            jump secret_pass_to_lab#_escape (if the player has previously discovered the passage this option should be available)
        #possibly a shoot first or fight option depending on what weapon(s) the player has
        #decrease sanity?
    
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
    "You feel more relaxed and refreshed after viewing the book." # if sanity < 100 +20 sanity, else no change
    call updateSanity(-20)
    "You put the book back into place and step away from the bookcase."
    jump bookChoices

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
    "You enter a dark, dank dungeon."
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
    jump to_Dungeon
        
label to_dungeon_1:
    $ menu_flag = True
    if not ratsAttacked:
        $ratsAttacked = True
        "You walk into the first dungeon cell to see a nest of sniveling, squeaking rats."
        "As you step into the room all the rats rush by you in a frenzy."
        "Physically, you suffer only minor scratches, but mentally you are wounded by the sight."
        call updateSanity(-20)
    "Its just an empty cell..."
    jump to_Dungeon
     
label to_dungeon_2:
    $ menu_flag = True
    "You walk into the second dungeon cell to see a skeleton on the floor."
    menu:
        "Examine the skull":
            jump examine_skull
        "Examine the ribs":
             jump examine_ribs
        "Examine the hands"if not eatenBread:
            jump examine_hands
        "Back out of the cell":
            jump to_Dungeon
    jump to_dungeon_2
             
label examine_skull:
    $ menu_flag = True
    "You take a closer look at the skull and notice that it has become merged with the stone floor."
    "You also notice that there is a strange gaping hole that looks vaguely key-shaped in the center of the skull."
    if SkeletonKey in bag:
        "Would you like to insert you skeleton key?"
        menu:
            "Yes":
                "You now realize that there are three small buttons on the skull. You assume that you need to press them in a certain order. "
                "The three buttons are Snake Bird and Fish, which do you want to start with?"
                menu:
                    "Snake":
                        "The buttons reset..."
                    "Bird":
                        "The button stayed pressed. What next?"
                        menu:
                            "Snake":
                                    "The buttons reset..."
                            "Bird":
                                    "The buttons reset..."
                            "Fish":
                                    "The buttons stayed pressed, what next?"
                                    menu:
                                        "Snake":
                                            "CLICK!"
                                            "A part of the wall behind the skeleton just shifted back, revealing a hidden door."
                                            "Upon pushing open the door you see a path leading away from the mansion!"
                                            "You run out to freedom..."
                                            jump escape
                                        "Bird":
                                            "The buttons reset..."
                                        "Fish":
                                            "The buttons reset..."
                    "Fish":
                        "The buttons reset..."

                #Bird fish snake
            "No":
                "You back away from the skeleton"

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
            $eatenBread = True
            jump eat_bread_dungeon
        "Back away from the skeleton":
            jump to_dungeon_2#_options
    jump examine_hands
             
label eat_bread_dungeon:
    $ menu_flag = True
    "You take the bread from the skeleton's hands and eat it."
    "It's a bit dusty and stale but it helps settle your stomach, and calm your nerves."
    call updateSanity(-20)
    jump to_dungeon_2#_options
    #restore sanity +10 if sanity < 100, else no change
     
label to_dungeon_3:
    $ menu_flag = True
    "You enter the third dungeon cell and immediately stop when you hear the jingling of chains from within the cell."
    menu:
        "Investigate the noise":
            jump chained_husk
        "Back out of the cell":
            jump to_Dungeon
    jump to_dungeon_3
             
label chained_husk:
    $ menu_flag = True
    "You step forward slowly and as you get closer you find the source of the rattling chains."
    "Someone chained a husk up in this cell, and you can see its silhouette as it struggles uselessly against the chains."
    "You feel badly for the creature but you know that whoever it was lost their mind long ago."
    "You back out of the cell as the husk continues its struggle to break free."
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
    jump to_dungeon_4
         
label examine_gold_band:
    $ menu_flag = True
    "The piece that caught you eye is a particularly exquisite golden band."
    menu:
        "Take the golden band":
            jump take_golden_band
        "Leave the golden band":
            jump to_dungeon_4#_options
    jump examine_gold_band
             
label take_golden_band:
    $ menu_flag = True
    "You pick up the golden band and put it into you bag."
    $bag.items.append(Crown)
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
            jump attemptToOpenBasementDoorToFirstFloor
        
        "Turn Back":
            jump to_basement
    jump from_basement
                  
#when player doesn't have the basement key in their bag   
label attemptToOpenBasementDoorToFirstFloor:
    $ menu_flag = True
    if BasementKey not in bag:
        "You attempt to open the door but it won't budge, it looks as if you may need a key to get in."  #only way to get to basement through mechanic? (unlocked_basement jump after play has unlocked the door)   
        jump basement_door_to_first_floor
    #basement_door_unlocked
    else:
        "You insert the basement key and the door opens effortlessly."
        jump entrance_hall
     #jump basement_door_unlocked_to_basement
 #to_Library_return and to_Lab_return jump calls to only display options upon returning to already visited locations  


#***NEEDS TO BE IMPLEMENTED***#
label up_level_2:
    with fade
    if bag.sanity > 50:
       play music "audio/Awkward Meeting.mp3" fadein 1.0 loop
    else:
       play music "audio/One of Them (Edited).mp3" fadein 1.0 loop

    "You go up the stairs to find yourself on the second floor."
    "Before you there is a stairway going up and  several labeled doors: 'Green Room', 'Orange Room', 'Red Room', 'Purple Room' and 'Master Bedroom'."
    menu:
        "Go to the Green Room":
            scene greenRoom
            with fade
            jump green_room
        "Go to the Orange Room":
            scene orangeRoom
            with fade
            jump orange_room
        "Go to the Red Room":
            scene redRoom
            with fade
            jump red_room
        "Go to the Purple Room":
            scene purpleRoom
            with fade
            jump purple_room
        "Go to the Master Bedroom":
            scene masterBedroom
            with fade
            jump master_bedroom
        "Go up the stairs in front of you":
            if PlainKey1 in bag:
                "You unlocked the door with you plain key!"
                jump up_level_3
            else:
                "There is a locked, plain door..."

            jump up_level_3 #to the third floor
        "Go back down the stairs to the main hall":
            jump entrance_hall #to the mainhall on level 1
    jump up_level_2
            
label return_level_2:
    scene mainhall
    with fade
    if bag.sanity > 50:
       play music "audio/Awkward Meeting.mp3" fadein 1.0 loop
    else:
       play music "audio/One of Them (Edited).mp3" fadein 1.0 loop
    "Before you there is a stairway going up and  several labeled doors: 'Green Room', 'Orange Room', 'Red Room', 'Purple Room' and 'Master Bedroom'."
    menu:
        "Go to the Green Room":
            scene greenRoom
            with fade
            jump green_room
        "Go to the Orange Room":
            scene orangeRoom
            with fade
            jump orange_room
        "Go to the Red Room":
            scene redRoom
            with fade
            jump red_room
        "Go to the Purple Room":
            scene purpleRoom
            with fade
            jump purple_room
        "Go to the Master Bedroom":
            scene masterBedroom
            with fade
            jump master_bedroom
        "Go up the stairs in front of you":
            if PlainKey1 in bag:
                "You unlocked the door with you plain key!"
                jump up_level_3
            else:
                "There is a locked, plain door..."

            jump up_level_3 #to the third floor
        "Go back to the main hall":
            jump entrance_hall #to the mainhall on level 1
    jump return_level_2
            
label green_room:
    $ menu_flag = True
    "In the Green Room you see a bed, a desk and a closet."
    menu:
        "Search the bed":
            jump search_green_bed
        "Search the desk":
            jump search_green_desk
        "Search the closet":
            jump search_green_closet
        "Leave the room":
            jump return_level_2
            
label search_green_bed:
     $ menu_flag = True
     "You find a nest of blankets under the bed."
     "It looks as if some has recently slept here."
     jump green_room
     
label search_green_desk:
     $ menu_flag = True
     "In the desk you find a crystal ball."
     "You stare into the ball, and see..."
     "Your own reflection."
     jump green_room
     
label search_green_closet:
     $ menu_flag = True
     "You open the closet to find a woman dressed in colorful rags murmuring to herself."
     menu:
         "Back away from the closet":
             jump green_room
         "Talk to the woman":
             jump talk_phoebe
         
label talk_phoebe:
    $ menu_flag = True #add dialog
    call talkToPhoebe
    jump green_room

label orange_room:
    $ menu_flag = True
    "In the Orange Room you see a bed, a desk and a closet."
    menu:
        "Search the bed" if Flashlight not in bag:
            jump search_orange_bed
        "Search the desk" if OrangeKey not in bag:
            jump search_orange_desk
        "Search the closet":
            jump search_orange_closet
        "Leave the room":
            jump return_level_2
            
label search_orange_bed:
     $ menu_flag = True
     "On the bed you find a flashlight."
     menu:
         "Test flashlight":
             jump test_flashlight
         "Take flashlight":
             jump take_flashlight
         "Back away":
             "You back away from the bed."
             jump orange_room
             
label test_flashlight:
    $ menu_flag = True
    "You pick up the flashlight and flip the switch, and a strong beam of light bursts forth."
    jump search_orange_bed

label take_flashlight: #add flashlight to bag
    $ menu_flag = True
    "You take the flashlight and put it into your bag."
    $bag.items.append(Flashlight)
    "You back away from the bed."
    jump orange_room

label search_orange_desk:
     $ menu_flag = True
     if metAvidem:
         "In the desk you see a strange key." #what is this and what does it have to do w/ Avidem
         menu:
             "Take the key":
                 jump take_orange_key
             "Leave the key":
                 "You back away from the desk"
                 jump orange_room
     else: 
        "There seems to be nothing on or in the desk."
        "You back away from the desk."
        jump orange_room

label take_orange_key: #add key to bag, or whatever happens with this specific key
    $ menu_flag = True
    "You take the key and put it into your bag."
    $bag.items.append(OrangeKey)
    "You back away from the desk."
    jump orange_room
    
label search_orange_closet:
     $ menu_flag = True
     "You open the closet to find nothing but dust."
     "You back away from the closet."
     jump orange_room
     
label red_room:
    $ menu_flag = True
    "In the Red Room you see a bed, a desk and a closet."
    menu:
        "Search the bed":
            if huskInRedBed:
                jump search_red_bed
            else: 
                "There's nothing here, just the bed where the husk had been"
                jump red_room
        "Search the desk":
            jump search_red_desk
        "Search the closet":
            jump search_red_closet
        "Leave the room":
            jump return_level_2

label search_red_bed:
     $ menu_flag = True
     "On the bed you see a motionless husk."
     menu:
         "Take a closer look":
             jump red_husk_attack
         "Back away":
             "You back away from the bed."
             jump red_room

label red_husk_attack:
    $ menu_flag = True
    $huskInRedBed = False
    "You lean in to get a closer look at the husk and it springs from the bed."
    "Before you know it you're being scratched and clawed by the rampaging husk!"
    "He beats you brutally and then runs away."
    call updateLives(10)
    "Luckily you have your first aid kit. You're alive but you had to use some of your supplies"
    jump red_room
    
label search_red_desk:
    $ menu_flag = True
    "In the desk you find notes with illegible scribbles on them."
    #if sanity is low enough maybe contain lore or information??? 
    #FIXED THIS IS A JOB FOR ANOTHER DAY :)
    #And that day is today :)))))
    if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
        "Riches... He had Riches but was not Contented...." ##ONLY THE DANKEST OF LORE
        "Gleaming.... Gleam of Jewel.... Gleam of Madness and Greed...."
        "Crimson.... Crimson Gem... Crimson Blood as he is Betrayed in his Sleep... Crimson Fog of Madness spreads forever and ever and ever"
    else:
        "You attempt to decipher anything useful but there is nothing to be learned here."
    "You back away from the desk."
    jump red_room
     
label search_red_closet:
    $ menu_flag = True
    "You open the door and see a rotting corpse inside."
    "The stench is horrible and the sight disturbs you."
    "You close the closet door and back away shaking."
    call updateSanity(-20)
    jump red_room
     
label purple_room:
    $ menu_flag = True
    "In the Purple Room you see a bed, a closet, and a man sitting at a desk."
    menu:
        "Search the bed":
            jump search_purple_bed
        "Search the closet":
            jump search_purple_closet
        "Talk to the man":
            "You approach the man, who seems to be writing on a pad of paper"
            jump talkToBasiltine
        "Leave the room":
            jump return_level_2

label search_purple_bed:
     $ menu_flag = True
     "Under the bed you find a mechanic's jacket."
     "The name tag on the jacket reads 'Archie'."
     "You back away from the bed."
     jump purple_room
     
label search_purple_closet:
     $ menu_flag = True
     "In the closet you find an fine old robe that looks like it's fit for royalty."
     "You close the closet door and back away."
     jump purple_room
    
label master_bedroom:
    $ menu_flag = True
    "In the Master Bedroom you see a woman sitting on the bed, a nightstand and a laundry chute."
    menu:
        "Investigate the laundry chute":
            jump bedroom_laundry_chute
        "Search the nightstand":
            jump search_nightstand_avidem
        "Speak to the woman":
            call talkToAvidem
            jump master_bedroom
        "Leave the room":
            jump return_level_2
            
label bedroom_laundry_chute:
    $ menu_flag = True
    "You approach the laundry chute."
    "You look down the chute and notice that it's fairly wide and might be able to fit a person."
    menu:
        "Climb into the chute":
            jump chute_to_laundry_room
        "Back away":
            jump master_bedroom
            
label chute_to_laundry_room:
    $ menu_flag = True
    "You squeeze into the chute and find it to be surprisingly roomy."
    "You let gravity take you and you slide down the metal chute."
    "You are thrown out of the shoot and  onto the floor of the laundry room."
    jump laundryRoom

label search_nightstand_avidem:
    $menu_flag = True
    "You see several photos on the nightstand."
    menu:
        "Get a closer look":
            jump avidem_alive_nightstand
        "Back away":
            jump master_bedroom

label avidem_alive_nightstand:
    "As you move in to get a better look at the pictures you notice the woman on the bed staring at you intensely."
    "All of a sudden a wave of fear overcomes you, and you freeze in place."
    "You turn your head to look at the woman and her gaze bring you to your knees."
    "She gets up and approaches you, then leans over and whispers into your ear 'Get out'."
    "You scramble to your feet and sprint out of the room, terrified."
    call updateSanity(-20)
    jump return_level_2
    
label up_level_3:
     if bag.sanity > 50:
        play music "audio/The Dread.mp3" fadein 1.0 loop
     else:
         play music "audio/Decay.mp3" fadein 1.0 loop
         "You enter the main hallway of the third floor and you see 8 doors."
         "There is an Office, a Bedroom, Game room, TV room, Nursery, Art studio, Charnel house and a room that looks as if it was the place of a large fire many years ago."
         menu:
             "Go to the Office":
                 scene office
                 with fade
                 jump to_office_3
             "Go to the Bedroom":
                 scene emptybedroom
                 with fade
                 jump to_bedroom_3
             "Go to the Game room":
                 scene gameroom
                 with fade
                 jump to_game_room
             "Go to the TV room":
                 scene TVroom
                 with fade
                 jump to_tv_room
             "Go to the Nursery":
                 scene nursery
                 with fade
                 jump to_nursery
             "Go to the Art studio":
                 scene artstudio
                 with fade
                 jump to_art_studio
             "Go to the Charnel house":
                 jump to_charnel_house
             "Go to the Burned room":
                 scene burnedroom
                 with fade
                 jump to_burned_room
             "Go down to the second floor":
                 jump return_level_2
            
label return_level_3:
    scene mainhall
    with fade
    if bag.sanity > 50:
        play music "audio/The Dread.mp3" fadein 1.0 loop
    else:
        play music "audio/Decay.mp3" fadein 1.0 loop
    "You enter the main hallway of the third floor and you see 8 doors."
    "There is an Office, a Bedroom, Game room, TV room, Nursery, Art studio, Charnel house and a room that looks as if it was the place of a large fire many years ago."
    menu:
        "Go to the Office":
            if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                scene office
                with fade
            else:
                scene officeInsane
                with fade
            jump to_office_3
        "Go to the Bedroom":
            if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                scene emptybedroom
                with fade
            else:
                scene emptybedroomInsane
                with fade
            jump to_bedroom_3
        "Go to the Game room":
            if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                scene gameroom
                with fade
            else:
                scene gameroomInsane
                with fade
            jump to_game_room
        "Go to the TV room":
            if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                scene TVroom
                with fade
            else:
                scene TVroomInsane
                with fade
            jump to_tv_room
        "Go to the Nursery":
            if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                scene nursery
                with fade
            else:
                scene nurseryInsane
                with fade
            jump to_nursery
        "Go to the Art studio":
            if bag.sanity < 50: # The number here is percent, this can be changed to whatever you want under 100
                scene artroom
                with fade
            else:
                scene artroomInsane
                with fade
            jump to_art_studio
        "Go to the Charnel house":
            jump to_charnel_house
        "Go to the Burned room":
            scene burnedroom
            with fade
            jump to_burned_room
        "Go down to the second floor":
            jump return_level_2
            
label to_office_3:
    $ menu_flag = True
    "In the office you see a desk, a table and a cabinet."
    menu:
        "Search the desk":
            jump office_desk_3
        "Search the table":
            jump office_table_3
        "Search the cabinet" if BasementKey not in bag:
            jump office_cabinet_3
        "Leave the room":
            jump return_level_3
            
label office_desk_3:
    $ menu_flag = True
    "In the desk you find several sheets of paper with illegible scribbles on them."
    "You place the papers back in the desk and back away."
    jump to_office_3
    
label office_table_3:
    $ menu_flag = True
    "On the table you find a faded map of the mansion."
    "You take a closer look, but the map is too faded to get a complete image of the map."
    "You decide that the map isn't worth taking so you leave the map on the table and back away."
    jump to_office_3
 
# add second Basement key
label office_cabinet_3:
    $ menu_flag = True
    "In the cabinet you find a key with a label reading 'Basement'."
    menu:
        "Take the key":
            jump take_key_3
        "Leave the key":
            "You leave the key in the cabinet and back away."
            jump to_office_3
            
label take_key_3:
    $ menu_flag = True
    $bag.items.append(BasementKey)
    "You put the basement key into your bag."
    jump to_office_3
        
label to_bedroom_3:
    $ menu_flag = True    
    "In the bedroom you see a bed, a closet and a desk."
    menu:
        "Search the bed":
            jump bedroom_bed_3
        "Search the desk":
            jump bedroom_desk_3
        "Search the closet":
            jump bedroom_closet_3
        "Leave the room":
            jump return_level_3
 
label bedroom_bed_3:
    $ menu_flag = True
    "As you approach the bed you notice that it's covered in blood."
    "You back away from the blood-stained bed and collect yourself."
    jump to_bedroom_3
    
label bedroom_desk_3:
    $ menu_flag = True
    "In the desk you find a strange looking key."
    "Upon further examination you realize the key is crafted in the likeness of a skull, with several bones protruding from it."
    menu:
        "Take the skeleton key":
            jump take_skeleton_key
        "Leave the skeleton key":
            "You leave the skeleton in the desk and back away."
            jump to_bedroom_3

# add skeleton key
label take_skeleton_key:
    $ menu_flag = True
    "You put the skeleton key into your bag."
    $bag.items.append(SkeletonKey)
    jump to_bedroom_3

label bedroom_closet_3:
    $ menu_flag = True
    "As you approach the closet you hear heavy breathing from within..."
    menu:
        "Open the closet":
            jump open_closet_3
        "Back away from the closet":
            jump to_bedroom_3

label open_closet_3:
    $ menu_flag = True
    "You open the closet door to see a husk staring back at you."
    "As you begin to back away it leaps at you wielding a letter opener!"
    "The husk attempts to stab you several times, but he manages to get only one good strike on your side."
    "You knock the husk down and sprint for the door, managing to escape with only one stab wound."
    call updateLives(10)
    jump return_level_3
# lose 1 health here^^^

label to_game_room:
    $ menu_flag = True
    "In the game room you see a lone table."
    menu:
        "Approach the table":
            jump game_room_table
        "Leave the room":
            jump return_level_3

label game_room_table:
    $ menu_flag = True
    "You see a chess board with only one of each black piece set up."
    menu:
        "Move the Pawn":
            "Nothing happens."
        "Move the Rook":
            "The chess piece won't budge."
        "Move the Knight":
            "As you touch the chess piece, a chilling wind whips through the room."
            "Do you really want to move it?"
            menu:
                "Yes":
                    "A noise comes from behind you"
                    "You turn around an a ghostly knight is standing inches from you"
                    if Sword in bag:
                        "You pull the sword that you found in the chess table from your bag and swing it before the knight has a chance to attack"
                        "Suddenly all the armor falls to the ground in a pile, as if the person inside suddenly vanished..."
                        $knightDead = True
                    else:
                        "Before you have time to react the knight slams you with his sword."
                        $bag.lives -= 15
                        "You black out."
                        "You wake up laying on the floor in front of the chess table."
                        "Maybe you could have defeated the knight if you had a better weapon..."
                        "Perhaps you should look closer at the chess board?"
                "No":
                    jump game_room_table
           
        "Move the Bishop":
            "Moving the chess piece reveals a slip of paper that was hidden underneath. It reads:"
            "'If you are wise, heed this order; Consort, Chivalry, Checkmate.'"
        "Move the Queen":
            "After moving the piece, you hear a soft click."
            "A hidden drawer, containing something that looks like a sword, slides out of the table."
            $bag.items.append(Sword)
        "Move the King": #if the knight is dead, give glass key, else nothing
            if knightDead:
                "The king moves to reveal a small compartment containing a glass key."
                "You take it and put it in your bag."
                $bag.items.append(GlassKey)
            else:
                "The king wont budge"
        "Back away":   
            jump to_game_room
    jump game_room_table
        
label to_tv_room:
    $ menu_flag = True
    "You see a television at the opposite end of the room."
    menu:
        "Take a closer look":
            jump look_tv
        "Leave the room":
            jump return_level_3

label look_tv:
    $ menu_flag = True
    "As you approach the TV you see..." #TODO add image based on sanity? or just add a default image.
    jump to_tv_room

label to_nursery:
    $ menu_flag = True
    "In the nursery you see a toy chest, a small pile of toys on the ground and a crib."
    menu:
        "Search the toy chest":
            jump search_toy_chest
        "Search the pile of toys":
            jump search_toy_pile
        "Search the crib":
            jump search_crib
        "Leave the room":
            jump return_level_3
            
label search_toy_chest:
    $ menu_flag = True
    "In the toy chest you see a few wooden blocks, a toy car and what looks like a gold crown."
    "The blocks and toy car have no use to you, but you have an odd feeling about the crown."
    menu:
        "Take the crown":
            jump take_toy_crown
        "Leave the crown":
            "You leave the crown in the toy chest and back away."
            jump to_nursery
            
label take_toy_crown:
    $ menu_flag = True
    $bag.items.append(FakeCrown)
    "You take the crown and put it into your bag." # add toy crown to the bag *NOTE* toy crown is the fake crown
    jump to_nursery
    
label search_toy_pile:
    $ menu_flag = True
    "You search through the small pile of toys and discover a box of matches underneath."
    menu:
        "Take the matches":
            jump take_matches
        "Leave the matches":
            "You leave the matches in the pile of toys and back away."
            jump to_nursery
            
label take_matches:
    $ menu_flag = True
    $bag.items.append(Matches)
    "You take the box of matches and put it into your bag." # add matches to the bag
    jump to_nursery
    
label search_crib:
    $ menu_flag = True
    "In the crib you see nothing, but you swear you can hear a baby crying..."
    "You back away from the crib and the crying fades away." #sounds based on sanity, if there's time.
    jump to_nursery

label to_art_studio:
    "In the art studio you see a singular painting hanging on the wall."
    menu:
        "Approach the painting":
            jump to_painting
        "Leave the room":
            jump return_level_3
            
label to_painting:
    $ menu_flag = True
    "As you approach the painting you see..." #TODO add image based on sanity?
    jump to_art_studio
    
label to_charnel_house:
    $ menu_flag = True
    "Upon entering the room you see several large meat hooks swaying back and forth."
    "You don't know why, but you are extremely unsettled by the hooks."
    menu:
        "Turn back":
            jump return_level_3
        "Keep going":
            jump inside_charnel_house
            
label inside_charnel_house:
    $ menu_flag = True
    "In the charnel house you see the swaying meat hooks and a metal table."
    menu:
        "Search the table":
            jump search_charnel_table
        "Leave the room":
            jump return_level_3
            
label search_charnel_table:
    $ menu_flag = True
    "On the table you see a chainsaw with old blood-stains on it."
    menu:
        "Take the chainsaw":
            jump take_chainsaw
        "Leave the chainsaw":
            "You leave the chainsaw on the table and back away."
            jump inside_charnel_house
            
label take_chainsaw:
    $ menu_flag = True
    "You take the chainsaw and stuff it into your bag. To your surprise the chainsaw fits inside."
    jump inside_charnel_house

label to_burned_room:
    $ menu_flag = True
    "In the burned room you see a pile of ash in the corner and what looks to be a corpse."
    menu:
        "Search the pile of ash":
            jump search_ash
        "Search the corpse":
            jump search_corpse
        "Leave the room":
            jump return_level_3
            
label search_ash:
    $ menu_flag = True
    "After digging through the ash pile you discover an old pacifier."
    "You decide it's of no use to you, so you leave it and back away."
    jump to_burned_room
    
label search_corpse:
    "As you approach the charred corpse you notice that it's grasping something in its hands."
    "You gingerly grab what looks like a note from the corpse's hands."
    "You attempt to read the note, but it has been severely burned.You cannot decipher any useful information."
    jump to_burned_room #note has information?

label choice_end_game:  
    $renpy.full_restart()
    return
    
## DONT PUT ANY CODE PAST HERE OR YOU WILL DIE!!!!! ##
    
