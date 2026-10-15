from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
from db import get_engine

engine = get_engine()
connection = engine.connect()

create_table_query = text("""CREATE TABLE IF NOT EXISTS air_quality (
times TIMESTAMP PRIMARY KEY,
pm10 FLOAT)""")
connection.execute(create_table_query)
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

print(f"Loaded {len(rows)} rows!")
connection.close()