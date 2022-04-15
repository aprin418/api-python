import requests

jsonUrl = 'http://127.0.0.1:3000'

response = requests.get(jsonUrl).json()

print(response)
