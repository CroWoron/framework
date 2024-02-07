import time

from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.enums.global_enums import TimeoutEnum


class BasePage:
    """
    Базовый класс страницы содержащий общие элементы
    """
    def __init__(self, browser):
        self.browser = browser

    def find_element_visibility(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод для поиска элементов с настройкой ожидания, пока элемент не станет видимым
        :param locator : локтор для поиска элемента
        :param timeout_for_wait : время ожидания появления элемента
        :return : web-element
        """

        try:
            element = WebDriverWait(self.browser, timeout_for_wait).until(
                EC.visibility_of_element_located(locator)
            )
            return element

        except TimeoutException as ex:
            raise ex

    def is_element_present(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод, проверяющий наличие элемента на странице
        :param locator : локтор для поиска элемента
        :param timeout_for_wait : время ожидания появления элемента
        :return : bool
        """

        try:
            self.find_element_visibility(locator, timeout_for_wait)
        except TimeoutException:
            return False
        return True

    def context_click_to_visible_element(self, locator):
        """
        Метод для нажатия правой кнопкой мыши на элемент.
        :param locator : локтор для поиска элемента
        """

        action = ActionChains(self.browser)
        try:
            element = self.find_element_visibility(locator)
            action.context_click(element)
            action.perform()
        except TypeError:
            action.context_click(locator)
            action.perform()

    def click_to_visible_element(self, locator):
        """
        Метод для клика по элементу, когда он станет видимым
        :param locator : локтор для поиска элемента
        """

        self.find_element_visibility(locator).click()

    def is_disappeared(self, locator, timeout_for_wait=TimeoutEnum.TEN_SEC.value):
        """
        Метод для проверки, что элемент исчез со страницы
        :param locator : локтор для поиска элемента
        :param timeout_for_wait : время ожидания появления элемента
        :return : bool
        """

        time.sleep(TimeoutEnum.ONE_SEC.value)
        try:
            WebDriverWait(self.browser, timeout_for_wait).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        time.sleep(TimeoutEnum.HALF_SEC.value)
        return True
