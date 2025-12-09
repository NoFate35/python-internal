from ticket import Ticket


class AirplaneTicket(Ticket):
    # BEGIN (write your solution here)
    def __init__(self, number, price, date, airline, seat_number, service_class):
        super().__init__(number, price, date)
        self.airline = airline
        self.seat_number = seat_number
        self.service_class = service_class
    
    def get_info(self):
        properties = super().get_info()
        properties['airline'] = self.airline
        properties['seat_number'] = self.seat_number
        properties['service_class'] = self.service_class
        return properties
    # END