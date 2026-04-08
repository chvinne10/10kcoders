from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name, pho, email):
        self.name = name
        self.pho = pho

class RideService:
    def __init__(self):
        self.ride = {
            "auto": 50,
            "bike": 30,
            "car": 100
        }

class Payment(ABC):

    def upi(self, pin, amount):
        self._pin = pin
        print(f"Paid {amount} using UPI")

    def creditcard(self, pin, amount, cardno):
        self._pin = pin
        self._cardno = cardno
        print(f"Paid {amount} using Card")

    @abstractmethod
    def pay_bill(self, amount):
        pass

class Rider(RideService, Payment):

    def __init__(self):
        RideService.__init__(self)

    def viewride(self):
        print("Available Rides:")
        for k, v in self.ride.items():
            print(f"{k} : {v}")

    def bookride(self, ridetype):

        if ridetype in self.ride:
            print(f"{ridetype} ride booked")
            return self.ride[ridetype]
        else:
            print("Invalid ride")
            return 0

    def pay_bill(self, amount):

        choice = input("Payment method (upi/card): ")

        if choice.lower() == "upi":
            pin = input("Enter PIN: ")
            self.upi(pin, amount)

        elif choice.lower() == "card":
            pin = input("Enter PIN: ")
            cardno = input("Enter card no: ")
            self.creditcard(pin, amount, cardno)

        else:
            print("Invalid payment method")

class Ride:
    def __init__(self):
        self.history = []

    def add_ride(self, ridetype):
        self.history.append(ridetype)

    def show_history(self):
        print("Ride History:", self.history)

class User(Customer):

    def __init__(self, name, pho, email):
        super().__init__(name, pho, email)

        self.rider = Rider()   
        self.ride = Ride()    

    def login(self):
        print("Login successful")

user = None
fare = 0

while True:

    print("""
1 Register User
2 Login
3 View Rides
4 Book Ride
5 Pay Bill
6 Ride History
7 Exit
""")

    ch = input("Enter choice: ")

    match ch:

        case "1":
            name = input("Name: ")
            pho = input("Phone: ")
            email = input("Email: ")

            user = User(name, pho, email)
            print("User registered successfully")

        case "2":
            if user:
                user.login()
            else:
                print("Register first")

        case "3":
            if user:
                user.rider.viewride()
            else:
                print("Login first")

        case "4":
            if user:
                r = input("Enter ride type: ")
                fare = user.rider.bookride(r)

                if fare > 0:
                    user.ride.add_ride(r)
            else:
                print("Login first")

        case "5":
            if user and fare > 0:
                user.rider.pay_bill(fare)
            else:
                print("Book ride first")

        case "6":
            if user:
                user.ride.show_history()
            else:
                print("Login first")

        case "7":
            break

        case _:
            print("Invalid choice")