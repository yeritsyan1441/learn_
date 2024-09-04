"""1․ Գրել MyShows class, որը․
   - __init__ ում կստանա
     -- սերիալի անունը (պետք է լինի տեքստ),
     -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
     -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
     -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
     -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
     -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
   - բոլոր ատրիբուտները կլինեն private,
   - կունենա getter բոլոր ատրիբուտների համար,
   - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
   - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
   - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
   - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ին"""


import imdb


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
        raise Exception("Movie name must be string")

    @staticmethod
    def _is_page(page_name) -> bool:
        if isinstance(page_name, str):
            return True
        raise Exception("Page name must be string")

    @staticmethod
    def _is_movie_data(movie_name) -> bool:
        if isinstance(movie_name, int):
            return True
        raise Exception("Movie date  must be integer")

    @staticmethod
    def _is_movie_number(movie_number) -> bool:
        if isinstance(movie_number, int):
            return True
        raise ValueError("Movie number must be integer")

    @staticmethod
    def _is_movie_actor(actors):
        if isinstance(actors, list):
            return True
        raise Exception("Movie actors must be list")

    @classmethod
    def _check_rating(cls, rate) -> bool:
        if cls.MIN_RATING <= rate <= cls.MAX_RATING:
            return True
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
        raise Exception("Movie number must be integer")

    @property
    def main_actors(self):
        return self.__main_actors

    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and MyShows.MIN_RATING <= value <= MinShows.MAX_RATING:
            self.__rating = value
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
        try:
            ia = imdb.IMDb()
            items = ia.search_movie(f'{self.__movie_name}')
            for i in items:
                print(i)
        except Exception:
            return "Movie not found"



