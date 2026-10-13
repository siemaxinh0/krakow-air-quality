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

create_table_query = text("""CREATE TABLE IF NOT EXISTS air_quality (
times TIMESTAMP PRIMARY KEY,
pm10 FLOAT)""")
connection.execute(create_table_query)
connection.commit()

create_daily_table_query = text("""CREATE TABLE IF NOT EXISTS pm10_daily_mean (
days DATE PRIMARY KEY,
pm10 FLOAT)""")
connection.execute(create_daily_table_query)
connection.commit()

measure_df = pd.read_csv('data/air_quality_krakow.csv',parse_dates=['times'])
rows = measure_df.to_dict("records")

for row in rows:
    if pd.isna(row["pm10"]):
        row["pm10"] = None

insert_query = text("""INSERT INTO air_quality (times, pm10) VALUES (:times, :pm10)
ON CONFLICT (times) DO UPDATE SET pm10 = EXCLUDED.pm10""")
connection.execute(insert_query, rows)
connection.commit()

insert_daily_query = text("""INSERT INTO pm10_daily_mean (days, pm10) SELECT CAST(times AS DATE) as days, AVG(pm10) AS pm10 FROM air_quality GROUP BY days
ON CONFLICT (days) DO UPDATE SET pm10 = EXCLUDED.pm10""")
connection.execute(insert_daily_query)
connection.commit()


print(f"Loaded {len(rows)} rows!")
connection.close()