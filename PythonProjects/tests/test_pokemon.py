import requests
import pytest

host = 'https://api.pokemonbattle.ru/v2/'
token = 'ff6f59eaf24d4ca03e2155094558141e'
Header = {'Content-Type': 'application/json', 'trainer_token': token}

TRAINER_ID = '17918'



def test_status_code(): 
    response = requests.get(url = f'{host}pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response(): 
    response_get = requests.get(url = f'{host}pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]["name"] == 'Alanis'

@pytest.mark.parametrize('key, value', [('name', 'Alanis'), ('trainer_id', TRAINER_ID), ('id','154888')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url = f'{host}pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value







