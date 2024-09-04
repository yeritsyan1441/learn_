class MyShows(object):

    MIN_RATING = 1
    MAX_RATING = 10

    def __init__(self, movie_name, page_name, movie_data, rating=None, movie_number=1,  main_actors=[]):
        if (self._is_movie_name(movie_name)
                and self._is_page(page_name)
                and self._is_movie_data(movie_data)
                and self._is_movie_number(movie_number)
                and self._check_rating(rating)):
            self.__main_actors = main_actors
            self.__movie_number = movie_number
            self.__rating = rating
            self.__movie_data = movie_data
            self.__page_name = page_name
            self.__movie_name = movie_name

    @staticmethod
    def _is_movie_name(movie_name) -> bool:
        if isinstance(movie_name, str):
            return True
        else:
            raise Exception("Movie name must be string")

    @staticmethod
    def _is_page(page_name) -> bool:
        if isinstance(page_name, str):
            return True
        else:
            raise Exception("Page name must be string")

    @staticmethod
    def _is_movie_data(movie_name) -> bool:
        if isinstance(movie_name, int):
            return True
        else:
            raise Exception("Movie date  must be integer")

    @staticmethod
    def _is_movie_number(movie_number) -> bool:
        if isinstance(movie_number, int):
            return True
        else:
            raise ValueError("Movie number must be integer")

    @staticmethod
    def _is_movie_actor(actors):
        if isinstance(actors, list):
            return True
        else:
            raise Exception("Movie actors must be list")

    @classmethod
    def _check_rating(cls, rate) -> bool:
        if cls.MIN_RATING <= rate <= cls.MAX_RATING:
            return True
        else:
            raise Exception("Rate must be <= 10")

    @property
    def movie_name(self):
        print('Movie Name:', end=' ')
        return self.__movie_name

    @property
    def page_name(self):
        print('Page Name:', end=' ')
        return self.__page_name

    @property
    def movie_data(self):
        print('Movie Data:', end=' ')
        return self.__movie_data

    @property
    def rating(self):
        return self.__rating

    @property
    def movie_number(self):
        return self.__rating

    @movie_number.setter
    def movie_number(self, value):
        if isinstance(value, int):
            self.__movie_number = value
        else:
            raise Exception("Movie number must be integer")

    @property
    def main_actors(self):
        return self.__main_actors

    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and MyShows.MIN_RATING <= value <= MyShows.MAX_RATING:
            print(f"New rating {value}")
            self.__rating = value
        else:
            raise ValueError('Rate must be number and in range (1,10)') 

    @rating.deleter
    def rating(self):
        del self.__rating

    def _update_list(self, name):
        self.__main_actors.append(name)

    def _delete_actor(self, actor_name):
        try:
            self.__main_actors.remove(actor_name)
        except ValueError:
            return f"{actor_name} not in actor list"

    def info(self):
        ...


user = MyShows("avenjers", "kinopoisk", 2022, 5, 1, ["hulk","captain america"])
print(user.rating)
user.rating = 10
