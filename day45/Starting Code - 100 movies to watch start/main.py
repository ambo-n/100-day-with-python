import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text,'html.parser')
movie_titles = soup.find_all("h3", class_="title")

with open("movies.txt",mode="w") as file:
    for n, title in enumerate(reversed(movie_titles), start=1):
        parts= title.get_text().split()[1:]
        movie_name= " ".join(parts)
        file.write(f"{n}){movie_name}\n")

