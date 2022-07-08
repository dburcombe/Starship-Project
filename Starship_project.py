import requests
from pprint import pprint

def API_Call_Ships():

    url = "https://swapi.dev/api/starships/?page=1"
    ship_list = []

    while True:
        response = requests.request("GET", url)
        data = response.json()
        url = data["next"]
        for ships in data["results"]:
            ship_list.append(ships)
        if data["next"] is None:
            break

    return ship_list

pprint(API_Call_Ships())

def API_Call_Pilots():

    pilot_list = []
    ships_data = API_Call_Ships()

    for ship in ships_data:
        for pilot in ship['pilots']:
                pilot_data = requests.get(pilot)
                pilot_info = pilot_data.json()
                pilot_name = pilot_info['name']
                pilot_list.append(pilot_name)

    return pilot_list

pprint(API_Call_Pilots())

















































