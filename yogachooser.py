import sys, os, random
from os import system

list_arm = open("./poses/arms.txt").readlines()
list_chest = open(".poses/chest.txt").readlines()
list_legs = open(".poses/legs.txt").readlines()
list_back = open(".poses/back.txt").readlines()

def display_menu(menu):
    for k, function in menu.items():
        print(k, function.__name__)

def Arms():
    print(random.choice(list_arm))

def Chest():
    print(random.choice(list_chest))

def Legs():
    print(random.choice(list_legs))

def Back():
    print(random.choice(list_back))

def Done():
    print("------GOODBYE-----")
    sys.exit()

def main():
    os.system("clear")
    functions_names = [Arms, Chest, Legs, Back, Done]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        print('-------YOGA-------')
        display_menu(menu_items)
        print('------------------')
        selection = int(
            input("SELECT AREA: "))
        selected_value = menu_items[selection]
        selected_value()


if __name__ == "__main__":
    main()
