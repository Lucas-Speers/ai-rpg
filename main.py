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
        self.hp -= max(0, amount - self.defense)
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
            self.magic -= 1  # Decrease magic points
            if enemy['hp'] <= 0:
                print(f"You defeated the {enemy['name']}!")
                self.exp += 50
                self.level_up()
                return True
        else:
            print("\nYou're out of magic!")
        return False

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

def part1(player):
    print("\n--- Part 1: The Quest Begins ---")
    print("You start in the snowy village of Frostvale, known for its harsh winters.")
    print("The village elder approaches you, pleading for help to find the Emberstone, a powerful artifact hidden in the Ironclad Caves.")
    print("The Emberstone is the only hope to restore warmth to Frostvale.\n")

    input("Press Enter to begin your journey...")

    # Minor obstacle
    enemy = {"name": "Wolf", "hp": 30, "attack": 8}
    print(f"\nOn your way to the cave, a wild {enemy['name']} appears!\n")
    battle(player, enemy)

def part2(player):
    print("\n--- Part 2: The Descent into Darkness ---")
    print("You arrive at the Ironclad Caves, a dark and dangerous place filled with unknown perils.")
    print("Ancient inscriptions hint that the Emberstone is cursed, and its protector is a fallen hero, Malak, betrayed long ago.")

    input("Press Enter to delve deeper into the cave...")

    # Intermediate enemy
    enemy = {"name": "Shadow Creature", "hp": 50, "attack": 12}
    print(f"\nA {enemy['name']} appears from the darkness!\n")
    battle(player, enemy)

def part3(player):
    print("\n--- Part 3: The Final Confrontation ---")
    print("At last, you reach the deepest chamber of the caves, where the Emberstone lies surrounded by enchanted stones.")
    print("Suddenly, a spectral figure appears before you. It is Malak, the fallen hero, now a vengeful spirit guarding the Emberstone.\n")
    print("Malak speaks, 'Only one with a worthy heart can claim the Emberstone. Will you prove yourself?'\n")

    action = input("Choose your action: [fight or reason]: ").lower()
    if action == "fight":
        enemy = {"name": "Malak, the Cursed Spirit", "hp": 80, "attack": 15}
        print("\nYou choose to fight Malak!\n")
        battle(player, enemy)
        print("\nWith Malak defeated, you claim the Emberstone and return to Frostvale.")
    elif action == "reason":
        print("\nYou choose to reason with Malak, speaking of his honorable past.")
        print("Malak, moved by your words, finds peace and willingly grants you the Emberstone.\n")
        print("With the Emberstone in hand, you return to Frostvale, restoring warmth and peace to the village.")
    else:
        print("Invalid choice. Malak becomes angry and attacks you!")
        enemy = {"name": "Malak, the Cursed Spirit", "hp": 80, "attack": 15}
        battle(player, enemy)
        print("\nWith Malak defeated, you claim the Emberstone and return to Frostvale.")

def battle(player, enemy):
    while player.hp > 0 and enemy["hp"] > 0:
        action = input("\nChoose an action: [attack, spell, stats, flee]: ").lower()

        if action == "attack":
            if player.attack_enemy(enemy):
                return  # Enemy defeated
            if player.take_damage(enemy["attack"]):
                print("Game Over.")
                exit()

        elif action == "spell":
            if player.cast_spell(enemy):
                return  # Enemy defeated
            if player.take_damage(enemy["attack"]):
                print("Game Over.")
                exit()

        elif action == "stats":
            print(f"\nStats: HP: {player.hp}, Attack: {player.attack}, Defense: {player.defense}, Magic: {player.magic}, Level: {player.level}, EXP: {player.exp}")

        elif action == "flee":
            print("\nYou fled from battle.")
            break
        else:
            print("Invalid action.")

def main():
    player = choose_class()
    part1(player)
    part2(player)
    part3(player)
    print("\n--- The End ---")
    print("Thank you for playing! You have completed the quest to restore warmth to Frostvale.")

if __name__ == "__main__":
    main()
