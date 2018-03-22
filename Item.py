class Item(object):
    def __init__(self, weapon, consumable):
        self.weapon = weapon
        self.consumable = consumable

class Weapons(object):
    def __init__(self, weapon, knife, gun, ar15, scythe):
        super(Item, self, weapon, knife, gun, ar15, scythe)

class Consumables(object):
    def __init__(self, bread, water):
        super(Weapons, self, bread, water)
        self.bread = bread
        self.water = water

class Defense(object):
    def __init__(self, shield, armor, potion):
        super(Item, self, shield, armor, potion)
        self.shield = shield
        self.armor = armor
        self.potion

class Knife(object):
    def __init__(self, description, damage):
        super(Item, self, description, damage)
        self.description = description

    def pick_up(self):
        if Knife.pick_up:
            print('You do not pick knife up')
        else:
            self.pick_up = True
            print('You do not pick up the knife')

class AR15(object):
    def __init__(self, description):
        super(Item, self, description)

class Key(object):
    def __init__(self, description):
        super(Item, self, description)

class Chest_Key(object):
    def __init__(self, description):
        super(Item, description)

class Armor(object):
    def __init__(self):
        super(Armor, self).__init__()