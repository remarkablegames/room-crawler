# Should the user be allowed to rollback the game? If set to False, the user cannot interactively rollback.
define config.rollback_enabled = False

label start:

    $ room = True

    scene bg room 0 with fade

    "Where am I?"
    "I was just dozing off in class."
    "I should get out of here."

    jump explore
