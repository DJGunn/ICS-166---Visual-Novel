﻿# The script of the game goes in this file.

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

    show caffeine

    #scene your_scene_title

    m "Ah yes, happy birthday to me, woo..."

    "Loki is an orphan that has been poor their entire life. Their parents were killed for not paying the protection fee and soon the same would happen to them."

    m "Now that I'm officially an adult I'm going to have to fight in GG duels to make a living."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black with dissolve
    scene greenaurora

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
