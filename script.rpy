# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc", image="eileen")
define l = Character(_("Loki"), color="#2ae6ff", image="loki")
define g = Character(_("Garm"), color="#fffc30", image="garm")
define lg = Character(_("Loki and Garm"), color="#ff3033")
define h = Character(_("Helpful Person"), color="#3033ff")
define ge = Character(_("Grand Entrance"), color="33cc33", image="grandentrance")
define uf = Character(_("???"), color="#01116e")
define f = Character(_("Fenrir"), color="#01116e", image="fenrir")
define ut = Character(_("???"), color="#f2f2f2")
define t = Character(_("Tyr"), color="f2f2f2")
define ggse = Character(_("GG Store Employee"), color="#1711ee", image="guard")
define pg = Character(_("Prison Guard"), color="#1711ee", image="guard")
define jn = Character(_("Jormungandr"), color="#9300FF", image="jornaked")
define j = Character(_("Jormungandr"), color="#9300FF", image="jor")
define jgg = Character(_("Gentle Giant"), color="#CF6800", image="jorgg")
define jggf = Character(_("Gentle Giant"), color="#CF6800", image="jorggf")
define b = Character(_("Baldur"), color="eeffff", image="baldur")
define s = Character(_("Surt"), color="ffeeee", image="surt")
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

#times before jumping
screen countdown1:
    timer timer_count action Jump(timer_label)

screen countdown2:
    timer timer_count action Jump(timer_label)

# define colors for use
init:
    $timer_count = 0
    $timer_label = 0
    $manifestations_done = False
    $rebellions_done = False
    $superiority_done = False
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))
    image cold = Solid((240, 255, 255, 255))

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
default ch1_menuset = set()

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
        tophat = Item("Golden Top Hat", 250000)
        suit = Item("Golden Suit", 750000)
        diamorph = Item("Diamond Morph Suit", 1000050)

    # how to declare chapter
label chapter1:

    scene black with dissolve

    show text "Chapter 1\nChildhood Friends" with Pause(5)

    # actual scene start
    scene black with dissolve

    # you can have multi-line text
    l "{i}My home has always been cold.{/i}"

    scene glacier with fade

    l "{i}Massive glaciers of twisted blue ice...{/i}"

    scene cloud with fade

    l "{i}Billowing clouds that blot out the sun...{/i}"

    scene wind with fade

    l "{i}Harsh winds that permeate your bones...{/i}"

    scene volcano with fade

    l "{i}Any warmth from the volcanoes throughout the land goes straight to the LOLs.{/i}"

    scene black with fade

    l "{i}The Lords of the Lands.{/i}"
    l "{i}Their immense wealth lets them have everything they could ever want.{/i}"
    l "{i}Warm, comfortable weather… plentiful, delicious food...{/i}"
    l "{i}Supernatural power bought through technological enhancements...{/i}"
    l "{i}The power of the Gentle Guy... of the GG... is one we could only dream of.{/i}"
    l "{i}With this wealth and power, they can bring ruin to our very lives...{/i}"

    # scenes
    scene lokichildhoodhome with fade
    play music "mellowbgm.wav" fadeout 1.0 fadein 0.0

    # These display lines of dialogue.
    l "....zzz...."

    uf "Loki."
    uf "Hey, Loki."

    l "mmm....zzz........"

    uf """
    Loki.
    Loki.
    Loki. Loki. Loki. Loki.
    """

    l "zz....hnghh....."

    uf "LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOKI!!!"

    play sound "book smack.ogg"
    l "{i}SMACK! I awaken to a heavy book smashing me in the face!{/i}"

    show loki surprised at left

    l "ugh... the hell?"

    l "{i}Standing in the doorway is the book-hurling culprit- my best friend, Fenrir.{/i}"

    show fenrir neutral at multibounce, right

    l "{i}To start, I’m being woken up by my best friend throwing a plot device book at me?{/i}"
    l "{i}What is this? A poorly-written visual novel?{/i}"

    show fenrir happy at right
    show loki neutral at left

    f "Hah! It's time you got up anyways!"

    show fenrir happy at singlebounce, right

    "{b}She laughs and gestures back to the book with a head nod, rustling her choppy dark hair.{/b}"

    f "Look at the book!"

    show loki mad at depress, left
    l "{i}I sigh in exasperation before mindlessly reaching for it.{/i}"
    show fenrir sad at depress, right
    l "If it’s another book of anthropomorphic animal people- Well then it’s the end of our friendship."


    show fenrir happy at singlebounce, right
    f """
    Hey, those drawings are cool!
    I was gonna show you the one I made. I gave her blue fur and-
    """
    show fenrir sad at depress, right
    f "Wait. Ugh that's not the point-"
    show fenrir happy at singlebounce, right
    f "C'mon, it's a book about GG's!"

    show loki surprised at left
    show fenrir neutral at singlebounce, center with move
    l "{i}She bounds up onto the bed to peer over my shoulder.{/i}"
    show loki neutral at left
    l "{i}The fact that she’s taller than me despite us being the same age is a bit irritating, but I turn my focus to the book instead.{/i}"
    l "{i}The cover shows a with thick dark hair proudly standing beside a massive godlike woman in black robes.{/i}"
    l "{i}The CLEARLY exaggerated proportions of both women cast doubt on the artist’s art skill AND their tastes.{/i}"

    show fenrir happy at singlebounce, center
    f "Wow, that lady and her GG are awesome!"
    show fenrir neutral at center
    l "{i}...and Fenrir's too.{/i}"
    l "{i}Rolling my eyes, I open the book to see the table of contents.{/i}"

