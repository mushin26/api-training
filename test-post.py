import requests
import json

headers = {"content-type": "application/json"}
payload = json.dumps({ "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
url = "https://api.restful-api.dev/objects/1"
r = requests.put(url, data=payload, headers=headers)

print(r.content)
