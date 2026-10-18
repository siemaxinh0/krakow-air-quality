Project related to air quality measurements in Kraków, Poland.

## Data
Data from open-meteo.com, fetched via its API. It covers 92 past days plus 5 days of forecast. The database grows by about 24 rows per day.
All values, including historical ones, are model estimates, not station measurements.
Some PM10 values are occasionally missing (stored as NULL). The CSV file holds only the latest window returned by the API, while the database keeps everything ever downloaded.

## Pipeline
- fetch.py downloads data from the API and saves it as a CSV file.
- load.py loads CSV and injects the data into PostgreSQL database (launched in Docker), overwriting hours that are already in the table and adding new ones
- After loading the hourly data, load.py also fills pm10_daily_mean: it averages PM10 over all available hours of each day. Missing (NULL) hours are ignored, so a day may be based on fewer than 24 values.
- Database works on port 5433, because 5432 is sometimes occupied by local Postgres.
- The pipeline is run manually with run_pipeline.ps1, because the database runs locally in Docker. Docker Desktop must be running first.

## Observations
While analyzing the charts, I observed an increase in PM10 from September to October.
Average PM10 by hour of day is lowest around 3 PM and highest around 10-11 PM, with a small peak around 7-8 AM.

## Hypotheses
An increase in PM10 might be related to the start of the heating season, but it's only my hypothesis, which I didn't check. Another hypothesis is that the small peak around 7-8 AM is triggered by high traffic caused by people commuting to work.

## Results
I wanted to predict the next day's value of PM10. The baseline predicts that tomorrow's value equals today's. I implemented a simple linear regression model to predict next day's PM10 value, whose basic version used two features: today's and yesterday's PM10. I also tried removing the previous-day feature, but the MAE was practically unchanged. Another experiment included information if the current day is part of the weekend but it did not noticeably improve the predictions either. All linear regression variants beat the baseline. However, the dataset is small (20 test days, one season), so I cannot tell whether the features help at all.

Results as of 2026-10-18. Training: 12 Jul - 26 Sep, test: 27 Sep - 16 Oct, 20 days.

| Model | MAE |
|---|---|
| Baseline | 13.90 |
| Regression (today, yesterday) | 9.81 | 
| Regression (only today) | 9.81 |
| Regression (today, yesterday, is_weekend) | 9.69 | 






