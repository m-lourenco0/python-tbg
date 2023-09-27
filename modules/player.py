# Player-related classes/functions (e.g., inventory, stats)
class Player:
    """
    Represents the player's state (inventory, current room, etc.)
    """
    def __init__(self, start_room):
        self.inventory = []
        self.current_room = start_room
        self.facing_door = None
        self.previous_room = None

    def pick_up(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)
        print(f"You picked up {item}.")

    def has_item(self, item):
        """Return True if the player has the item, False otherwise."""
        if item in self.inventory:
            # print("You have " + item + "on you.")
            return True
        # print("You don't have " + item + "on you.")
        return False

    def show_inventory(self):
        """Display the player's inventory."""
        if self.inventory:
            print("You have: " + ", ".join(self.inventory))
        else:
            print("You have nothing.")

    def move(self, new_room):
        """Move to a new room."""
        self.previous_room = self.current_room  # Update previous room before moving
        self.current_room = new_room
        self.facing_door = None  # Reset facing door when moving to a new room

    def face_door(self, direction):
        """Face the door."""
        self.facing_door = direction

    def go_back(self):
        """Go back to the previous room."""
        if self.facing_door:
            self.facing_door = None
        elif self.previous_room:
            self.current_room, self.previous_room = self.previous_room, self.current_room
            self.facing_door = None  # Reset facing door

    # Additional methods can be added as needed
