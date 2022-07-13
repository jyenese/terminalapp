from travel_data import Wishlist_data

class Wishlist:
    def __init__(self, travel_dict):
        self.travel_dict = travel_dict

    def wishlist_menu(self):
        print("            Welcome to the WISHLIST!")
        print("  NAME  |  DATE  |  DURATION  |  COST")
        for item in self.travel_dict:
            item.wishlist_data()
        
