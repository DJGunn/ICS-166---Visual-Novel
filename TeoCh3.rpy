# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc", image="eileen")
define l = Character(_("Loki"), color="#2ae6ff", image="loki")
define g = Character(_("Garm"), color="#fffc30", image="garm")
define lg = Character(_("Loki and Garm"), color="#ff3033")
# define h = Character(_("Helpful Person"), color="#3033ff")
define ge = Character(_("Grand Entrance"), color="#33cc33", image="grandentrance")
define ggse = Character(_("GG Store Employee"), color="#1711ee", image="guard")
define pg = Character(_("Prison Guard"), color="#1711ee", image="guard")
define uf = Character(_("???"), color="#01116e")
define f = Character(_("Fenrir"), color="#01116e", image="fenrir")
define ut = Character(_("???"), color="#f2f2f2")
define t = Character(_("Tyr"), color="f2f2f2")
define jn = Character(_("Jormungandr"), color="#9300FF", image="jornaked")
define j = Character(_("Jormungandr"), color="#9300FF", image="jor")
define jgg = Character(_("Gentle Giant"), color="#CF6800", image="jorgg")
define jggf = Character(_("Gentle Giant"), color="#CF6800", image="jorggf")
transform singlebounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    yoffset 0

# stop bouncing by showing character again without bounce
transform multibounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    yoffset 0
    repeat

# moves character downwards
transform depress:
    pause .15
    yoffset 0
    easein .175 yoffset 20

# define colors for use
init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))

# python code for credits-related things
init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        # credits == credits
        def __init__(self, credits=20):
            self.credits = credits
            self.items = []

        def buy(self, item):
            if self.credits >= item.cost:
                self.credits -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.credits += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False


# The game starts here.

default gq_menuset = set()

label chapter3:

    # how to declare chapter
    scene black with dissolve

    show text "Chapter 3\nAn Unexpected Guest" with Pause(5)

    # actual scene start
    scene prisoncell with dissolve
    show fenrir neutral

    # you can have multi-line text
    f """
    We don't have much time so we need to hurry. Lots has happened while I have been in here and we need to act fast!

    You need to meet my cell mate Jormungandr. He is the reason you were able to get in here without any resistence!
    """
    # scenes
    hide fenrir
    show jornaked neutral at singlebounce, left 
    show garm suprised at right
    show loki neutral

    # These display lines of dialogue.
    play music "ominousbgm.wav"
    "{b}A half naked man steps out of the shadows to the surprise of the two visitors{/b}"

    jn "Hello, I am Jormungandr. I have been waiting for this meeting for many years." 

    jn "Loki, your current awakening of Grand Entrance is no mere coincidence. "

    jn "The LOLs have been pooling their resources to create a GG that nobody in the resistance can stand up to.... Loki... You are our champion."

    show loki surprised
    l "{b}WHAT?? Why me?{/b}"

    jn "Because Loki, you are one of them now. You have spent the last 5 years amassing wealth so you couldone day fight against the LOLs from the inside."

    jn "Your gentlemanly powers have matured enough to manifest Grand Entrance almost entirely on your own. You are our only hope Loki. You have much to learn."

    jn "I will teach you how to control your GG to fight against those that would use the power of the GGs for nefarious purposes."

    l """

    But I dont understand. How will Grand Entrance allow me to do anything to the LOLs? They have countless GGs to fight for them, and if what you say is true

    then they will soon have a GG stronger than any other in history.

    """

    jn "You will soon learn that you have a power greater than anything the elite LOLs will ever posess.... "

    jn "{b}Plot armor{/b}"

    show loki surprised
    l "Plot Armor? What is that?"

    show loki neutral
    jn "Have you never watched an anime? Naruto? Bleach? What do they all have in common?"

    jn "The main character can never die. Eventually they become incredibly OP and nobody stands a chance against them."

    jn "This is your story Loki. You were made for this."

    show loki mad
    l "I didn't ask for this! I wanted to save my friend, but I can't take on the LOLs all by myself!"

    
    jn "{b}You won't be alone!{/b}"

    play music "normalbgm.wav"
    hide jornaked
    show jor happy at left
    show jorggf neutral at multibounce, center
    show loki surprised at right

    j "This is my GG! Gentle Giant. Do not fear Loki, we have stronger allies than you think."

    j "Now you must choose a path. Will you fight for justice? Or will you run and hide, spitting on the backs of everyone who has put their life on the line to bring down the LOLs?"

    j "Come Loki, accept your fate and become the hero you were always meant to be!"

    show jorggf neutral at center
    # this is an example of what a route would look like, usually if you want to put a bad end in your chapter
    menu:

        "What should I do!?"

        "Fight":

            jump positive3_1

        "Run and Hide":

            jump negative3_1

