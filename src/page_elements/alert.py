from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class Alert(BasePage):
    """
    Элемент Алерт
    """
    ALERT_SUCCESS = (By.XPATH, '//div[contains(@class,"alert-success")]')
