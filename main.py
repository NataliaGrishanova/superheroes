import requests
import json

superheroes = ['Hulk', 'Captain America', 'Thanos']
token = 2619421814940190
url = 'https://www.superheroapi.com/api/'
best_intelligence = 0
superhero_name = 0

for superhero in superheroes:
    seach = url + str(token) + '/search/' + superhero
    response = requests.get(seach)
    response_json = response.json()

    intelligence = int(response_json['results'][0]['powerstats']['intelligence'])

    if intelligence > best_intelligence:
        best_intelligence = int(response_json['results'][0]['powerstats']['intelligence'])
        superhero_name = superhero

print(f'Самый умный супрегерой – это {superhero_name}. Его интеллект составляет {best_intelligence}.')