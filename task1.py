import pandas as pd

df_ratings = pd.read_csv("ratings.dat", sep="::", index_col=0, header=None, names=["UserID", "MovieID", "Rating", "Timestamp"], engine='python') 
#df_users = pd.read_csv("users.dat", sep="::", index_col=0, header=None, names=["UserID", "Gender", "Age", "Occupation", "Zip-code"], engine='python') 
df_movies = pd.read_csv("movies.dat", sep="::", index_col=0, header=None, names=["MovieID", "Title", "Genres"], engine='python') 

df_movies_ratings = pd.merge(df_movies, df_ratings, how='left', on='MovieID')[["Title", "Rating"]].groupby("Title").mean()
df_movies_ratings = df_movies_ratings.rename(columns={"Rating": "avgRating"})

n = int(input("Введите N\n"))
print(df_movies_ratings.nlargest(n, columns="avgRating"))