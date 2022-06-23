class Flight():
    def __init__(self, capasity):
        self.capacity = capasity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(5)

bookers = ["harry", "ron", "maguire", "yu", "oika", "mac", "ned", "tobey"]
for person in bookers:
    success = flight.add_passenger(person)
    if success:
        print(f"{person} is added to the flight")
    else:
        print(f"{person} is out from the flight")

