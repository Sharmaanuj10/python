from random import randint
class Dice:


    def roll_dice(self):

        self.roll = randint(1,6)
        return self.roll


dice = Dice()
print(dice.roll_dice())