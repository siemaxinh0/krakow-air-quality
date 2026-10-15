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
print(len(air_quality_df))
air_quality_df = air_quality_df.dropna(subset=['pm10_next_day'])
print(len(air_quality_df))
print(air_quality_df.tail(3))



