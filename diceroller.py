from random import randint as randint

def roll_dice(dice_count=1, die_number=6):
    i = 1
    roll = 0
    while i <= dice_count:
        roll = roll + randint(1, die_number)
        i += 1
    return roll

#TODO: Add special die types