class Airline:
    def __init__(self):
        self.firstClass = [False, False, False, False, False]
        self.economyClass = [False, False, False, False, False]
        self.firstClass_count = 0
        self.economyClass_count = 5

    def assign_seat(self, is_first_class):
        if is_first_class:
            self.firstClass_count += 1
            seat_number = self.firstClass[0] = True
            return seat_number
        else:
            self.economyClass_count += 1
            seat_number = self.economyClass[5] = True
            return seat_number
