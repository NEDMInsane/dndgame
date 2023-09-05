from diceroller import roll_dice

class Character:
    """
    Represents a character in the fame with a name, size, hitpoints, attributes
    """
    def __init__(self, name):
        """
        Initialize a character with their attributes.

        Args:
            name (str): The character's name.
            strength (int): Strength attribute.
            dexterity (int): Dexterity attribute.
            constitution (int): Constitution attribute.
            intelligence (int): Intelligence attribute.
            wisdom (int): Wisdom attribute.
            charisma (int): Charisma attribute.
        """
        self.name = name
        self.size = 'Medium'
        self.hitpoints = '1' #This will be modified later
        self.level = 1
        self.sex = ''
        self.alignment = (0, 0) #Tuple to define where your alignment is.
        self.race = 'None'
        
        self.attributes = {
            "Str": 0,
            "Dex": 0,
            "Con": 0,
            "Int": 0,
            "Wis": 0,
            "Cha": 0
        }

        self.class_attributes = {
            "die_type"          : '',
            "armor_type"        : '',
            "weapon_type"       : '',
            "primary_ability"   : '',
            "saving_throw"      : '',
            "character_class"   : '' 
        }

        self.character_skills = {
            "Dex Skills"    : {'Acrobatics' : 0, 'Sleight of Hand' : 0, 'Stealth' : 0},
            "Wis Skills"    : {'Animal Handling' : 0, 'Insight' : 0, 'Medicine' : 0, 'Survival' : 0},
            "Int Skills"    : {'Arcana' : 0, 'History' : 0, 'Investigation' : 0, 'Nature' : 0, 'Religion' : 0},
            "Str Skills"    : {'Athletics' : 0},
            "Cha Skills"    : {'Deception' : 0, 'Intimidation' : 0, 'Performance' : 0, 'Persuasion' : 0}
        }

        self.inventory = {}
        self.equip={
            "Head"      : [],
            "Chest"     : [],
            "Main Hand" : [],
            "Off Hand"  : [],
            "Legs"      : [],
            "Feet"      : [],
            "Rings"     : [],
            "Cape"      : []
        }
        self.spellbook = {}

        self.languages = ['Common']

    def increment_attribute(self, attribute, increment_amount):
        """
        Increment the value of an attribute.

        Args:
            attribute (str): The attribute to increment.
            increment_amount (int): The amount to increment the attribute by.
        """
        self.attributes[attribute] = self.attributes[attribute] + increment_amount

    def set_attribute(self, attribute, number):
        self.attributes[attribute] = number
    
    def get_attribute(self, attribute):
        """
        Get the value of a character's attribute.

        Args:
            attribute (str): The attribute to retrieve.

        Returns:
            int: The value of the specified attribute.
        """
        return self.attributes[attribute]

    def set_all_class_attributes(self, die_type, armor_type, weapon_type, primary_ability, saving_throw, character_class):
        """
        Set the class-specific attributes of the character.

        Args:
            die_type (str): The type of die for hit points (e.g., 'd8').
            armor_type (list): List of armor types character can use.
            weapon_type (list): List of weapon types character can use.
            primary_ability (str): The character's primary ability for attacks.
            saving_throw (list): List of saving throw abilities.
            character_class (str): The character's class.
        """
        self.class_attributes["die_type"] = die_type
        self.class_attributes["armor_type"] = armor_type
        self.class_attributes["weapon_type"] = weapon_type
        self.class_attributes["primary_ability"] = primary_ability
        self.class_attributes["saving_throw"] = saving_throw
        self.class_attributes["character_class"] = character_class

    def set_hitpoints(self, hitpoints):
        self.hitpoints = hitpoints

    def get_hitpoints(self):
        return self.hitpoints

    def set_equip(self, slot, equip_list):
        self.equip[slot] = equip_list

    def get_equip(self, slot):
        return self.equip[slot]

    def set_skills(self, skill_type, skill, point_value):
        self.character_skills[skill_type[skill]] = point_value

    def get_skill(self, skill_type, skill):
        return self.character_skills[skill_type[skill]]

    def set_sex(self, sex):
        self.sex = sex

    def get_sex(self):
        return self.sex

    def __repr__(self):
        return f'({self}, {self.name} Obj)'
    
    def __str__(self):
        return f'{self.name}, the {self.race} {self.class_attributes["character_class"]}.'

