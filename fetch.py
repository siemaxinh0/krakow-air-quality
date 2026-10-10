import requests
import pandas as pd

address = 'https://air-quality-api.open-meteo.com/v1/air-quality?latitude=50.06&longitude=19.94&hourly=pm10&timezone=auto'

response = requests.get(address)
if response.status_code != 200:
    raise Exception(f"Error! Status code {response.status_code}")
data = response.json()

times = data["hourly"]["time"]
pm10 = data["hourly"]["pm10"]

measure_dict = {'times': times, 'pm10': pm10}

measure_df = pd.DataFrame(measure_dict)

measure_df['times'] = pd.to_datetime(measure_df['times'])

measure_df.info()




