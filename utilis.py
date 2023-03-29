import json


def read(file, data_type):
    with open(file) as f:
        data = json.load(f)[data_type]

        return data