class Human(Character):
    """
    Represents a Human character with racial traits and bonuses.
    """
    def __init__(self, name):
        super().__init__(name)
        self.increment_attribute('Str', 1) #Racial Trait Bonus
        self.increment_attribute('Dex', 1) #Racial Trait Bonus
        self.increment_attribute('Con', 1) #Racial Trait Bonus
        self.race = 'Human'

class Elf(Character):
    """
    Represents an Elf character with racial traits and bonuses.
    """
    def __init__(self, name):
        super().__init__(name)
        self.increment_attribute('Dex', 2) #Racial Trait Bonus
        self.increment_attribute('Wis', 1) #Racial Trait Bonus
        self.race = 'Elf'

class Dwarf(Character):
    """
    Represents a Dwarf character with racial traits and bonuses.
    """
    def __init__(self, name):
        super().__init__(name)
        self.increment_attribute('Con', 1) #Racial Trait Bonus
        self.increment_attribute('Str', 2) #Racial Trait Bonus
        self.race = 'Dwarf'

class Halfling(Character):
    """
    Represents a Halfling character with racial traits and bonuses.
    """
    def __init__(self, name):
        super().__init__(name)
        self.increment_attribute('Dex', 2) #Racial Trait Bonus
        self.increment_attribute('Cha', 1) #Racial Trait Bonus
        self.size = 'Small' #Racial Trait Bonus
        self.race = 'Halfling'

class Character_Class:
    def __init__(self, name = 'None'):
        self.name = name
    
    def apply_class_attributes(self, character):
        character.set_all_class_attributes('None', 'None', 'None', 'None', 'None', 'None')

class Cleric(Character_Class):
    def __init__(self):
        super().__init__('Cleric')
        self.description = """Cleric: A priestly Champion who wields divine magic in service of a higher power."""
    
    def apply_class_attributes(self, character):
        character.set_all_class_attributes('d8', 
                                        ['Medium', 'Light', 'None'], 
                                        ['Shield', 'Simple'], 
                                        'Wis', 
                                        ['Wis', 'Cha'], 
                                        'Cleric')

class Fighter(Character_Class):
    def __init__(self):
        super().__init__('Fighter')
        self.description = """Fighter: A master of martial combat, skilled with a variet of weapon and armor."""
    
    def apply_class_attributes(self, character):
        character.set_all_class_attributes('d10', 
                                        ['Heavy', 'Medium', 'Light', 'None'], 
                                        ['Shield', 'Simple', 'Melee'], 
                                        'Str', 
                                        ['Str', 'Con'], 
                                        'Fighter')

class Rogue(Character_Class):
    def __init__(self):
        super().__init__('Rogue')
        self.description = """Rogue: A scoundrel who uses stealth and trickery to overcome obstacles and enemies."""
    
    def apply_class_attributes(self, character):
        character.set_all_class_attributes('d8', 
                                        ['Light', 'None'], 
                                        ['Crossbow','Sword', 'Simple', 'Melee'], 
                                        'Dex', 
                                        ['Dex', 'Int'], 
                                        'Rogue')

class Wizard(Character_Class):
    def __init__(self):
        super().__init__('Wizard')
        self.description = """Wizard: A scholarly magic-user capable of manipulating the structures of reality."""
    
    def apply_class_attributes(self, character):
        character.set_all_class_attributes('d8', 
                                        ['None'], 
                                        ['Staff','Simple', 'Thrown', 'Melee'], 
                                        'Int', 
                                        ['Int', 'Wis'], 
                                        'Wizard')

def create_character(character_name, character_race, character_class):
    match character_race:
        case 'Human':
            new_player = Human(character_name)
        case 'Elf':
            new_player = Elf(character_name)
        case 'Dwarf':
            new_player = Dwarf(character_name)
        case 'Halfling':
            new_player = Halfling(character_name)
        case _:
            print(f'ERR: Race({character_race}) does not exist.')
            new_player = Character(character_name)
        
    match character_class:
        case 'Cleric':
            Cleric().apply_class_attributes(new_player)
        case 'Fighter':
            Fighter().apply_class_attributes(new_player)
        case 'Rogue':
            Rogue().apply_class_attributes(new_player)
        case 'Wizard':
            Wizard().apply_class_attributes(new_player)
        case _:
            print(f'ERR: Class({character_class}) does not exist.')
            Character_Class().apply_class_attributes(new_player)
    return new_player
        
def build_character(character):
    for atrribute in character.attributes:
        character.attributes[atrribute] += roll_dice(1, 6)
    print(character.attributes)
        
if __name__ == "__main__":
    jimmy = create_character('Jimmy', 'human', 'cleric')
    build_character(jimmy)
    print(jimmy)