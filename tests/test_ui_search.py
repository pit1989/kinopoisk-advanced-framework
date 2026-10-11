from playwright.sync_api import expect

def test_ui_displays_mocked_movie_data(movie_page):
    """Тест проверяет, что интерфейс правильно отрисовывает данные из нашего успешного мока"""
    
    # 1. Настраиваем перехват: при запросе к API отдаем наш JSON с 'Зеленой милей'
    movie_page.mock_movie_response(status_code=200, mock_filename="movie_success.json")
    
    # 2. Открываем страницу (в реальности мок перехватит внутренний запрос страницы)
    movie_page.open_movie(435)
    
    # 3. Проверяем, что на экране появились именно наши замоканные данные
    expect(movie_page.movie_title).to_have_text("Зеленая миля")
    expect(movie_page.movie_rating).to_have_text("9.1")
    expect(movie_page.movie_description).to_contain_text("В тюрьме для смертников")


def test_ui_handles_server_error_gracefully(movie_page):
    """Тест проверяет, что при падении бэкенда (500) UI показывает ошибку, а не ломается"""
    
    # Подсовываем серверную ошибку 500 вместо данных
    movie_page.mock_movie_response(status_code=500, mock_filename="movie_404.json")
    
    movie_page.open_movie(435)
    
    # Проверяем, что интерфейс отреагировал понятным для пользователя уведомлением
    expect(movie_page.error_notification).to_be_visible()
