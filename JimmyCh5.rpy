# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc", image="eileen")
define l = Character(_("Loki"), color="#2ae6ff", image="loki")
define g = Character(_("Garm"), color="#fffc30", image="garm")
define lg = Character(_("Loki and Garm"), color="#ff3033")
# define h = Character(_("Helpful Person"), color="#3033ff")
define ge = Character(_("Grand Entrance"), color="33cc33", image="grandentrance")
define ggse = Character(_("GG Store Employee"), color="#1711ee", image="guard")
define pg = Character(_("Prison Guard"), color="#1711ee", image="guard")
define uf = Character(_("???"), color="#01116e")
define f = Character(_("Fenrir"), color="#01116e", image="fenrir")
define ut = Character(_("???"), color="#f2f2f2")
define t = Character(_("Tyr"), color="f2f2f2")
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

label chapter 4:

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
    scene black with dissolve

    show text "Chapter 4\nnow...RUN!!" with Pause(5)

    # actual scene start
    scene prison-outside with dissolve
    show fenrir happy at singlebounce, center
    
    # you can have multi-line text
    play music "netherplace.mp3"
    f """
    {i}Cool!!We escaped from prison. Let us take a break now.{/i}

    {i}Ok guys. What is the plan? {/i}
    """
    
    show fenrir happy at left with move
    show loki neutral at right
    
    l """
      {i}Well...That is a nice question!{/i}
      {i}I didn't think about this.{/i}
      {i}What do u think, Garm?{/i}
      """
    
    show garm surprised at center, singlebounce 
    g "I thought you have the whole plan!"
    
    f @ mad "OKOK! Any suggestion? we need to keep moving!"
    f "We can go straight this road and destory everything stops us."
    
    g "What about we go this way? I know a path few people know. That is safer."
    
    menu:

        "Now, what is the next move?"

        "Agree with Fenrir, go straight":
            
            l "I agree with Fenrir. We don't have time to waste. Just go!"
        
            #$ gg_power+=10

            jump road

        "Agree with Garm, go the path":
            
            l "I agree with Gram. We can not fight right now."
        
            #$ gg_power+=5

            jump path

        "I don't know......":
            
            l "I really don't know. Maybe...."
        
            #$ gg_power-=10
            
            jump encountered


# this is an example of what a more complex series of events could look like
label road:

    scene prison-outside
    with dissolve
    play music "boxcat.mp3"
    
    show loki neutral at center

    l "Let us go. The guards are coming. I can hear that."
    
    show fenrir happy at right
    
    f "As I know, there is only one obstacle on this road, that is baldur." 
    
    f @ neutral "He has been responsible for keeping here for 3 years, and has never made mistakes."
    
    show garm sad at left
    g "Why we choose this...!"
    
    f @ happy "Haha.... Because I believe you and Loki!"
    
    f @ neutral "If we can not win this fight, that means we need to stay at prison. That is just a choice of fate."
    
    l @ happy "No worry. We got this!"
    
    g "You guys are crazy!!" 
    
    hide loki neutral
    hide garm sad
    hide fenrir happy
    
    scene fight1 with dissolve
    show baldur neutral at center, singlebounce
    play music "boxcat.mp3"
    
    b "I know you are there Fenrir"
    b "Do not try to hide! I don't want to waste time!"
    
    show baldur at left with move
    show fenrir neutral at right
    
    f "OKOK! Here we are!"
    
    b "I am the most faithful servant of LOL, Guardian outside the prison -- Baldur."
    b @ smile "Speak out your names! I never kill nonames!"
    
    hide fenrir neutral
    show loki neutral at right
    
    l "My name is Loki. I am sure I won't get kill here. And I don't want to fight with you."
    l @ happy "What about just let us go?"
    
    b "Are you insulting me? Go to hell!! I pormise to the LOL, you will die today"
    
    l "It is not a good time to fight, let us finish this ASAP and get to a safe place."
    # fight 
    
    menu:

        "How you want to fight?"

        "Fight with Fenrir":
            
            l "I need your help,Fenrir. We can end this soon."
        
            #$ gg_power+=10
            
            l "Attack the ice layer between us and him, cause cracks and run away."
            
            show fenrir happy at center
            f "No problem. Come out, my GG! I will let you see my power."
            
            l "Show me your power, GG!"
            
            "Ice layer is broken. A huge crack between Baldur and the group of Loki."
            
            b @ angry "You insidious cunning villain. I will catch you and You will regret for this!"
            
            l @ happy "Bye-bye!!"

            jump run

        "Fight with Garm":
            
            l "I need your help,Garm. We can end this soon."
        
            #$ gg_power+=10
            
            l "Attack the ice layer between us and him, cause cracks and run away."
            
            show garm surprised at center
            g "Oh me? OK! let us do this. GG! Help me!"
            
            l "Show me your power, GG!"
            
            "Ice layer is broken. A huge crack between Baldur and the group of Loki."
            
            b @ angry "You insidious cunning villain. I will catch you and You will regret for this!"
            
            l @ happy "Bye-bye!!"

            jump run

        "Fight by Loki himself":
            
            l "I can do it by myself."
            
            #$ gg_power-=10
            
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
            
            b @ angry "You insidious cunning villain. I will catch you and You will regret for this!"
            
            l @ happy "Bye-bye!!"
            
            show garm sad at center
            g "Stop talking shit. You almost got us killed!"
            
            l @ happy "Hahaha, it happens. A true gentleman will forgive me."
            
            jump run
            
        "Fight by Fenrir and Garm":
            
            l "No time to waste. Let us do it together."
            
            l "Attack the ice layer between us and him, cause cracks and run away."
            
            #$ gg_power+=20
            
            show fenrir neutral at center
            f "Wise choise!"
            
            hide fenrir neutral
            show garm neutral at center
            g "I agree with you!"
            hide garm neutral
            
            l "Show me your power, GG!"
            
            "Ice layer is broken. A huge crack between Baldur and the group of Loki."
            
            b @ angry "You insidious cunning villain. I will catch you and You will regret for this!"
            
            l @ happy "Bye-bye!!"
            
            jump run
    

