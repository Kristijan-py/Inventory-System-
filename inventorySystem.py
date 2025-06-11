'''Create a program that manages a basic inventory system using a class. The program should:

Use a class called Inventory with:

An attribute to store items (as a dictionary, where the key is the item name and the value is the quantity).
Methods to:
Add an item (increase quantity if it already exists).
Remove an item (decrease quantity or remove the item entirely if quantity becomes zero).
Display all items in the inventory.
Handle cases where the user tries to remove an item that doesn't exist using try-except.
Include a menu in the program with the following options:

Add an item.
Remove an item.
Show inventory.
Exit.
'''

class Inventory:
    def __init__(self):
        self.store_items = {}
        
    def add_item(self,item_name,quantity):
        if item_name in self.store_items:
            self.store_items[item_name] += quantity    # if it is already there, just add quantity
        else:
            self.store_items[item_name] = quantity   # if not, add as new one to the set
        
    
    def remove_item(self,item_name,quantity):
        if item_name not in self.store_items:
            raise KeyError("Item not found !")
        if self.store_items[item_name] < quantity:   # Cannot remove because is more than we have
            raise ValueError("Cannot remove more than you have !")
        self.store_items[item_name] -= quantity   # subtract the quantity
        if self.store_items[item_name] == 0:
            del self.store_items[item_name]
    
    def display_items(self):
        if not self.store_items:
            print("Inventory is empty")
        else:
            print("Here are all the items")
            for key,value in self.store_items.items():
                print(f"{key} : {value}")
            
        

# Main program
def main():
    inventory = Inventory() #initialize
    running = True
    
    while running: 
        print("\nMenu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Show all items")
        print("4. Exit")
        
        try:
            choice = int(input("Odberi od 1 do 4: "))
            
            if choice == 1:
                item_name = input("Type any item to add: ").lower().strip()
                quantity = int(input("how many: "))
                inventory.add_item(item_name,quantity)           
                continue
            elif choice == 2:
                item_name = input("what you want to remove: ").lower().strip()
                quantity = int(input("How many: "))
                inventory.remove_item(item_name,quantity)
                continue
            elif choice == 3:
                inventory.display_items()
                continue
            elif choice == 4:
                print("Goodbye !")
                break
            else:
                print("Invalid choice, choose from 1 to 4")
                
        except ValueError:
            print("Invalid! Only numbers")
            
main()
            
            