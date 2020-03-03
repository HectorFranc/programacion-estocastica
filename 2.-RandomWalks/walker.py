import random


class Walker:
    def __init__(self):
        pass

    def walk(self):
        return (0, 1)


class NormalWalker(Walker):
    def __init__(self):
        super().__init__()

    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
