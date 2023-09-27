import json
from modules.game import display_room, get_user_command, interpret_command
from modules.player import Player

def load_rooms(filename):
    """Load room data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    """Main game loop."""
    # Load the room data
    rooms = load_rooms('data/rooms.json')
    # Initialize the player with the starting room
    player = Player(rooms["start"])

    print("Welcome to the Text-Based Game!")
    print("Type 'exit' anytime to quit.")

    while True:
        # Check if the player is facing a locked door
        if player.facing_door:
            door = player.current_room["doors"].get(player.facing_door)
            if door and door["status"] == "locked":
                print(f"You are facing the {player.facing_door} door. It's locked.")
            else:
                # If the door is not locked or there's no door, reset facing_door
                player.facing_door = None
                display_room(player.current_room)
        else:
            # If the player is not facing any door, display the room description
            display_room(player.current_room)
        command = get_user_command()

        if command == "exit":
            print("Thanks for playing!")
            break

        interpret_command(command, player, rooms)

if __name__ == "__main__":
    main()
