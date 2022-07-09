from os import system
from travel_data import Travel_data
from seed import seed

travel_dict = seed()

def print_options():
    print("1. Travel Directory")
    print("2. Check travel log leaderboard")
    print("3. Add Future/Previous travels.")
    print("4. Delete a destination from the menu.")
    print("5. Edit travels.")
    print("6. Describe an item in travel log")
    print("7. Exit")
    option = input("Select your option (1-7): ")
    return option

def leaderboard():
    print("Welcome to the leaderboard")
    travel_dict.print_header()
    sorted  = travel_dict.leaderboard()
    for item in sorted:
        item.show_data()

def describe_travel():


def add_travel():
    name = input("What was the name of location? ")
    date = input(f"What was the date you went to {name}? e.g 22/2/22:   ")
    duration = input(f"How long were you at {name}? e.g 5 Days:     ")
    rating = 0
    while True:
        rating = float(input(f"What would you rate the trip when you went to {name} on {date} for {duration}? (1 being worst, 10 being best):      "))
        if rating <= 10 and rating >= 0:
            break
        else:
            print("Incorrect value")
    travel_dict.add_travels(name, date, duration, rating)
    print(f"{name}, {date}, {duration}, {rating} has been added to the travel log!")

def edit_travel():
    pass
def remove_travels():
    date = input("What was the date of which destination you would like to remove? (1/11/11):   ")
    travel_dict.remove_travels(date)

option = ""

while option != "6":
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
        continue
    else:
        print("Invalid option")
        
    input("press Enter to continue...")
    system('clear')

print("Thanks for using (Jyes Travel Log) terminal application!")