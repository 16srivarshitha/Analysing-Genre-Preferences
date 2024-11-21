import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataset_spotify.csv')
attributes = ['danceability', 'energy', 'valence', 'tempo', 'acousticness', 'loudness', 'popularity']
popularity_corr = df[attributes].corrwith(df['popularity'])

plt.figure(figsize=(10, 6))
popularity_corr.plot(kind='bar', color='teal')
plt.title('Feature Correlation with Popularity')
plt.xlabel('Feature')
plt.ylabel('Correlation with Popularity')
plt.tight_layout()
plt.savefig('feature_correlation_with_popularity.png')
plt.close()