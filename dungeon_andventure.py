import random
player_name = input("Enter your character's name: ")
print(f"Hello, {player_name}! Welcome to the dungeon adventure.\n")
# Set health to 10.
player_health = 10
# Create an empty list to store their inventory.
player_inventory = []
Treasures = {"Suspicious Stick": 1, "Sack of Gold": 10, "Rusty Sword": 5, "Potion": 1, "Chain Armor": 15, "Spell Tome": 20, "Map": 3, "Excalibur": 999 }
print("Options:")
print("1. Search for treasure. \n2. Move to next room. \n3. Check health and inventory. \n4. Quit the game.\n")


for room in range(1,6):
    print(f"You are in room: {room}\n")

    while True:
        choice = input("Choose an option: 1-4\n")
        try:
            choice = int(choice)
            if choice == 3:
                print(f"You have {player_health} health points.")
                if len(player_inventory) == 0:
                    print("You have no items in your inventory.\n")
                else:
                    print(f"Inventory: {', '.join(player_inventory)}\n")
                
                print(f"You are in room: {room}")
                print("Options:")
                print("1. Search for treasure. \n2. Move to next room. \n3. Check health and inventory. \n4. Quit the game.\n")
            elif 1 <= choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

# Step 4: Implement treasure search
# If the player chooses to search, randomly decide if they find treasure or a trap.
# If treasure, randomly pick from the treasure dictionary and add to inventory.
# If trap, deduct 2 health points and print a message.
    if choice == 1:
        if random.choice([True, False]):
            treasure = random.choice(list(Treasures.keys()))
            if treasure == "Excalibur":
                print(f"Congratulations, {player_name}! You found {treasure}! You are now the chosen one!\nMoving to next room.\n")
                player_inventory.append(treasure)
                del Treasures[treasure]
            else:
                print(f"Congratulations, {player_name}! You found a {treasure}.\nMoving to next room.\n")
                player_inventory.append(treasure)
        else:
            player_health -= 2
            print(f"It's a trap! You lost 2 health points.\nMoving to next room.\n")
    elif choice == 2:
        if room < 5:
            print(f"Moving to next room:{room + 1}...\n")
        else:
            print("You have reached the last room. Game Over!\n")
            break
  
   # elif choice == 3:
    #    print(f"You have {player_health} health points.")
     #   print(f"Inventory: {', '.join(player_inventory) if player_inventory else 'empty'}\n")
      #  continue

    elif choice == 4:
        break
# Step 5: Check health
# If health drops to 0 or below, print a Game Over message and break the loop.
    if player_health <= 0:
        print("Game Over! You lose all your health.\n")
        break

player_gains = sum(Treasures.get(item, 0) for item in player_inventory)
print("Thanks for playing! You have reached the end of your adventure.\n")
print(f"Game summary:")
print(f"Player: {player_name} \nFinal Health: {player_health}")
if len(player_inventory) == 0:
    print("You collected no treasures.")
else:
    print(f"Inventory: {', '.join(player_inventory)}")
print(f"Spoils of adventure: {player_gains} gold.")




