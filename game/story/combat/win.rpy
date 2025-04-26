init python:
    from math import ceil

default money = 0
default loot = 0
default interest = 0
default rewards = 0
default wins = 0

label win:

    stop music fadeout 1
    queue music win1 volume 0.7

    "You survived the encounter!"

    $ player.reset()
    $ wins += 1
    $ interest = ceil(money * 0.4)
    $ loot = renpy.random.randint(wins, round(wins * 1.5) + 1)
    $ money += loot + interest

    "You earned $[loot] + $[interest] (interest)."

    if wins == 10:
        jump escape

    elif wins % 3 == 1:
        stop music fadeout 1

        $ rewards += 1

        jump reward

    else:
        stop music fadeout 1

        jump explore
