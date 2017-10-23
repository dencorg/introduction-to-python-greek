# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import datetime

def get_current_year():
    """Επιστέφει τον τρέχοντα χρόνο"""

    now = datetime.datetime.now()
    return now.year


def get_popular_movies(year):
    """Μαζέυει και τυπώνει τα δεδομένα ταινιών απο το imdb"""

    url = 'http://www.imdb.com/search/title?release_date=' + str(year)

    r = requests.get(url)
    html_contents = r.text

    soup = BeautifulSoup(html_contents, 'html.parser')
    movies_list = soup.find_all('div', class_='lister-item')

    if (len(movies_list) == 0):
        print('No movies found!')
        return

    print(50 * '*')
    print('***** Movie title - Imdb Rating - Genres *********')
    print(50 * '*')

    for movie in movies_list:

        # get title
        title = movie.h3.a.string

        # get imdb rating
        imdb_rating = movie.find('div', class_='ratings-imdb-rating')
        if (imdb_rating is None):
            imdb_rating = '-'
        else:
            imdb_rating = imdb_rating.strong.string

        # get genres
        genres = movie.find('span', class_='genre')
        if (genres is None):
            genres = '-'
        else:
            genres = genres.string.strip()

        # print data to console
        print('{} - {} - {}'.format(title, imdb_rating, genres))


if __name__ == '__main__':

    year = int(input('Pick a year: '))

    current_year = get_current_year()

    # check if year is valid
    if (year < 1874 or year > current_year):
        print('Please enter a valid year!')
        exit()

    get_popular_movies(year)