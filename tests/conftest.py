import pytest
import allure

from src.enums.global_enums import UrlEnum
from src.helpers.project_root import get_project_root
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser():
    """
    Подключение драйвера в начале теста и закрытие его в конце
    """
    with allure.step('set up'):
        root = get_project_root()
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        service = Service(f'{root}/src/data/chromedriver/chromedriver.exe')
        browser = webdriver.Chrome(options=options, service=service)
        yield browser
        browser.quit()


@pytest.fixture
def open_start_page(browser):
    """
    Открытие стартовой страницы
    :param browser: фикстура браузера
    """
    browser.get(f'{UrlEnum.PROTOCOL.value}{UrlEnum.HOST_PROD.value}')
