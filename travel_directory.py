from sys import setdlopenflags
from travel_data import Travel_data

class TravelDirectory:
    def __init__(self, travel_dict):
        self.travel_dict = travel_dict

dest1 = Travel_data("Queenstown, New Zealend", "20/7/2015", "10 Days", 8.5)
dest2 = Travel_data("Bali", "31/8/2015","7 Days", 6.5)
dest3 = Travel_data("Budapest","28/7/2016","4 Days", 7)
dest4 = Travel_data("Lagos, Lisbon", "2/8/2016","5 Days", 8.5)
dest5 = Travel_data("Barcelona, Spain", "7/8/2016","5 Days", 8)
dest6 = Travel_data("Prague, Czech Republic", "12/8/2016","3 Days", 6)
dest7 = Travel_data("Hvar, Croatia", "15/8/2016","6 Days", 9)
dest8 = Travel_data("Split, Croatia", "21/8/2016","2 Days" ,5)
dest9 = Travel_data("Big White(Ski, Resort), Canada", "26","" ,)
