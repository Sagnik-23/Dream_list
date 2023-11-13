import requests
import json

API_KEY = "6ba1f1149fcaab82cbfb0f993c5b3bba"

name = input("Enter movie name: ")
modified_name = name.replace(" ", "+")

response = requests.get(
    f"https://api.themoviedb.org/3/search/movie?query={modified_name}&api_key={API_KEY}")

data = response.json()

movie_title = data['results'][0]['original_title']
movie_desc = data['results'][0]['overview']
print(movie_title)
print(movie_desc)
