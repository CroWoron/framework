from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class ProductCard(BasePage):
    """
    Карточка продукта
    """
    PRODUCT_CARD = (By.XPATH, '//div[contains(@class,"product-thumb")]')
    _button_wrapper = PRODUCT_CARD[1] + '//button[contains(@onclick,"{}")]'
    BUTTON_ADD_TO_CARD = (By.XPATH, _button_wrapper.format('cart.add'))
    BUTTON_ADD_TO_WISH_LIST = (By.XPATH, _button_wrapper.format('wishlist'))
    BUTTON_COMPARE_PRODUCT = (By.XPATH, _button_wrapper.format('compare'))
    CARD_TITLE = (By.XPATH, PRODUCT_CARD[1] + '//h4//a')
