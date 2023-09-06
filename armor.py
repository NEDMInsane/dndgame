
class Armor:
    def __init__(self):
        self.armor_name = ''
        self.armor_type = ''
        self.equip_type = ''

        self.armor_value = ''
        self.armor_price = ''
        self.armor_condition = ''

        self.enchantment = ''
        self.enchantment_vaule = ''
        self.enchantment_sepcial = []

        self.weight = ''
        self.stealth = False
        self.small = False
        self.str_reqirement = 0

class Cloth_Armor(Armor):
    def __init__(self, name = ''):
        super().__init__()
        self.armor_name = name
        self.armor_type = 'Cloth'

        self.armor_value = '5'
        self.armor_price = (0.5, 'GP')
        self.weight = '1'
        self.stealth = True

class Padded_Armor(Armor):
    def __init__(self, name = ''):
        super().__init__()
        self.armor_name = name
        self.armor_type = 'Light'

        self.armor_value = '11'
        self.armor_price = (5, 'GP')
        self.weight = 8

class Leather_Armor(Armor):
    def __init__(self, name = ''):
        super().__init__()
        self.armor_name = name
        self.armor_type = 'Light'

        self.armor_value = '11'
        self.armor_price = (10, 'GP')
        self.weight = 10
        self.stealth = True

class Studded_Leather_Armor(Armor):
    def __init__(self, name = ''):
        super().__init__()
        self.armor_name = name
        self.armor_type = 'Light'

        self.armor_value = '12'
        self.armor_price = (45, 'GP')
        self.weight = 13
        self.stealth = True

class Hide_Armor(Armor):
    def __init__(self, name = ''):
        super().__init__()
        self.armor_name = name
        self.armor_type = 'Medium'

        self.armor_value = '12'
        self.armor_price = (10, 'GP')
        self.weight = 12
        self.stealth = True

class Scale_Armor(Armor):
    def __init__(self, name = ''):
        super().__init__()
        self.armor_name = name
        self.armor_type = 'Medium'

        self.armor_value = '14'
        self.armor_price = (50, 'GP')
        self.weight = 45

class Half_Plate_Armor(Armor):
    def __init__(self, name = ''):
        super().__init__()
        self.armor_name = name
        self.armor_type = 'Medium'

        self.armor_value = '15'
        self.armor_price = (750, 'GP')
        self.weight = 40