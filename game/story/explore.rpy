default room = False
default explore_room = -1

label explore:

    queue music eerie

    menu:
        "What do you want to do?"

        "Explore the hall" if not room:
            jump hall

        "Enter a room" if not room:
            $ room = True

            jump room

        "Explore the room" if room and not explore_room == wins:
            jump explore_room

        "Leave the room" if room:
            $ room = False

            jump hall

        "Check the shop" if wins > 0:
            jump shop

label hall:

    python:
        renpy.scene()
        renpy.show(f"bg hall {wins % 10}")
        renpy.with_statement(fade)

        narrator(renpy.random.choice([
            "The atmosphere feels heavy...",
            "The air feels chilly...",
            "It feels ominous...",
            "There’s an eerie presence...",
            "It’s a little quiet here...",
            "Something doesn’t feel right...",
        ]))

    "Something is approaching!"

    jump combat

label room:

    python:
        renpy.scene()
        renpy.show(f"bg room {wins % 10}")
        renpy.with_statement(fade)

        narrator(renpy.random.choice([
            "This room is unsettling...",
            "Where is everybody?",
            "It’s quiet in this room...",
        ]))

    jump explore

label explore_room:

    $ explore_room = wins

    if not wins or renpy.random.random() < 0.4:
        "There’s nothing in this room."

    else:
        "You see something shiny in the corner."

        $ random = renpy.random.random()

        menu:
            "Should you approach the shiny object?"

            "Approach it":
                "You move towards the shiny object..."

                if random < 0.1:
                    "It’s a trap!"

                    jump combat

                elif random < 0.2:
                    "It’s a trap!"

                    $ health -= health // 2

                    "You lose half your health."

                    jump explore

                elif random < 0.3:
                    "You found a reward!"

                    $ rewards += 1

                    jump reward

                elif random < 0.8:
                    $ loot = renpy.random.randint(round(wins / 2) + 1, wins + 1)
                    $ money += loot

                    "You found $[loot]!"

                else:
                    "It turned out to be nothing."

                    pass

            "Ignore it":
                "You decided to avoid the shiny object."

                pass

    jump explore
