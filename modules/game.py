# Main game logic (game loop, command interpreter, etc.)

def display_room(room):
    """Display the current room's description and any objects present."""
    print(room["description"])
    if room["objects"]:
        print("You see: " + ", ".join(room["objects"]))

def get_user_command():
    """Get a command from the user."""
    return input("> ").strip().lower()

def interpret_command(command, player, rooms):
    """Interpret and execute the user's command based on the player's state and game rooms.
    Update the player's state accordingly.
    """
    current_room = player.current_room
    if command.startswith("go "):
        direction = command.split(" ")[1]
        if direction == "back":
            if player.previous_room:
                player.go_back()
                print(f"You moved back to the {player.current_room['name']}.")
            else:
                print("You can't go back any further.")
        else:
            door = current_room["doors"].get(direction)
            if door:
                if door["status"] == "unlocked":
                    player.move(rooms[door["leads_to"]])
                elif door["status"] == "locked":
                    player.face_door(direction)
            else:
                print(f"There's no door to the {direction}.")
    elif command.startswith("pick up "):
        item = command.split("pick up ")[1]
        if item in current_room["objects"]:
            player.pick_up(item)
            current_room["objects"].remove(item)
        else:
            print(f"There's no {item} here.")
    elif command == "open door":
        if player.facing_door:
            door = current_room["doors"].get(player.facing_door)
            if door["status"] == "locked":
                required_key = door.get("required_key")
                if player.has_item(required_key):
                    door["status"] = "unlocked"
                    print(f"You unlocked the {player.facing_door} door with the {required_key}!")
                    player.move(rooms[door["leads_to"]])
                else:
                    print(f"You don't have the key to unlock the {player.facing_door} door.")
            else:
                print(f"The {player.facing_door} door is already unlocked.")
        else:
            print("You are not facing any door.")
    elif command == "see inventory":
        player.show_inventory()
    else:
        print("I don't understand that command.")
