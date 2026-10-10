import pandas as pd
import matplotlib.pyplot as plt

measure_df = pd.read_csv('data/air_quality_krakow.csv', parse_dates=['times'])
measure_df['hour'] = measure_df['times'].dt.hour

hourly_mean = measure_df.groupby("hour")['pm10'].mean()
print(hourly_mean)


hourly_mean.plot()
plt.show()