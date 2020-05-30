# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc", image="eileen")
define l = Character(_("Loki"), color="#2ae6ff", image="loki")
define g = Character(_("Garm"), color="#fffc30", image="garm")
define lg = Character(_("Loki and Garm"), color="#ff3033")
define h = Character(_("Helpful Person"), color="#3033ff")
define ge = Character(_("Grand Entrance"), color="33cc33")
define uf = Character(_("???"), color="#01116e")
define f = Character(_("Fenrir"), color="#01116e", image="fenrir")
define ut = Character(_("???"), color="#f2f2f2")
define t = Character(_("Tyr"), color="f2f2f2")

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
label chapter1:

    $ gg_power = 5
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

    show loki sad at depress, left
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

            show loki sad at left
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

            show loki sad at left
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
    return
