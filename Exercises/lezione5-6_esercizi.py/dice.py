import random

class Dice:
    
    def __init__(self, sides: int = 6) -> None:
        
        self.sides: int = sides

    def roll_dice(self, sides)->int:

        return random.randrange(1, self.sides)
    

lancio: Dice = Dice()

print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print(lancio.roll_dice(lancio.sides))
print('\n')
lancio1: Dice = Dice(sides = 10)

print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print(lancio1.roll_dice(lancio1.sides))
print('\n')
lancio2: Dice = Dice(sides = 20)

print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))
print(lancio2.roll_dice(lancio2.sides))