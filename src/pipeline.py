import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor


class DateTimeFeatures:
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X['datetime'] = pd.to_datetime(X['datetime'])

        X['hour'] = X['datetime'].dt.hour
        X['day'] = X['datetime'].dt.day
        X['month'] = X['datetime'].dt.month
        X['weekday'] = X['datetime'].dt.weekday

        return X.drop(columns=['datetime'])


def create_pipeline():
    pipeline = Pipeline(steps=[
        ("datetime_features", DateTimeFeatures()),
        ("scaler", StandardScaler()),
        ("model", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    return pipeline
"""{
  "datetime": "2011-01-01 00:00:00",
  "season": 1,
  "holiday": 0,
  "workingday": 0,
  "weather": 1,
  "temp": 9.84,
  "atemp": 14.365,
  "humidity": 81,
  "windspeed": 0,
    "casual": 3,
    "registered": 13
}"""

# cd c:\Users\ag225\Desktop\project\akash\akash\bike-demand-ml
# .venv\Scripts\python.exe -m uvicorn api.app:app --reload --host 127.0.0.1 --port 8000