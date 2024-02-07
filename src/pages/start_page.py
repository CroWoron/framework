from src.page_elements.alert import Alert
from src.page_elements.navbar import Navbar
from src.page_elements.product_card import ProductCard

from src.pages.base_page import BasePage


class StartPage(BasePage):
    """
    Стартовая страница
    """
    @property
    def alert(self):
        return Alert(self.browser)

    @property
    def navbar(self):
        return Navbar(self.browser)

    @property
    def product_card(self):
        return ProductCard(self.browser)