label book:
    menu:
        set ch1_menuset
        "What should I read first...?"

        "GG Manifestations":

            l "{i}It would be cool to manifest a GG, so I turn to the chapter and begin reading.{/i}"
            "A Gentle Guy, commonly referred to as a GG, is a manifestation of a person's gentlemanly spirit."
            "Therefore, a person having a strong gentlemanly spirit, one that is too strong to contain within themselves, can result in a manifestation."
            "These manifestations vary in appearance based on each individual's perception of being a gentleman, from humanoid to animal to chanting amalgamation of eyes and tentacles."
            "Over time, the number of natural manifestations as well as those with GG's have diminished greatly."
            "These changes are a result of the GG Rebellions and the overwhelming power from the credit-powered LOL's GG's."
            "More details regarding the GG Rebellions are provided in its unique chapter."
            l "{i}I feel like I learned about GG's. Reading further might tell me more though.{/i}"

            if manifestations_done == False:
                $gg_power += 1
                $manifestations_done = True
            jump book

        "The GG Rebellions":

            l "{i}The word 'rebellion' peaks my interest, so I turn to the chapter and begin reading.{/i}"
            "GG's have existed throughout history with powerful figures such as ."
            "However after the 'Dreadful, Most Horrifying, Seriously I Can't Even Describe How Bad it Was Event' and the subsequent rise of the LOL's to power, GG's became much more common."
            "Individuals who wanted to improve the lives of their loved ones, who bonded with those experiencing the same hardships, who wanted to fight against the {s}un{/s}fairness of the LOLs..."
            "These people began quickly manifesting GG's and helping others manifest their own until they numbered in the thousands."
            "With their newfound power in both numbers and GG's, they rebelled against the LOL's."
            "{s}Un{/s}fortunately, the LOL's quickly used their vast credit stores to help their GG's reach insane levels of power allowing them to handily crush the rebels."
            "Any who refused to submit were often exi--- or k------. Any surviving children were often raised with LOL propa------- and closely monitored for any signs of reb-------."
            l "{i}I felt like some parts were missing, but I've learned a bit more about GG's.{/i}"

            if rebellions_done == False:
                $gg_power += 1
                $rebellions_done = True
            jump book

        "The Superiority of the LOLs":

            l "{i}I notice the chapter title is hastily scrawled onto the bottom of the table of contents, but flip to the page anyway.{/i}"
            l "{i}The actual chapter is in worse shape and looks to be just a stack of loose pages with more hastily scrawled text.{/i}"
            l "{i}I look to Fenrir, but she just shrugs so I read on.{/i}"
            "The LOL's are the truest masters of the GG. Therefore, honestly just stay awed at their majesty."
            "{s}We{/s} LOL's power of GG is far beyond any other, as they increase their power levels to the max."
            "The technology needed to power up a GG is only available to LOL's."
            "Even the lowest level upgrade costs 5000 credits. That's more than a peasant like you will ever see in your life."
            "So just give up now, got it?"
            l "{i}I'm not sure how educational that was...{/i}"

            $superiority_done = True
            jump book

        "Books are for nerds. I'm not reading this." if manifestations_done == False and rebellions_done == False:

            show loki mad at left
            l "{i}I close the book and toss it aside. I don't have time for this.{/i}"
            show fenrir sad at depress, center
            f "What're you doing? I thought we were gonna read it together.."

            menu:

                "There are those puppy dog eyes..."

                "Ugh. Fine.":

                    show fenrir happy at singlebounce, center
                    l "{i}She instantly perks up and smiles.{/i}"
                    l "{i}I know she played me, but I'm powerless against her when she does that...{/i}"
                    l "{i}I sigh, pick up the book, and open the table of contents.{/i}"
                    jump book

                "Nope. That won't work.":

                    l "{i}She pouts at me and picks the book up.{/i}"
                    show fenrir mad at center
                    f "I'll just read it later myself. You'll regret it when I find out all the secrets of the GG and you don't!"
                    $gg_power -= 1
                    jump finishbook

        "Books aren't for nerds, but I am done reading this." if manifestations_done == True and rebellions_done == True:

            l "{i}Finished with my readings, I close the book and hand it back to Fenrir.{/i}"
            show fenrir happy at center
            f "Thanks for reading it! Isn't it awesome?"
            $gg_power += 1
            jump finishbook

label finishbook:

    show loki neutral at left
    show fenrir sad at depress, right with move
    f "Oh man, I wish I could use a GG...the LOLs are so lucky."
    show fenrir neutral at right
    f "All I've got is this knife I fished out of a river."

    l "{i}She flicks open the knife a little to close to my arm for comfort.{/i}"
    show fenrir happy at singlebounce, right
    f "It's pretty cool though right!"

    f "Anyways, d'ya think I could get Tyr to teach me how to use a GG?"

    l "{i}Tyr is the only LOL we’ve ever met.{/i}"
    l "{i}He’s the uptight law-toting sort, but he’s nice enough to actually talk to kids like us.{/i}"
    l """
    {i}Fenrir likes him a lot though. {/i}
    {i}80 percent of that affection is probably because he dresses like an old school detective.{/i}
    {i}The leather gloves, the trenchcoat, and all.{/i}
    """
    l "He can’t give away all their secrets. They don’t want you surpassing them."

    show fenrir sad at depress, right
    f "Lame."
    show fenrir neutral at singlebounce, right
    f "Crap, the sun is going down! I have to get back to make dinner!"
    show fenrir happy at multibounce, right
    f "Oh, come with! Garm will wanna see you!"
    f "And we're having our once a month curry~"

    menu:

        "Curry, huh...?"

        "I love curry.":

            show loki happy at left
            l "Well, I’m there then! I can’t say no to curry."

            f "Wow! Guess I should’ve led with curry."

            jump rejoincurry

        "I don't like curry.":

            show loki mad at left
            l "You know curry isn’t really my favorite..."

            f "Just come for Garm then! We can always make you some food for people who don’t have taste buds."

            jump rejoincurry

label rejoincurry:

    show loki neutral at left
    show fenrir at singlebounce, right
    f "Let's hurry up then!"

    show loki happy at singlebounce, center with move
    l "{i}We both quickly pile on a closet full of coats, scarves, and hats before making the trek through the snow to Fenrir’s house.{/i}"

    scene black with fade
    stop music
    l "{i}The house is quiet and dark as we enter.{/i}"
    l "{i}Fenrir’s pathetic attempts at whispering cut through the silence.{/i}"

    show fenrir neutral at right
    play music "ominousbgm.wav" fadeout 1.0 fadein 1.0
    f "Why's it all dark? Is Tyr still here?"

    hide fenrir neutral
    scene stairs with fade
    l "{i}We tiptoe up the stairs, trying to avoid disturbing the tense atmosphere.{/i}"
    l "{i}At the top, we hear the barest hint of Garm’s voice.{/i}"

    g "Please..."
    g "Fen... please come back..."

    ut "Just stay still please."
    ut "The laws of this land state you must listen. We Lords have the ultimate power."

    l """
    {i}Ugh, that must be Tyr. Those robotic words...{/i}
    {i}Wait! What is he saying to Garm?{/i}
    """

    show fenrir mad at center
    play music "battlebgm.wav" fadeout 0.0 fadein 2.0
    l "{i}I hear Fenrir gasp beside me and glimpse a flash of silver in her hand.{/i}"

    l "{i}Her knife!{/i}" with vpunch

    show fenrir mad at singlebounce, right with move

    l "{i}Before I can respond, she leaps towards the door and rips it open-{/i}"

    l "{i}-to witness the horrifying scene before us...{/i}"

    scene fenrirhouse with fade
    show garm sad at depress, left
    l "{i}Garm is huddled in one corner of the room with Tyr towering over her.{/i}"
    l "{i}Her eyes are wide and pleading as Tyr stretches one glove-clad palm towards her bare thigh.{/i}"

    show fenrir mad at singlebounce, right
    f "You!"
    f "Loki, block the door!"

    t "Stay where you are!"

    $timer_count = 3
    $timer_label = 'stay'
    show screen countdown1

    menu:

        "What should I do...?"

        "Block the door":
            hide screen countdown
            l "{i}I quickly stand in front of the door, both to help Fenrir and to avoid her wrath.{/i}"
            $ gg_power += 2
            jump rejoinorder

        "Stay where you are":
            hide screen countdown
            jump stay

label stay:

    l "{i}I can’t help unconsciously following an order of a powerful LOL and instead uselessly stand in the middle of the room.{/i}"

    jump rejoinorder

