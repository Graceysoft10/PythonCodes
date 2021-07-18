from . import Airline


class Passenger:
    def __init__(self):
        self.passengerName = None
        self.passengerId = 0
        self.seatNumber = None

    def book_seat(self, is_first_class, airline):
        if is_first_class:
            seatNumber = airline.assign_seat()
            self.seatNumber = seatNumber
        else:
            seatNumber = airline.assign_seat()