"Модуль с функционалом меню"
from typing import Optional

from .database import (
    create_movie,
    delete_movie,
    load_movies_from_file,
    save_movies_to_file,
)
from .utils import file_name_input, required_input
from .annotations import (
    Filters,
    Movie
)
from .config import (
    MENU_OPTIONS,
    DURATION_RANGE,
    YEAR_RANGE
)


def display_menu() -> None:
    "Выводит меню на экран"
    print('*----------- ФИЛЬМЫ -----------*')
    for num, option in enumerate(MENU_OPTIONS, start=1):
        print(f'{num}) {option}')
    print('*------------------------------*')


def get_menu_option_idx() -> int:
    """Показывает меню, предлагает выбор опции из него и возвращает индекс
    выбранного элемента"""
    display_menu()
    return required_input('Выберите действие: ', int,
                          value_range=(1, len(MENU_OPTIONS))) - 1


def load_movies(movies: list[Movie], default_file_name: str) \
        -> tuple[list[Movie], str]:
    """Загружает фильмы из файла, который задает пользователь, и возвращает
    данные вместе с именем последнего файла"""
    file_name = file_name_input('json',
                                f'Введите имя файла ({default_file_name}): ',
                                default_file_name)
    loaded_movies = load_movies_from_file(file_name)

    if not loaded_movies:
        print('Файл пустой или не существует! Фильмы не были загружены.')
        return movies, file_name

    print('Фильмы успешно загружены из файла!')
    return loaded_movies, file_name


def print_movies(movies: list[Movie]) -> None:
    """Выводит фильмы на экран в красивом формате, если они существуют"""
    if not movies:
        print('Не найдено ни одного фильма!')
        return

    print()
    for number, movie in enumerate(movies, start=1):
        hours = movie['duration'] // 60
        minutes = movie['duration'] % 60

        print(f'-------- {movie['title']} --------',
              f'Фильм №{number}',
              f'Режиссер: {movie['director']}',
              f'Сценарист: {movie['screenwriter']}',
              f'Длительность: {hours} часов, {minutes} минут',
              f'Год выпуска: {movie['year_released']}',
              (len(movie['title']) + 18) * '-',
              '\n', sep='\n', end='')


def save_movies(movies: list[Movie], default_file_name: str) -> str:
    """Сохраняет фильмы в файл, который задает пользователь, и возвращает
    имя последнего файла"""
    file_name = file_name_input('json',
                                f'Введите имя файла ({default_file_name}): ',
                                default_file_name)
    save_movies_to_file(movies, file_name)
    print('Фильмы успешно сохранены в файл!')
    return file_name


def change_search_query(filters: Filters) -> None:
    """Меняет запрос в параметрах поиска с клавиатуры"""
    filters['query'] = input('Найти (ничего для сброса): ')


def change_search_filters(filters: Filters) -> None:
    """Меняет фильтры в параметрах поиска с клавиатуры"""
    options = (
        ('год выхода', 'year_released', int, YEAR_RANGE),
        ('продолжительность (минуты)', 'duration', int, DURATION_RANGE)
    )
    print('1) Изменить фильтр по году',
          '2) Изменить фильтр по продолжительности',
          '3) Удалить фильтр по году',
          '4) Удалить фильтр по продолжительности',
          '5) Удалить все фильтры',
          '6) Выход', sep='\n')
    option_idx = required_input('Выберите действие: ', int,
                                value_range=(1, 6)) - 1

    if option_idx in (0, 1):
        prompt, attr, var_type, value_range = options[option_idx]
        value = required_input(f'Введите {prompt}: ', var_type,
                               value_range=value_range)
        filters[attr] = value
    elif option_idx == 2:
        filters['year_released'] = None
    elif option_idx == 3:
        filters['duration'] = None
    elif option_idx == 4:
        filters['year_released'] = None
        filters['duration'] = None
    elif option_idx == 5:
        return
    print('Фильтры успешно изменены!')


def add_new_movie() -> Movie:
    """Запрашивает у пользователя ввод данных о новом фильме с
    клавиатуры и добавляет результат в список"""
    title = required_input('Введите название: ').strip()
    director = required_input('Введите режиссера: ').strip()
    screenwriter = required_input('Введите сценариста: ').strip()
    duration = required_input('Введите длительность (в минутах): ', int,
                              value_range=DURATION_RANGE)
    year_released = required_input('Введите год выхода: ', int,
                                   value_range=YEAR_RANGE)

    new_movie = create_movie(title, director, screenwriter,
                             duration, year_released)
    print(f'Фильм "{title}" был успешно создан!')
    return new_movie


def remove_movie(movies: list[Movie], movies_to_display: list[Movie]) \
                -> Optional[list[Movie]]:
    """Позволяет пользователю удалить определенный элемент из списка
    найденных фильмов, модифицируя основной список"""
    print_movies(movies_to_display)
    if not movies_to_display:
        return None

    delete_num = required_input('Введите номер удаляемого элемента (0 для '
                                'выхода): ', int,
                                value_range=(0, len(movies)))
    if delete_num == 0:
        return None

    movie_to_delete = movies_to_display[delete_num - 1]
    new_movies = delete_movie(movies, movie_to_delete['id'])
    print(f'Фильм "{movie_to_delete['title']}" успешно удален!')
    return new_movies
