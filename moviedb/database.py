"Модуль с функциями базы данных"
from uuid import uuid4
from typing import Optional

from .utils import load_from_json, save_to_json
from .annotations import Movie, Filters


def load_movies_from_file(file_name: str) -> Optional[list[Movie]]:
    "Загружает фильмы из файла"
    return load_from_json(file_name)


def save_movies_to_file(movies: list[Movie],
                        file_name: str) -> None:
    "Сохраняет фильмы в файл"
    save_to_json(movies, file_name)


def find_movies(movies: list[Movie], filters: Filters) -> list[Movie]:
    """Ищет фильмы на основе заданных параметров и возвращает их"""
    query = filters['query'].lower().strip()
    return [
        movie for movie in movies
        if (
                (query in movie['title'].lower()) and
                (filters['year_released'] is None or
                 filters['year_released'] == movie['year_released']) and
                (filters['duration'] is None or
                 filters['duration'] == movie['duration'])
        )
    ]


def create_movie(
        title: str,
        director: str,
        screenwriter: str,
        duration: int,
        year_released: int
) -> Movie:
    "Создает новый фильм и возвращает его"
    new_movie: Movie = {
        'id': str(uuid4()),
        'title': title,
        'director': director,
        'screenwriter': screenwriter,
        'duration': duration,
        'year_released': year_released
    }
    return new_movie


def delete_movie(movies: list[Movie], id_to_delete: str) -> list[Movie]:
    "Удаляет фильм по id из заданного списка"
    return [movie for movie in movies
            if movie['id'] != id_to_delete]
