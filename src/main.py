# Entry point for the game
import json
from modules.game import display_room, get_user_command, interpret_command
# Additional imports as needed

def load_game_data(filename):
    """
    Load game data from a JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    """
    Main game logic (game loop, command interpreter, etc.)
    """
    # Load game data
    rooms = load_game_data("data/rooms.json")

    # Initialize game state
    current_room = rooms["start"]
    player_inventory = []

    # Game loop
    while True:
        # Display current room and available actions
        display_room(current_room)
        
        # Get player input
        command = get_user_command()

        # Special command to quit the game
        if command == "quit":
            print("Thanks for playing!")
            break

        # Interpret and execute command
        current_room = interpret_command(command, current_room, rooms, player_inventory)
        # Note: We need to expand interpret_command to handle player inventory and other game states later.

if __name__ == "__main__":
    main()
