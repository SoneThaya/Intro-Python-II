from room import Room
from player import Player

print("""
*************************************      
*      WELCOME TO THE BEST GAME     *
*************************************
      """)

player_name = input('Enter your name: ')

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
player = Player(player_name, current_room=room['outside'])
   


print(player)
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
while True:
    direction = input('You are outside, which direction do you want to go? ')
    
    if direction == 'q':
        break
    elif direction == 'n':
        player.current_room = room['outside'].n_to
        print(player)
    else:
        print("Cant go that way!!!")
        
        
    foyer_stop = input('Which direction do you want to go? ')
    
    if foyer_stop == 'q':
        break
    elif foyer_stop == 'n':
        player.current_room = room['foyer'].n_to
        print(player)
    elif foyer_stop == 's':
        player.current_room = room['foyer'].s_to
        print(player)
    elif foyer_stop == 'e':
        player.current_room = room['foyer'].e_to
        print(player)
    else:
        print("Cant go that way!!!")
        
    overlook_stop = input('Which direction do you want to go? ')
    
    if overlook_stop == 'q':
        break
    elif overlook_stop == 's':
        player.current_room = room['foyer']
        print(player)
    else:
        print("Cant go that way!!!")
        
    foyer_stop2 = input('Which direction do you want to go? ')
    
    if foyer_stop2 == 'q':
        break
    elif foyer_stop2 == 'n':
        player.current_room = room['overlook']
        print(player)
    elif foyer_stop2 == 's':
        player.current_room = room['outside']
        print(player)
    elif foyer_stop2 == 'e':
        player.current_room = room['narrow']
        print(player)
    else:
        print("Cant go that way!!!")
        
    narrow_stop = input('Which direction do you want to go? ')
    
    if narrow_stop == 'q':
        break
    elif narrow_stop == 'n':
        player.current_room = room['treasure']
        print(player)
    elif narrow_stop == 'w':
        player.current_room = room['foyer']
        print(player)
    else:
        print("Cant go that way!!!")
        
    if player.current_room == room['treasure']:
        
        
        print("""
***************************************************************
    CONGRATULATIONS YOU FOUND THE TREASURE ROOM YOU WIN!!!
***************************************************************
          """)
    break
