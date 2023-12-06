
def get_available_seats(train_data):
    available_seats = (
        s
        for s in train_data["seats"].values()
        if s["coach"] == "A" and not s["booking_reference"]
    )
    return available_seats


def reserve_seats(train_data, seat_count, train_id, booking_reference):
    available_seats = get_available_seats(train_data)
    to_reserve = []
    for i in range(seat_count):
        to_reserve.append(next(available_seats))

    seat_ids = [s["seat_number"] + s["coach"] for s in to_reserve]
    reservation = {
        "train_id": train_id,
        "booking_reference": booking_reference,
        "seats": seat_ids,
    }

    reservation_payload = {
        "train_id": reservation["train_id"],
        "seats": reservation["seats"],
        "booking_reference": reservation["booking_reference"],
    }
    return reservation_payload, reservation
