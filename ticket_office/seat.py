from dataclasses import dataclass


@dataclass
class Seat:
    seat_number: int
    coach: str
    booking_reference: str
