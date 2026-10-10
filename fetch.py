import requests
import pandas as pd

address = 'https://api.open-meteo.com/v1/forecast?latitude=50.06&longitude=19.94&hourly=temperature_2m'

response = requests.get(address)
data = response.json()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

measure_dict = {'times': times, 'temps': temps}

measure_df = pd.DataFrame(measure_dict)
measure_df['times'] = pd.to_datetime(measure_df['times'])
# print(measure_df.head())
measure_df.info()



