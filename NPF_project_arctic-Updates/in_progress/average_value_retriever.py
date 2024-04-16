import pandas as pd
import numpy as np
import sys

# Read dataset
df = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\Data\\Data_arctic\\in_progress\\output_combined.csv')
# Prep the dataset
df = df.dropna()
df = df.drop(df.columns[df.columns.str.contains('Unnamed')], axis=1)
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.dayofyear
df = df.drop(df.index[-1])

npf_df_NPF = df[df['day.type'] == 'NPF']
average_temp_NPF = np.mean(npf_df_NPF['temperature'])
average_P_NPF = np.mean(npf_df_NPF['pressure'])
average_RH_NPF = np.mean(npf_df_NPF['RH'])
average_SRAD_NPF = np.mean(npf_df_NPF['SWD'])
average_SO2_NPF = np.mean(npf_df_NPF['SO2'])
average_SO4_NPF = np.mean(npf_df_NPF['SO4'])
average_NH3_NPF = np.mean(npf_df_NPF['NH3'])
average_NH4_NPF = np.mean(npf_df_NPF['NH4'])

npf_df_non_NPF = df[df['day.type'] == 'Non']
average_temp_non = np.mean(npf_df_non_NPF['temperature'])
average_P_non = np.mean(npf_df_non_NPF['pressure'])
average_RH_non = np.mean(npf_df_non_NPF['RH'])
average_SRAD_non = np.mean(npf_df_non_NPF['SWD'])
average_SO2_non = np.mean(npf_df_non_NPF['SO2'])
average_SO4_non = np.mean(npf_df_non_NPF['SO4'])
average_NH3_non = np.mean(npf_df_non_NPF['NH3'])
average_NH4_non = np.mean(npf_df_non_NPF['NH4'])

npf_df_undef = df[df['day.type'] == 'undefined']
average_temp_undef = np.mean(npf_df_undef['temperature'])
average_P_undef = np.mean(npf_df_undef['pressure'])
average_RH_undef = np.mean(npf_df_undef['RH'])
average_SRAD_undef = np.mean(npf_df_undef['SWD'])
average_SO2_undef = np.mean(npf_df_undef['SO2'])
average_SO4_undef = np.mean(npf_df_non_NPF['SO4'])
average_NH3_undef = np.mean(npf_df_non_NPF['NH3'])
average_NH4_undef = np.mean(npf_df_non_NPF['NH4'])

# Redirect stdout to a file
with open(r'C:\\Users\\Masloriy\\Desktop\\Data\\Data_arctic\\in_progress\\statistics_results.txt', 'w') as file:
    sys.stdout = file
    print('Avg temperature during NPF days:', average_temp_NPF)
    print('Avg temperature during non-NPF days:', average_temp_non)
    print('Avg temperature during Undefined days:', average_temp_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg pressure during NPF days:', average_P_NPF)
    print('Avg pressure during non-NPF days:', average_P_non)
    print('Avg pressure during Undefined days:', average_P_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg RH during NPF days:', average_RH_NPF)
    print('Avg RH during non-NPF days:', average_RH_non)
    print('Avg RH during Undefined days:', average_RH_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg SRAD during NPF days:', average_SRAD_NPF)
    print('Avg SRAD during non-NPF days:', average_SRAD_non)
    print('Avg SRAD during Undefined days:', average_SRAD_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg SO2 during NPF days:', average_SO2_NPF)
    print('Avg SO2 during non-NPF days:', average_SO2_non)
    print('Avg SO2 during Undefined days:', average_SO2_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg SO4 during NPF days:', average_SO4_NPF)
    print('Avg SO4 during non-NPF days:', average_SO4_non)
    print('Avg SO4 during Undefined days:', average_SO4_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg NH3 during NPF days:', average_NH3_NPF)
    print('Avg NH3 during non-NPF days:', average_NH3_non)
    print('Avg NH3 during Undefined days:', average_NH3_undef)
    print('-----------------------------------------------------------------------------------')
    print('Avg NH4 during NPF days:', average_NH4_NPF)
    print('Avg NH4 during non-NPF days:', average_NH4_non)
    print('Avg NH4 during Undefined days:', average_NH4_undef)
    sys.stdout = sys.__stdout__
