import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

spotify=pd.read_csv('Songs.csv')
print(spotify)
# convert into DataFrame-
song=pd.DataFrame(spotify)
print(song)


# Q1. Top 5 genres find karo based on average energy.
find=song.groupby('track_genre')['energy'].mean() * 100
new=find.sort_values(ascending=False).head(5)
print(new)

# Q2. Top 10 songs find karo jinki popularity 90 se above hai.
find=song[song['popularity'] >= 90]
print(find[['track_name','artists','popularity']].head(10))


# Q3. Artist-wise total songs count karo aur top 10 artists nikalo.
find=song.groupby('artists')['track_name'].count()
sort=find.sort_values(ascending=False).head(10)
print(sort)

# Q4. Find karo ki explicit songs ki average popularity non-explicit songs se zyada hai ya nahi.
# Q5. Find karo ki sabse zyada danceable songs kis genre mein hain.
find=song.groupby('track_genre')['danceability'].mean() * 100
at=song.sort_values(by='danceability',ascending=False).head(10)
print(at[['track_genre','danceability']])

print(song.info())

# Data Cleaning-

check=song.isnull().sum()
print(check)

# Remove Missing Values in cols-

remove=song.dropna(subset=['artists','album_name','track_name'],inplace=True)
print(remove)

check=song.isnull().sum()
print(check)

# Check Duplicate Values-
check=song[song.duplicated()].sum()
print(check)

# Check Outliers in Dataset-
check=song.describe()
print(check)

# Remove Outliers in Dataset-
Q1 = song['duration_ms'].quantile(0.25)
Q3 = song['duration_ms'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = song[
    (song['duration_ms'] < lower) |
    (song['duration_ms'] > upper)
]

print("Lower Limit:", lower)
print("Upper Limit:", upper)
print("Total Outliers:", outliers.shape[0])


# check outlier is drop and usefulll in dataset-
print(outliers[['track_name', 'artists', 'duration_ms']].sort_values(by='duration_ms', ascending=False).head(15))

# Add new columns "duration_min"!
song['duration_min'] = song['duration_ms'] / 60000

print(song[['track_name', 'duration_min']].head())


print(song['duration_min'].describe())


# Histogram Plot-

# plt.figure(figsize=(10,5))

# plt.hist(song['duration_min'], bins=50)

# plt.xlabel('Duration (Minutes)')
# plt.ylabel('Number of Tracks')
# plt.title('Spotify Track Duration Distribution')

# plt.show()

# Export Csv-
songs=song.to_csv('Spotify_Cleaned.csv', index=False)
print(songs)