label rejoinorder:
    l "{i}Despite me, Fenrir begins yelling as Tyr stands frozen.{/i}"

    f "You tricked us!" with vpunch

    "{b}Fenrir strides towards Tyr, knife in hand, and angry words spill from her mouth...{/b}"
    "{b}...but the words are different...{/b}"

    f """
    I trusted you!
    Garm trusted you!
    My family and I placed our trust into your hands, but you tainted it!
    Tainted it with your selfish lust..
    """
    "{b}The air surrounding her body seems to chill as she takes another step forward.{/b}" with hpunch
    scene cold with dissolve
    hide fenrir
    hide garm
    """
    {b}Cold blue light fills the room as Fenrir raises her knife-wielding hand above her head.{/b}
    {b}It’s cold.{/b}
    {b}Cold like the ice of our home... like the steel of the knife...{/b}
    {b}Like the eyes of the ghostly wolf rising from the light!{/b}
    """
    play sound "howl.wav"
    show protectorofthepack at center with hpunch
    "{b}The wolf's large body fills the room as it floats besides Fenrir, both shielding her and following her movements.{/b}"

    show fenrir mad at right
    f "I WILL PROTECT MY PACK!" with vpunch
    f "Your sinful hand will never touch anyone again!"

    "{b}In a flash and with an echo of fangs, she swings her knife toward Tyr's hand-{/b}" with vpunch

    stop music
    play sound "knife meat.wav"
    queue sound "bite.ogg"
    "{b}Leaving behind a bloody stump, as his hand falls to the ground with a sickening squelch...{/b}"

    scene black with dissolve
    l "{i}The blue light dissipates from the room along with the wolf within it, leaving us with only darkness and our shaky breaths.{/i}"

    t "Of course you would end up being trouble..."

    scene white with dissolve
    """
    {b}Suddenly, harsh lights flash into the room as guards pour in.{/b}
    {b}They hone in on Fenrir and push her down to the ground, forcing her hands into cuffs.{/b}
    """
    $timer_count = 2
    $timer_label = 'donothing'
    show screen countdown2
    menu:

        "They're going to take my best friend..."

        "Fight against the guards":
            hide screen countdown

            l "{i}I try to run towards Fenrir in a gallant attempt to stop the guards, but it’s useless.{/i}"
            l "{i}I take just one step and the remaining guards are on me, tossing me like a doll away from them.{/i}"
            $ gg_power += 3

            jump rejoinfight

        "Let it happen":
            hide screen countdown
            jump donothing

label donothing:

    l "{i}Even before I can take a step, I know it’s useless to fight them.{/i}"
    l "{i}The LOLs and their power are absolute. The only way I could win is if I was one...{/i}"

    jump rejoinfight

label rejoinfight:

    f "No! Ugh, just take care of Garm for me!" with vpunch
    f "I’ll be back! Just you watch!"

    l "{i}As they pulled my best friend away, I couldn’t get the vision of that powerful wolf reflecting the strength of Fenrir’s courage out of my head.{/i}"
    scene black with fade
    l "{i}That night, even as I comforted Garm, one thought remained...{/i}"
    l "{i}Could that ghostly wolf surrounding Fenrir in those last moments be the power of the GG...?{/i}"

    scene black with dissolve

    show text "Chapter 2\nA True Gentleman?!" with Pause(5)

    # actual scene start
    scene black with dissolve
    "{b}A couple years after that fateful night...{/b}"
    show loki neutral   # this would use loki neutral.png/loki neutral.jpg when character is added to the images directory

    # you can have multi-line text
    l """
    {i}Ah yes, happy birthday to me, woo...{/i}

    {i}I really don't understand why people care so much about birthdays, for me it's basically a day to eat cake.{/i}

    {i}I don't like cake, but company is always welcome.{/i}
    """
    # scenes
    scene oldlokiroom with dissolve
    show loki neutral
    show garm happy at multibounce, right

    # These display lines of dialogue.
    play music "normalbgm.wav"
    g "KNOCK KNOCK!"

    l "Ugh, who's there?"

    g "IT'S ME!"

    l @ surprised "What kind of joke is that?!"

    # b is for bold text
    "{b}Garm opens the door and enters Loki's room.{/b}"

    show loki neutral at left
    with move

    g "How are you doing on this fine day?!"

    # this is an example of what a route would look like, usually if you want to put a bad end in your chapter
    menu:

        "Now, how am I feeling today..."

        "Positive":

            jump ch2positive

        "Negative":

            jump ch2negative

# this is an example of what a more complex series of events could look like
label ch2positive:

    # Initialize a variable.
    $ gg_power = 5

    scene oldlokiroom
    with dissolve

    show loki neutral at center

    # you can do multi-line dialogue with tags used sometimes
    l """
    {i}I guess I have no real reason to feel sad since I'm used to being poor, and also I'd be such a downer if I said I -wasn't- in a good mood today.{/i}

    {i}Sure, why not at least play along to being happy today?{/i}
    """
    show loki happy at singlebounce, center
    l "I can't wait to see what today has in store for me!"

    show garm happy at singlebounce, right
    g "Haha okay! Sorry I couldn't find a gift for you, so I'll just give you the credits I would have spent on a gift! What's your NeoMo?"

    l "{i}Aw they're so nice to me. They really didn't have to, but I can't turn them down when they're so willing to give me something for my birthday can I?{/i}"

    l "It's uh..."

    l @ neutral "{i}Man why did I name my NeoMo account this...{/i}"

    l @ neutral "TheRealLokiGG."

    # showing characters after they've already been shown will have the most recent effect happen
    # this removes the previous instance of that character
    show garm happy at multibounce, right
    g "HAHAHA, THAT'S SO FUNNY!"

    show loki mad at depress, center
    l "Please don't speak of it again, haaaa..."

    g "In any case, here you go!"

    # how to earn credits
    $ inventory.earn(20)
    $ current_credits = inventory.credits
    # to show a variable's value in dialogue, put brackets around it


    show loki happy at singlebounce, center
    l "Alright, I got it! Thanks so much! Now I have %(current_credits)d!"

    show garm happy at singlebounce, right
    g "You're welcome!"

    l "Well um... time to share it with you in the form of food!"

    show loki neutral at left
    show garm neutral at right
    with move

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
                jump ch2resume1

        "Sushi %(sushicost)d":
            if inventory.buy(sushi):
                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump ch2resume1

        "French Fries %(friescost)d":
            if inventory.buy(fries):
                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump ch2resume1

label ch2resume1:
    stop music fadeout 1.0
    l "..."

    g "..."
    hide loki neutral
    hide garm neutral
    show loki surprised at left
    show garm surprised at right

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

    show loki neutral at depress, center

    "Loki woke up at 8AM per usual, but what was on his mind was unusual."

    l """

    {i}Living rich is nice since I don't really have a care in the world, but...{/i}

    {i}That thing that appeared by Fenrir way back when, what was that?{/i}
    """

    "Like, who thinks like that? Oh well, this makes my job easier."

    "Onwards with the story!"

    play music "mellowbgm.wav"
    show garm happy at right

    g "You're awake right?"

    l "Yea-"

    show garm happy at multibounce, left
    with move

    "{b}Garm bounces into Loki's room and immediately rushes to open the blinds.{/b}"

    scene white with dissolve
    show loki mad at depress, center
    show garm happy at multibounce, left
    play music "normalbgm.wav"
    l "MY EYES!" with hpunch

    g "GOOOOOOD MORNING!"

    "{b}Loki gets out of bed.{/b}"

    scene lokiroom with dissolve
    show loki neutral at center
    show garm happy at multibounce, left

    l "Agh... Um, Garm?"

    stop music fadeout 1.0
    show garm happy at left

    g "Oh, what is it, Loki?"

    l "I just randomly had this thought this morning, but what was that thing way back when Fenrir-"

    show garm neutral at left

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

    show garm happy at left

    g "Haha, there's actually no real reason to feel totally hopeless!"

    l "{i}Thank goodness I'm not crazy, but now I have even more questions.{/i}"

    show loki neutral at right
    show garm neutral at left
    with move
    $ gqcount = 0
    $ gqbonus = 0
    play music "mellowbgm.wav"

