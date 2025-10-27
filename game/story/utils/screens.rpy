screen stat(name, current, max):
    text "[name]: [current]/[max]"
    bar value AnimatedValue(current, max):
        xsize 300


screen player_stats():
    zorder 1
    frame:
        yalign 1.0
        vbox:
            use stat("Health", player.health, player.health_max)
            null height 15
            use stat("Energy", player.energy, player.energy_max)
            null height 15
            text "Money: $[money]"


screen tooltip():
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                text "[tooltip!i]"
                xalign 0.5


screen enemy_stats(enemy, xalign_pos):
    frame:
        xalign xalign_pos
        vbox:
            use stat("Health", enemy.health, enemy.health_max)


screen enemy_stats0(enemy, xalign_pos):
    use enemy_stats(enemy, xalign_pos)


screen enemy_stats1(enemy, xalign_pos):
    use enemy_stats(enemy, xalign_pos)


screen enemy_stats2(enemy, xalign_pos):
    use enemy_stats(enemy, xalign_pos)
