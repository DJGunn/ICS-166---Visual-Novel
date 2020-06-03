# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character(_("Loki"), color="#2ae6ff", image="loki")
# define h = Character(_("Helpful Person"), color="#3033ff")
define f = Character(_("Fenrir"), color="#01116e", image="fenrir")
define ut = Character(_("???"), color="#f2f2f2")
define t = Character(_("Tyr"), color="f2f2f2")
define s = Character(_("Surt"), color="f2f2f2")

transform singlebounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    yoffset 0


# The game starts here.

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

    ut "Where do you think you are going?"
    "A voice suddenly appears. It seems someone has already catched up."

    show loki surprised
    l "Who's that..."
    "Loki have never met this man, but he can feel there is something unusual about him."
    hide loki

    show tyr neutral
    ut "I am Tyr, the blessed son of Hymir, Destined Hunter of Fenrir, the Immuned One."
    t "Fenrir, you will run no further."
    "Tyr spoke in a sharp tone, with a dedicated look in his eyes."
    hide tyr

    show surt neutral
    s "I'm sorry guys. I can't help you on this one, not with Tyr on the other side."
    s "I wish you the best of luck."
    "Surt runs away, as like being chased by a bear."
    hide surt

    show fenrir sad at left
    f "No no no no no no...Run Loki! You can't beat him! Run now!"
    f "I'll surrender only if you promise not to hurt Loki."
    "Fenrir is terrified."
    "She knows this man, and for some reason believes running away is the only way out of this."

    show loki surprised at right
    l "Don't be silly. I will never leave you behind."
    l "I have manifested my GG power. I'll fight to my last breath to protect you."
    "Loki looks into Fenrir's eyes."
    "After years of separation, how could he leave her here with this stranger?"
    "Even if he's strong, Loki believes in his GG power."
    f "No you don't get it! Tyr is..."

    hide loki
    hide fenrir

    show tyr neutral
    t "Enough talking. Surrender now or embrace your fate."
    "Tyr is obviously bored."
    hide tyr

    show loki mad
    l "You are the one who's talking too much!"

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













    # This ends the game.

return
