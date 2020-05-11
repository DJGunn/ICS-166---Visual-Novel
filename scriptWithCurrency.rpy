# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc")
define l = Character(_("Loki"), color="#2ae6ff")
define g = Character(_("Garm"), color="#fffc30")
define b = Character(_("Bad Guy"), color="#ff3033")
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

# python code for money-related things
init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        # credits == money
        def __init__(self, money=20):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False


# The game starts here.

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
    show garmdefault at multibounce, right

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
    show lokihappy at singlebounce, center
    l "I can't wait to see what today has in store for me!"

    show garmhappy at singlebounce, right
    g "Haha okay! Sorry I couldn't find a gift for you, so I'll just give you the credits I would have spent on a gift! What's your NeoMo?"

    l "{i}Aw they're so nice to me. They really didn't have to, but I can't turn them down when they're so willing to give me something for my birthday can I?{/i}"

    l "It's uh..."

    show lokidefault at center

    l """
    {i}Man why did I name my NeoMo account this...{/i}

    TheRealLokiGG.
    """

    # showing characters after they've already been shown will have the most recent effect happen
    # this removes the previous instance of that character
    show garmhappy at multibounce, right
    g "HAHAHA, THAT'S SO FUNNY!"
    show lokisad at depress, center
    l "Please don't speak of it again, haaaa..."

    g "In any case, here you go!"

    $ inventory.earn(20)
    $ current_money = inventory.money
    # to show a variable's value in dialogue, put brackets around it

    show lokihappy at singlebounce, center
    l "Alright, I got it! Thanks so much! Now I have %(current_money)d!"

    show garmhappy at singlebounce, right
    g "You're welcome!"

    l "Well um... time to share it with you in the form of food!"

    show lokidefault at left
    show garmdefault at right
    # credit example
    jump preshop1
    jump shop1

label preshop1:
    $ chococost = choco.cost
    $ sushicost = sushi.cost
    $ friescost = fries.cost

label shop1:

    menu store1:

        "What do I want..."

        # multiple things can happen after every menu choice
        "Chocolate %(chococost)d":
            if inventory.buy(choco):
                $ current_money = inventory.money
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_money)d credits remaining, thank you for using NeoFood!"
                jump resume1

        "Sushi %(sushicost)d":
            if inventory.buy(sushi):
                $ current_money = inventory.money
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_money)d credits remaining, thank you for using NeoFood!"
                jump resume1

        "French Fries %(friescost)d":
            if inventory.buy(fries):
                $ current_money = inventory.money
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_money)d credits remaining, thank you for using NeoFood!"
                jump resume1

label resume1:

    l "Ah yes this is going to be yummy!"

    g "IT'S GOING TO BE GREAT!"

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
    "Now for an example of how to buy things to increase GG power with money (credits)."

    # credits to buy GG upgrades example

    jump preshop2
    jump shop2

label preshop2:
    $ tophatcost = tophat.cost
    $ suitcost = suit.cost
    $ maxGGGcost = maxGGG.cost

label shop2:

    menu store2:

        "Welcome to the GG store, what can I get for you? You have %(current_money)d credits."

        "Golden Top Hat (%(tophatcost)d credits)":
            if inventory.buy(tophat):
                l "This top hat defines a GG!"
                $ gg_power+=5
                $ current_money = inventory.money
                "You have %(current_money)d credits remaining, thank you for using the GG Store!"
                jump resume2

        "Golden Suit (%(suitcost)d credits)":
            if inventory.buy(suit):
                l "A suit to enhance my GG!"
                $ gg_power+=10
                $ current_money = inventory.money
                "You have %(current_money)d credits remaining, thank you for using the GG Store!"
                jump resume2

        "GG Max Level Book (%(maxGGGcost)d credits)":
            if inventory.buy(maxGGG):
                $ gg_power+=9001
                $ current_money = inventory.money
                "You have %(current_money)d credits remaining, thank you for using the GG Store!"
                jump resume2

label fallthrough:
    l "Not enough credits..."
    jump shop2

label resume2:

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
