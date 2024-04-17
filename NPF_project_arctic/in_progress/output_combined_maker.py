import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Read files
df1 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\raw_data\\ar_chem_2010_2021_ppb.csv')
df2 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\raw_data\\14_NPF_date_summary.csv')
df3 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\raw_data\\ar_aws_2015_2021.csv')
df4 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\raw_data\\ar_srad_2013_2021.csv')
df5 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\raw_data\\14_PM_gas.csv')
df7 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\raw_data\\CS_pm10_pm25.csv')

# Trim df4 by columns
df4_selected = df4.drop(columns=["DIR", "DIF", "LWD", "SWU", "LWU", "temperature", "RH", "pressure", "net.irr"])
df4 = df4_selected

# Convert df4 from hourly to daily
df4['date'] = pd.to_datetime(df4['date']).dt.strftime('%Y/%m/%d')
df4_new = df4.groupby('date').mean()
df4 = df4_new.reset_index()
df4['date'] = pd.to_datetime(df4['date'])

# Conversion of df5 and trimming by dates
df5['date'] = pd.to_datetime(df5['date'])
res_temp_df5 = df5[~(df5['date'] < '2016/10/1')]
res_df5 = res_temp_df5[~(res_temp_df5['date'] > '2020/2/1')]
df5 = res_df5

# Prepare df7 for df6
df7_selected = df7.drop(columns=["pm10", "pm25"])
df7 = df7_selected
df7 = df7.drop(df7.columns[0], axis=1)
df7['date'] = pd.to_datetime(df7['date'])
df7 = df7.dropna()

# df6 generation
df6 = pd.DataFrame({'date': df5['date'], 'CS': None})
# Add pm10 column to df6
df6['pm10'] = df5['pm10']
filename = 'CS_pm10_regression_model.sav'
loaded_model = joblib.load(filename)
X = df6[['pm10']]
y = df6['CS']
y_predict = loaded_model.predict(X)
df6['CS'] = y_predict

# Merge df6 and df7
df6 = pd.merge(df6, df7[['date', 'CS']], on='date', how='left', suffixes=('_df6', '_df7'))
df6['CS'] = df6['CS_df7'].combine_first(df6['CS_df6']).astype(float)
df6 = df6.drop(['CS_df6', 'CS_df7'], axis=1)
df6 = df6.drop(columns=["pm10"])

# Plotting
plt.scatter(df6['date'], df6['CS'], label='Actual Data')
plt.title('date vs CS')
plt.xlabel('date')
plt.ylabel('CS')
plt.legend()
plt.grid(True)
plt.show()

# Trimming df5 by columns
df5_selected = df5.drop(columns=["so2", "o3", "no2", "hno3"])
df5 = df5_selected

# Trim df4 by dates
res_temp_df4 = df4[~(df4['date'] < '10/1/2016')]
res_df4 = res_temp_df4[~(res_temp_df4['date'] > '1/2/2020')]
df4 = res_df4


# Convert df3 from hourly to daily
df3['date'] = pd.to_datetime(df3['date']).dt.strftime('%Y/%m/%d')
df3_new = df3.groupby('date').mean()
df3 = df3_new.reset_index()
df3['date'] = pd.to_datetime(df3['date'])

# Trim df3 by years (2016-2020)
res_temp_df3 = df3[~(df3['date'] < '10/1/2016')]
res_df3 = res_temp_df3[~(res_temp_df3['date'] > '1/2/2020')]
df3 = res_df3

# Trim df3 by columns
df3_selected = df3.drop(columns=["wd", "ws"])
df3 = df3_selected

# Trim df1 and df2 by years (2016-2020)
df2_selected = df2.drop(columns=["coverage"])
df2 = df2_selected
df1['date'] = pd.to_datetime(df1['date'])
df2['date'] = pd.to_datetime(df2['date'])

res_temp_df1 = df1[~(df1['date'] < '10/1/2016')]
res_df1 = res_temp_df1[~(res_temp_df1['date'] > '1/2/2020')]
df1 = res_df1

# Conversion into Y-m-d
df1['date'] = pd.to_datetime(df1['date']).dt.strftime('%Y/%m/%d')
df2['date'] = pd.to_datetime(df2['date']).dt.strftime('%Y/%m/%d')
df3['date'] = pd.to_datetime(df3['date']).dt.strftime('%Y/%m/%d')
df4['date'] = pd.to_datetime(df4['date']).dt.strftime('%Y/%m/%d')
df5['date'] = pd.to_datetime(df5['date']).dt.strftime('%Y/%m/%d')
df6['date'] = pd.to_datetime(df6['date']).dt.strftime('%Y/%m/%d')

df1_selected = df1[["date", "NH3", "NH4", "HNO3", "SO4", "SO2"]].copy()
df1 = df1_selected

merged_data = pd.merge(df1, df2, how='outer', on='date')

merged_data_new = pd.merge(merged_data, df3, how='outer', on='date')
merged_data_new_new = pd.merge(merged_data_new, df4, how='outer', on='date')
merged_data_new_new_new = pd.merge(merged_data_new_new, df5, how='outer', on='date')
merged_data_new_new_new_new = pd.merge(merged_data_new_new_new, df6, how='outer', on='date')
result = merged_data_new_new_new_new
result = result.drop(result.tail(31).index)
result.to_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\in_progress\\output_combined.csv')
