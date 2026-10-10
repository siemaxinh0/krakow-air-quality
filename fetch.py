import requests
import pandas as pd

address = 'https://api.open-meteo.com/v1/forecast?latitude=50.06&longitude=19.94&hourly=temperature_2m'

response = requests.get(address)
data = response.json()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]
print(type(times))
print(times[0])
print(type(times[0]))
print(type(temps[0]))
