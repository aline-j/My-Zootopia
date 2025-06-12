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
    for animal_data in animals_data:
        # append information to each string
        output += '<li class="cards__item">'
        output += f"Name: {animal_data['name']}<br/>\n"
        output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
        output += f"Location: {animal_data['locations'][0]}<br/>\n"
        if 'type' in animal_data['characteristics']:
            output += f"Type: {animal_data['characteristics']['type']}<br/>\n"
        else:
            continue
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
