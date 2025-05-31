import pytest  # импорт pytest
from playwright.sync_api import sync_playwright, Page, expect  # Импорт PlayWright (синхронный API), класс Page и функцию
from config.conftest import *

from src.data import *
from src.locator import *


@pytest.fixture
def tp_template_login(page: Page):
    def tp_template_login_fync():
        page.goto(URL_CAT_BUTTON)  # зашли на сайт
        page.click(LOCATOR_BASIC)  # кликнуть
        page.wait_for_timeout(1000)  # подождать
        page.go_back()  # вернуться назад

    return tp_template_login_fync


@pytest.fixture
def tp_template(page: Page):
    def tp_template_fync():
        page.click(LOCATOR_FIND)  # кликнуть вторую кнопку
        page.mouse.wheel(0, 1000)  # прокрутка вниз
        page.keyboard.press(LOCATOR_BUTTON)  # клавиатура жмет W
        page.click(LOCATOR_BUTTON_JUMP1)  # кнопка
        page.go_back()
        page.go_back()  # вернуться назад

        page.click(LOCATOR_DYNAMIC)
        page.click(LOCATOR_BUTTON_TABLE)
        page.fill(LOCATOR_ID, DATA_FILL)
        page.click(LOCATOR_REFRESH)

    return tp_template_fync
