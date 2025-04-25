init python:
    import json

    class Levels:
        def __init__(self) -> None:
            self.levels = json.load(renpy.file("story/data/levels.json"))

        def get(self, level: int) -> dict:
            """
            Get level data.
            """
            try:
                return self.levels[str(level)]

            except KeyError:
                level = { "enemies": [] }
                enemies = ["Goblin", "Minotaur", "Skeleton Knight", "Skeleton Soldier"]
                random = renpy.random.random()

                if random < 0.3:
                    enemies_count = 3
                elif random < 0.6:
                    enemies_count = 2
                else:
                    enemies_count = 1

                while enemies_count > 0:
                    enemy_name = renpy.random.choice(enemies)
                    enemies.remove(enemy_name)
                    attack_min = round(wins * (1 + renpy.random.random())) + 1
                    heal_min = round(wins * (1 + renpy.random.random())) + 1

                    level["enemies"].append({
                        "name": enemy_name,
                        "health": round(5 * (wins + 1) * (1 + renpy.random.random())),
                        "attack_min": attack_min,
                        "attack_max": attack_min + wins + 1,
                        "heal_min": heal_min,
                        "heal_max": heal_min + wins + 1,
                    })

                    enemies_count -= 1

                return level

default levels = Levels()
