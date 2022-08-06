import json
from vars import districts,cities


def filter_cities():
    f = open('../data/cities.json')
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    cities = {}
    with open('cities_filtered.json', 'w', encoding='utf8') as json_file:
        for row in data:
            id = row["id"]
            del row["id"]
            cities[id] = row
        json.dump(cities, json_file, ensure_ascii=False)

def filter_districts():
    f = open('../data/districts.json')
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    districts = {}
    with open('districts_filtered.json', 'w', encoding='utf8') as json_file:
        for row in data:
            id = row["id"]
            cityId = row["value"]
            try:
                city = cities[cityId]
            except:
                # no city found
                city = None
            del row["id"]
            row["city_data"] = city
            districts[id] = row
        json.dump(districts, json_file, ensure_ascii=False)

filter_districts()