import requests

address = 'https://api.open-meteo.com/v1/forecast?latitude=50.06&longitude=19.94&hourly=temperature_2m'

response = requests.get(address)

print(response.status_code)