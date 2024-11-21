import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataset_spotify.csv')
attributes = ['danceability', 'energy', 'valence', 'tempo', 'acousticness', 'loudness', 'popularity']
correlation_matrix = df[attributes].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Audio Features')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()