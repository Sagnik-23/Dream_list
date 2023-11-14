import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Search
# name = input("Enter movie name: ")
# modified_name = name.replace(" ", "+")

# response = requests.get(
#     f"https://api.themoviedb.org/3/search/movie?query={modified_name}&api_key={API_KEY}")

# data = response.json()
# print(data)

# movie_title = data['results'][0]['original_title']
# movie_desc = data['results'][0]['overview']
# print(movie_title)
# print(movie_desc)
# Search end


# Movie genre List
response = requests.get(
    f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={API_KEY}")
data = response.json()
# print(data)
# # print(data['genres'][0]['name'])
# print(len(data['genres']))

for i in range(0, len(data['genres'])):
    print("id: ", data['genres'][i]['id'])
    print("name: ", data['genres'][i]['name'])
# Movie genre List end

# Movie feed list
page_no = 1
url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page_no}&sort_by=popularity.desc&api_key={API_KEY}"
