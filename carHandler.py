import csv
import os
from uuid import uuid4
import json

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

files_to_create = [slow_cars, fast_cars, sport_cars, cheap_cars, medium_priced_cars, expensive_cars, audi_cars, volvo_cars]

path = "/output_data"
path_exists = os.path.exists(path)
path_slash = '/'

if not path_exists:
    os.makedirs(path)
else:
    for file in files_to_create:
        file_name = str(file.__str__())+'.json'
        path_final = path + path_slash
        path_to_file = os.path.join(path_final, file_name)
        with open(path_to_file, 'w') as json_file:
            json.dump(file, json_file)
