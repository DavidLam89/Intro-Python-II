from room import Room
from player import Player
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

# Make a new player object that is currently in the 'outside' room.

myplayer = Player('David', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
print(f"Player {myplayer.name} is in {myplayer.room.name}")
print("Please enter 'q' to quit, 'n','s','e','w' to move")
userinput = ''
while userinput != 'q':
    userinput = input("What do you want to do: ")
    try:
        if userinput == 'n':
            myplayer.room = myplayer.room.n_to
        elif userinput == 's':
            myplayer.room = myplayer.room.s_to
        elif userinput == 'e':
            myplayer.room = myplayer.room.e_to
        elif userinput == 'w':
            myplayer.room = myplayer.room.w_to
    except AttributeError:
        print("Player can't move in this direction")
    print(f"Player {myplayer.name} is in {myplayer.room.name}")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
