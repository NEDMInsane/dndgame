from diceroller import roll_dice
import npc


def run_dungeon(dungeon, player_character):
    won = False
    run = False
    enemy_list = []
    level = dungeon[2]
    rooms = dungeon[0]
    enemies = dungeon[1]
    current_room = 0
    rooms_left = rooms
    boss = npc.Goblin(level, 200, 'Boss', 'Male', 'Goblin_Boss')
    print(f'{player_character.name} is going to battle in a level {level} dungeon. It has {rooms} rooms, and {enemies} enemies.')
    while player_character.hitpoints > 0 and won is False and run is False:
        # enemies should be populated in the first n rooms, while the last room holds the boss.
        while len(enemy_list) != enemies - 1:
            enemy_list.append(npc.Goblin(level - 1, 100, 'Scout', 'Male', 'Grunt'))
            print(enemy_list)
        player_selection = ''
        if current_room == 0:
            player_selection = input(f'''Your parties current level is: {player_character.level}
                                        Will you run? Or will you FIGHT?\t''')
            if player_selection.lower() == 'fight':
                current_room = 1
                rooms_left -= 1
            elif player_selection.lower() == 'run':
                run = True
            else:
                print(f'Cannot determine input: {player_selection} ... running.')
                run = True
        elif current_room < rooms:
            # TODO: fight through the current room and iterate.
            pass

