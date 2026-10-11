import json
import os
from playwright.sync_api import Page

class MoviePage:
    def __init__(self, page: Page):
        self.page = page
        
        # Элементы интерфейса Кинопоиска (названия, рейтинги, описания)
        self.movie_title = page.locator("[data-tid='movie-title']")
        self.movie_rating = page.locator("[data-tid='rating-value']")
        self.movie_description = page.locator("[data-tid='movie-description']")
        self.error_notification = page.locator(".error-alert-box")

    def open_movie(self, movie_id: int):
        # Открываем страницу любого фильма
        self.page.goto(f"https://kinopoisk.ru{movie_id}/")

    def mock_movie_response(self, status_code: int, mock_filename: str):
        """Метод перехватывает запрос бэкенда Кинопоиска и подменяет его JSON-файлом"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", "mocks", mock_filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            mock_data = json.load(f)

        def handle_route(route):
            route.fulfill(
                status=status_code,
                content_type="application/json",
                body=json.dumps(mock_data)
            )

        # Перехватываем внутренний запрос сайта к данным о фильме
        self.page.route("**/api/v1/movie/*", handle_route)
