# Main game logic (game loop, command interpreter, etc.)

def display_room(room):
    """
    Display the current room's description and any objects present.
    """
    print(room["description"])
    if room["objects"]:
        print("You see: " + ", ".join(room["objects"]))

def get_user_command():
    """
    Get a command from the user.
    """
    return input("> ").strip().lower()

def interpret_command(command, current_room, rooms, player_inventory):
    """
    Interpret and execute the user's command based on the current room and game state.
    Return the new current room.
    """
    # If user types "go [direction]" and [direction] is a valid direction
    if command.startswith("go "):
        direction = command.split(" ")[1]
        if direction in current_room["directions"]:
            door = current_room["doors"].get(direction)
            if door and door["status"] == "unlocked":
                return rooms[door["leads_to"]]
            elif door and door["status"] == "locked":
                print("The door is locked!")
            else:
                print("You can't go that way.")
        else:
            print("You can't go that way.")
    elif command.startswith("pick up "):
        item = command.split("pick up ")[1]
        if item in current_room["objects"]:
            player_inventory.append(item)
            current_room["objects"].remove(item)
            print(f"You picked up {item}.")
        else:
            print(f"There's no {item} here.")
    else:
        print("I don't understand that command.")
    
    return current_room  # Return the same room if no valid move was made
