import random

class Character:
    def __init__(self, name, hp, attack, defense, magic):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.level = 1
        self.exp = 0
        self.inventory = []

    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.hp += 10
            self.attack += 2
            self.defense += 2
            self.magic += 2
            print(f"\nYou leveled up! You're now level {self.level}.")
            print(f"New stats - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Magic: {self.magic}")

    def take_damage(self, amount):
        damage_taken = max(0, amount - self.defense)
        self.hp -= damage_taken
        print(f"\nThe enemy deals {damage_taken} damage to you.")
        print(f"Your current health: {self.hp}")
        if self.hp <= 0:
            print("\nYou have been defeated.")
            return True
        return False

    def attack_enemy(self, enemy):
        damage = self.attack + random.randint(-2, 5)
        print(f"\nYou attack the {enemy['name']} for {damage} damage!")
        enemy['hp'] -= damage
        if enemy['hp'] <= 0:
            print(f"You defeated the {enemy['name']}!")
            self.exp += 50
            self.level_up()
            return True
        return False

    def cast_spell(self, enemy):
        if self.magic > 0:
            spell_damage = self.magic * 2
            print(f"\nYou cast a spell on the {enemy['name']} for {spell_damage} damage!")
            enemy['hp'] -= spell_damage
            self.magic -= 1
            if enemy['hp'] <= 0:
                print(f"You defeated the {enemy['name']}!")
                self.exp += 50
                self.level_up()
                return True
        else:
            print("\nYou're out of magic!")
        return False

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"\nYou picked up: {item}")

def choose_class():
    classes = {
        "Warrior": Character("Warrior", hp=120, attack=15, defense=10, magic=2),
        "Mage": Character("Mage", hp=80, attack=5, defense=5, magic=15),
        "Rogue": Character("Rogue", hp=90, attack=12, defense=8, magic=5),
        "Paladin": Character("Paladin", hp=110, attack=10, defense=12, magic=4),
        "Hunter": Character("Hunter", hp=85, attack=13, defense=7, magic=3)
    }

    print("Choose your class:")
    for cls_name in classes:
        print(f"- {cls_name}")

    choice = input("\nEnter the class you want to play: ").capitalize()
    while choice not in classes:
        print("Invalid choice. Please choose again.")
        choice = input("\nEnter the class you want to play: ").capitalize()

    print(f"\nYou have chosen the {choice} class!\n")
    return classes[choice]

def display_location(location, map_directions, items_in_rooms):
    descriptions = {
        "village": "You are in the village of Frostvale, where the elders gather around a small fire, waiting for someone to retrieve the Emberstone.",
        "path": "You are on the path leading towards the mountains. The air is cold, and you hear distant howls.",
        "forest": "You find yourself in a dense, dark forest. The trees are thick, and shadows move in the corners of your vision.",
        "clearing": "A small clearing in the forest, with sunlight breaking through. The ground is covered in strange runes.",
        "lake": "You arrive at a frozen lake, the surface glistening under the pale sunlight. The ice looks fragile in places.",
        "cave_entrance": "You stand at the entrance of the Ironclad Caves. The shadows seem to watch you, and the air is dense with mystery.",
        "cave_depths": "Deeper inside the cave, strange inscriptions line the walls. The air grows colder, and the silence is unsettling.",
        "chamber": "You enter the final chamber of the cave. The Emberstone lies in the center, surrounded by enchanted stones and guarded by the spirit of Malak."
    }
    
    print(f"\n{descriptions[location]}")
    
    exits = map_directions[location]
    print("\nYou can go in the following directions:")
    for direction, destination in exits.items():
        print(f"- {direction.capitalize()} to {destination.replace('_', ' ').capitalize()}")
    
    if location in items_in_rooms:
        item = items_in_rooms[location]
        print(f"\nYou see a {item} here.")

def move_player(location, direction, map_directions):
    if direction in map_directions[location]:
        new_location = map_directions[location][direction]
        return new_location
    else:
        print("\nYou can't go that way.")
        return location

def show_commands():
    print("\nAvailable commands:")
    print("- go <direction>: Move in the specified direction (e.g., 'go north').")
    print("- pick up <item>: Pick up an item in the room.")
    print("- inventory: View your current inventory.")
    print("- stats: View your character's current stats.")

def main():
    player = choose_class()
    location = "village"
    
    map_directions = {
        "village": {"north": "path", "east": "forest"},
        "path": {"south": "village", "north": "cave_entrance", "east": "clearing"},
        "forest": {"west": "village", "east": "lake"},
        "clearing": {"west": "path", "east": "cave_entrance"},
        "lake": {"west": "forest"},
        "cave_entrance": {"south": "path", "west": "clearing", "north": "cave_depths"},
        "cave_depths": {"south": "cave_entrance", "north": "chamber"},
        "chamber": {"south": "cave_depths"}
    }

    items_in_rooms = {
        "village": "healing potion",
        "clearing": "ancient rune",
        "lake": "mystic herb",
        "cave_entrance": "torch",
        "cave_depths": "spell scroll"
    }

    print("\n--- Part 1: The Quest Begins ---")
    print("The elder has tasked you with retrieving the Emberstone to restore warmth to Frostvale.")
    
    while location != "chamber":
        display_location(location, map_directions, items_in_rooms)
        
        # Show the available commands each turn
        show_commands()
        
        command = input("\nWhat would you like to do? ").lower().split()

        if command[0] == "go":
            direction = command[1]
            location = move_player(location, direction, map_directions)

        elif command[0] == "pick" and command[1] == "up":
            item = items_in_rooms.get(location)
            if item:
                player.add_to_inventory(item)
                del items_in_rooms[location]
            else:
                print("There is nothing here to pick up.")

        elif command[0] == "inventory":
            print(f"\nInventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")

        elif command[0] == "stats":
            print(f"\nStats: HP: {player.hp}, Attack: {player.attack}, Defense: {player.defense}, Magic: {player.magic}")

        else:
            print("\nInvalid command. Please try again.")

    print("\n--- The End ---")
    print("You have completed the quest and restored warmth to Frostvale!")

if __name__ == "__main__":
    main()
