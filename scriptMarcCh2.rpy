# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc")
define l = Character(_("Loki"), color="#2ae6ff")
define g = Character(_("Garm"), color="#fffc30")
define lg = Character(_("Loki and Garm"), color="#ff3033")
define h = Character(_("Helpful Person"), color="#3033ff")

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

label start:

    # python runs at the moment the game starts
    # this means that all items that need to be bought need to be put here
    python:
        inventory = Inventory() # initializes number of credits too
        # for shop1
        choco = Item("Choco", 5)
        sushi = Item("Sushi", 20)
        fries = Item("Fries", 10)
        # for shop2
        tophat = Item("Golden Top Hat", 10)
        suit = Item("Golden Suit", 20)
        maxGGG = Item("Max Level GG Guide", 9001)

    # how to declare chapter
    scene black with dissolve

    show text "Chapter 2\nA True Gentleman?!" with Pause(5)

    # actual scene start
    scene black with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "lokidefault.png" or "lokidefault.jpg"
    # to the images directory.

    show lokidefault   # this would use lokidefault.png/lokidefault.jpg when character is added to the images directory

    # you can have multi-line text
    l """
    {i}Ah yes, happy birthday to me, woo...{/i}

    {i}I really don't understand why people care so much about birthdays, for me it's basically a day to eat cake.{/i}

    {i}I don't like cake, but company is always welcome.{/i}
    """
    # scenes
    scene greenaurora with dissolve
    show lokidefault
    show garmhappy at multibounce, right

    # These display lines of dialogue.

    g "KNOCK KNOCK!"

    l "Ugh, who's there?"

    g "IT'S ME!"

    l "What kind of joke is that?!"

    # the tag {b} needs an ending tag {b} to show where the tag ends
    # b is for bold text
    "{b}Garm opens the door and enters Loki's room.{/b}"

    show lokidefault at left
    with move

    g "How are you doing on this fine day?!"

    # this is an example of what a route would look like, usually if you want to put a bad end in your chapter
    menu:

        "Now, how am I feeling today..."

        "Positive":

            jump positive

        "Negative":

            jump negative

# this is an example of what a more complex series of events could look like
label positive:

    # Initialize a variable.
    $ gg_power = 5

    scene greenaurora
    with dissolve

    show lokidefault at center

    # you can do multi-line dialogue with tags used sometimes
    l """
    {i}I guess I have no real reason to feel sad since I'm used to being poor, and also I'd be such a downer if I said I -wasn't- in a good mood today.{/i}

    {i}Sure, why not at least play along to being happy today?{/i}
    """
    hide lokidefault
    show lokihappy at singlebounce, center
    l "I can't wait to see what today has in store for me!"

    show garmhappy at singlebounce, right
    g "Haha okay! Sorry I couldn't find a gift for you, so I'll just give you the credits I would have spent on a gift! What's your NeoMo?"

    l "{i}Aw they're so nice to me. They really didn't have to, but I can't turn them down when they're so willing to give me something for my birthday can I?{/i}"

    l "It's uh..."
    hide lokihappy
    show lokidefault at center

    l """
    {i}Man why did I name my NeoMo account this...{/i}

    TheRealLokiGG.
    """

    # showing characters after they've already been shown will have the most recent effect happen
    # this removes the previous instance of that character
    show garmhappy at multibounce, right
    g "HAHAHA, THAT'S SO FUNNY!"
    hide lokidefault
    show lokisad at depress, center
    l "Please don't speak of it again, haaaa..."

    g "In any case, here you go!"

    # how to earn credits
    $ inventory.earn(20)
    $ current_credits = inventory.credits
    # to show a variable's value in dialogue, put brackets around it

    hide lokisad
    show lokihappy at singlebounce, center
    l "Alright, I got it! Thanks so much! Now I have %(current_credits)d!"

    show garmhappy at singlebounce, right
    g "You're welcome!"

    l "Well um... time to share it with you in the form of food!"
    hide lokihappy
    hide garmhappy
    show lokidefault at left
    show garmdefault at right
    # credit example
    jump preshop1
    jump shop1

label preshop1:
    $ chococost = choco.cost
    $ sushicost = sushi.cost
    $ friescost = fries.cost
    $ inventory.earn(1000000)
label shop1:

    menu store1:

        "What do I want..."

        # multiple things can happen after every menu choice
        "Chocolate %(chococost)d":
            if inventory.buy(choco):

                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump resume1

        "Sushi %(sushicost)d":
            if inventory.buy(sushi):
                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump resume1

        "French Fries %(friescost)d":
            if inventory.buy(fries):
                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump resume1

