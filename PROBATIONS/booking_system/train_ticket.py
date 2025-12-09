from ticket import Ticket


class TrainTicket(Ticket):
    # BEGIN (write your solution here)
    def __init__(self, number, price, date, train_number, seat_number, wagon_type):
        super().__init__(number, price, date,)
        self.train_number = train_number
        self.seat_number = seat_number
        self.wagon_type = wagon_type
    
    def get_info(self):
        properties = super().get_info()
        properties['train_number'] = self.train_number
        properties['seat_number'] = self.seat_number
        properties['wagon_type'] = self.wagon_type
        return properties
    # END
