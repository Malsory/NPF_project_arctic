import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'SRAD':    0.251435,
    'date':    0.174925,
    'T':    0.136532,
    'RH':    0.127760,
    'P':    0.112066,
    'SO4':    0.063107,
    'NH3':   0.060823,
    'SO2':    0.045826,
    'NH4':    0.027527
}

plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(10, 10))
plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors, textprops={'fontsize': 15})
plt.title('Importance of parameters', fontsize=15)
plt.axis('equal')
plt.savefig('C:\\Users\\Masloriy\\Desktop\\Data\\Data_arctic\\png\\\pie_chart2.png', dpi=300)
