"Тесты модуля database.py"
import unittest

import moviedb as db

LOAD_MOVIES_FILE_NAME = 'test-load.json'
SAVE_MOVIES_FILE_NAME = 'test-save.json'


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_movies: list[db.Movie] = []
        self.mock_movies.append(db.create_movie('Interstellar',
                                                'Christopher Nolan',
                                                'Jonathan Nolan', 169, 2014))
        self.mock_movies.append(db.create_movie('Movie', 'Director',
                                                'Screenwriter', 120, 2020))

    def test_create_movie(self) -> None:
        actual = self.mock_movies[0]
        expected: db.Movie = {
            'id': actual['id'],
            'title': 'Interstellar',
            'director': 'Christopher Nolan',
            'screenwriter': 'Jonathan Nolan',
            'duration': 169,
            'year_released': 2014
        }
        self.assertEqual(actual, expected)

    def test_delete_movie(self) -> None:
        id_to_delete = self.mock_movies[0]['id']
        actual = db.delete_movie(self.mock_movies, id_to_delete)
        expected: list[db.Movie] = [movie for movie in self.mock_movies
                                    if movie['id'] != id_to_delete]
        self.assertEqual(actual, expected)

    def test_find_movies(self) -> None:
        filters: db.Filters = {
            'query': 'mo',
            'duration': 120,
            'year_released': None
        }
        actual = db.find_movies(self.mock_movies, filters)
        expected = [movie for movie in self.mock_movies if
                    filters['query'] in movie['title'].lower() and
                    filters['duration'] == movie['duration']]
        self.assertEqual(actual, expected)

    def test_find_movies_no_matches(self) -> None:
        filters: db.Filters = {
            'query': 'will not find anything',
            'duration': 120,
            'year_released': None
        }
        actual = db.find_movies(self.mock_movies, filters)
        self.assertEqual(actual, [])

    def test_load_movies_from_file(self) -> None:
        actual = db.load_movies_from_file(LOAD_MOVIES_FILE_NAME)
        expected = self.mock_movies
        for i in range(len(self.mock_movies)):
            actual[i]['id'] = expected[i]['id']
        self.assertEqual(actual, expected)

    def test_save_movies_to_file(self) -> None:
        db.save_movies_to_file(self.mock_movies, SAVE_MOVIES_FILE_NAME)
        actual = db.load_movies_from_file(SAVE_MOVIES_FILE_NAME)
        expected = self.mock_movies
        self.assertEqual(actual, expected)
