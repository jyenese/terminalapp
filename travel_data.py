from unicodedata import name


class Travel_data:
    def __init__(self, name, date, duration, rating):
        self.name = name
        self.date = date
        self.duration = duration
        self.rating = rating

    def show_data(self):
        print(f"{self.name}, {self.date}, {self.duration}, {self.rating}")


