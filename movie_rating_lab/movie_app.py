"""Movie Rating App

An app to rate movies just like the web site Rotten Tomatoes.
"""
search_or_ratings = 1
movie_title = 'Back to the Future'
movie_ratings = 8


def print_movie_title():
    print(movie_title)


def print_movie_rating():
    print(movie_ratings)


def print_single_movie_rating():
    print('The rating for', movie_title, 'is', movie_ratings)


def print_all_ratings(movie_list):
    for movie in movie_list:
        print('The movie', movie, 'has a great rating!')


def list_search_results(movie_titles):
    for title in movie_titles:
        print('    ', title)


def main():
    default_movie_list = ['Back to the Future', 'Blade', 'Spirited Away']
    print_all_ratings(default_movie_list)
    if search_or_ratings == 1:
        list_search_results(default_movie_list)
    elif search_or_ratings == 2:
        print_movie_rating()
    else:
        print_single_movie_rating()


if __name__ == '__main__':
    main()