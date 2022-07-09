from os import system
def print_options():
    print("1. Travel Directory")
    print("2. Check travel log leaderboard")
    print("3. Add Future/Previous travels.")
    print("4. Delete a destination from the menu.")
    print("5. Edit travels.")
    print("6. Exit")
    option = input("Select your option (1-6): ")
    return option

def travel_log():
    pass            
def leaderboard():
    pass
def add_travel():
    pass
def edit_travel():
    pass
def remove_travel():
    pass

option = ""

while option != "6":
    system('clear')
    option = print_options()
    system('clear')
    if option == "1":
        travel_log()
    elif option == "2":
        leaderboard()
    elif option == "3":
        add_travel()
    elif option == "4":
        remove_travel()
    elif option == "5":
        edit_travel()
        continue
    elif option == "6":
        continue
    else:
        print("Invalid option")
        
    input("press Enter to continue...")
    system('clear')

print("Thanks for using (Jyes Travel Log) terminal application!")