import pandas as pd
import matplotlib.pyplot as plt

measure = pd.read_csv('data/air_quality_krakow.csv', parse_dates=['times'])

measure.info()

measure.plot(x='times', y='pm10')
plt.show()