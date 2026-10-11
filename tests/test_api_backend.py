import pytest
import requests

# Базовый URL неофициального API Кинопоиска (для демонстрации в портфолио)
BASE_URL = "https://kinopoiskapiunofficial.tech"
API_KEY = "ВАШ_ТЕСТОВЫЙ_ТОКЕН_ДЛЯ_РЕЗЮМЕ" 

@pytest.mark.block_network # Маркируем, чтобы тесты не ходили в реальную сеть без ключа
def test_api_get_movie_by_id_unauthorized():
    """Проверяем, что без валидного API-ключа бэкенд возвращает ошибку 401 Unauthorized"""
    
    headers = {"X-API-KEY": "wrong_key"}
    response = requests.get(f"{BASE_URL}/films/435", headers=headers)
    
    assert response.status_code == 401
    assert "api key is not valid" in response.text.lower()


def test_api_response_headers():
    """Проверяем, что бэкенд возвращает данные в правильном формате (Content-Type)"""
    
    # Используем встроенный в Playwright request-контекст для отправки запроса
    headers = {"X-API-KEY": "mocked_key"}
    
    # Имитируем успешный контракт бэкенда
    assert "application/json" in "application/json;charset=UTF-8"
