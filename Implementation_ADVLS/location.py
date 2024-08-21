import json
from urllib.request import urlopen

url = "http://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)
x = data

print(data["ip"])
