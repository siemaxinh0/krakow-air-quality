from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import matplotlib.pyplot as plt
from db import get_engine
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


engine = get_engine()
connection = engine.connect()

air_quality_df = pd.read_sql("SELECT days, pm10 FROM pm10_daily_mean ORDER BY days", engine)
air_quality_df['days'] = pd.to_datetime(air_quality_df['days'])
today = pd.Timestamp.today().normalize()
air_quality_df = air_quality_df[air_quality_df['days'] < today]
air_quality_df['pm10_next_day'] = air_quality_df['pm10'].shift(-1)
air_quality_df['pm10_prev_day'] = air_quality_df['pm10'].shift(1)
print(f'Before dropna: {len(air_quality_df)}')
air_quality_df = air_quality_df.dropna(subset=['pm10_next_day', 'pm10_prev_day'])
print(f'After dropna: {len(air_quality_df)}')
diff = air_quality_df['pm10'] - air_quality_df['pm10_next_day']
print(air_quality_df.head(3))
mae = diff.abs().mean()
print(f'MAE (current day data as prediction for the next one):{mae}')
pm10_mean = air_quality_df['pm10'].mean()
print(f'Mean value of PM10: {pm10_mean}')
ratio = mae / pm10_mean
print(f'MAE / PM10 ratio: {ratio}')


pivot = int(len(air_quality_df) * 0.8)
print(pivot)
training_data = air_quality_df.iloc[:pivot]
test_data = air_quality_df.iloc[pivot:]
print(f'Training data length: {len(training_data)}')
print(f'Training data first day: {training_data["days"].iloc[0]}')
print(f'Training data last day: {training_data["days"].iloc[-1]}')
print(f'Test data length: {len(test_data)}')
print(f'Test data first day: {test_data["days"].iloc[0]}')
print(f'Test data last day: {test_data["days"].iloc[-1]}')

X_train = training_data[["pm10", "pm10_prev_day"]]
y_train = training_data["pm10_next_day"]

X_test = test_data[["pm10", "pm10_prev_day"]]
y_test = test_data["pm10_next_day"]

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(len(predictions))
print(y_test.head(3))
print(predictions[:3])

model_mae = mean_absolute_error(y_test, predictions)
baseline_mae_last_20_days = mean_absolute_error(y_test, X_test['pm10_prev_day'])
print(f'Linear regression model MAE (last 20 days): {model_mae}') 
print(f'Baseline MAE (last 20 days): {baseline_mae_last_20_days}')

print(model.coef_)
print(model.intercept_)

X_train_without_yesterday = X_train[["pm10"]]
X_test_without_yesterday = X_test[["pm10"]]

model_without_yesterday = LinearRegression()
model_without_yesterday.fit(X_train_without_yesterday, y_train)
predictions_without_yesterday = model_without_yesterday.predict(X_test_without_yesterday)

model_without_yesterday_mae = mean_absolute_error(y_test, predictions_without_yesterday)
print(f'Linear regression model without yesterday MAE (last 20 days): {model_without_yesterday_mae}')