# this is an example of what a more complex series of events could look like
label positive3_1:

    # Initialize a variable.
    $ gg_power = 20

    show loki mad at right
    l "I will fight. If I truly have this plot armor you speak of, and the fate of everyone in the rebellion lies in the balance. I guess I have no other choice."

    l "I can't just stand by as more and more people are exploited for the beneifit of the LOLs."

    show jor happy at left
    j "You made the right choice Loki. Now, there is much you must know before we leave here. I only recently allowed myself to be captured so that I could meet Fenrir here in prison."

    j "I couldn't reach you earlier as we all needed to be together in order for the next part of my plan to work. "

    j "Before we break out of this place, I need to tell you all more about what the LOLs are planning."

    j "Gentle Giant, you can go for now. I will call on you soon."

    hide jorggf neutral at center
    show jor neutral at left
    show loki neutral at right
    j "The LOLs have been moving their resources recently. Large amounts of cash have been flowing into accounts owned by Tyr and his allies."

    j "I don't know exactly what they have planned, but it can't be good."

    j "You don't know this, but Fenrir is the one that was onto them originally. If it weren't for her initial work we wouldn't know what we do now."

    j "As we speak, the LOLs are gathering their forces to stop any resistance before they can complete their ultimate plan."

    l "Okay, so how long do we have until they are at full strength?!"

    j "From what it seems they will be ready within the next few weeks. In this time we will gather the resources necessary to defeat the LOLs once and for all."

    j "Tyr, the scumbag that locked Fenrir up in the first place, is at the heart of the LOLs"
    show garm neutral at center

    g "If they know we are trying to gather our forces to fight against them, where will we hide?"

    j "Good question Garm. You three will have to go on your own into the wilderness. There is a safe place not far from the city that the LOLs will never find."

    j "I will have to leave you to take care of some things and may not be able to get back to you for a while. You must wait and begin training."

    j "You will be on the run for a while, so you must keep moving."

    g "But where will you be going?"
    
    j "I need to take care of some things in the city. There is even a chance that we won't meet again before we need to fight."

    show jor happy at left

    j "Do not be afraid though, you will meet people along the way who will help you."

    show jor neutral at left
    # you can do multi-line dialogue with tags used sometimes
    hide jor
    hide loki
    hide garm

    show fenrir neutral at singlebounce, center
    with hpunch

    f "Guys! Our time is running out, we need to start moving."

    f "The real guards are coming, They shouldn't be here!"
    
    hide fenrir neutral at center
    show jor neutral at right
    show loki neutral at left
    j "Loki, it is time for your first lesson."
    
    l "Okay, I am ready."

    l "What do I need to do."

    j "First you must manifest your GG."

    "Loki concentrates deeply, bringing up all of the gentlemanly power he can muster."

    show grandentrance at center

    show loki at singlebounce
    l "I did it!"
    j "Good."

    j "Now, there are many things that you can do with your GG. Things you couldn't even dream of."

    j "I can sense the gentlemanly power emenating from Grand Entrance."

    j "You must concentrate and connect with your GG. You will instinctively feel what you can have him do!"
    $ lr_flag = False
    menu:

        "What should Grand Entrance do!?"

        "Call To Arms!":

            jump cta

        "Milady":

            jump milady
        
        "Last Resort":

            jump lr

