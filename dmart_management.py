import pandas as pd
import numpy as np
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
data = pd.merge(ratings, movies, on='movieId')
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')
user_correlation_matrix = user_movie_matrix.corr(method='pearson', min_periods=50)
def predict_ratings(user_id, movie_title):
    similar_users = user_correlation_matrix[user_id].dropna()
    movie_ratings_by_similar_users = user_movie_matrix[movie_title].dropna()
    similar_users = similar_users[similar_users.index.isin(movie_ratings_by_similar_users.index)]
    if similar_users.empty:
        return np.nan
    weighted_ratings = movie_ratings_by_similar_users[similar_users.index] * similar_users
    return weighted_ratings.sum() / similar_users.sum()
def recommend_movies(user_id, num_recommendations=5):
    user_ratings = user_movie_matrix.loc[user_id].dropna()
    movies_not_rated = user_movie_matrix.columns.difference(user_ratings.index)
    predicted_ratings = [predict_ratings(user_id, movie) for movie in movies_not_rated]
    predicted_ratings_df = pd.DataFrame({
        'movie_title': movies_not_rated,
        'predicted_rating': predicted_ratings
    }).dropna()
    top_movies = predicted_ratings_df.sort_values(by='predicted_rating', ascending=False).head(num_recommendations)
    return top_movies
user_id = 1
recommendations = recommend_movies(user_id, num_recommendations=5)
print(f"Top 5 movie recommendations for User {user_id}:\n")
print(recommendations)
