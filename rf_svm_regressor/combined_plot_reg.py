import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.dates as mdates
from scipy.ndimage import gaussian_filter
import matplotlib.colors as mcolors

# Function to plot contour plot given data, title, and color map
def plot_contour(df, custom_cmap, min_date, max_date, ax, title_text, actual_min_value, actual_max_value):
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date').resample('60min').mean().reset_index()
    df = df[(df['date'] >= min_date) & (df['date'] <= max_date)]
    df['date'] = pd.to_datetime(df['date'])

    X = df.drop(columns=["date"])
    date = df['date']
    X = X.abs().astype(np.float32)

    df = X.T.iloc[::-1]
    row = df.index.astype(np.float32)

    blurred_df = gaussian_filter(df, sigma=0.9)
    norm = mcolors.Normalize(vmin=np.nanmin(blurred_df), vmax=np.nanmax(blurred_df))
    X, Y = np.meshgrid(date, row)

    contour = ax.contourf(X, Y, blurred_df, cmap=custom_cmap, levels=200, norm=norm, extend='both')

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.set_xlabel('')
    ax.set_ylabel('Diameter (nm)', fontsize=100, labelpad=20)
    ax.set_yscale('log')
    ax.set_title(title_text, fontsize=40, pad=30)
    ax.tick_params(axis='both', which='both', width=5, length=40, direction='out', pad=5)
    ax.set_yticks([10.2, 30, 59.4])
    ax.set_yticklabels(['10', '30', '60'])
    
    cbar = plt.colorbar(contour, ax=ax, ticks=[])
    cbar.ax.tick_params(width=5, length=50, labelsize=40)
    cbar.outline.set_linewidth(5)
    cbar.ax.text(5, 0.5, r'dN/dlogDp ($10^3$ cm$^{-3}$)', va='center', ha='left', rotation=90, fontsize=80, transform=cbar.ax.transAxes)

    cbar.ax.set_yticks([actual_min_value, actual_max_value])
    cbar.ax.set_yticklabels(['0', '1'])

    ax.spines['top'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_linewidth(5)
    ax.spines['right'].set_linewidth(5)

# Load and process y_test data
df1 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_svm_regressor\\y_test_df.csv')
df1['date'] = pd.to_datetime(df1['date'])
df1 = df1.drop(df1.columns[df1.columns.str.contains('Unnamed')], axis=1)

df_orig_y_test = df1.copy().drop(columns=['date'])

# min_date = pd.to_datetime('2019-01-01')
# max_date = pd.to_datetime('2020-01-01')

min_date = pd.to_datetime('2019-06-01')
max_date = pd.to_datetime('2019-09-01')

# Define color map
colors_y_test = [(0, 'blue'),
                 (0.0001, 'powderblue'),
                 (0.005, 'lightblue'),
                 (0.015, 'green'),
                 (0.045, 'yellow'),
                 (0.07, 'orange'),
                 (0.09, 'red'),
                 (0.15, 'darkred'),
                 (1, 'maroon')]

custom_cmap_y_test = LinearSegmentedColormap.from_list('custom_cmap', colors_y_test)

# Load and process predictions data
df2 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_svm_regressor\\predictions_df.csv')
df2['date'] = pd.to_datetime(df2['date'])
df2 = df2.drop(df2.columns[df2.columns.str.contains('Unnamed')], axis=1)

df_orig_predictions = df2.copy().drop(columns=['date'])

# Define color map for predictions
# colors_predictions = [(0, 'blue'),
#                       (0.16, 'powderblue'),
#                       (0.17, 'lightblue'),
#                       (0.2, 'green'),
#                       (0.37, 'yellow'),
#                       (0.44, 'orange'),
#                       (0.55, 'red'),
#                       (0.6, 'darkred'),
#                       (1, 'maroon')]

colors_predictions = [(0, 'blue'),
                      (0.16, 'powderblue'),
                      (0.17, 'lightblue'),
                      (0.2, 'green'),
                      (0.37, 'yellow'),
                      (0.38, 'orange'),
                      (0.4, 'red'),
                      (0.5, 'darkred'),
                      (1, 'maroon')]

custom_cmap_predictions = LinearSegmentedColormap.from_list('custom_cmap', colors_predictions)

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=2, figsize=(200, 50))

# Plot the y_test data (top subplot)
actual_min_value_y_test = df_orig_y_test.min(skipna=True).values.min()
actual_max_value_y_test = df_orig_y_test.max(skipna=True).values.max()
title_text_y_test = f'{min_date.strftime("%Y-%m-%d")} to {max_date.strftime("%Y-%m-%d")} Test plot {" " * 193}Range : 10 - 60 nm'
plot_contour(df1, custom_cmap_y_test, min_date, max_date, axes[0], title_text_y_test, actual_min_value_y_test, actual_max_value_y_test)

axes[0].set_title(title_text_y_test, fontsize=100, pad=60)
axes[0].tick_params(axis='x', labelsize=100)
axes[0].tick_params(axis='y', labelsize=100)

# Plot the predictions data (bottom subplot)
actual_min_value_predictions = df_orig_predictions.min(skipna=True).values.min()
actual_max_value_predictions = df_orig_predictions.max(skipna=True).values.max()
title_text_predictions = f'{min_date.strftime("%Y-%m-%d")} to {max_date.strftime("%Y-%m-%d")} Predictions plot {" " * 183}Range : 10 - 60 nm'
plot_contour(df2, custom_cmap_predictions, min_date, max_date, axes[1], title_text_predictions, actual_min_value_predictions, actual_max_value_predictions)

axes[1].set_title(title_text_predictions, fontsize=100, pad=60)
axes[1].tick_params(axis='x', labelsize=100)
axes[1].tick_params(axis='y', labelsize=100)

plt.subplots_adjust(hspace=0.5)

# Save and show the final plot
plt.savefig('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic\\rf_svm_regressor\\combined_plot.png', dpi=100)