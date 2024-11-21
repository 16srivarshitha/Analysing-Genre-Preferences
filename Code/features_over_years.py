import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_spotify.csv')
features = ['danceability', 'tempo', 'valence', 'energy', 'loudness', 'acousticness','popularity','speechiness']
features_by_year = df.groupby(df['release_year'])[[*features]].mean()

for feature in features:
    plt.figure(figsize=(12, 6))
    plt.plot(features_by_year.index, features_by_year[feature], marker='o', color='teal')
    plt.title(f'{feature.capitalize()} Over Years', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel(f'Average {feature.capitalize()}', fontsize=12)
    plt.grid(visible=True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    plt.savefig(f'{feature}_over_years.png')
    plt.close()
