import json
import requests

url = 'http://data.cityofnewyork.us/resource/7x9x-zpz6.json'
response = requests.get(url).content

incidents = json.loads(response)

print incidents[0]['lat_lon']['coordinates'][0]