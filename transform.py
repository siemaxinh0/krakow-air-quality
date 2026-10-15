from db import get_engine
from sqlalchemy import text

engine = get_engine()
connection = engine.connect()

create_daily_table_query = text("""CREATE TABLE IF NOT EXISTS pm10_daily_mean (
days DATE PRIMARY KEY,
pm10 FLOAT)""")
connection.execute(create_daily_table_query)
connection.commit()

insert_daily_query = text("""INSERT INTO pm10_daily_mean (days, pm10) SELECT CAST(times AS DATE) as days, AVG(pm10) AS pm10 FROM air_quality GROUP BY days
ON CONFLICT (days) DO UPDATE SET pm10 = EXCLUDED.pm10""")
connection.execute(insert_daily_query)
connection.commit()

connection.close()