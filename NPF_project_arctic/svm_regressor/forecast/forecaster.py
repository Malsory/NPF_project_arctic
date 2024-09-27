import pandas as pd
import joblib

best_model = joblib.load('best_model.pkl')
X_test = pd.read_csv(r'forecast.csv')
X_test['date'] = pd.to_datetime(X_test['date'])
X_test = X_test.set_index('date').resample('60min').mean().reset_index()
X_test = X_test.dropna()
dates = X_test[['date']].copy()
X_test = X_test.drop(columns=['date'])
predictions = best_model.predict(X_test)

predictions_df = pd.DataFrame(predictions)
predictions_df.reset_index(drop=True, inplace=True)
predictions_df['date'] = dates[['date']].copy()
predictions_df.to_csv('forecasts_df.csv')