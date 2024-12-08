import requests
host = 'https://api.pokemonbattle.ru/v2/'
token = 'ff6f59eaf24d4ca03e2155094558141e'
Header = {'Content-Type': 'application/json', 'trainer_token': token}

body_create = {
    "name": "Gena",
    "photo_id": "702"
}

body_changename = {
    "pokemon_id": "154881",
    "name": "Mimi"
}

body_inpokeboll = {
    "pokemon_id": "154881"
}


response_create = requests.post(url = f'{host}pokemons', headers = Header, json = body_create )
print(response_create.text)

response_changename = requests.patch(url = f'{host}pokemons', headers= Header, json = body_changename)
print(response_changename.text)

response_inpokeboll = requests.post(url = f'{host}trainers/add_pokeball', headers= Header, json = body_inpokeboll)
print(response_inpokeboll.text)