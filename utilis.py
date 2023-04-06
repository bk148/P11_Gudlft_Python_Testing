from datetime import datetime
import json


def change(file, data_type):
    with open(file) as f:
        data = json.load(f)[data_type]

        return data


def points_mis_a_jour(points: str, places: str, id_club: int, id_comp=int):

    with open('clubs.json') as f:
        data = json.load(f)
        data['clubs'][id_club]['points'] = points
        json.dump(data, open('clubs.json', 'w'), indent=4)

    with open('competitions.json') as f:
        data = json.load(f)
        data['competitions'][id_comp]['numberOfPlaces'] = places
        json.dump(data, open('competitions.json', 'w'), indent=4)


def past_competition_updated(competitions: list) -> list:
    past_comp = []
    date_format = "%Y-%m-%d %H:%M:%S"
    for comp in competitions:
        comp['date'] = datetime.strptime(comp["date"], date_format)
        try:
            if comp['date'] < datetime.now():
                comp['past'] = True
                past_comp.append(comp)
            else:
                past_comp.append(comp)
        except ValueError:
            past_comp.append(comp)
    return past_comp






