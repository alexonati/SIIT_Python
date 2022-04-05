import csv
import json
import os
from uuid import uuid4

with open('input.csv', 'r') as csv_file:
    rows = csv.reader(csv_file, delimiter=';')
    cars_data = list(rows)
    keys = list(cars_data[0])
    keys.insert(0, 'UUID')
    keys = tuple(keys)
    values = cars_data[1:]
    for value in values:
        uuid = str(uuid4())
        value.insert(0, uuid)
    cars = []
    for item in cars_data:
        for value in values:
            car = dict(zip(keys, value))
            cars.append(car)

slow_cars = [car for car in cars if int(car['HP']) < 120]
fast_cars = [car for car in cars if 120 <= int(car['HP']) < 180]
sport_cars = [car for car in cars if int(car['HP']) >= 180]

cheap_cars = [car for car in cars if int(car['PRICE']) < 1000]
medium_priced_cars = [car for car in cars if 1000 <= int(car['PRICE']) < 5000]
expensive_cars = [car for car in cars if int(car['PRICE']) >= 1000]

audi_cars = [car for car in cars if car['MAKE'] == 'Audi']
volvo_cars = [car for car in cars if car['MAKE'] == 'Volvo']

path = "./output_data"
path_exists = os.path.exists(path)

if not path_exists:
    os.makedirs(path)

with open(os.path.join('output_data', 'slow_cars.json'), 'w') as json_file:
    json.dump(slow_cars, json_file, indent=4)
with open(os.path.join('output_data', 'fast_cars.json'), 'w') as json_file:
    json.dump(fast_cars, json_file, indent=4)
with open(os.path.join('output_data', 'sport_cars.json'), 'w') as json_file:
    json.dump(sport_cars, json_file, indent=4)
with open(os.path.join('output_data', 'cheap_cars.json'), 'w') as json_file:
    json.dump(cheap_cars, json_file, indent=4)
with open(os.path.join('output_data', 'medium_cars.json'), 'w') as json_file:
    json.dump(medium_priced_cars, json_file, indent=4)
with open(os.path.join('output_data', 'expensive_cars.json'), 'w') as json_file:
    json.dump(expensive_cars, json_file, indent=4)
with open(os.path.join('output_data', 'audi_cars.json'), 'w') as json_file:
    json.dump(audi_cars, json_file, indent=4)
with open(os.path.join('output_data', 'volvo_cars.json'), 'w') as json_file:
    json.dump(volvo_cars, json_file, indent=4)

# an improvement would be to find a way to have the .json files names generated
# dynamically based on the name of the variable that holds them in the following list
# fx. to have a for loop for the items in the list where a path variable changes depending on the name of the item
# as far as I could research this cannot be done easily
files_to_create = [slow_cars, fast_cars, sport_cars, cheap_cars, medium_priced_cars, expensive_cars, audi_cars,
                   volvo_cars]
