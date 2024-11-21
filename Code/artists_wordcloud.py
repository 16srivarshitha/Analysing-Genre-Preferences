import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_spotify.csv')

artist_counts = df['artist_name'].value_counts().head(5000)
artist_count_dict = artist_counts.to_dict()

wordcloud = WordCloud(width=800, height=600, background_color='white', 
                      colormap='Blues', relative_scaling=0.5).generate_from_frequencies(artist_count_dict)

plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.title('Top Artists by Frequency of Appearance (Word Cloud)', fontsize=16)
plt.tight_layout()

plt.savefig('top_artists_wordcloud.png')
plt.show()


