# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc")
define m = Character(_("Main Character"), color="#2ae6ff")
define s = Character(_("Side Character"), color="#fffc30")
define b = Character(_("Bad Guy"), color="#ff3033")
define h = Character(_("Helpful Person"), color="#3033ff")

# define colors for use
init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))


# The game starts here.

label start:

    scene black with dissolve

    show text "Chapter 1\nWait, I'm Rich?!" with Pause(5)

    scene black with dissolve

    show lokidefault   # this should be lokidefault when character is made

    m "Ah yes, happy birthday to me, woo..."

    "Loki is an orphan that has been poor their entire life. Their parents were killed for not paying the protection fee and soon the same would happen to them."

    m "Now that I'm officially an adult I'm going to have to fight in GG duels to make a living."

    #scene black with dissolve
    scene greenaurora with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show lokidefault
    show sidecharadefault at right

    # These display lines of dialogue.

    s "KNOCK KNOCK!"

    m "Ugh, who's there?"

    s "IT'S ME!"

    m "What kind of joke is that?!"

    "***Side character opens the door and enters Loki's room.***"

    show lokidefault at left
    with move

    s "How are you doing on this fine day?!"

    menu:

        "Now, am I feeling positive or negative today..."

        "Positive":

            jump positive

        "Negative":

            jump negative

label positive:

    scene greenaurora
    with dissolve

    show lokidefault

    m "I can't wait to see what today has in store for me!"

    "A fool's thinking, but this would be the kind of thinking that would change the world."

    "{b}Good Ending{/b}."
    # This ends the game.
    return

label negative:

    scene black
    with dissolve

    show lokidefault

    m "I don't feel so good."

    "{b}Bad Ending{/b}."
    # This ends the game.
    return
