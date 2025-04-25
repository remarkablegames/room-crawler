label combat:

    stop music fadeout 1
    queue music battle

    show screen player_stats

    $ enemies.show()
    $ player.energy = player.energy_max

    jump player_turn
