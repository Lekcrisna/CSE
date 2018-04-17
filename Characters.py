"""Must have
Take Damage
Status Effect (paralyze, poison, hunger, etc.)
Death
Attack
Move
Pick Up
"""


class Character(object):
    def __init__(self, name, description, inventory, attack):
        super(Character, self).__init__()
        self.name = name
        self.description = description
        self.inventory = inventory
        self.move = False
        self.pick_up = False
        self.attack = attack

    def name(self, name):
        print(name)

    def move(self):
        if Character.move:
            print('You do not move')
        else:
            self.move = True
            print('Character moves forward')

    def pick_up(self):
        if Character.pick_up:
            print('You do not pick %d up')
        else:
            self.pick_up = True
            print('You pick %d up')

    def damage(self):
        print('you get damage')

    def attack(self):
        if Character.attack:
            print("YOu attack")

            