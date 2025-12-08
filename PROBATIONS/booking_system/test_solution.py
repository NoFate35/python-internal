import pytest

from airplane_ticket import AirplaneTicket
from train_ticket import TrainTicket
from cinema_ticket import CinemaTicket
from booking_system import BookingSystem


@pytest.fixture()
def airplane_ticket_data():
    return {
        "number": 1,
        "price": 100,
        "date": '2024-01-01',
        "airline": "Аэрофлот",
        "seat_number": "1A",
        "service_class": "Бизнес"
    }


@pytest.fixture()
def train_ticket_data():
    return {
        "number": 2,
        "price": 50,
        "date": '2024-02-02',
        "train_number": "001",
        "seat_number": "10",
        "wagon_type": "Плацкарт"
    }


@pytest.fixture()
def cinema_ticket_data():
    return {
        "number": 3,
        "price": 200,
        "date": '2024-03-03',
        "movie_title": "Матрица",
        "seat_number": "5B",
        "hall_number": 3
    }


def test_book_ticket(airplane_ticket_data, train_ticket_data, cinema_ticket_data):
    booking_system = BookingSystem()
    airplane_ticket = AirplaneTicket(**airplane_ticket_data)
    train_ticket = TrainTicket(**train_ticket_data)
    cinema_ticket = CinemaTicket(**cinema_ticket_data)

    booking_system.book_ticket(airplane_ticket)
    assert airplane_ticket in booking_system.get_ticket_list()
    booking_system.book_ticket(train_ticket)
    assert train_ticket in booking_system.get_ticket_list()
    booking_system.book_ticket(cinema_ticket)
    assert cinema_ticket in booking_system.get_ticket_list()


def test_cancel_booking(airplane_ticket_data, train_ticket_data, cinema_ticket_data):
    booking_system = BookingSystem()
    airplane_ticket = AirplaneTicket(**airplane_ticket_data)
    train_ticket = TrainTicket(**train_ticket_data)
    cinema_ticket = CinemaTicket(**cinema_ticket_data)

    booking_system.book_ticket(airplane_ticket)
    assert booking_system.cancel_booking(1) is True
    assert airplane_ticket not in booking_system.get_ticket_list()

    booking_system.book_ticket(train_ticket)
    assert booking_system.cancel_booking(2) is True
    assert train_ticket not in booking_system.get_ticket_list()

    booking_system.book_ticket(cinema_ticket)
    assert booking_system.cancel_booking(3) is True
    assert cinema_ticket not in booking_system.get_ticket_list()


def test_get_ticket(airplane_ticket_data, train_ticket_data, cinema_ticket_data):
    booking_system = BookingSystem()
    airplane_ticket = AirplaneTicket(**airplane_ticket_data)
    train_ticket = TrainTicket(**train_ticket_data)
    cinema_ticket = CinemaTicket(**cinema_ticket_data)

    booking_system.book_ticket(airplane_ticket)
    assert booking_system.get_ticket(1) == airplane_ticket
    assert booking_system.get_ticket(1).get_info() == airplane_ticket_data

    booking_system.book_ticket(train_ticket)
    assert booking_system.get_ticket(2) == train_ticket
    assert booking_system.get_ticket(2).get_info() == train_ticket_data

    booking_system.book_ticket(cinema_ticket)
    assert booking_system.get_ticket(3) == cinema_ticket
    assert booking_system.get_ticket(3).get_info() == cinema_ticket_data


def test_cancel_non_existing_booking():
    booking_system = BookingSystem()
    assert booking_system.cancel_booking(999) is False


def test_get_non_existing_ticket_info():
    booking_system = BookingSystem()
    assert booking_system.get_ticket(9999) is None
