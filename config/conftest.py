import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.fixture(scope="module")  # Фикстура для запуска браузера, с областью видимости на модуль (один раз на все тесты в
def browser():
    with sync_playwright() as p:  # Запускаем PlayWright (открываем контекст PlayWright)
        browser = p.firefox.launch(headless=False)  # запускаем Chromium браузер в видимом режиме (headless=False)
        yield browser  # Возвращаем браузер тестам
        browser.close()  # После окончания тестов закрываем браузер

@pytest.fixture
def page(browser):
    page = browser.new_page()  # создаем новую вкладку в браузере
    yield page  # передаем эту страницу тесту
    page.close()  # после теста нажимаем вкладку