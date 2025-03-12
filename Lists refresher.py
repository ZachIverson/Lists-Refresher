# Lists: Inventory choices
weapons = ["Sword", "Bow", "Axe", "Dagger", "Spear"]

# User lists
player_inventory = []

# function to display items
def display_weapons():
    print("\nAvailable weapons:")
    for index, weapon in enumerate(weapons, start=1):
        print(f"{index}. {weapon}")

# Function to pick items
def pick_weapon():
    display_weapons()
    choice = int(input("\nEnter the number of the weapon you want to pick: ")) - 1
    if 0 <= choice < len(weapons):
        player_inventory.append(weapons[choice])
        print(f"{weapons[choice]} has been added to your inventory.")
    else:
        print("Invalid choice!")

# Function to remove item from user
def drop_weapon():
    if not player_inventory:
        print("Your inventory is empty!")
        return
    print("\nYour Inventory:")
    for index, item in enumerate(player_inventory, start=1):
        print(f"{index}. {item}")
    choice = int(input("\nEnter the number of the weapon you want to drop: ")) - 1
    if 0 <= choice < len(player_inventory):
        removed_item = player_inventory.pop(choice)
        print(f"{removed_item} has been removed from your inventory.")
    else:
        print("Invalid choice!")

# Function to show inventory
def show_inventory():
    print("\nYour Inventory:")
    print(player_inventory if player_inventory else "Empty")

# Function demonstrating operations
def list_operations():
    print("\nList Operations:")
    print("First two weapons:", weapons[:2]) 
    print("Last weapon:", weapons[-1])  
    print("Total weapons available:", len(weapons))  
    nested_list = [weapons, player_inventory]  
    print("Nested list example:", nested_list)

# Main code
while True:
    print("\nMenu:")
    print("1. Pick a weapon")
    print("2. Drop a weapon")
    print("3. Show inventory")
    print("4. List operations")
    print("5. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        pick_weapon()
    elif choice == "2":
        drop_weapon()
    elif choice == "3":
        show_inventory()
    elif choice == "4":
        list_operations()
    elif choice == "5":
        print("Exit program, Thank you")
        break
    else:
        print("Invalid, please select a valid option.")