label path:
    
    scene path
    with dissolve
    play music "boxcat.mp3"
    show loki neutral at center

    l "Let us go. The guards are coming. I can hear that."
    
    show loki neutral at right with move
    show fenrir neutral at left
    f @ happy "I am sure this path can buy us time."
    f "I noticed that you can not control GG very well, did you practise on that?"
    
    l "What do you mean about that?"
    
    f @ neutral "I mean your GG actually is a very poworful one. But you only show 50 persent of that!"
    
    l "I did try my best. How come...?"
    
    f "Let me teach you how to contorl GG. I didn't waste time in these years."
    f "The power of GG comes from yourself. And that depending on QUALITIES OF A GENTLEMAN."
    f @ happy "Remember to keep gentleman all the time."
    f "And you can exert its great power when you need to."
    f "Just keep practising from now on."
    
    l "OK. I see."
    
    hide loki neutral
    hide fenrir neutral
    "After a while"
    
    show garm happy at center
    g "Oh, we finally came out!"
    
    show fenrir happy at left
    f "Keep going. We are not safe yet."
    
    jump run
    
label encountered:
    
    play music "battle1.mp3"

    f "Holy, they catch up."
       
    "You lose! Loki and his friend got caught!"
       
    return

label run:
    
    scene glacier with dissolve
    
    show loki neutral at center 
    play music "battle1.mp3"
    l "Oh, no. The guards are there. We need to run now!"
    
    show loki neutral at left with move
    show baldur angry at right
    
    b "Stop running! I swear to the great LOL, I gonna kill you all!"
    l @ happy "No way!!"
    
    hide baldur angry
    show loki neutral at center with move
    
    l "They are annoying! Need to do something to get rid of them."
    
    show garm sad at left
    
    g "Oh, no! There is a guy there! We are surrounded!"
    l @ mad "We walked through him at the fastest speed and escaped here as soon as possible."
    
    hide garm sad
    l "Don't block us!!!!"
    
    show loki neutral at left with move
    show surt suprised at right
    
    s "Stop! I am not theirs. Get into the ice cave and I will help you."
    
    menu:

        "Should Loki believe this guy?"
        
        "Yes, he looks nice!":
            
            l "It looks we can believe this guy. There are lots of exits in the ice cave. We can try."
            #$ gg_power-=10
            
        "No, he is suspicious.":
        
            l "I can not believe you!"
            
            s "There is no other way. Just hide. I will due with them."
        
            l "Don't let me down. You can not survive if that happens."
            #$ gg_power+=10
            
            
        "Loki and his group get into the ice cave."
        
    hide loki neutral
    show surt neutral at left with move
    show baldur angry at right
    
    b "Surt. An exile! Tell me where are they if you see that 3 strangers."
    
    s "If you are talking about one boy and two girls, they are going that way."
    
    b "All right. Step back. You useless waste."
    
    hide baldur angry 
    
    "Baldur went to another side"
    
    play music "netherplace.mp3"
    
    show loki neutral at right
    
    l "Thanks man. You are a nice guy."
    
    s @ smite "It is not safe yet. Let me lead you to my place."
    
    jump icecave
    
