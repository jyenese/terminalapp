from unicodedata import name


class Travel_data:
    def __init__(self, name, date, duration, rating):
        self.name = name
        self.date = date
        self.duration = duration
        self.rating = rating

    def show_data(self):
        print(f"{self.name}, {self.date}, {self.duration}, {self.rating}")

dest1 = Travel_data("Bali", "22/2/22","5 Days", "*4")
print(dest1.show_data())


