from diceroller import roll_dice


class GameMaster:
    # TODO: Create new game master class. Class created for more functionality
    def __init__(self, level, location):
        self.level = level
        self.current_dungeon = 'None'
        self.location = location

    def create_dungeon(self):
        rooms = self.level * 2
        monsters = self.level * 3
        boss_level = self.level * 2
        self.current_dungeon = [rooms, monsters, boss_level]
        print(self.current_dungeon)
        return self.current_dungeon

    def clear_dungeon(self):
        self.current_dungeon = 'None'


class EasyGM(GameMaster):
    def __init__(self, level):
        self.level = level


class HardGM(GameMaster):
    def __init__(self, level):
        self.level = level + 3

