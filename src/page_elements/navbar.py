from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class Navbar(BasePage):
    """
    Навигационная панель выбора товаров
    """
    _navbar_element_wrapper = '//div[@id="narbar-menu"]//a[text()="{inner_text}"]'
    DROPDOWN_DESKTOPS = (By.XPATH, _navbar_element_wrapper.format(inner_text='Desktops'))
    DROPDOWN_LAPTOPS = (By.XPATH, _navbar_element_wrapper.format(inner_text='Laptops & Notebooks'))
    DROPDOWN_COMPONENTS = (By.XPATH, _navbar_element_wrapper.format(inner_text='Components'))
    DROPDOWN_TABLETS = (By.XPATH, _navbar_element_wrapper.format(inner_text='Tablets'))
    DROPDOWN_SOFTWARE = (By.XPATH, _navbar_element_wrapper.format(inner_text='Software'))
    DROPDOWN_PHONES = (By.XPATH, _navbar_element_wrapper.format(inner_text='Phones & PDAs'))
    DROPDOWN_CAMERAS = (By.XPATH, _navbar_element_wrapper.format(inner_text='Cameras'))
    DROPDOWN_MP3_PLAYERS = (By.XPATH, _navbar_element_wrapper.format(inner_text='MP3 Players'))

