class Bedroom(object):
    def __init__(self, name):
        self.name = name


class Room(property):
    def __init__(self, name):
        self.name = name


class Character(property):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Item(object):
    def __init__(self, weapon, consumable, durability):
        super(Item, weapon, consumable)
        self.weapon = weapon
        self.consumable = consumable
        self.durability = durability


class Weapons(object):
    def __init__(self, weapon, knife, gun, ar15, scythe):
        super(Item, self, weapon, knife, gun, ar15, scythe)
        self.self = self
        self.weapon = weapon
        self.knife = knife


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
        self.potion = potion


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


class Handgun(object):
    def __init__(self, description, name):
        super(Item, self, description, name)
        self.name = name
        self.description = description


class Key(object):
    def __init__(self, description):
        super(Item, self, description)


class ChestKey(object):
    def __init__(self, description):
        super(Item, description)


class Armor(object):
    def __init__(self):
        super(Armor, self).__init__()


class HealthPotion(object):
    def __init__(self, name):
        super(HealthPotion, self, name).__init__()


class Apple(object):
    def __init__(self, description):
        super(Item, self, description)


class WoodenSword(object):
    def __init__(self):
        super(self).__init__()


class Character(property):
    def __init__(self, name, description, inventory, attack):
        super(Item, name, description, inventory, attack)
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
        super(Character, self).damage()

    def attack(self):
        if Character.attack:
            print("You Attack")


class Room(property):
    def __init__(self, name, north, east, south, west, description):
        super(Room, self).__init__(name, north, south, east)
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description


def move(self, direction):
    global current_node
    current_node = globals()[getattr(self, direction)]


self = Room('CENTER AREA', 'PORCH', 'DEAD END', 'nothing', 'FOREST/SIDE YARD', 'A room where you can sleep do anything'
                                                                               'in a room and you also find some '
                                                                               'shiny object like a key to some door.')

bedroom = Room('SIDE YARD', 'TREES', 'CENTER AREA', 'TREES', 'TREES', 'You only see trees and you cant go anywhere else'
                                                                      'so you just go back to where you came from')

Kitchen = Room('KITCHEN', 'WALL', 'WALL', 'WALL', 'SMALL LIVING ROOM', 'A kitchen where you can find some food like'
                                                                       'bread  you eat it and it taste good.')

Restroom = Room('Restroom', 'A wall', ' side room', 'room', 'wall', 'A restroom where you find a sort of item'
                                                                    'and you can use the restroom')

bedroom = Room('Bedroom', 'Room', 'some stairs', 'room', 'wall', ' A bedroom where you can sleep')

room = Room('Master Bedroom', 'door', 'wall', 'wall', 'This is the master bedroom it takes a while to open the door but'
                                                      'you eventually get it to open you so a bunch of things like ')


current_node = Room
directions = ['north', 'east', 'south', 'west']
short_direction = ['n', 'e', 's', 'w']

while True:
            print(current_node[Room])
            print(current_node[directions])
            command = input('>_').lower().strip
            if command == 'quit':
                quit(0)
            elif command in short_direction:
                pos = short_direction.index(command)
                command = directions(pos)
            if command in directions:
                try:
                    name_of_node = current_node['PATHS'][command]
                    current_node = Room[name_of_node]
                except KeyError:
                    print('You cannot go this way')
            else:
                print("Command not recognised")
                if command[:7] == "pick up":
                    item: command[8:]
                print('this doesnt even work')