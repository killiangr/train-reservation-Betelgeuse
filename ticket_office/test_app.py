import json
import requests

from function import get_available_seats


def test_reserve_seats_from_empty_train():
    train_id = "express_2000"

    session = requests.Session()
    response = session.post(f"http://127.0.0.1:8081/reset/{train_id}")
    response.raise_for_status()

    response = session.post(
        "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 4}
    )

    assert response.status_code == 200, response.text
    reservation = response.json()
    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["1A", "2A", "3A", "4A"]


def test_reserve_four_additional_seats():
    train_id = "express_2000"

    session = requests.Session()
    response = session.post(f"http://127.0.0.1:8081/reset/{train_id}")
    response.raise_for_status()

    response = session.post(
        "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 4}
    )
    assert response.status_code == 200, response.text

    response = session.post(
        "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 4}
    )
    assert response.status_code == 200, response.text
    reservation = response.json()
    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["5A", "6A", "7A", "8A"]


def test_get_available_seats():
    # Mock train_data for testing
    train_data = {
        "seats": {
            "1A": {"seat_number": 1, "coach": "A", "booking_reference": None},
            "2A": {"seat_number": 2, "coach": "A", "booking_reference": "ABC123"},
            "3A": {"seat_number": 3, "coach": "A", "booking_reference": None},
        }
    }

    result = list(get_available_seats(train_data))

    # Check that only seats without booking_reference are returned
    expected_result = [
        {"seat_number": 1, "coach": "A", "booking_reference": None},
        {"seat_number": 3, "coach": "A", "booking_reference": None},
    ]

    assert result == expected_result
