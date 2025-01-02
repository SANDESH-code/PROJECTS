# Importing necessary tools
import pandas as pd
import numpy as np

# Read movie data from a file called 'movies.csv' and rating data from 'ratings.csv'
movies = pd.read_csv('movies.csv')  # Loads movie data (like titles and IDs)
ratings = pd.read_csv('ratings.csv')  # Loads ratings data (user ratings for movies)

# Combine movie and rating data into one big table based on 'movieId'
data = pd.merge(ratings, movies, on='movieId')  # Combine both data sets

# Create a table where each row is a user and each column is a movie, showing the ratings
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

# Create a table that shows how similar each user is to every other user using their ratings
user_correlation_matrix = user_movie_matrix.corr(method='pearson', min_periods=50)  # Pearson method to find similarity

# Function to predict a rating for a movie that a user hasn't rated yet
def predict_ratings(user_id, movie_title):
    # Find other users who are similar to the current user
    similar_users = user_correlation_matrix[user_id].dropna()  # Get users who are similar to the current user
    movie_ratings_by_similar_users = user_movie_matrix[movie_title].dropna()  # Ratings for the given movie
    
    # Keep only the users who have rated the movie
    similar_users = similar_users[similar_users.index.isin(movie_ratings_by_similar_users.index)]
    
    # If no similar users are found, return "NaN" (not a number)
    if similar_users.empty:
        return np.nan
    
    # Calculate the predicted rating by giving more importance to more similar users
    weighted_ratings = movie_ratings_by_similar_users[similar_users.index] * similar_users
    return weighted_ratings.sum() / similar_users.sum()

# Function to recommend movies to a user by predicting ratings for movies they haven't rated
def recommend_movies(user_id, num_recommendations=5):
    # Get the movies the user has already rated
    user_ratings = user_movie_matrix.loc[user_id].dropna()  # Movies already rated by the user
    movies_not_rated = user_movie_matrix.columns.difference(user_ratings.index)  # Movies not rated by the user
    
    # Predict ratings for the movies that the user has not rated
    predicted_ratings = [predict_ratings(user_id, movie) for movie in movies_not_rated]  # Get predicted ratings
    
    # Create a list of predicted ratings for the user and sort them
    predicted_ratings_df = pd.DataFrame({
        'movie_title': movies_not_rated,
        'predicted_rating': predicted_ratings
    }).dropna()  # Remove rows where the prediction is not available
    
    # Sort the predicted ratings and return the top recommended movies
    top_movies = predicted_ratings_df.sort_values(by='predicted_rating', ascending=False).head(num_recommendations)
    return top_movies

# Example usage:
# We will give recommendations to the user with ID 1. You can change the ID to get recommendations for others.
user_id = 1  # Example user who wants movie recommendations

# Get the top 5 movie recommendations for the user
recommendations = recommend_movies(user_id, num_recommendations=5)

# Show the movie recommendations for the user
print(f"Top 5 movie recommendations for user {user_id}:\n")
print(recommendations)
