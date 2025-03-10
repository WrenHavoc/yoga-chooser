# Yoga class project

# Imports
import sys, os, random
from os import system

# link pose files
list_arm = open("./poses/arms.txt").readlines() # reads arms.txt in poses and turns it into a list called list_arm
list_chest = open("./poses/chest.txt").readlines()
list_legs = open("./poses/legs.txt").readlines()
list_back = open("./poses/back.txt").readlines()

# display menu
def display_menu(menu):
    for k, function in menu.items():
        print(k, function.__name__)

# arms
def Arms(): # creates a function called 'Arms'
    print(random.choice(list_arm)) # picks a random item from list_arm

# chest
def Chest():
    print(random.choice(list_chest))

# legs
def Legs():
    print(random.choice(list_legs))

# back
def Back():
    print(random.choice(list_back))

# exit program
def Done():
    print("GOODBYE")
    sys.exit()

# menu
def main():
    os.system("clear") # calls the system command "clear" to clear the screen
    functions_names = [Arms, Chest, Legs, Back, Done] # creates a list from the functions defined above
    menu_items = dict(enumerate(functions_names, start=1)) # enumerates the functions called in functions_names and puts them in a new list called menu_items

    while True:
        print('------------------') # creates a super cool banner
        display_menu(menu_items)
        print('------------------')
        selection = int(
            input("SELECT AREA: "))
        selected_value = menu_items[selection]
        selected_value()


if __name__ == "__main__":
    main()
