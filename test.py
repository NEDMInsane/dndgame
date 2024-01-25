import character
import gamemaster
import battle


if __name__ == '__main__':
    player1 = character.create_character('Paul', 'Human', 'Cleric')
    character.build_character(player1)
    gm = gamemaster.EasyGM(1)
    battle.run_dungeon(gm.create_dungeon(), player1)

