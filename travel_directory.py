from sys import setdlopenflags
from travel_data import Travel_data


class TravelDirectory:
    def __init__(self, travel_dict):
        self.travel_dict = travel_dict

    def header_space(self):
        print(("--------------------------------------------------------"))
    
    def print_menu(self):
        print("            Welcome to MY TRAVEL LOG!")
        self.print_header()
        self.header_space()
        for item in self.travel_dict:
            item.show_data()
        self.header_space()
    
    def print_header(self):
        print("        NAME | DATE  | DURATION  | RATING")

    def add_travels(self, name, date, duration, rating, comment):
        self.travel_dict.append(Travel_data(name, date, duration, rating, comment))

    def remove_travels(self,date):
        for item in self.travel_dict:
            saved = item.name
            if item.date == date:
                self.travel_dict.remove(item)
                return print(f"The time you traveled to {saved} on the {date} has been removed.")
        return print(f"{date} you haven't been anywhere on this date.")

    def get_by_date(self, date):
        for item in self.travel_dict:
            if item.date == date:
                return item
        return None

    def leaderboard(self):
        sort = sorted(self.travel_dict, key=lambda x: x.rating, reverse=True)
        return sort


        