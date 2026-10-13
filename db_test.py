import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

load_dotenv()
password = os.getenv("POSTGRES_PASSWORD") # wyciagniecie hasla do bazy z .env

address = f'postgresql+psycopg://postgres:{password}@localhost:5433/postgres'

engine = create_engine(address)

print(engine)

connection = engine.connect()
print("Connected!")

create_table_query = text("""CREATE TABLE IF NOT EXISTS air_quality (
times TIMESTAMP PRIMARY KEY,
pm10 FLOAT)""")
connection.execute(create_table_query)
connection.commit()

measure_df = pd.read_csv('data/air_quality_krakow.csv',parse_dates=['times'])
rows = measure_df.to_dict("records")
# measure_df.to_sql("air_quality", engine, if_exists="append", index=False)

print(rows[0])


for row in rows:
    if pd.isna(row["pm10"]):
        row["pm10"] = None

insert_query = text("""INSERT INTO air_quality (times, pm10) VALUES (:times, :pm10)
ON CONFLICT (times) DO UPDATE SET pm10 = EXCLUDED.pm10""")
connection.execute(insert_query, rows)
connection.commit()

res = connection.execute(text("SELECT COUNT(*) FROM air_quality WHERE pm10 IS NULL"))
print(res.fetchall())
connection.close()