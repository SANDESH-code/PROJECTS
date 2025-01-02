import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import yfinance as yf
movies_data = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "director": "Christopher Nolan", "year": 2010},
    {"id": 2, "title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan", "year": 2008},
    {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "director": "Christopher Nolan", "year": 2014},
    {"id": 4, "title": "The Matrix", "genre": "Sci-Fi", "director": "The Wachowskis", "year": 1999},
    {"id": 5, "title": "The Prestige", "genre": "Drama", "director": "Christopher Nolan", "year": 2006},
    {"id": 1, "title": "RRR", "genre": "Action, Drama", "year": 2022, "rating": 8.0, "language": "Telugu"},
    {"id": 2, "title": "Baahubali: The Beginning", "genre": "Action, Adventure, Drama", "year": 2015, "rating": 8.0, "language": "Telugu"},
    {"id": 3, "title": "Baahubali: The Conclusion", "genre": "Action, Adventure, Drama", "year": 2017, "rating": 8.3, "language": "Telugu"},
    {"id": 4, "title": "Eega", "genre": "Action, Fantasy", "year": 2012, "rating": 7.8, "language": "Telugu"},
    {"id": 5, "title": "Arjun Reddy", "genre": "Drama, Romance", "year": 2017, "rating": 8.1, "language": "Telugu"},
    {"id": 6, "title": "Maharshi", "genre": "Action, Drama", "year": 2019, "rating": 7.5, "language": "Telugu"},
    {"id": 7, "title": "Kshana Kshanam", "genre": "Action, Comedy, Drama", "year": 1991, "rating": 7.9, "language": "Telugu"},
    {"id": 8, "title": "Vakeel Saab", "genre": "Drama, Thriller", "year": 2021, "rating": 7.4, "language": "Telugu"},
    {"id": 9, "title": "Jersey", "genre": "Drama, Sports", "year": 2019, "rating": 8.3, "language": "Telugu"},
    {"id": 10, "title": "F2: Fun and Frustration", "genre": "Comedy, Drama", "year": 2019, "rating": 7.3, "language": "Telugu"}
]
def recommend_movies(genre):
    return [movie for movie in movies_data if genre.lower() in movie['genre'].lower()]
def main():
    print("Welcome to the Movie Recommendation System!")
    genre = input("Enter a genre to get movie recommendations (e.g., Sci-Fi, Action): ")
    recommended_movies = recommend_movies(genre)
    if recommended_movies:
        print(f"Movies recommended for the genre '{genre}':")
        for movie in recommended_movies:
            director = movie.get('director', 'N/A')
            print(f"ID: {movie['id']}, Title: {movie['title']}, Director: {director}, Year: {movie['year']}")
    else:
        print(f"No movies found for the genre '{genre}'.")
if __name__ == "__main__":
    main()
