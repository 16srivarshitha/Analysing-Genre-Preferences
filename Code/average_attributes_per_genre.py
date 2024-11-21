
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset_spotify.csv')
genres = df['genre'].str.split(',').explode().str.strip()

attributes = ['danceability', 'energy' , 'valence','tempo','acousticness','loudness','popularity']

df_expanded = df.copy()
df_expanded = df_expanded.assign(genre=df_expanded['genre'].str.split(',')).explode('genre')

avg_attributes_per_genre = df_expanded.groupby('genre')[attributes].mean()

print("Average Attributes Per Genre:")
print(avg_attributes_per_genre)

avg_attributes_per_genre.to_csv('average_attributes_per_genre.csv')


# from IPython.display import display
# display(avg_attributes_per_genre.style.background_gradient(cmap='viridis'))