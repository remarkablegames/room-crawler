# Should the user be allowed to rollback the game? If set to False, the user cannot interactively rollback.
define config.rollback_enabled = False


# Enemy names that are mapped to their respective images. E.g., name "Skeleton Soldier" becomes image "skeleton_soldier".
default ENEMIES = ["Goblin", "Minotaur", "Skeleton Knight", "Skeleton Soldier"]


init python:
    # Add tooltip tag
    def tooltip_custom_text_tag(tag, argument):
        return [(renpy.TEXT_TAG, "tooltip")]

    config.custom_text_tags["tooltip"] = tooltip_custom_text_tag


# To customize levels, see `game/story/data/levels.json`.
