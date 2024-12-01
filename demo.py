"Демонстрационный файл с примером работы"
import moviedb as db
from moviedb.menu import display_menu, print_movies
from moviedb.utils import wait_for_input


FILE_NAME_TO_SAVE = 'example.json'
MOVIE_ID_TO_DELETE = '66cff4e2-7bac-4f1f-b6be-1f15fffc3872'


def main() -> None:
    "Точка входа в программу"
    filters_1: db.Filters = {
        'query': 'Ave',
        'duration': None,
        'year_released': None
    }
    filters_2: db.Filters = {
        'query': '',
        'duration': 169,
        'year_released': 2014
    }

    display_menu()
    wait_for_input()

    # Загрузка фильмов из файла
    print(f'Фильмы загружены из файла {db.DEFAULT_FILE_NAME}!')
    movies: list[db.Movie] = db.load_movies_from_file(db.DEFAULT_FILE_NAME)
    print_movies(movies)
    wait_for_input()

    # Поиск фильмов по наименованию
    found_movies = db.find_movies(movies, filters_1)
    print(f'Найдены фильмы по запросу "{filters_1['query']}"!')
    print_movies(found_movies)
    wait_for_input()

    # Поиск фильмов по году выхода и продолжительности
    found_movies = db.find_movies(movies, filters_2)
    print(f'Найдены фильмы по {filters_2['year_released']} году выхода '
          f'и продолжительности {filters_2['duration']} минут')

    # Создание фильма
    movies.append(db.create_movie('Test', 'test director',
                                  'test screenwriter', 120, 2008))
    print(f'Добавлен новый фильм "{movies[-1]['title']}"!')
    print_movies(movies)
    wait_for_input()

    # Удаление фильма (Interstellar)
    movies = db.delete_movie(movies, MOVIE_ID_TO_DELETE)
    print(f'Удален фильм с id "{MOVIE_ID_TO_DELETE}"!')
    print_movies(movies)
    wait_for_input()

    # Сохранение фильмов в файл
    db.save_movies_to_file(movies, FILE_NAME_TO_SAVE)
    print(f'Полученные фильмы сохранены в файл {FILE_NAME_TO_SAVE}!')
    wait_for_input()


if __name__ == '__main__':
    main()
