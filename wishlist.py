from travel_data import Wishlist_data


class Wishlist:
    def __init__(self, wishlist_dict):
        self.wishlist_dict = wishlist_dict

    def wishlist_menu(self):
        print("            Welcome to the WISHLIST!")
        print("  NAME  |  DATE  |  DURATION  |  COST")
        print(("--------------------------------------------------------"))
        for item in self.wishlist_dict:
            item.wishlist_items()
        print(("--------------------------------------------------------"))
        
    def wishlist_add(self, name, date, duration, cost):
        self.wishlist_dict.append(Wishlist_data(name, date, duration, cost))