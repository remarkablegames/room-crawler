label escape:

    scene bg lose with fade

    stop music fadeout 1
    queue music eerie

    "You can see the exit in the distance."

    menu:
        "What would you like to do?"

        "Escape":
            jump escaped

        "Remain":
            "You decided to stay."

            jump explore

label escaped:

    scene bg win with fade

    stop music fadeout 1
    queue music win2

    "You managed to escape!"

    jump end