label garmquestions:
    menu:
        set gq_menuset
        l "What should I ask about..."

        "Wait, you said that people know about them, who are these people?":
            $ gqcount+=1

            g """
            The people include those of us with GGs, those who know others with GGs, and the LOLs.

            These are pretty self-explanatory, but the LOLs have the strongest GGs.
            """

            l "Wait, you said \"us\", do you mean to say that we both have GGs?"

            show garm happy at singlebounce, left

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
                    show garm neutral at left
                    g "Actually your parents and my parents were a part of the previous uprising against to LOLs, but they're either exiled from this area or dead now..."

                    l "Oh, can you teach me how to manifest a GG later? I'm probably going to have to sit and think for things a bit after I'm either done asking you questions or you get tired of answering them, haha."

                    show garm happy at left

                    g "Sure thing!"

                    show garm neutral at left

                    jump garmquestions

                "{i}Ask nothing{/i}":

                    jump garmquestions

        "Why did Fenrir have to be taken away for manifesting their GG?":
            $ gqcount+=1

            g "They probably didn't want some kind of force strong enough to cause an uprising against the LOLs so Tyr made the decision to lock her up."

            hide loki neutral
            show loki mad at depress, right
            l "But she was only acting in self-defense!"

            g "Yeah, but the LOLs care more about maintaining their power than human rights."

            l "That's not good at all..."
            hide loki mad
            show loki neutral at right

            jump garmquestions

        "Wait, you said LOLs have the strongest GGs, so how do GGs get stronger?":
            $ gqcount+=1

            #https://www.finaltouchschool.com/business/10-qualities-of-a-modern-gentleman/
            g """
            GGs become stronger based on their owner. In principle, the more gentlemanly, ladylike for girls, you are, the stronger your GG will be.

            This can include showing a geniuine interest in the people you're interacting with, helping someone in need, being a truthful and effective communicator, being virtuous, and the list goes on.

            However, the LOLs don't show many of these qualities so they make their GGs stronger by from making their GG looking sharper since that's where they can have unlimited possibilities through sheer credits.
            """

            l "Um, so basically either be more of a gentleman or just use money?"

            g "Or..."

            show garm happy at singlebounce, left

            g "BOTH!"
            show loki happy at singlebounce, right
            l "HAHA alright gotcha!"

            show garm neutral at left
            show loki neutral at right

            jump garmquestions

        "I think I'm done asking questions.":
            jump ch2resume2

label ch2resume2:
    show garm neutral at left
    show loki neutral at center

    if gqcount==3 and gqbonus==1:
        $ gg_power+=10
        g "Alright! In the future, do remember that your decisions will influence the power of your GG, for better or for worse!"

        g "Good job on showing interest in everything I was saying or leading up to in our conversation!"

        l @ happy "Thanks for talking with me about all of those things, Garm!"

        l "{i}Wait, is Garm an esper? Oh well, Garm is Garm and that's all that matters.{/i}"

    elif gqcount==3:
        $ gg_power+=5
        g "Alright! In the future, do remember that your decisions will influence the power of your GG, for better or for worse!"

        l "Thanks for letting me know about things, Garm!"
    elif gqcount < 3 and gqcount!=0:
        $ gg_power+=3
        g """
        Alright! In the future, do remember that your decisions will influence the power of your GG, for better or for worse!

        I was super eager to tell you things, but you didn't ask me about everything you were wondering about, wink wink!
        """
        l "I don't know what you mean, but thanks for letting me know about things, Garm!"

        l "{i}Wait, is Garm an esper? Oh well, Garm is Garm and that's all that matters.{/i}"
    else:
        $ gg_power-=10
        show garm sad at depress, left
        g "Oh, I thought you wanted to know things..."

        l "Sorry, I think I'm okay."

        g "Hmm... if you say so."

        l "{i}It seems like I didn't do something right, or as right as I could have... I'll be more careful in the future, hopefully.{/i}"

    g "Alright! On to breakfast!"

    l "That sounds good, I'm starving."
    stop music fadeout 1.0
    scene black with dissolve
    "Loki and Garm prepare some food and begin to eat."

    scene diningroom with dissolve
    show loki neutral at left
    show garm neutral at right
    play music "normalbgm.wav"
    l "After we eat, can you teach me how to use a GG?"

    g "Ah right, sure!"

    l @ surprised"Wow, you make that sound like it's easy to manifest a GG."

    hide garm neutral
    show garm happy at singlebounce, right

    g "It's not that it's easy, it's that I'm amazing!"

    "They eat for a bit and finish cleaning up and whatnot."

    g "Alright, time to go to the basement gym!"

    l @ happy "Okay, gotcha."

    scene indoorgym with dissolve
    show loki neutral at center
    show garm neutral at right

    g "Okay so think of what an ideal gentleman is to you, like really visualize it."

    l "Um okay got it."

    g "Now try REALLY hard to believe that it'll just pop out and become real."

    l @ mad "Mmmm... No actually can't do that part."

    g "Oh right, remember that episode of GoGo's Strange Venture where the main guy yells out \"SMOOTH PALMS\"?"

    l @ surprised "Wait are you serious so I'm supposed to try to be all epic and come up with a name?"

    g @ happy "That's exactly what I'm telling you to do!"

    l """

    {i}Hmm, well a gentleman does stand out looking all cool and stuff...{/i}

    {i}Mmmm, he needs to have a cool looking suit, good face, looks somewhat mysterious...{/i}

    {i}So basically he stands out and people's eyes go towards him as he enters an area...{/i}

    {i}What do you even call that, a grand entrance?{/i}

    {i}Well, here goes nothing!{/i}

    IT'S TIME TO MAKE YOUR APPEARANCE, GRAAAAAND ENTRAAAAANCE!!!
    """
    stop music fadeout 1.0
    show grandentrance at left with hpunch

    l "Ah okay."

    g "Yep, nice."

    lg "..."

    hide loki neutral
    hide garm neutral
    show loki surprised at center
    show garm surprised at right

    lg "HOLY CRAP IT ACTUALLY WORKED!" with vpunch

    hide loki surprised
    hide garm surprised
    show loki neutral at center
    show garm neutral at right

    play music "normalbgm.wav"
    g """
    ... Alright, so that's how to manifest your GG! Now, if you have watched Dokimon you can tell your GG to do things.

    Also, the more enthusiastic you are about what you're saying when you control your GG, it will do the thing you want better.
    """
    menu:
        l "{i}Oh, well in that case I guess I can just choose some gentlemanly trait and make it more dramatic right?{/i}"

        "GRAND ENTRANCE, USE DAZZLING GAZE AT GARM!":
            $ gg_power +=10
            stop music fadeout 1.0
            show grandentrance at singlebounce, left
            g @ surprised "Wha-"
            hide garm neutral
            show garm happy at singlebounce, right
            g "Oooo well hello handsome!"

            "Garm is now smitten with your GG, it was super effective!"

            l @ surprised "AAAA THAT'S WEIRD YOU CAN STOP NOW GRAND ENTRANCE!"

            hide garm happy
            show garm neutral at right
            g "Ahm, wow yeah that's something I haven't seen before, good job!"

        "Grand Entrance, use fly?":
            $ gg_power -=5
            stop music fadeout 1.0
            g @ mad "Didn't I just tell you that were were supposed to be enthusiastic? Dang it Loki..."

            g @ mad "Also if you didn't already notice, your GG is already flying..."

            l "Oh, you're right..."

            l "{i}I should really pay attention to what people are saying...{/i}"

    play music "normalbgm.wav"

    g "Yep, there are plenty of ways to use and not use your GG, but it'll be up to you to figure that out!"

    l "Um, so the LOL's don't really use the GGs by being all enthusiastic or gentlemanly right?"

    g "Right yeah, they buy stuff. Actually, do you want to go the place where you can buy things for your GG?"

    hide garm neutral
    show garm happy at right

    menu:
        l "{i}That doesn't sound like a bad idea.{/i}"

        "Yes":
            g "Alright! Though, why did you pause for a second?"
        "Yes":
            g "Alright! Though, why did you pause for a second?"

    l @ surprised "Um, no reason, lets go!"

    stop music fadeout 1.0
    scene black with dissolve

    "Loki and Garm take the NeoShuttle to the Neo Shopping District."

    scene mall with dissolve
    show loki neutral at left
    show garm happy at right

    play music "mellowbgm.wav"

    l "You made it sound like a really casual thing by the way, Garm."

    g "What do you mean?"

    l "A store for GG stuff? If most people can't even have a GG, wouldn't that mean that a store for GGs would not be a common thing?"

    g "You're right, but it's actually a gaming shop as a front, but there's a section in the back for actual GG items!"

    l "Oh wow okay, what is it called?"

    g "You'll know, Loki, you'll know."

    scene ggstoresign with dissolve
    play music "normalbgm.wav"

    g "Yep, here we are!"

    l "ARE YOU KIDDING ME!" with vpunch

    l "Okay lets just go in..."

    g "HAHA! Yeah, lets!"

    scene ggstore with dissolve

    # credits to buy GG upgrades example

    jump preshop2
    jump shop2

