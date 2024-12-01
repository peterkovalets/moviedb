# MovieDB

Пакет, позволяющий создать базу данных фильмов с возможностью добавления, удаления, загрузки и сохранения данных

```python
>>> import moviedb as db
>>> from moviedb.menu import print_movies
>>> movies: list[db.Movie] = []
>>> new_movie = db.create_movie('Interstellar', 'Christopher Nolan', 'Jonathan Nolan', 169, 2014)
>>> movies.append(new_movie)
>>> db.print_movies(movies)

-------- Interstellar --------
Фильм №1
Режиссер: Christopher Nolan
Сценарист: Jonathan Nolan
Длительность: 2 часов, 49 минут
Год выпуска: 2014
------------------------------
```

MovieDB доступен на PyPI:

```console
$ pip install moviedb
```