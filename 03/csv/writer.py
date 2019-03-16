import csv

data = [
    ['name', 'description', 'cost'],
    ['apple', 'Some, apple', '100', ],
    ['potato', '"some POTATO"', '200'],
    ['Onion', "some 'onion'", '300'],
]

dict_data = [
    {
        'name': 'apple',
        'description': 'Some, apple',
        'cost': '100'
    }
]

with open('csv/data.csv', 'w') as file:
    # writer = csv.writer(file)
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)
    # for row in data:
    #     writer.writerow(row)


with open('csv/dict_data.csv', 'w') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['name', 'description', 'cost'],
        quoting=csv.QUOTE_NONNUMERIC
    )
    writer.writeheader()
    for itm in dict_data:
        writer.writerow(itm)