label preshop2:
    $ tophatcost = tophat.cost
    $ suitcost = suit.cost
    $ diamorphcost = diamorph.cost

label shop2:
    show guard happy at singlebounce, right
    menu store2:

        ggse "Welcome to the GG store, what can I get for you? You have %(current_credits)d credits."

        "Golden Top Hat (%(tophatcost)d credits)":
            if inventory.buy(tophat):
                show guard happy at singlebounce, right
                l "This top hat defines a GG!"
                $ gg_power+=5
                $ current_credits = inventory.credits
                show guard happy at singlebounce, right
                ggse "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump store2

        "Golden Suit (%(suitcost)d credits)":
            if inventory.buy(suit):
                l "A suit to enhance my GG!"
                $ gg_power+=10
                $ current_credits = inventory.credits
                show guard happy at singlebounce, right
                ggse "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump store2

        "Diamond Morph Suit (%(diamorphcost)d credits)":
            if inventory.buy(diamorph):
                show guard sad at right
                ggse """
                You're...
                You're hacking..."""
                $ gg_power+=9001
                $ current_credits = inventory.credits
                ggse "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump store2

        "Actually, I think I'm done buying things.":
            show guard happy at singlebounce, right
            ggse "Alright, thank you for coming to the GG Store!"
            jump resume3

label fallthrough:
    l "Not enough credits..."
    jump shop2

label resume3:

    if inventory.has_item(tophat) or inventory.has_item(suit):
        g @ neutral "Nice upgrade!"
    else:
        $ gg_power+=20
        g "Ooo, you don't want to buy things because you want to find your own strength, unlike the LOLs? That's pretty admirable!"

    # CONTINUE MARC
    scene mall with dissolve
    show loki neutral at left
    show garm neutral at right
    stop music fadeout 1.0
    g """
    Hmm...
    do you want to visit Fenrir?
    """

    l @ surprised "Wait, visit Fenrir? You know where she is and we can visit her?"

    g @ sad "Yeah, I was doing some research and there is this one prison that holds \"extremely dangerous individuals.\""

    g """I'm sure she has to be in there.
    Usually you'd think that the prison wouldn't allow something like that since everyone in there is so dangerous, but I think they're very confident in their security.
    """
    l @ mad"""
    {i}It's been so long... I mean I trust Garm's judgement, but actually being able to visit her today...{/i}

    {i}The same day I manifest my GG...{/i}

    {i}This can't just be coincidence...{/i}
    """

    l "Okay yeah lets go, lead the way Garm."

    scene black with dissolve
    "They walked for a couple minutes and one could feel the tension in the air."
    "They both were thinking of Fenrir, even during transit to the prison."

    scene prison with dissolve
    show loki neutral at right
    show garm neutral at center
    show guard neutral at left
    play music "ominousbgm.wav"

    g "Can we see Fenrir?"

    pg "One second, what's their last name?"

    g "Actually it's just Fenrir, so it should be at the top of your list."

    pg "Oh wow, that's interesting... and you are?"

    g "I'm Garm, her sister. The other one with me is Loki."

    pg "Ah okay, follow me."

    l @ surprised "{i}Wait, didn't I just run into this person?{/i}"

    scene prisoncell with dissolve
    show loki neutral at right
    show garm neutral at center
    show guard neutral at left

    pg "Okay you have visitors, Fenrir. You guys have an hour."

    f "Visitors?"

    hide guard neutral
    show fenrir happy at multibounce, left
    show loki happy at right
    show garm happy at center
    with move
    play music "normalbgm.wav"

    f "Garm! Loki!"

    show garm happy at multibounce, center
    g "It's so good to see you! Are you okay?! Did you miss us?!"

    show loki happy at singlebounce, right
    l "We've missed you so much!"

    f "Yes, yes, and yes! I've got some questions for you and I bet you guys have some questions for me too, haha!"

    l "Oh you bet we do!"

    g "There's so much to talk about!"

    scene black with dissolve
    stop music fadeout 1.0

    l "{i}Thank goodness she is able to still smile after all these years in prison...{/i}"

    l "{i}I can only hope things weren't too bad...{/i}"

    "{b}Good Path!{/b}"
    # This ends the game.
    jump chapter3

label ch2negative:

    stop music fadeout 1.0
    scene black
    with dissolve

    show loki neutral at depress, center

    l "I don't feel so good."

    g """
    Loki..?
    Loki?
    LOOOOOOOKIIIIIII!!!
    """

    "Loki died of..."
    "WAIT, HOW?!" with vpunch

    "{b}Bad Ending{/b}."
    # This ends the game.
    return

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
    show garm surprised at right
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
    $ gg_power += 20

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
    scene black with dissolve
    """
    Finally out in the streets, the group takes a moment to collect themselves.
    """
    scene citystreet with dissolve
    show jor neutral at center

    j """
    It is time we part ways. Keep moving out of the city. Into the forest, run West and you will find what you are looking for. I know things are uncertain.
    But you must do this. Good Luck.
    """

    hide jor
    "And just like that, Jormungandr was gone."

    show loki neutral at center
    show fenrir neutral at left
    show garm neutral at right
    l "Well, I guess we have no other choice."
    g "I guess so"
    f "This is crazy!"

    jump chapter4



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

