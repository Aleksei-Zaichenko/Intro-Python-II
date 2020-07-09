from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items= {
    'sword': Item('sword', 'very sharp and metally'),
    'bag of food': Item('bag of food', 'very tasty and fulfilling'),
    'coins': Item('coins', 'goldie stuff that we all love')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
print(room['outside'])

# Make a new player object that is currently in the 'outside' room.

player = Player('Alex', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

userInput = None

while(userInput != 'q'):
    player.displayCurrentLocation()
    player.current_room.displayRoomsItems()
    player.current_room.displayDescription()
    
    correct = False
    directionsDictionary = {'n_to':player.current_room.n_to,'s_to':player.current_room.s_to, 'e_to':player.current_room.e_to, 'w_to':player.current_room.w_to,}

    while not correct:
        userInput = input(
        "Enter which direction you want to go ( n, s, e, w), 'i' or 'inventory' to see your item and 'q' to quit: ")

        if len(userInput.split(' ')) == 1:
            roomDirection = userInput + '_to'
            if userInput == 'i' or userInput == 'inventory':
                player.displayPlayerItems()
            elif userInput != 'q' and directionsDictionary[roomDirection] != None:
                player.movePlayerToRoom(directionsDictionary[roomDirection])
                correct = True
            elif userInput != 'q' and directionsDictionary[roomDirection] == None:
                print('No road that direction')
            else:
                correct = True
        elif len(userInput.split(' ')) == 2:
            if userInput == 'get' or userInput =='take':
                pass
            elif userInput == 'drop':
                pass