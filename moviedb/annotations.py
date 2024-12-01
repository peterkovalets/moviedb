"Модуль с аннотациями типов"
from typing import TypedDict, Optional

Movie = TypedDict('Movie', {
    'id': str,
    'title': str,
    'director': str,
    'screenwriter': str,
    'duration': int,
    'year_released': int
})

Filters = TypedDict('Filters', {
    'query': str,
    'year_released': Optional[int],
    'duration': Optional[int]
})
