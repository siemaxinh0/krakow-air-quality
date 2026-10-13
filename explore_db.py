import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

load_dotenv()
password = os.getenv("POSTGRES_PASSWORD") # wyciagniecie hasla do bazy z .env

address = f'postgresql+psycopg://postgres:{password}@localhost:5433/postgres'

engine = create_engine(address)
connection = engine.connect()

air_quality_df = pd.read_sql("SELECT * FROM pm10_daily_mean ORDER BY days", engine)
air_quality_df['days'] = pd.to_datetime(air_quality_df['days'])
print(air_quality_df)

