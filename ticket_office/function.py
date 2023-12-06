
def get_available_seats(seats):
    available_seats = [
        seat
        for seat in seats
        if seat.coach == "A" and not seat.booking_reference
    ]
    return available_seats


def reserve_seats(train, booking_reference):
    available_seats = get_available_seats(train.train_data)
    to_reserve = []
    for i in range(train.seat_count):
        to_reserve.append(next(available_seats))

    seat_ids = [s["seat_number"] + s["coach"] for s in to_reserve]
    reservation = {
        "train_id": train.train_id,
        "booking_reference": booking_reference,
        "seats": seat_ids,
    }

    reservation_payload = {
        "train_id": reservation["train_id"],
        "seats": reservation["seats"],
        "booking_reference": reservation["booking_reference"],
    }
    return reservation_payload, reservation
