import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()["iss_position"]["longitude"]
print(data)