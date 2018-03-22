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

<<<<<<< HEAD
class Gun(object):
=======
class AR15(object):
>>>>>>> fb1628cb2b3b926c3d8db91cca39808ae61174a4
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
<<<<<<< HEAD
        super(Armor, self).__init__()

class Sword(object):
    def __init__(self, description):
        super(Item, description)

class Axe(object):
    def __init__(self, material, description):
        self.material
        self.description

class Health_Potion(object):
    def __init__(self, description):
        super(Item, description)

class Ramen(object):
    def __init__(self):
        super(Ramen, self).__init__()

class
=======
        super(Armor, self).__init__()
>>>>>>> fb1628cb2b3b926c3d8db91cca39808ae61174a4
