import json


data = [
    {
        'name': 'apple', 
        'description': 'some apple', 
        'cost': 123
    },
    {
        'name': 'apple',
        'description': 'some apple',
        'cost': 123
    },
    {
        'name': 'apple',
        'description': 'some apple',
        'cost': 123
    },
]

with open('json/data.json', 'w') as file:
    json.dump(data, file, sort_keys=True, indent=2)


with open('json/data.json') as file:
    print(
        type(
            json.load(file)
        )
    )
