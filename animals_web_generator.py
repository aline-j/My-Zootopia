import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('My-Zootopia/animals_data.json')


def get_animal_data():
    for animal in animals_data:
        name = animal['name']
        diet = animal['characteristics']['diet']
        location = animal['locations'][0]

        if 'type' in animal['characteristics']:
            animal_type = animal['characteristics']['type']
            print(f'Name: {name}')
            print(f'Diet: {diet}')
            print(f'Location: {location}')
            print(f'Type: {animal_type}')
        else:
            print(f'Name: {name}')
            print(f'Diet: {diet}')
            print(f'Location: {location}')
