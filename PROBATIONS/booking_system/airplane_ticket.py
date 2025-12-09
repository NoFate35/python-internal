from ticket import Ticket


class AirplaneTicket(Ticket):
    # BEGIN (write your solution here)
    def __init__(self, airline, seat_number, service_class):
        super().__init__()
        self.airline = airline
        self.seat_number = seat_number
        self.service_class = service_class
    # END