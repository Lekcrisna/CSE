world_map = {
    'MANSION': {
        'NAME': 'PORCH OF MANSION',
        'DESCRIPTION': 'There is a door in front of you everywhere else is just darkness',
        'PATHS': {
            'SOUTH': 'CENTER AREA'
        }
    },
    'CENTER AREA': {
        'NAME': 'LIVING ROOM',
        'DESCRIPTION': 'You are in a center area you can go east and west, the door south is locked',
        'PATHS': {
            'WEST': 'FOREST/SIDE YARD',
            'EAST': 'DEAD END',
            'SOUTHWEST': 'KITCHEN'
        }
    },
    'FOREST': {
        'NAME': 'SIDE YARD',
        'DESCRIPTION': 'Everywhere you look is only trees but to the left of you can see some sort of shiny '
                       'object hanging of the tree',
        'PATHS': {
            'EAST': 'CENTER AREA'
        }
    },
    'RANDOM ROOM': {
        'NAME': 'BEDROOM',
        'DESCRIPTION': 'It has a bed and hanging next to the bed is a rusty knife',
        'PATHS': {
            'WEST': 'CENTER AREA'
        }
    },
    'KITCHEN': {
        'NAME': 'KITCHEN',
        'DESCRIPTION': 'Its like any other kitchen you find a loaf of bread',
        'PATHS': {
            'SOUTH': 'SMALL LIVING ROOM'
        }
    },
    'SMALLER LIVING ROOM': {
        'NAME': 'SMALL LIVING ROOM',
        'DESCRIPTION': 'Its a small living room it has a tv',
        'PATHS': {
            'NORTH': 'KITCHEN',
            'EAST': 'MASTER BED ROOM'
        }
    },
    'BED ROOM': {
        'NAME': 'MASTER BED ROOM',
        'DESCRIPTION': 'Its a big area it will take a while to search everything',
        'PATHS': {
            'NORTH': 'CENTER AREA',
            'EAST': 'ANOTHER ROOM'
        }

    },
    'ROOM': {
        'NAME': 'INTERSECT ROOM',
        'DESCRIPTION': 'This room isnt important its just an intersection for rooms',
        'PATHS': {
            'NORTHWEST': 'RESTROOM',
            'SOUTH': 'GATED ROOM',
            'UP': 'ATTIC',
            'EAST': 'BALCONY'
        }
    },
    'NORTHWEST': {
        'NAME': 'RESTROOM',
        'DESCRIPTION': 'Its a normal restroom with a shower, toilet, and sink. You find some item',
        'PATHS': {
            'SOUTHEAST': 'INTERSECT ROOM'
        }
    },
    'UP': {
        'NAME': 'ATTIC',
        'DESCRIPTION': 'you are in the attic its dark but you turn on the light you find a bunch of boxes and one box'
                       'catches your eye you look inside and its just a number on a piece of paper, it says 4201',
        'PATHS': {
            'DOWN': 'INTERSECT ROOM'
        }
    },

}
current_node = world_map['MANSION']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You cannot go this way')
    else:
        print("Command not recognised")
