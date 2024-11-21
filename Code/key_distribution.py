
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_spotify.csv')
plt.figure(figsize=(10, 6))
sns.countplot(x='key', data=df, color='blue')
plt.title('Distribution of Musical Keys')
plt.xlabel('Key')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('key_distribution.png')
plt.close()