label chapter4:

    # how to declare chapter
    scene black with dissolve

    show text "Chapter 4\Now...RUN!!" with Pause(5)

    # actual scene start
    scene prison-outside with dissolve
    show fenrir happy at singlebounce, center

    # you can have multi-line text
    play music "netherplace.mp3"
    f """
    {i}Cool! We escaped from prison. Let's take a break now.{/i}

    {i}Okay guys. What's the plan? {/i}
    """

    show fenrir happy at left with move
    show loki neutral at right

    l """
      {i}Well... That's a good question!{/i}
      {i}I didn't think about that...{/i}
      What do you think, Garm?
      """

    show garm surprised at center, singlebounce
    g "I thought you had the whole plan!"

    f @ mad "Any suggestions?! We need to keep moving!"
    f "We can go straight on this road and destory everything stops us!"

    g "What about we go this way? It's a less known path so it's safer."

    menu:

        "What to do..?"

        "Agree with Fenrir, go straight":

            l "I agree with Fenrir. We don't have time to waste. Let's go!"

            $ gg_power+=10

            jump road

        "Agree with Garm, go on the path":

            l "I agree with Gram. We can't fight right now."

            $ gg_power+=5

            jump path

        "I don't know...":

            l "I really don't know. Maybe...."

            $ gg_power-=10

            jump encountered

label road:

    scene prison-outside
    with dissolve
    play music "boxcat.mp3"

    show loki neutral at center

    l "I can hear the guards coming, let's go!"

    show fenrir happy at right

    f "As I know, there is only one obstacle on this road, that is Baldur."

    f @ neutral "He's the one responsible for keeping here for 3 years, and has never made mistakes."

    show garm sad at left
    g "Why did we choose this..?!"

    f @ happy "Haha.... Because I believe in you and Loki!"

    f @ neutral "If we can't win this fight, then that means we stay in prison. It's just fate at that point."

    l @ happy "Don't worry, we got this!"

    g "You guys are crazy!" with vpunch

    hide loki neutral
    hide garm sad
    hide fenrir happy

    scene fight1 with dissolve
    show baldur neutral at center, singlebounce
    play music "boxcat.mp3"

    b "I know you're there Fenrir!"
    b "Don't try to hide! It's a waste of time for both of us!"

    show baldur at left with move
    show fenrir neutral at right

    f @ mad "Okay, we're here, do what you will..!"

    b "I am the most faithful servant of LOL, Guardian outside the prison -- Baldur."
    b @ smile "Speak out your names! I never kill anyone unless I know their name!"

    hide fenrir neutral
    show loki neutral at right

    l "My name is Loki. I am sure I won't get killed here and I don't want to fight with you."
    l @ happy "What about you just let us go?"

    b "Are you insulting me?"
    b @ angry "Go to hell! I swear to the LOLs that you will die here today!"

    l "{i}It's not a good time to fight, let's finish this ASAP and get to a safe place.{/i}"
    # fight

    menu:

        l "How to fight though?"

        "Fight with Fenrir":

            l "I need your help, Fenrir. We can end this soon."

            $ gg_power+=10

            l "Attack the ice layer between us and him, cause cracks and run away!"

            show fenrir happy at center
            f "No problem. Come out, my GG! I will let you see my power."

            l "Show me your power, GG!"

            "The ice layer is broken. A huge crack is created between Baldur and the group of Loki."

            b @ angry "You insidious cunning villain..! I will catch you and you will regret for this!"

            l @ happy "Bye-bye!!"

            jump run

        "Fight with Garm":

            l "I need your help, Garm. We can end this soon."

            $ gg_power+=10

            l "Attack the ice layer between us and him, cause cracks and run away."

            show garm surprised at center
            g "Oh me? OK! let us do this. GG! Help me!"

            l "Show me your power, GG!"

            "The ice layer is broken. A huge crack is created between Baldur and the group of Loki."

            b @ angry "You insidious cunning villain..!"
            b @ angry "I will catch you and You will regret for this!"

            l @ happy "Bye-bye!!"

            jump run

        "Fight by Loki himself":

            l "I can do it by myself."

            $ gg_power-=10

            l "Show me your power, GG! Attack the ice layer between us and him."

            show fenrir happy at center
            f "Smart! Loki wanna create a crack"
            f @ sad "But it seems not work! Loki's power is not enough! Let us help him Garm."
            f "Come out, my GG!"

            hide fenrir happy
            show garm sad at center
            g "Oh, you silly boy Loki!! GG! Help me!"
            hide garm sad

            "Ice layer is broken. A huge crack between Baldur and the group of Loki."

            b @ angry "You insidious cunning villain..!"
            b @ angry "I will catch you and You will regret for this!"

            l @ happy "Bye-bye!!"

            show garm sad at center
            g "Stop talking shit. You almost got us killed!"

            l @ happy "Hahaha, it happens. A true gentleman will forgive me."

            jump run

        "Fight by Fenrir and Garm":

            l "Fenrir, Garm, let's do this!"

            l "Attack the ice layer between us and him, cause cracks and run away!"

            $ gg_power+=20

            show fenrir neutral at center
            f "Wise choise!"

            hide fenrir neutral
            show garm neutral at center
            g "I agree with you!"
            hide garm neutral

            l "Show me your power, GG!"

            "Ice layer is broken. A huge crack between Baldur and the group of Loki."

            b @ angry "You insidious cunning villain..!"
            b @ angry "I will catch you and You will regret for this!"

            l @ happy "Bye-bye!!"

            jump run


label path:

    scene path
    with dissolve
    play music "boxcat.mp3"
    show loki neutral at center

    l "Let's go, I can hear the guards coming!"

    show loki neutral at right with move
    show fenrir neutral at left
    f @ happy "I'm sure this path can buy us time."
    f "I noticed that you can't control your GG very well, did you practice using it?"

    l "What do you mean?"

    f @ neutral "I mean your GG actually is a very powerful one, but you only show 50 percent of its true power!"

    l @ mad "I thought I tried my best..."

    l "What am I doing wrong?"

    f "Let me teach you how to control your GG. I didn't waste time in these past years."
    f "The power of the GG comes from yourself. And that depends on the your gentlemanly qualities."
    f @ happy "Remember to be a gentlemanly at all times!"
    f "If you do that, you can exert its great power when you need to."
    f @ happy "Well, if you keep practicing from now on, that is!"

    l "Alright gotcha! Thanks Fenrir!"

    f @ happy "You're welcome!"

    hide loki neutral
    hide fenrir neutral
    "{b}Some time later...{/b}"

    show garm happy at center
    g "Finally we're out!"

    show fenrir happy at left
    f "Keep going. I don't think we're safe yet."

    jump run

label encountered:

    play music "battle1.mp3"

    f "What in the, they caught up!"

    "You lose! Loki and his friend got caught!"

    "{b}Bad Ending.{/b}"

    return

label run:

    scene glacier with dissolve

    show loki neutral at center
    play music "battle1.mp3"
    l "Oh no! The guards are here, we need to run now!"

    show loki neutral at left with move
    show baldur angry at right

    b "Stop running! I swear to the great LOLs that I  am gonna kill you all!"
    l @ happy "No way!!"

    hide baldur angry
    show loki neutral at center with move

    l "{i}They're annoying! We need to do something to get rid of them!{/i}"

    show garm sad at left

    g "No way, there is a guy there! We're surrounded!"
    l @ mad "Lets run by him at the fastest speed and get out of here ASAP!"

    hide garm sad
    l @ mad "Don't block us!"

    show loki neutral at left with move
    show surt suprised at right

    s "Stop! I'm not with them! Get into the ice cave and I'll help you!"

    menu:

        "Should Loki believe this guy?"

        "Yes, he looks nice!":

            l "It looks we can believe this guy. There are lots of exits in the ice cave. We can try."
            $ gg_power+=10

        "No, he is suspicious.":

            l "I can't believe you!"

            s "There is no other way. Just hide. I will deal with them."

            l "Don't let me down. You can't survive if can't."
            $ gg_power-=10


        "Loki and his group get into the ice cave."

    hide loki neutral
    show surt neutral at left with move
    show baldur angry at right

    b "Surt, an exile! Tell me, did you happen to see 3 strangers pass by just now?"

    s "If you are talking about one boy and two girls, they are going that way."

    b "All right, step back you useless waste!"

    hide baldur angry

    "Baldur went opposite to where Loki's squad was."

    play music "netherplace.mp3"

    show loki neutral at right

    l "Thanks man. You're a good guy."

    s @ smite "It's not safe yet. Let me lead you to my place."

    jump icecave

