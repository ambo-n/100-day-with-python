import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text,'html.parser')
movie_titles = soup.find_all("h3", class_="title")

with open("movies.txt",mode="w") as file:
    for title in movie_titles[::-1]:
        movie_name = title.get_text()
        file.write(f"{movie_name}\n")

