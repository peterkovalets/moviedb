"Модуль с импортами основного функционала пакета"
from .database import (
    load_movies_from_file,
    save_movies_to_file,
    create_movie,
    delete_movie,
    find_movies
)
from .annotations import Movie, Filters
from .config import (
    DURATION_RANGE,
    DEFAULT_FILE_NAME,
    MENU_OPTIONS,
    YEAR_RANGE
)