label icecave:

    scene icecave with dissolve

    show loki neutral at left
    show surt neutral at right

    s "Here is my place. You are safe now."

    l "Thanks again. Why did you help us, by the way?"

    s "My name is Surt. I helped you because I hate LOLs."
    s "Me and my sister Samira used to be servants of Baldur."
    s @ angry "One day I was gardening in the garden and Samira was serving a guest of Baldur."
    s @ angry "But my sister made a mistake by pouring the tea on the guests."
    s @ angry "After Baldur heard of it, he killed my sister. Then he burned me because I pleaded for her."
    s "Finally I was exiled here, the Icelandic wilderness."
    s "I don't have the power to avenge her, but I will do whatever I can to detriment the LOLs out of their sight."
    s "That's my story. A useless waste's story."

    l "Surt, I don't think you're a useless person. I mean it."
    l @ mad "LOLs are very cruel to the people."
    l @ mad "There are so many people who are dissatisfied with them outside and we decided to rebel against them."
    l @ happy "We'd love it if you could join us. Only you can save yourself."

    s "Can I? Are you willing to accept me who has nothing?"
    s "I have no power to contend with LOL... I will only drag you down."

    l @ happy "No problem, we think we can teach you how to manifest a GG."

    $counter = 0
    l "The power of GG comes from yourself. And that depends on QUALITIES OF A GENTLEMAN."
    l "Here is how to be a gentleman."

    menu:

        l "A gentleman chooses to be positive. What you will do if your friend make a mistake?"

        "Ignore it.":
            s "That answer sounds a little off what one would usually think...."
        "Encourage your friend to learn something from this mistake.":
            $counter+=1
        "Laugh at him.":
            s "That answer sounds a little off what one would usually think...."

    menu:

        l "A gentleman maintains a teachable posture and actively seeks new challenges. What you will do if you see something you never know?"

        "Escape from it.":
            s "That answer sounds a little off what one would usually think...."
        "Learn until you know it.":
            $counter+=1
        "Pretend not to see it.":
            s "That answer sounds a little off what one would usually think...."
    menu:

        l "A gentleman is well-spoken and a focused listener. He demonstrates conversational competence and leaves others feeling inspired, engaged, and understood."
        l "What you will do if someone want to talk to you?"

        "Escape from the guy.":
            s "That answer sounds a little off what one would usually think...."
        "Tell someone else to talk to him.":
            s "That answer sounds a little off what one would usually think...."
        "Listen carefully and show respect.":
            $counter+=1

    menu:

        l "A gentleman does the right thing even when no one is watching."
        l "What you will do if you walk on a street no one is there?"

        "Do whatever you want.":
            s "That answer sounds a little off what one would usually think...."
        "Just be yourself.":
            s "That answer sounds a little off what one would usually think...."
        "Only do the right thing even no one knows.":
            $counter+=1


    if counter == 4:
        $ gg_power+=20
        s "I can feel GG. I think I can do it."
    else:
        $ gg_power+=5
        s "I feel nothing about the GG. It is too hard for me."

    l @ happy "We still have time. Keep practicing."

    hide loki neutral
    hide surt neutral

    jump twodayslater


label twodayslater:

    "Two days later, outside the ice cave"

    scene wild with dissolve

    show baldur angry at center, multibounce
    play music "battle1.mp3"
    b "Surt! You useless waste! You lied to me!"
    b "I will to kill you with those who escaped!"

    show baldur angry at left with move
    show loki happy at right

    l "Look at this dummy, stupid and blames others!"
    l "Kill me if you can!"

    show baldur angry at center with move
    show guard neutral at left

    b "Go kill these escapers. I will kill Surt first!"
    l @ mad "Surt! Run!"

    hide guard
    hide loki happy

    show baldur angry at left with move
    show surt suprised at right

    b "Now it's only us! You're gonna die today, Surt!"
    s @ angry "I won't run anymore! The time of my revenge is now! Lets go GG, show time!"

    scene surtfight with dissolve

    s "This is payback for what you did to my sister!"

    "{b}Surt kills Baldur.{/b}"

    # This ends the game.
    jump chapter5

label chapter5:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene wild with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show loki surprised at left
    show fenrir neutral at right

    # These display lines of dialogue.

    l "Nice shot Surt!"

    f "We should keep moving now. More guards must be following us."

    show surt neutral
    s "It's too late now..."

    hide surt
    hide loki
    hide fenrir

    ut "Where do you think you're going?"
    "Suddenly there is a voice. It sounds like someone caught up."

    show loki surprised
    l "Who's that..."
    "Loki has never met this guy, but he can feel there is something unusual about him."
    hide loki

    show tyr neutral
    ut "I am Tyr, the blessed son of Hymir, Destined Hunter of Fenrir, the Immuned One."
    t "Fenrir, you will run no further."
    "Tyr spoke in a commanding tone, with a determined look in his eyes."
    hide tyr

    show surt neutral
    s "I'm sorry guys. I can't help you on this one, not with Tyr on the other side."
    s "I wish you the best of luck."
    "Surt runs away, as if they were being chased by a bear."
    hide surt

    show fenrir sad at left
    f """
    No no no no no no...

    Run Loki!

    You can't beat him! Run now!"""

    f "I'll surrender only if you promise not to hurt Loki."
    "Fenrir is terrified."
    "She knows him, and believes running away is the only way out of this."

    show loki surprised at right
    l "Don't be silly, I will never leave you behind!"
    l "I have manifested my GG power and I'll fight to my last breath to protect you!"
    "Loki looks into Fenrir's eyes."
    "After years of separation, how could he leave her here with this stranger?"
    "Even if Tyr's strong, Loki believed in his GG power."
    f "No you don't get it! Tyr is..."

    hide loki
    hide fenrir

    show tyr neutral
    t "Enough talk. Surrender now or embrace your fate."
    "Tyr is obviously bored."
    hide tyr

    show loki mad
    l "You're the one who's talking too much!"

    menu:
        "Manifest GG power":
            hide loki
            jump resume5_1

