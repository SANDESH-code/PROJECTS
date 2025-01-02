import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import yfinance as yf

# here is the list of movies with their id, title, genre, director, and year
movies_data = [
    {"id": 1, "title": "inception", "genre": "sci-fi", "director": "christopher nolan", "year": 2010},
    {"id": 2, "title": "the dark knight", "genre": "action", "director": "christopher nolan", "year": 2008},
    {"id": 3, "title": "interstellar", "genre": "sci-fi", "director": "christopher nolan", "year": 2014},
    {"id": 4, "title": "the matrix", "genre": "sci-fi", "director": "the wachowskis", "year": 1999},
    {"id": 5, "title": "the prestige", "genre": "drama", "director": "christopher nolan", "year": 2006},
    {"id": 6, "title": "rrr", "genre": "action, drama", "year": 2022, "rating": 8.0, "language": "telugu"},
    {"id": 7, "title": "baahubali: the beginning", "genre": "action, adventure, drama", "year": 2015, "rating": 8.0, "language": "telugu"},
    {"id": 8, "title": "baahubali: the conclusion", "genre": "action, adventure, drama", "year": 2017, "rating": 8.3, "language": "telugu"},
    {"id": 9, "title": "eega", "genre": "action, fantasy", "year": 2012, "rating": 7.8, "language": "telugu"},
    {"id": 10, "title": "arjun reddy", "genre": "drama, romance", "year": 2017, "rating": 8.1, "language": "telugu"},
    {"id": 11, "title": "maharshi", "genre": "action, drama", "year": 2019, "rating": 7.5, "language": "telugu"},
    {"id": 12, "title": "kshana kshanam", "genre": "action, comedy, drama", "year": 1991, "rating": 7.9, "language": "telugu"},
    {"id": 13, "title": "vakeel saab", "genre": "drama, thriller", "year": 2021, "rating": 7.4, "language": "telugu"},
    {"id": 14, "title": "jersey", "genre": "drama, sports", "year": 2019, "rating": 8.3, "language": "telugu"},
    {"id": 15, "title": "f2: fun and frustration", "genre": "comedy, drama", "year": 2019, "rating": 7.3, "language": "telugu"}
]

# this function will recommend movies based on the genre entered
def recommend_movies(genre):
    # look for movies that match the genre entered
    return [movie for movie in movies_data if genre.lower() in movie['genre'].lower()]

# main function to start the program
def main():
    print("welcome to the movie recommendation system!")
    
    # ask user for genre to recommend movies
    genre = input("enter a genre to get movie recommendations (e.g., sci-fi, action): ")
    
    # get the list of recommended movies based on genre
    recommended_movies = recommend_movies(genre)
    
    # if movies found for the genre, print them
    if recommended_movies:
        print(f"movies recommended for the genre '{genre}':")
        for movie in recommended_movies:
            # get the director name, if available
            director = movie.get('director', 'n/a')
            print(f"id: {movie['id']}, title: {movie['title']}, director: {director}, year: {movie['year']}")
    else:
        print(f"no movies found for the genre '{genre}'.")

# run the program
if __name__ == "__main__":
    main()
