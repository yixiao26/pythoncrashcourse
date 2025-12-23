from random import randint


class Die:
    """Generates a die with a given number of sides"""

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die = Die(6)
print("Rolling a 6-sided die 10 times:")
for i in range(10):
    number = die.roll_die()
    print(number)


die = Die(10)
print("Rolling a 10-sided die 10 times:")
for i in range(10):
    number = die.roll_die()
    print(number)


die = Die(20)
print("Rolling a 20-sided die 10 times:")
for i in range(10):
    number = die.roll_die()
    print(number)