label icecave:
    
    scene icecave with dissolve
    
    show loki neutral at left 
    show surt neutral at right
    
    s "Here is my place. You are safe now."
    
    l "Thanks again. Why you help us, my friend."
    
    s "My name is Surt. I help you because I hate LOLs."
    s "Me and my sister Samira used to be the servant of Baldur"
    s @ angry "One day I was gardening in the garden and Samira was serving a guest of Baldur." 
    s @ angry "But my sister made a mistake, she poured the tea on the guests."
    s @ angry "After Baldur knows it, he killed my sister. And burned me because I plead for her."
    s "Finally I was exiled here. The Icelandic wilderness."
    s "I have no power to avenge. But I will do whatever they are no willing to see."
    s "That is my story. A useless waste's story."
    
    l "Surt, my friend. Believe me. You are not a useless person."
    l @ mad "In these years, LOLs are very cruel to the people."
    l @ mad "There are so many people who are dissatisfied with them outside, we decided to rebel against them."
    l @ happy "Join us. The only way to save yourself is on yourself."
    
    s "Can I? Are you willing to accept me who has nothing?"
    s "But I have no power to contend with LOL, I will only drag you down."
    
    l @ happy "No problem. We can teach you how to manifest a GG."
    
    $counter = 0
    l "The power of GG comes from yourself. And that depending on QUALITIES OF A GENTLEMAN."
    l "Here is how to be a gentleman."
    
    menu:
        
        "A gentleman chooses to be positive. What you will do if your friend make a mistake?"
        
        "Ignore it.":
            s "The answer sounds rare."
        "Encourage your friend to learn something from this mistake.":
            $counter+=1
        "Laugh at him.":
            s "The answer sounds rare."
        
    menu:
        
        "A gentleman maintains a teachable posture and actively seeks new challenges. What you will do if you see something you never know?"
        
        "Escape from it.":
            s "The answer sounds rare."
        "Learn till you know it.":
            $counter+=1
        "Pretend not to see it.":
            s "The answer sounds rare."
    menu:
        
        "A gentleman is well-spoken and a focused listener. He demonstrates conversational competence and leaves others feeling inspired, engaged, and understood."
        "What you will do if someone want to talk to you?"
        
        "Escape from the guy.":
            s "The answer sounds rare."
        "Tell someone else to talk to him.":
            s "The answer sounds rare."
        "Listen carefully and show respect.":
            $counter+=1
    
    menu:
        
        "A gentleman does the right thing even when no one is watching."
        "What you will do if you walk on a street no one is there?"
        
        "Do whatever you want.":
            s "The answer sounds rare."
        "Just be yourself.":
            s "The answer sounds rare."
        "Only do the right thing even no one knows.":
            $counter+=1
            
            
    if counter == 4:
        #$ gg_power+=20
        s "I can feel GG. I think I can do it."
    else:
        #$ gg_power+=20
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
    
    l "Look at this no brain. Stupid and blame others."
    l "I am here. Kill me if you can!"
    
    show baldur angry at center with move
    show servent at left
    
    b "Go kill these escapers. I will kill Surt first!"
    l @ mad "Run! Surt!"
    
    hide servent
    hide loki happy
    
    show baldur angry at left with move
    show surt suprised at right
    
    b "Now it is only us! You gonna die today, Surt!"
    s @ angry "I will not run anymore! It is time to revenge! My GG! It is show time!"
    
    scene surtfight with dissolve
    
    s "This was given back to you for my sister!!"
    
    "Surt killed Baldur."
    
    # This ends the game.
    return
