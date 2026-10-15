from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import matplotlib.pyplot as plt
from db import get_engine


engine = get_engine()
connection = engine.connect()

# air_quality_df = pd.read_sql("SELECT COUNT(*) FROM pm10_daily_mean ORDER BY days", engine)
# air_quality_df['days'] = pd.to_datetime(air_quality_df['days'])
# air_quality_df.info()

show_query = text("""SELECT COUNT(*) FROM air_quality""")
res = connection.execute(show_query)
print(res.fetchall())

# air_quality_df.plot(x='days', y='pm10', kind='line')
# plt.show()

