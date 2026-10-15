from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import matplotlib.pyplot as plt
from db import get_engine


engine = get_engine()
connection = engine.connect()

air_quality_df = pd.read_sql("SELECT days, pm10 FROM pm10_daily_mean ORDER BY days", engine)
air_quality_df['days'] = pd.to_datetime(air_quality_df['days'])
today = pd.Timestamp.today().normalize()
air_quality_df = air_quality_df[air_quality_df['days'] < today]
air_quality_df['pm10_next_day'] = air_quality_df['pm10'].shift(-1)
air_quality_df['pm10_prev_day'] = air_quality_df['pm10'].shift(1)
print(f'Before dropna: {len(air_quality_df)}')
air_quality_df = air_quality_df.dropna(subset=['pm10_next_day', 'pm10_prev_day'])
print(f'After dropna: {len(air_quality_df)}')
diff = air_quality_df['pm10'] - air_quality_df['pm10_next_day']
print(air_quality_df.head(3))
mae = diff.abs().mean()
print(f'MAE:{mae}')
pm10_mean = air_quality_df['pm10'].mean()
print(f'Mean value of PM10: {pm10_mean}')
ratio = mae / pm10_mean
print(f'MAE / PM10 ratio: {ratio}')




