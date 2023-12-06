from requests import Session
import json

from flask import Flask, request

from function import reserve_seats


def create_app():
    app = Flask("ticket_office")

    @app.post("/reserve")
    def reserve():
        payload = request.json
        seat_count = payload["count"]
        train_id = payload["train_id"]

        session = Session()

        booking_reference = session.get(
            "http://localhost:8082/booking_reference").text

        train_data = session.get(
            f"http://localhost:8081/data_for_train/" + train_id
        ).json()

        reservation_payload, reservation = reserve_seats(
            train_data, seat_count, train_id, booking_reference)

        response = session.post(
            "http://localhost:8081/reserve",
            json=reservation_payload,
        )
        assert response.status_code == 200, response.text
        response = response.json()

        return json.dumps(reservation)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8083)
