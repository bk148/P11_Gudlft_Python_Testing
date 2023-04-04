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

