from unicodedata import name


class Travel_data:
    def __init__(self, name, date, duration, rating, comment):
        self.name = name
        self.date = date
        self.duration = duration
        self.rating = rating
        self.comment = comment

    def show_data(self):
        print(f"{self.name}, {self.date}, {self.duration}, {self.rating}")

    def pretty_print(self):
        print(f"""
        Name: {self.name}
        Date: {self.date}
        Duration of stay: {self.duration}
        Rating out of 10: {self.rating}
        Additional comments: {self.comment}
        
        """)

class Wishlist_data:
    def __init__(self, name, date, duration, cost):
        self.name = name
        self.date = date
        self.duration = duration
        self.cost = cost
        
    def wishlist_data(self):
        print(f"{self.name}, {self.date}, {self.duration}, {self.cost}")