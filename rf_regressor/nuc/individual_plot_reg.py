import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.dates as mdates
from scipy.ndimage import gaussian_filter
import matplotlib.colors as mcolors

colors1 = [(0, 'blue'),
          (0.0001, 'powderblue'),
          (0.005, 'lightblue'),
          (0.015, 'green'),
          (0.045, 'yellow'),
          (0.07, 'orange'),
          (0.09, 'red'),
          (0.15, 'darkred'),
          (1, 'maroon')]

colors2 = [(0, 'blue'),
          (0.0598, 'powderblue'),
          (0.0599, 'lightblue'),
          (0.06, 'green'),
          (0.095, 'yellow'),
          (0.11, 'orange'),
          (0.2, 'red'),
          (0.22, 'darkred'),
          (1, 'maroon')]

custom_cmap1 = LinearSegmentedColormap.from_list('custom_cmap', colors1)
custom_cmap2 = LinearSegmentedColormap.from_list('custom_cmap', colors2)

df1 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\nuc\\y_test_df.csv')
df1['date'] = pd.to_datetime(df1['date'])
df1.reset_index(drop=True, inplace=True)
df1 = df1.drop(df1.columns[df1.columns.str.contains('Unnamed')], axis=1)

df_orig = df1.copy()
df_orig = df_orig.drop(columns=['date'])

df1 = df1.set_index('date').resample('60min').mean().reset_index()

min_date = pd.to_datetime('2019-06-01')
max_date = pd.to_datetime('2019-09-01')

df1 = df1[(df1['date'] >= min_date) & (df1['date'] <= max_date)]
df1['date'] = pd.to_datetime(df1['date'])

X = df1.drop(columns=["date"])
date = df1['date']
X = X.abs()
X = X.astype(np.float32)
df1 = X.copy()

min_date = date.min()
max_date = date.max()
min_date_str = min_date.strftime('%Y-%m-%d')
max_date_str = max_date.strftime('%Y-%m-%d')

# def round_to_nearest_five(x):
#     return 2 * round(x / 2)

df1 = df1.T.iloc[::-1]
df1.index = df1.index.astype(np.float32)
row = df1.index
row = np.array(row)
# rounded_row = [round_to_nearest_five(x) for x in row]
rounded_row = row.copy()

blurred_df1 = gaussian_filter(df1, sigma=0.9)
norm = mcolors.Normalize(vmin=np.nanmin(blurred_df1), vmax=np.nanmax(blurred_df1))
X, Y = np.meshgrid(date, rounded_row)

plt.figure(figsize=(200,25))
contour = plt.contourf(X, Y, blurred_df1, cmap=custom_cmap1, levels=200, norm=norm, extend='both')
ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.DayLocator())
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d'))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xlabel('')
plt.ylabel('Diameter (nm)', fontsize=120, labelpad=40)
plt.yscale('log')
title_text = f'{min_date_str} to {max_date_str}{" " * 208}Range : 10 - 25 nm'
plt.title(title_text, fontsize=100, pad=60)
plt.xticks(fontsize=100)
plt.yticks(fontsize=100)

cbar = plt.colorbar(contour, ticks=[])
cbar.ax.tick_params(width=10, length=100, labelsize=80)

cbar.outline.set_linewidth(10)
ax.spines['top'].set_linewidth(10)
ax.spines['bottom'].set_linewidth(10)
ax.spines['left'].set_linewidth(10)
ax.spines['right'].set_linewidth(10)
ax.tick_params(axis='both', which='both', width=10, length=80, direction='out', pad=10)

ax.set_yticks([10.2, 20, 25])
ax.set_yticklabels(['10', '20', '25'])

cbar.ax.text(5, 0.5, r'dN/dlogDp ($10^3$ cm$^{-3}$)',
             va='center', ha='left', rotation=90, fontsize=100, transform=cbar.ax.transAxes)

actual_min_value = df_orig.min(skipna=True).values.min()
actual_max_value = df_orig.max(skipna=True).values.max()
actual_max_value_print = int(actual_max_value/1000)
cbar.ax.set_yticks([actual_min_value, actual_max_value])
cbar.ax.set_yticklabels(['0', '1'])
cbar.ax.tick_params(axis='both', which='both', width=10, length=80, direction='out', pad=10)

plt.savefig('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\nuc\\y_test.png', dpi=100)

df1 = pd.read_csv(r'C:\\Users\\Masloriy\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\nuc\\predictions_df.csv')
df1['date'] = pd.to_datetime(df1['date'])
df1.reset_index(drop=True, inplace=True)
df1 = df1.drop(df1.columns[df1.columns.str.contains('Unnamed')], axis=1)

df_orig = df1.copy()
df_orig = df_orig.drop(columns=['date'])
df1 = df1.set_index('date').resample('60min').mean().reset_index()

df1 = df1[(df1['date'] >= min_date) & (df1['date'] <= max_date)]
df1['date'] = pd.to_datetime(df1['date'])

X = df1.drop(columns=["date"])
date = df1['date']
X = X.abs()
X = X.astype(np.float32)
df1 = X.copy()

min_date = date.min()
max_date = date.max()
min_date_str = min_date.strftime('%Y-%m-%d')
max_date_str = max_date.strftime('%Y-%m-%d')

# def round_to_nearest_five(x):
#     return 2 * round(x / 2)

df1 = df1.T.iloc[::-1]
df1.index = df1.index.astype(np.float32)
row = df1.index
row = np.array(row)
# rounded_row = [round_to_nearest_five(x) for x in row]
rounded_row = row.copy()

blurred_df1 = gaussian_filter(df1, sigma=0.9)
norm = mcolors.Normalize(vmin=np.nanmin(blurred_df1), vmax=np.nanmax(blurred_df1))
X, Y = np.meshgrid(date, rounded_row)

plt.figure(figsize=(200,25))
contour = plt.contourf(X, Y, blurred_df1, cmap=custom_cmap2, levels=200, norm=norm, extend='both')
ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.DayLocator())
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d'))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xlabel('')
plt.ylabel('Diameter (nm)', fontsize=120, labelpad=40)
plt.yscale('log')
title_text = f'{min_date_str} to {max_date_str}{" " * 208}Range : 10 - 25 nm'
plt.title(title_text, fontsize=100, pad=60)
plt.xticks(fontsize=100)
plt.yticks(fontsize=100)

cbar = plt.colorbar(contour, ticks=[])
cbar.ax.tick_params(width=10, length=100, labelsize=80)

cbar.outline.set_linewidth(10)
ax.spines['top'].set_linewidth(10)
ax.spines['bottom'].set_linewidth(10)
ax.spines['left'].set_linewidth(10)
ax.spines['right'].set_linewidth(10)
ax.tick_params(axis='both', which='both', width=10, length=80, direction='out', pad=10)

ax.set_yticks([10.2, 20, 25])
ax.set_yticklabels(['10', '20', '25'])

cbar.ax.text(5, 0.5, r'dN/dlogDp ($10^3$ cm$^{-3}$)',
             va='center', ha='left', rotation=90, fontsize=100, transform=cbar.ax.transAxes)

actual_min_value = df_orig.min(skipna=True).values.min()
actual_max_value = df_orig.max(skipna=True).values.max()
actual_max_value_print = int(actual_max_value/1000)
cbar.ax.set_yticks([actual_min_value, actual_max_value])
cbar.ax.set_yticklabels(['0', '1'])
cbar.ax.tick_params(axis='both', which='both', width=10, length=80, direction='out', pad=10)

plt.savefig('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_regressor\\nuc\\predictions.png', dpi=100)