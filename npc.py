from diceroller import roll_dice


class NPC:
    # TODO: Create the bas class for an NPC
    def __init__(self):
        self.level = 1
        self.race = 'None'
        self.hit_points = 100
        self.alignment = (0, 0)
        self.job = 'None'
        self.sex = 'None'
        self.monster_class = 'None'

        self.inventory = {
            'Gold'  :   10
        }

        self.equipment = {
            "Head"      : [],
            "Chest"     : [],
            "Main Hand" : [],
            "Offhand"   : [],
            "Legs"      : [],
            "Feet"      : [],
            "Rings"     : [],
            "Cape"      : []
        }


class Goblin(NPC):
    def __init__(self, level, hit_points, job, sex, monster_class):
        self.level = level
        self.race = 'Goblin'
        self.hit_points = hit_points
        self.alignment = (-1, 0)
        self.job = job
        self.sex = sex
        self.monster_class = monster_class
