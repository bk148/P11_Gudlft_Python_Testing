import pytest
from server import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def info_clubs():
    data_clubs = {"name": "Simply Lift", "email": "john@simplylift.co", "points": 11, "zeroPoint": 0}
    return data_clubs


@pytest.fixture
def info_comp():
    data_competition = {"name": "Spring Festival", "date": "2020-03-27 10:00:00", "numberOfPlaces": 25}
    return data_competition


@pytest.fixture
def test_past_comp():
    return {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    }

