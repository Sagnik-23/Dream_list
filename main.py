from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import sqlite3
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


def get_genres(id):
    response = requests.get(
        f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={API_KEY}")
    data = response.json()
    length = len(data['genres'])
    for i in range(0, len(data['genres'])):
        if data['genres'][i]['id'] == id:
            genre = data['genres'][i]['name']
            return genre


def get_feed_movies(page_no, index):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page_no}&sort_by=popularity.desc&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    background_image = data['results'][index]['backdrop_path']
    background_image_url = f"https://image.tmdb.org/t/p/w400{background_image}"
    title = data['results'][index]['title']
    overview = data['results'][index]['overview']
    genre_id = data['results'][index]['genre_ids']
    genres = []
    for id in genre_id:
        genres.append(get_genres(id))
    return index, background_image_url, genres, title, overview


@app.route('/')
def index():
    # if not session.get("name"):
    #     return redirect("/login")
    page_title = "DreamList"
    background_image_url = []
    genres = []
    title = []
    overview = []
    index = []
    for i in range(0, 20):
        movie_index, movie_background_image_url, movie_genres, movie_title, movie_overview = get_feed_movies(
            1, i)
        index.append(movie_index)
        background_image_url.append(movie_background_image_url)
        genres.append(movie_genres)
        title.append(movie_title)
        overview.append(movie_overview)
    return render_template("home.html", page_title=page_title, index=index, background_image_url=background_image_url, genres=genres, title=title, overview=overview)


if __name__ == "__main__":
    app.run(debug=True)
