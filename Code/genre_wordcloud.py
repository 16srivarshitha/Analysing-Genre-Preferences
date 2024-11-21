import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
df = pd.read_csv('dataset_spotify.csv')
genres = df['genre'].str.split(',').explode().str.strip()
genre_counts = genres.value_counts()
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='YlGnBu', 
                      relative_scaling=0.5).generate_from_frequencies(genre_counts)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.title('Word Cloud of Music Genres')
plt.tight_layout()

plt.savefig('genre_wordcloud.png')
plt.show()