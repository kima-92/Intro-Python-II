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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['foyer'].add_new_item(Item("hat", "A very pretty hat"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

outside_room = room['outside']

player_name = input("\nWelcome to Mystical Wonders!\n\nWhat is your name?: ")
player = Player(player_name, outside_room)

# Print game intro Dialogue

print(f"\nHello {player.name}! You are currently in: {player.current_room.name}")
print("""\nYou can enter different rooms by moving North, South, East or West. 
To move use the commands 'n', 's', 'e' or 'w'. 
Use the 'q' keyword when you decide you want to exit the game.""")

# Attributes

new_direction = ""
current_room = player.current_room

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

# def grab_direction(direction_strin)

# def check_if_room_available(direction):

def display_items():

    items = current_room.items

    if items != []:
        
        print("\nThis room has items!\n")
        
        for i in items:
            print(i)

def try_to_move(direction):

    global current_room

    if direction == "n":
        
        if current_room.n_to == []:
            print("There is nothing in this direction, try another direction.")

        else:
            current_room = current_room.n_to
            print(f"You moved North! You are currently in the {current_room.name}. {current_room.description}")

            display_items()

    elif direction == "s":
        
        if current_room.s_to == []:
            print("There is nothing in this direction, try another direction.")

        else:
            
            current_room = current_room.s_to
            print(f"You moved South! You are currently in the {current_room.name}. {current_room.description}")

    elif direction == "e":

        if current_room.e_to == []:
            print("There is nothing in this direction, try another direction.")

        else:
            
            current_room = current_room.e_to
            print(f"You moved East! You are currently in the {current_room.name}. {current_room.description}")

    elif direction == "w":

        if current_room.w_to == []:
            print("There is nothing in this direction, try another direction.")

        else:
            
            current_room = current_room.w_to
            print(f"You moved West! You are currently in the {current_room.name}. {current_room.description}")

    elif direction != "q":
        print("Invalid entry, please try 'n', 's', 'e', 'w' or 'q'")



while new_direction != "q":

    new_direction = input("\nWhere do you want to go? : ")

    try_to_move(new_direction)
