import pytest
from pages.movie_page import MoviePage

@pytest.fixture
def movie_page(page):
    """Фикстура автоматически создает и отдает объект страницы фильма в каждый тест"""
    return MoviePage(page)
