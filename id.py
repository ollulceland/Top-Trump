import random
import requests


url = 'https://swapi.dev/api/starships/#/'
response = requests.get(url)
starwars = response.json()
print(starwars)