label resume1:
    l "..."

    g "..."

    "{b}Looks at each other{/b}"

    lg "WHAAAAAAAAT?!" with vpunch

    lg "WHERE THE HECK DID THOSE CREDITS COME FROM?!"

    scene black with dissolve

    """
    They enjoyed their food and began to live the good life together.

    They weren't a couple, but Garm was Loki's only real friend and they both lived alone so it was Loki's choice for them to live together.

    Of course Garm refused at first, but Loki insisted since there would be no point in being rich with no one to share the riches with.

    Speaking of Fenrir...
    """
    show text "1 year later" with Pause(5)

    show lokidefault at depress, center

    "Loki woke up at 8AM per usual, but what was on his mind was unusual."

    l """

    {i}Living rich is nice since I don't really have a care in the world, but...{/i}

    {i}That thing that appeared by Fenrir way back when, what was that?{/i}
    """

    "Like, who thinks like that? Oh well, this makes my job easier."

    "Onwards with the story!"

    show garmhappy at right

    g "You're awake right?"

    l "Yea-"

    show garmhappy at multibounce, left

    "{b}Garm bounces into Loki's room and immediately rushes to open the blinds.{/b}"

    scene white with dissolve
    show lokidefault at depress, center
    show garmhappy at multibounce, left

    l "MY EYES!" with hpunch

    g "GOOOOOOD MORNING!"

    "{b}Loki gets out of bed.{/b}"

    scene lokiroom with dissolve
    show lokidefault at center
    show garmhappy at multibounce, left

    l "Agh... Um, Garm?"

    show garmhappy at left

    g "Oh, what is it, Loki?"

    l "I just randomly had this thought this morning, but what was that thing way back when Fenrir-"

    hide garmhappy
    show garmdefault at left

    l """
    Um, got taken away?

    There was something that appeared by her and I'm not sure if I'm just misremembering, but was that like a pet of hers or something?

    I still don't understand why Fenrir got taken away for something like that...
    """

    g """
    ...You're not crazy.

    That thing you're talking about is a Gentle Guy, but everyone calls them GGs.

    Well, people who know about them, that is.
    """

    l "Wait, you said that people know about them, who are these people?"

    g """
    The people include those of us with GGs, those who know others with GGs, and the LOLs.

    These are pretty self-explanatory, but the LOLs have the strongest GGs.
    """

    l "Oh, that makes sense. A year ago I was actually feeling pretty hopeless, you know being poor and not being able to do anything about it."

    hide garmdefault
    show garmhappy at left

    g "Haha, there's actually no real reason to feel totally hopeless!"

    l "{i}Thank goodness I'm not crazy, but now I have even more questions.{/i}"

    show lokidefault at right
    hide garmhappy
    show garmdefault at left
    $ gqcount = 0
    $ gqbonus = 0

label garmquestions:
    menu:
        set gq_menuset
        "What should I ask about..."

        "Wait, you said that people know about them, who are these people?":
            $ gqcount+=1

            g """
            The people include those of us with GGs, those who know others with GGs, and the LOLs.

            These are pretty self-explanatory, but the LOLs have the strongest GGs.
            """

            l "Wait, you said \"us\", do you mean to say that we both have GGs?"

            hide garmdefault
            show garmhappy at singlebounce, left

            g "Yep, that's exactly what that means!"

            l """
            Oh okay!

            ...

            ACTUALLY, WHY DIDN'T YOU TELL ME THIS BEFORE?!
            """

            g "You never asked!"

            menu:

                l "Oh um, well I guess that's true..."

                "Wait, but how do I have one?":

                    $ gqbonus = 1
                    hide garmhappy
                    show garmdefault at depress, left
                    g "Actually your parents and my parents were a part of the previous uprising against to LOLs, but they're either exiled from this area or dead now..."

                    l "Oh, can you teach me how to manifest a GG later? I'm probably going to have to sit and think for things a bit after I'm either done asking you questions or you get tired of answering them, haha."

                    hide garmdefault
                    show garmhappy at left

                    g "Sure thing!"

                    show garmdefault at left

                    jump garmquestions

                "{i}Ask nothing{/i}":

                    jump garmquestions

        "Why did Fenrir have to be taken away for manifesting their GG?":
            $ gqcount+=1

            g "They probably didn't want some kind of force strong enough to cause an uprising against the LOLs so Tyr made the decision to lock her up."

            l "But she was only acting in self-defense!"

            g "Yeah, but the LOLs care more about maintaining their power than human rights."

            l "That's not good at all..."

            jump garmquestions
        "Wait, you said LOLs have the strongest GGs, so how do GGs get stronger?":
            $ gqcount+=1

            g "Usually if one is related to someone who has a GG and/or a strong will to obtain something."

            l "Wait, so since you're Fenrir's sister, does that mean you have a GG?"
            jump garmquestions
        "I think I'm done asking questions.":
            jump resume2

label resume2:
    if gqcount==3:
        $ gg_power+=5
    scene black with dissolve

    "You can change scenes as much as you want in your chapter."
    "The original gg_power is set to %(gg_power)d."

    scene white with dissolve
    show lokidefault at center

    # gg_power example
    menu:

        "GG Power Test"

        "Add 5":
            $ gg_power+=5
        "Add 3":
            $ gg_power+=3
        "Minus 5":
            $ gg_power-=5

    "Now the gg_power is %(gg_power)d."
    "Menus don't even need to have an impact on a variable, it could be just text. This is good for getting to know characters, for example."
    "Now for an example of how to buy things to increase GG power with credits (credits)."

    # credits to buy GG upgrades example

    jump preshop2
    jump shop2

label preshop2:
    $ tophatcost = tophat.cost
    $ suitcost = suit.cost
    $ maxGGGcost = maxGGG.cost

label shop2:

    menu store2:

        "Welcome to the GG store, what can I get for you? You have %(current_credits)d credits."

        "Golden Top Hat (%(tophatcost)d credits)":
            if inventory.buy(tophat):
                l "This top hat defines a GG!"
                $ gg_power+=5
                $ current_credits = inventory.credits
                "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump resume3

        "Golden Suit (%(suitcost)d credits)":
            if inventory.buy(suit):
                l "A suit to enhance my GG!"
                $ gg_power+=10
                $ current_credits = inventory.credits
                "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump resume3

        "GG Max Level Book (%(maxGGGcost)d credits)":
            if inventory.buy(maxGGG):
                $ gg_power+=9001
                $ current_credits = inventory.credits
                "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump resume3

label fallthrough:
    l "Not enough credits..."
    jump shop2

label resume3:

    "After all that the gg_power is now %(gg_power)d."

    "{b}Good Ending{/b}."
    # This ends the game.
    return

label negative:

    scene black
    with dissolve

    show lokidefault at depress, center

    l "I don't feel so good."

    "{b}Bad Ending{/b}."
    # This ends the game.
    return
