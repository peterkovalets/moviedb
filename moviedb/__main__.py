"Модуль для запуска пакета как скрипта"
import moviedb as db
import moviedb.menu as menu
from moviedb.utils import wait_for_input


def start(movies: list[db.Movie], filters: db.Filters, file_name: str) \
        -> tuple[bool, list[db.Movie], str]:
    """Функция, отвечающая за вызов функций меню, выход из программы и
    синхронизацию данных"""
    founded_movies = db.find_movies(movies, filters)
    menu_actions = (lambda: menu.load_movies(movies, file_name),
                    lambda: menu.print_movies(founded_movies),
                    lambda: menu.change_search_query(filters),
                    lambda: menu.change_search_filters(filters),
                    lambda: menu.add_new_movie(),
                    lambda: menu.remove_movie(movies, founded_movies),
                    lambda: menu.save_movies(movies, file_name))

    menu_option_idx = menu.get_menu_option_idx()
    if menu_option_idx == len(db.MENU_OPTIONS) - 1:
        return False, movies, file_name

    action = menu_actions[menu_option_idx]
    result = action()

    if isinstance(result, tuple):
        movies, file_name = result
    elif isinstance(result, str):
        file_name = result
    elif isinstance(result, list):
        movies = result
    elif isinstance(result, dict):
        movies.append(result)

    wait_for_input()
    return True, movies, file_name


def main() -> None:
    """Точка входа в программу"""
    movies: list[db.Movie] = []
    file_name = db.DEFAULT_FILE_NAME
    is_running = True
    filters: db.Filters = {
        'query': '',
        'year_released': None,
        'duration': None
    }

    while is_running:
        is_running, movies, file_name = start(movies, filters, file_name)


if __name__ == '__main__':
    main()
