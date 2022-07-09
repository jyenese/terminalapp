from travel_data import Travel_data
from travel_directory import TravelDirectory

def seed():
    dest1 = Travel_data("Queenstown, New Zealend", "20/7/2015", "10 Days", 8.5)
    dest2 = Travel_data("Bali", "31/8/2015","7 Days", 6.5)
    dest3 = Travel_data("Budapest","28/7/2016","4 Days", 7)
    dest4 = Travel_data("Lagos, Lisbon", "2/8/2016","5 Days", 8.5)
    dest5 = Travel_data("Barcelona, Spain", "7/8/2016","5 Days", 8)
    dest6 = Travel_data("Prague, Czech Republic", "12/8/2016","3 Days", 6)
    dest7 = Travel_data("Hvar, Croatia", "15/8/2016","6 Days", 9)
    dest8 = Travel_data("Split, Croatia", "21/8/2016","2 Days" ,5)
    dest9 = Travel_data("Big White(Ski, Resort), Canada", "26/12/2016","5 Days", 9)
    dest9 = Travel_data("Whistler(Ski Resort), Canada", "1/1/2017", "5 Days", 6)
    dest9 = Travel_data("Las Vegas, Nevada", "23/6/2017","3 Days", 8)
    dest10 = Travel_data("Santa Barbara, California","26/6/2017","3 Days", 5)
    dest11 = Travel_data("San Francisco", "29/6/2017","4 Days", 4)
    dest12 = Travel_data("San Diego", "3/7/2017", "5 Days", 8)
    dest13 = Travel_data("Niseko, Japan", "7/1/2018", "10 Days", 7.5)
    dest14 = Travel_data("Bali", "16/1/2019","7 Days", 8)
    dest15 = Travel_data("Niseko, Japan","7/3/2020", "7 Days", 9)
    travel_dict = TravelDirectory([dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8, dest9, dest10, dest11, dest12, dest13, dest14, dest15])
    return travel_dict





