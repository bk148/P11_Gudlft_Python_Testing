import os
import pytest
import server
from flask import template_rendered
from server import create_app


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CHROME_DRIVER_PATH = os.path.join(ROOT_DIR, '../chromedriver.exe')

def info_club():
    return [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "30",
            "reservations": {
                "Spring Festival": "0",
                "Fall Classic": "0",
                "Summer Festival 2022": "0"
            }
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4",
            "reservations": {
                "Spring Festival": "0",
                "Fall Classic": "0",
                "Summer Festival 2022": "0"
            }
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12",
            "reservations": {
                "Spring Festival": "0",
                "Fall Classic": "0",
                "Summer Festival 2022": "0"
            }
        }
    ]


def info_comp():
    return [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "20"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Summer Festival 2022",
            "date": "2022-06-22 13:30:00",
            "numberOfPlaces": "23"
        }
    ]


@pytest.fixture
def app(mocker):
    mocker.patch.object(server, "COMPETITIONS", info_comp())
    mocker.patch.object(server, "CLUBS", info_club())
    return create_app({"TESTING": True})


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
