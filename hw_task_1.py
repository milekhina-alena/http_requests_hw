import requests
import json

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)

data = response.json()

with open('superheroes.json', 'w') as file:
    result = json.dump(data, file, indent=4)
    result

superheroes = {'hero_1': 'Hulk', 'hero_2': 'Captain America', 'hero_3': 'Thanos'}
intel_stats = {}
def find_intel(file):
    for hero in file:
        if hero['name'] == superheroes['hero_1']:
            intel_stats['Hulk'] = hero['powerstats']['intelligence']
        elif hero['name'] == superheroes['hero_2']:
            intel_stats['Captain America'] = hero['powerstats']['intelligence']
        elif hero['name'] == superheroes['hero_3']:
            intel_stats['Thanos'] = hero['powerstats']['intelligence']
    
with open('superheroes.json') as file:
    json_data = json.load(file)

find_intel(json_data)

# print(intel_stats)
max_intel = max(intel_stats)
print(f'Самый умный супергерой - {max_intel}, уровень его интеллекта = {intel_stats[max_intel]}.')
