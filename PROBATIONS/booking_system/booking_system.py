class BookingSystem:
    # BEGIN (write your solution here)
    def __init__(self):
        self.tickets = []
    
    def book_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_ticket(self, number):
        for ticket in self.tickets:
            properties = ticket.get_info()
            if properties['number'] == number:
                return ticket
    
    def get_ticket_list(self):
        return self.tickets
    
    def cancel_booking(self, number):
        for ticket in self.tickets:
            properties = ticket.get_info()
            if properties['number'] == number:
                self.tickets.remove(ticket)
                return True
        return False
    # END
