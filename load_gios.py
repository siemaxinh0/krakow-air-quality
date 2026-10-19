import pandas as pd

df = pd.read_excel("data/gios/2024_PM10_1g.xlsx", header=None)
stations = df.iloc[5]
mask = stations.astype(str).str.startswith("MpKrak")
mask[0] = True
df_krakow = df.loc[:, mask]
names = df_krakow.iloc[1]
df_krakow = df_krakow.iloc[6:]
df_krakow.columns = names
df_krakow = df_krakow.reset_index(drop=True)
df_krakow.columns.name = None
df_krakow = df_krakow.rename(columns={"Kod stacji":"times"})
columns_with_numbers = df_krakow.columns[1:]
df_krakow[columns_with_numbers] = df_krakow[columns_with_numbers].astype(float)
df_krakow['times'] = pd.to_datetime(df_krakow['times'])

df_krakow = df_krakow.melt(id_vars="times", var_name="station", value_name="pm10")
df_krakow['times'] = df_krakow['times'] - pd.Timedelta(hours=1)

print(df_krakow['times'].iloc[-1])

print(df_krakow.head(3))
df_krakow.info()