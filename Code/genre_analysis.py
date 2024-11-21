import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset_spotify.csv')
genres = df['genre'].str.split(',').explode().str.strip()
genre_counts = genres.value_counts()
top_genres = genre_counts.head(10)
others = genre_counts.tail(len(genre_counts) - 10).sum()
final_genres = pd.concat([top_genres, pd.Series({'Others': others})])
plt.figure(figsize=(8, 8))
sns.set_palette("husl")
final_genres.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("BuPu", len(final_genres)))
plt.title('Top 10 Music Genres and Others')
plt.ylabel('')
plt.savefig('genre_distribution_pie_chart.png')
plt.show()
genres = df['genre'].str.split(',').explode().str.strip()
genre_counts = genres.value_counts()
top_genres = genre_counts.head(10)
top_genre_list = top_genres.index


for genre in top_genre_list:
    plt.figure(figsize=(12, 8))  


    genre_df = df[df['genre'].str.contains(genre, case=False, na=False)]
    
    genre_year_popularity = genre_df.groupby('release_year')['popularity'].mean()
    plt.plot(genre_year_popularity.index, genre_year_popularity.values, label=genre, color=sns.color_palette("deep")[top_genre_list.get_loc(genre)])

    plt.title(f'{genre} Popularity Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Average Popularity')

    plt.xticks(rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{genre}_popularity_over_years.png')
    plt.show()