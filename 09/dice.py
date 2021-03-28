from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

dice = Dice()
print(dice.sides)
for i in range(10):
    print(f"{i}: {dice.roll_die()}")
print("\n")

dice10 = Dice(10)
print(dice10.sides)
for i in range(10):
    print(f"{i}: {dice10.roll_die()}")
print("\n")

dice20 = Dice(20)
print(dice20.sides)
for i in range(10):
    print(f"{i}: {dice20.roll_die()}")
print("\n")
