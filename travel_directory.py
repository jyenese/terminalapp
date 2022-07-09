from sys import setdlopenflags
from travel_data import Travel_data

class TravelDirectory:
    def __init__(self, travel_dict):
        self.travel_dict = travel_dict

    def print_menu(self):
        print("""Welcome to MY TRAVEL LOG! 
        NAME/DATE/DURATION/RATING""")
        for item in self.travel_dict:
            item.show_data()
    
    def add_travels(self, name, date, duration, rating):
        new_item = Travel_data(name, date, duration, rating)
        self.travel_dict.append(new_item)
