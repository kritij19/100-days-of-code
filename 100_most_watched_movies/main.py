# Extracts the 100 greatest movies of all times from a website.

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.timeout.com/newyork/movies/best-movies-of-all-time")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

# Getting all tags containing movie titles
all_movie_tags = soup.find_all(name="h3", class_="_h3_cuogz_1")
# Making a list of movie titles from the tags
all_movie_titles = [tag.getText().split('\xa0')[1]
                    for tag in all_movie_tags[:100]]

# Writing the data into a file
count = 1
with open("movies.txt", mode="w") as movies_file:
    for movie in all_movie_titles:
        movies_file.write(f"{count}. {movie}\n")
        count += 1
