import json


def load_data(file_path):
    """
    Loads a JSON file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def get_animal_data():
    """
    Formats animal data into a plain text block,
    with each animal's info on separate lines.
    """
    output = ''  # define an empty string
    for animal_obj in animals_data:
        # append information to each string
        output += serialize_animal(animal_obj)
    return output


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<div class="card__text">'
    output += '<ul>'
    output += f'<li><strong>Diet: </strong> {animal_obj["characteristics"]["diet"]}</li>'
    output += f'<li><strong>Location: </strong> {animal_obj["locations"][0]}</li>'
    if 'type' in animal_obj['characteristics']:
        output += f'<li><strong>Type: </strong> {animal_obj["characteristics"]["type"]}</li>'
    output += f'<li><strong>Class: </strong> {animal_obj["taxonomy"]["class"]}</li>'
    if 'name_of_young' in animal_obj['characteristics']:
        output += f'<li><strong>Name of young: </strong> {animal_obj["characteristics"]["name_of_young"]}</li>'
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


output = get_animal_data()

# Read the HTML template
with open('animals_template.html', 'r') as htmlfile:
    template = htmlfile.read()

# Replace placeholder with animal info
final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

# Write the final HTML
with open('animals.html', 'w') as newhtmlfile:
    newhtmlfile.write(final_html)
