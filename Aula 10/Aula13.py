from urllib.request import urlopen
import json

resp = urlopen("http://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/items.json").read().decode('utf8')
data = json.loads(resp)[5]

print(data['name']['english'])