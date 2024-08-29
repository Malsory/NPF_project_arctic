import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.dates as mdates
from scipy.ndimage import gaussian_filter

# df1 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\misc\\output_combined.csv')
# df1['date'] = pd.to_datetime(df1['date'])
# df1.set_index('date', inplace=True)
# df1 = df1.resample('H').ffill()
# df1.reset_index(drop=False, inplace=True)
# print(df1.columns)

# df1.to_csv('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\misc\\output_combined_h.csv')

df1 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\misc\\smps_output_combined.csv')
df2 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\misc\\output_combined_h.csv')
df1['date'] = pd.to_datetime(df1['date'])
df2['date'] = pd.to_datetime(df2['date'])
# df2 = df2.drop(columns='Unnamed: 0')
merged_df = pd.merge(df1, df2, on='date', how='outer')
print(merged_df)
merged_df.to_csv('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\misc\\smps_output_combined_test.csv')
 
# df1 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_urban\\NPF_project_urban\\rf_regressor\\total_2024.csv')
# df2 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_urban\\NPF_project_urban\\rf_regressor\\data.csv')
# df3 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_urban\\NPF_project_urban\\rf_regressor\\smps_output_combined_test.csv')
# # df2 = df2[['date', 'day.type']].copy()
# df1['date'] = pd.to_datetime(df1['date'])
# df2['date'] = pd.to_datetime(df2['date'])
# df1.reset_index(drop=True, inplace=True)
# df2.reset_index(drop=True, inplace=True)
# df1 = df1.drop(df1.columns[df1.columns.str.contains('Unnamed')], axis=1)
# df2 = df2.drop(df2.columns[df2.columns.str.contains('Unnamed')], axis=1)
# df1 = df1.set_index('date').resample('60min').mean().reset_index()
# df1 = df1.dropna()
# merged_df = pd.merge(df1, df2, on='date', how='outer')
# merged_df = merged_df.dropna()
# print(merged_df)

# filtered_df1 = merged_df[~merged_df['date'].isin(df3['date'])]
# min_date = pd.to_datetime('2024-07-01')
# max_date = pd.to_datetime('2024-12-31')
# filtered_df1 = filtered_df1[(filtered_df1['date'] >= min_date) & (filtered_df1['date'] <= max_date)]
# filtered_df1['date'] = pd.to_datetime(filtered_df1['date'])
# print(filtered_df1)
# filtered_df1.to_csv('C:\\Users\\Masloriy\\Desktop\\NPF_project_urban\\NPF_project_urban\\rf_regressor\\test_set.csv')
