from room import Room
from player import Player
from item import Item

print("""
*************************************      
*      WELCOME TO THE BEST GAME     *
*************************************
      """)

input_name = input('Enter your name: ')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [
                         Item("sword", "very sharp"),
                         Item("shield", "very flat"),
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [
        Item("rock", "very hard"),
        Item("mirror", "very reflective"),
    ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [
        Item("wand", "very long"),
        Item("water", "very holy"),
    ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [
        Item("stick", "very skinny"),
        Item("lantern", "very bright"),
    ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [
        Item("Coin", "very shiny"),
        Item("necklace", "very expensive"),
    ]),
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

def move_direction(player, direction):
    attribute = direction + '_to'
    
    if hasattr(player.location, attribute):
        player.location = getattr(player.location, attribute)
        
    else:
        print("Can not move in that direction!")
# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], input_name)

# Write a loop that:
while True:
    #
    # * Prints the current room name
    player.print_status()
    # * Prints the current description (the textwrap module might be useful here).
    print('\n')
    print(f"{player.player_name} is at {player.location}")
    
    print('\n')
    # * Waits for user input and decides what to do.
    command = input("\nCommand: ").strip().lower()
    command = command[0]
    
    # If the user enters "q", quit the game.
    if command == 'q':
        break 
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    
    print(f"{player.print_inventory()}")
    if command == 'n':
        move_direction(player, command)
    elif command == 's':
        move_direction(player, command)
    elif command == 'e':
        move_direction(player, command)
    elif command == 'w':
        move_direction(player, command)
    
    
