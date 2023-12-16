class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the seats availaible in the train is {self.seats}")

    def fareinfo(self):
        print(f"the name of the train is {self.fare}")

    def bookticket(self):
        if (self.seats > 0):
            print("Your ticket has been booked")
            self.seats = self.seats-1
        else:
            print("Sorry! this train is full")


Intercity = Train("Intercity express", 90, 2)
Intercity.getstatus()
Intercity.fareinfo()
Intercity.bookticket()
Intercity.getstatus()
Intercity.bookticket()
Intercity.bookticket()
