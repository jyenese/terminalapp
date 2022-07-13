from os import system
from travel_data import Travel_data
from seed import seed
from seed import wishlist_seed
from travel_data import Wishlist_data
from wishlist import Wishlist

travel_dict = seed()

def print_options():
    print("1. Travel Directory")
    print("2. Check travel log leaderboard")
    print("3. Add Future/Previous travels")
    print("4. Delete a destination from the menu")
    print("5. Edit travels")
    print("6. More information panel")
    print("7. Wishlist")
    print("8. Exit")
    option = input("Select your option (1-8): ")
    return option

def leaderboard():
    print("            Welcome to the leaderboard")
    print("     10 being best, 1 being worst (Top-Bottom)")
    travel_dict.print_header()
    travel_dict.header_space()
    sorted  = travel_dict.leaderboard()
    for item in sorted:
        item.show_data()
    travel_dict.header_space()

def describe_travel():
    travel_dict.print_menu() 
    date = input(f"What was the date from the travel log? e.g 22/2/22:   ")
    item = travel_dict.get_by_date(date)
    if item == None:
        print("Nothing found on that date")
        return
    item.pretty_print()


def add_travel():
    name = input("What was the name of location? ")
    date = input(f"What was the date you went to {name}? e.g 22/2/22:   ")
    duration = input(f"How long were you at {name}? e.g 5 Days:     ")
    comment = input(f"Additional comments about the trip: ")
    rating = 0
    while True:
        rating = float(input(f"What would you rate the trip when you went to {name} on {date} for {duration}? (1 being worst, 10 being best):      "))
        if rating <= 10 and rating >= 0:
            break
        else:
            print("Incorrect value")
    travel_dict.add_travels(name, date, duration, rating, comment)
    print(f"{name}, {date}, {duration}, {rating} has been added to the travel log!")

def edit_travel():
    travel_dict.print_menu()
    name = input("What date of destination do you want to edit? e.g 11/11/11 ")
    travel_dict.travel_edit(name)
    

def remove_travels():
    travel_dict.print_menu()
    date = input("What was the date of which destination you would like to remove? (11/11/11):   ")
    travel_dict.remove_travels(date)

def wishlist():
    wishlist_dict = wishlist_seed()
    option = input("What would you like to do? (view or add)?: ")
    if option == "add":
        name = input("Where is somewhere you'd like to travel in the future?:  ")
        date = input(f"When would you like to travel to {name}?:  ")
        duration = input(f"How long would you like to spend in {name}? e.g 5 Days:     ")
        cost = input(f"How much is it going to roughly cost to travel to {name} for {duration}?: ")
        wishlist_dict.wishlist_add(name, date, duration, cost)
        print(f"{name}, {date}, {duration}, {cost} has been added to the wishlist!")
        wishlist_dict.wishlist_menu()
    elif option == "view":
        wishlist_dict.wishlist_menu()
    else:
        print("Invlaid")
    # Why is this not getting added when 'add' function is displayed for the wishlist
    


option = ""

while option != "8":
    system('clear')
    option = print_options()
    system('clear')
    if option == "1":
        travel_dict.print_menu()
    elif option == "2":
        leaderboard()
    elif option == "3":
        add_travel()
    elif option == "4":
        remove_travels()
    elif option == "5":
        edit_travel()
    elif option == "6":
        describe_travel()
    elif option == "7":
        wishlist()
    elif option == "8":    
        continue
    else:
        print("Invalid option")
        
    input("press Enter to continue...")
    system('clear')

print("Thanks for using (Jyes Travel Log) terminal application!")