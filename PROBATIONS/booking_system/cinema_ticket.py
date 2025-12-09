from ticket import Ticket


class CinemaTicket(Ticket):
    # BEGIN (write your solution here)
    def __init__(self, number, price, date, movie_title, seat_number, hall_number):
        super().__init__(number, price, date)
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.hall_number = hall_number
    
    def get_info(self):
        properties = super().get_info()
        properties['movie_title'] = self.movie_title
        properties['seat_number'] = self.seat_number
        properties['hall_number'] = self.hall_number
        return properties
    # END
