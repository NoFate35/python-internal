from ticket import Ticket


class TrainTicket(Ticket):
    # BEGIN (write your solution here)
    def __init__(self, train_number, seat_number, wagon_type):
        super().__init__()
        self.train_number = train_number
        self.seat_number = seat_number
        self.wagon_type = wagon_type
    # END
