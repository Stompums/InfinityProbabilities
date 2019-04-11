import random as rand


class Dice:

    def __init__(self):
        self.rolls = []

    def roll_dice(self, num=1, type=20):
        for i in range(num):
            roll = rand.randint(1, type)
            self.rolls.append(roll)

    def load_dice(self, *args):
        self.rolls = list(args)

    def reset(self):
        self.rolls.clear()

