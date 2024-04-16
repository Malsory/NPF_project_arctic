import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\in_progress\\heatmap_accuracy.csv')
df1 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\in_progress\\heatmap_precision.csv')
df2 = pd.read_csv(r'C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\in_progress\\heatmap_recall.csv')

plt.figure(figsize=(10, 10))
plt.rcParams['font.family'] = 'Times New Roman'
min_value = df.iloc[1:, 1:].values.min()
max_value = df.iloc[1:, 1:].values.max()
sns.heatmap(df.iloc[0:, 1:], annot=True, cmap='RdYlGn', fmt='.2f', center=(min_value + max_value) / 2, square=True)
plt.title('Heatmap of accuracies of combinations', fontsize=15)
plt.xlabel('Models', fontsize=15)
plt.ylabel('Combination', fontsize=15)
plt.xticks(fontsize=15)
plt.savefig('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\png\\heatmap_comp_accuracy.png', dpi=300)

plt.figure(figsize=(10, 10))
plt.rcParams['font.family'] = 'Times New Roman'
sns.heatmap(df1.iloc[0:, 1:], annot=True, cmap='RdYlGn', fmt='.2f', center=(min_value + max_value) / 2, square=True)
plt.title('Heatmap of precision of combinations', fontsize=15)
plt.xlabel('Models', fontsize=15)
plt.ylabel('Combination', fontsize=15)
plt.xticks(fontsize=15)
plt.savefig('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\png\\heatmap_comp_precision.png', dpi=300)

plt.figure(figsize=(10, 10))
plt.rcParams['font.family'] = 'Times New Roman'
sns.heatmap(df2.iloc[0:, 1:], annot=True, cmap='RdYlGn', fmt='.2f', center=(min_value + max_value) / 2, square=True)
plt.title('Heatmap of recall of combinations', fontsize=15)
plt.xlabel('Models', fontsize=15)
plt.ylabel('Combination', fontsize=15)
plt.xticks(fontsize=15)
plt.savefig('C:\\Users\\Masloriy\\Desktop\\NPF_project_arctic\\NPF_project_arctic-Updates\\png\\heatmap_comp_racall.png', dpi=300)