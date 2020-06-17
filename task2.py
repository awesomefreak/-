import pandas as pd
import matplotlib.pyplot as plt

df_ratings = pd.read_csv("ratings.dat", sep="::", index_col=0, header=None, names=["UserID", "MovieID", "Rating", "Timestamp"], engine='python') 
#df_users = pd.read_csv("users.dat", sep="::", index_col=0, header=None, names=["UserID", "Gender", "Age", "Occupation", "Zip-code"], engine='python') 
df_movies = pd.read_csv("movies.dat", sep="::", index_col=0, header=None, names=["MovieID", "Title", "Genres"], engine='python') 

df_movies_ratings = pd.merge(df_movies, df_ratings, how='left', on='MovieID')[["Title", "Rating"]].groupby("Title").mean().reset_index()

df_year_ratings = df_movies_ratings
df_year_ratings["Title"] = df_year_ratings["Title"].map(lambda x: x[-5:-1])
df_year_ratings = df_year_ratings.rename(columns={"Title": "Year"})
df_year_ratings = df_year_ratings.groupby("Year").mean().reset_index()
df_year_ratings.sort_values(by=["Year"])
plt.plot(df_year_ratings["Year"], df_year_ratings["Rating"], marker="o", c="g")
plt.xticks(rotation=90)
plt.show()