import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("spotify.csv")

# Show first 5 songs
print("🎵 Top Songs in Your Dataset:\n")
print(df[["Track Name", "Artist", "Popularity"]].head())

# 1️⃣ Scatter Plot: Popularity vs Danceability
plt.figure(figsize=(8,5))
plt.scatter(df["Danceability"], df["Popularity"], color='orange', edgecolors='black')
plt.title("Popularity vs Danceability")
plt.xlabel("Danceability")
plt.ylabel("Popularity")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart: Energy Levels of Songs
plt.figure(figsize=(10,6))
plt.bar(df["Track Name"].head(10), df["Energy"].head(10), color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Energy Levels of Top 10 Songs")
plt.ylabel("Energy")
plt.tight_layout()
plt.show()
