import numpy as np
import pandas as pd


print("NumPy Version:", np.__version__)
print("Pandas Version:", pd.__version__)

# data = pd.DataFrame({
#     'Name': ['Asad', 'Rahul'],
#     'Age': [21, 22]
# })

# print(data)

df=pd.read_csv('Spotify.csv')
print(df)

# Asking question-

# Data Wrangling-
# -Data Gathering-
### OKAY--
### Accesing Dataset in kaggle and Analysis-
# -Data Assessing-
## - Write Your Dataset and find Conclusion unclean Data-
### Conclusions Write-
# (i)- Dirty Data!
# -1 Missing value on Artist and track name Col!
# -Remove missing value in DataSet-

# id=df['duration_ms'].isnull().sum()
# print(id)

# # (ii)- Messy Data!
# # - Remove Track_id because its not usefull-
# df2=df.drop(columns='track_id')
# print(df2)
# # genre=df1.groupby('track_genre').size().head(3)
# # print(genre)

# # -Data Cleaning-
# song=df.info()
# print(song)

# missing=df.isnull().sum()
# print(missing)

# integer=df.describe()
# print(integer)

# drop=df.drop_duplicates(inplace=True)
# print(drop)

# missing1=df.dropna(how='all',inplace=True)
# print("Check Missing Value",missing)

# # EDA- ( Explotry Data Analysis)-
# 1-  Find Total Songs in Dataset?
total=df['track_name'].count()
print("Total Songs=",total)
# 2- How many unique artists in Dataset?
unique=df['artists'].unique().count()
# 3-Find Top 10 Most Popular Song?
popular = df.sort_values(by='popularity',ascending=False).head(10)
print(popular[['track_name', 'artists', 'popularity']])
# 4- Find Top 10 Artists?
artists = df.groupby('artists')['popularity'].mean()
top_artists = artists.sort_values(ascending=False).head(10)
print(top_artists)
# 5- Which Genre is most Popular is Dataset?
genre = df.groupby('track_genre')['popularity'].mean()
most = genre.sort_values(ascending=False).head(10)
print(most)
# 6- what is the relationship b/w Danceability and Energy?
#- Check the relation b/w energy and Dance!
check=df[['energy','danceability']].mean()
print(check)
# 7- Which songs are Romance and piano? 
# (i)- Find Piano Song!
piano=df[df['track_genre']  == 'piano']
print(piano)
add=piano[['track_name','popularity','track_genre']]
print(add)
# Export into CSV File--
# Find Romance Song?
# 1000 Romance Song Existing in this col!
romance=df[df['track_genre'] == 'romance']
print(romance)
romantic=romance[['track_name','popularity','track_genre']]
print(romantic)
# 8-Acoustic songs aur energetic songs mein kya difference hai?
check=df[['acousticness','energy']].mean()
print(check)
# Result points-
# 9-Major aur Minor key mein kitne songs hain?
# -Count major songs?
mode1=df[df['mode'] == 0].sum()
print("Total Major Songs =",mode1)
# Answer is= 
# Count Minor Songs?
mode2=df[df['mode'] == 1].sum()
print("Total Minor Songs =",mode2)
# Answer is =

# 10-Explicit aur Non-explicit songs ka ratio kya hai?
 ## Skippped
# 11-Songs ki average duration kitni hai?
duration=df['duration_ms'].mean()
print("Total Average Duraiton =",duration)
# 12-Popularity aur danceability/energy ka kya relationship hai?

check = df[['popularity', 'danceability', 'energy']].corr()

print(check)

# check side by side Popularity check in terms!



# check=df.duplicated().sum()
# print(check)

# check=df.dropna(subset=['artists', 'track_name'],inplace=True)
# print(check)





# Convert Csv into Excel File-

# Graph Plotting-

# Conclusion write-






# Q1. Top 5 genres find karo based on average energy.
find=df.groupby('track_genre')['energy'].mean()
new=find.sort_values(ascending=False).head(5)

# Q2. Top 10 songs find karo jinki popularity 90 se above hai.
# Q3. Artist-wise total songs count karo aur top 10 artists nikalo.
# Q4. Find karo ki explicit songs ki average popularity non-explicit songs se zyada hai ya nahi.
# Q5. Find karo ki sabse zyada danceable songs kis genre mein hain.










