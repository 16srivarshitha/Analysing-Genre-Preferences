import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('combined_output.csv')
attributes = ['danceability', 'energy', 'valence', 'tempo', 'acousticness', 'loudness', 'popularity']

for attribute in attributes:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[attribute], kde=True, color='skyblue', bins=30)
    plt.title(f'Distribution of {attribute}')
    plt.xlabel(attribute)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f'{attribute}_histogram.png')
    # plt.close()