label cta:

    hide loki
    hide jor
    show grandentrance at center
    "Loki draws in a deep breath. Focuses on Grand Entrance and Grand Entrance alone."

    "Listening to his gentlemanly heart, Loki calls out to Grand Entrance."

    "Grand Entrance lets out an uninteligable sound"

    show grandentrance at singlebounce, center
    ge "{b}GAHAWEALL REEEEE ARAREMAMS"

    hide grandentrance
    show grandentrance at left
    show jorggf neutral at singlebounce, right
    with hpunch

    show jor neutral at center

    j "WOW! Grand Entrance forcefully manifested my GG. I can feel incredible strength coming from Gentle Giant."

    j "It seems as though Grand Entrance has powered up Gentle Giant."

    l "Why didn't it bring out Fenrir's GG?"

    j "I don't know, it may only bring out GG's that have the power that is needed for a specific situation."

    jump resume3_1

label milady:

    hide loki
    hide jor

    show grandentrance at right
    show garm neutral at left
    "Loki draws in a deep breath. Focuses on Grand Entrance and Grand Entrance alone."

    "Listening to his gentlemanly heart, Loki calls out to Grand Entrance."

    show grandentrance at center with move
    "Grand Entrance approaches garm. Bows deeply, gently grabs her hand and gives it a soft kiss."

    "Garm faints only to be caught by Grand Entrance. Grand Entrance lays her down softly on the cot so Garm can catch her breath."

    hide garm
    hide grandentrance
    show jor neutral at center
    j "Hmm, that is quite the charm. But I don't think that is what we need in order to get out of here Loki!"

    hide jor
    show loki neutral at center

    l "Sorry I was just listening to my heart!"

    menu:

        "What should Grand Entrance do!?"

        "Call To Arms!":

            jump cta

        "Last Resort":

            jump lr

label lr:
    $ lr_flag = True
    hide loki
    hide jor
    show grandentrance at center

    "Loki draws in a deep breath. Focuses on Grand Entrance and Grand Entrance alone."

    "Listening to his gentlemanly heart, Loki calls out to Grand Entrance."

    "Grand Entrance crosses his arms across his chest. Staring deeply at Loki."

    "Loki felt a sudden sense of dread. Grand Entrance was about to do something bad."

    "Grand entrance reaches his arms out suddenly"
    show grandentrance at singlebounce, center with hpunch

    "The entire building began to shake, The approaching guards began to scream!"

    $ gg_power -=10

    hide grandentrance
    show jor worried at center
    j "Loki! Stop it!! You're killing them"

    l "I'll try!"

    "Loki reached out to Grand Entrance, begging him to stop."

    "The building stopped shaking suddently, throwing everyone to the ground" with hpunch

    hide jor
    show fenrir neutral at center

    f "They are still alive, but they are unconscious. We need to get out of here. Is there anything else you can do Loki?"
    hide fenrir
    menu:

        "What should Grand Entrance do!?"

        "Call To Arms!":

            jump cta

label resume3_1:
    play music "ominousbgm.wav"

    show jor neutral at center

    if lr_flag == True:
        j "What Loki just did probably set off hundreds alarms, we are out of time."

        j "This is a long shot, but I sense more power from Gentle Giant than ever before."

        j "I believe I can break down this wall for us to escape to the city streets."

    else:
        j "I have never felt this kind of power from Gentle Giant."

        j "He is pulling me towards the wall. I think he wants to break it down!"

    j "Every, get ready to run. This is our only shot!"

    "Everyone was holding their breath as Jormungandr closed his eyes and focused on Gentle Giant. Urging him forward."
    hide grandentrance
    hide jorggf
    show jorgg neutral at right
    show jorgg neutral at left with move

    stop music fadeout 1.0
    """ 
    A silence fell over the room.

    Gentle Giant approached the wall.

    Energy began forming around Gentle Giant's fist. 
    """

    "Gentle Giant slammed his hand into the wall, clasting it into pieces" with hpunch

    "A large hole replaced the former wall."

    hide jorgg
    j "Everyone out!! GO!"

    scene citystreet with dissolve

    

label negative3_1:

    stop music fadeout 1.0
    scene black
    with dissolve

    "Loki ran back to his home where he was met by the LOL forces that were looking for him."

    uf """
    Ah, hello Loki. So good of you to come. We've been waiting for you.
    """

    "Loki was slammed to the ground, before he could make a move he felt something smash into the back of his head."
    with vpunch
    uf "A pity, you could have been something great Loki. Now you will be nothing more than a body."
    "{b}Bad Ending{/b}."
    # This ends the game.
    return
