class Ticket:
    def __init__(self, number, price, date):
        self.number = number
        self.price = price
        self.date = date

    def get_info(self):
        return {
           "number": self.number,
           "price": self.price,
           "date": self.date,
        }