label resume5_1:
    show fenrir mad
    f "NO! STOP!"
    "Fenrir reached out to stop Loki, but it's already too late."
    hide fenrir

    show tyr neutral
    t "Boring."
    "Tyr didn't even move a bit."
    hide tyr

    show loki surprised at left and singlebounce
    l "AHHHHHHHHHHHHHHHHHH!"
    "Loki's power was somehow deflected back to himself?!"
    "Loki was knocked back to the ground, by his own GG power."

    show fenrir sad at right
    f "Loki! Are you alright! You can't use that against him!"
    "Fenrir runs to Loki, so worried that tear has filled her eyes."

    show loki mad
    l "That power...It's different from others..."
    "Loki could somehow feel that. He now knows Tyr might be his greatest enemy so far."
    l "How did you do that? Who are you! Answer me!"
    "Loki crawls up, stare right into Tyr's face."

    hide loki
    hide fenrir

    show tyr laugh
    t "So you really have no idea huh."
    show tyr happy
    t "I am the blessed son of Hymir."
    t "That means I am a Jötunn. Do you know what that means?"


    hide tyr

    show loki surprised at left
    show fenrir sad at right
    l "Jötunn? What...what's that??"
    f "It's the old name of..."
    f "The Giant"
    hide loki
    hide fenrir

    show tyr laugh
    t "Aren't you a little smarter than that moron."
    show tyr neutral
    t "Yes, I am the last giant walking on Earth."
    t "My contract with the elder gods protects me from your laughable GG power."
    t "Whoever use GG power in front of me will only experience that power deflected back to himself."
    t "Without your GG power, you are merely as mortal as human."
    hide tyr

    show fenrir sad
    f "Forget it Loki! Don't try again."
    f "It's my fate..."
    hide fenrir

    show loki surprised
    l "How...how could it be..."
    show loki mad
    l "I thought I finally have the power to protect you!"
    l "And this guy just jump out of nowhere and told me I am nothing??"
    hide loki

    show tyr confused
    t "This Déjà vu! Where have I seen this..."
    show tyr laugh
    t "Sisyphus!"
    t "Oh my god. You are Sisyphus in person!"
    t "You are the ultimate manifestation of absurd."
    show tyr happy
    t "Have you read The Myth of Sisyphus by Albert Camus?"
    t "Sisyphus is cursed to spend all his life to push a rock to the top of the mountain."
    t "Only have it rolled back to the bottom every single time."
    t "Camus said that Sisyphus's fate is no less absurd...but only tragic when he's conscious about his fate."
    show tyr laugh
    t "Isn't that you hahaha!"
    t "Spent your life to grow your GG power, only to find it's useless now."
    t "Now that you know it's useless, you are just tragic."
    show tyr neutral
    t "You thought you could do everything with your GG power."
    t "You thought there will be some Deus Ex Machina to help you out."
    t "You thought you are the protagonist of a manga."
    show tyr disgust
    t "Give up that childish fantasy of yours!"
    t "Do you have any idea what you have done?"
    t "Give her to me now."
    hide tyr

    show loki mad
    l "Tell me why! We haven't even met you before!"
    l "Why do you have to stop us!"
    hide loki

    show tyr confused
    t "Are you stupid or something?"
    t "Are you really a LOL?"
    hide tyr

    show loki mad at left
    l "I don't care! I just want to save Fenrir! She does not deserve being kept in that prison!"
    l "I just want some answers! Why do you all want her locked up when she has done nothing wrong!"
    show fenrir sad at right
    f "Stop Loki...You don't understand..."
    hide loki
    hide fenrir

    show tyr disgust
    t "I'm trying to save us all!"
    t "She's Fenrir! The wolf of Ragnarök! Don't you understand?"
    t "If she is not locked up, then someday she will trigger the doomsday!"
    t "You, me, Garm, Jormungandr, even Odin himself will all die along with this world!"
    t "All because of her!"
    show tyr neutral
    t "Now tell me again she's done nothing wrong."
    t "She's a threaten to the world simply by living."
    t "It is my fate to stop her, and I fully intend to do so."
    t "The only way you take her away today is by stepping over my body."
    hide tyr

    show fenrir sad at left
    f "He's right Loki..."
    f "I have tried to break out from that prison more times than I care to remember..."
    f "But Tyr always track me down and bring me back."
    f "He's a giant...no one can beat him without GG power..."
    show loki neutral at right
    l "What's his GG power?"
    f "He doesn't have GG power. That contract does not allow him to have one."
    f "But even so, he is still strong as hell! He once punched through a concrete wall to chase me!"
    f "Please...Just go!"
    l "So I can still punch him in the face right?"
    show fenrir mad at left and singlebounce
    f "Wh...what? No! Don't!"
    f "Didn't you listen to what I just said?"
    f "He is unbelieveably strong!"
    hide fenrir
    hide loki

    show loki neutral
    l "If that's the case, then it's all the same."
    l "A true gentleman will never step away when a lady is in need of help."
    l "Even without my GG power, you are still no comparison with me."
    hide loki

    show tyr confused
    t "Sigh...I really thought you could be more reasonable."
    show tyr happy
    t "Well, if this is what you desire, then I guess you are ready to break some bones."
    show tyr neutral
    t "Just yell for help when you can take it anymore."
    t "I'm not from Minneapolis so I'll let you go if you surrender."
    show tyr laugh
    t "But Fenrir stay with me anyway so don't struggle too hard."
    hide tyr

    "Now Loki will fight with his fist."
    "If Tyr shows disgust on his face, then click to throw a punch at him when he's losing balance!"
    "Don't click when Tyr shows joy, you can't win over his sheer strength!"
    "Comment: I tried to make a reaction-based fight, but I couldn't write it out in code."
    "Comment: Just click it."
    "Comment: Since you cannot lose the fight now, you can't reach bad end."
    "Comment: Bad end is Loki is mind-controlled to kill Fenrir then become a puppet."

python:
    tyrHealth = 5
    chance = 0
    while(tyrHealth > 0):
        chance += 1
        i = renpy.random.randint(1,5)
        if i < 3:
            renpy.show("tyr disgust")
            renpy.say("Tyr", "Wait!")
            tyrHealth -= 1
        else:
            renpy.show("tyr laugh")
            renpy.say("Tyr", "Just give up!")

label end:

    show tyr disgust
    "Somehow Loki winned this fight."
    "Now Tyr has passed out on the ground, but Loki still has not chilled down his rage."
    "He grabbed a stone beside him, and raised it right above Tyr's head."
    hide tyr

    show fenrir sad at left
    f "Loki! No! Don't!"
    show loki mad at right
    l "If I don't kill him now, he'll always come back to you!"

    hide loki
    hide fenrir

    menu:
        "Smash the stone into Tyr's head":
            jump normal_end
        "Put away the stone":
            jump good_end

label bad_end:

    return


label normal_end:

    "Loki is in so much rage that he couldn't control himself."
    "He poured all his strength into that stone, then smashed it down."
    "But there is no blood."
    "Tyr woke up right before the stone falled and dogded it."
    show tyr disgust at left
    t "I couldn't believe you actually tried to kill me!"
    t "You got me once, but not again."
    "Tyr throw a punch right into Loki's face. "
    "Loki is already exhausted from the previous fight. The punch is so forceful that Loki blacked out instantly."
    show fenrir sad at right
    f "NO!!!LOKI!!!"
    t "He chose his own fate."
    t "Now you must face yours."
    "Tyr took away Fenrir."
    "NORMAL END"
    return

label good_end:

    "Fenrir's yell put some sanity into Loki's head. He suddenly come back to his sense."
    "Loki drops the stone and stand up."
    show loki neutral at left
    l "Come! We must run now!"
    show fenrir happy at right
    f "Thank you Loki!"
    hide loki
    hide fenrir

    "The two ran away into the wilderness."
    "Will it be 'happily ever after'?"
    "Probably not. Ragnarok still will come someday."
    "But before that day comes, Loki and Fenrir will always stays by each other's side."
    "GOOD END"
    return
