import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_spotify.csv')
time_signature_counts = df['time_signature'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(time_signature_counts.index, time_signature_counts.values, marker='o', linestyle='-', color='orange', label='Time Signatures')

plt.title('Distribution of Time Signatures')
plt.xlabel('Time Signature')
plt.ylabel('Count')

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend()
plt.tight_layout()
plt.savefig('time_signature_distribution_lineplot.png')
plt.show()

avg_duration_per_year_minutes = df.groupby('release_year')['duration_ms'].mean() / 60000  # Convert ms to minutes
plt.figure(figsize=(12, 6))
plt.plot(avg_duration_per_year_minutes.index, avg_duration_per_year_minutes.values, marker='o', linestyle='-', color='green', label='Average Duration (Minutes)')

plt.title('Average Song Duration vs Year')
plt.xlabel('Year')
plt.ylabel('Average Duration (Minutes)')

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('average_duration_vs_year_lineplot_minutes.png')
plt.show()