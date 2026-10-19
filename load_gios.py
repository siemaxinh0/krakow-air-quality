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
print(df_krakow.shape)
print(df_krakow.head(8))