import allure

from src.pages.start_page import StartPage

SECTION = 'Секция - Проверка карточки товара'


@allure.feature(SECTION)
class TestCheckProductCard:
    """
    Класс с тестами для проверки карточек товара"
    """

    @allure.title('добавление в корзину')
    @allure.severity(allure.severity('major'))
    @allure.sub_suite('добавление в корзину')
    def test_adding_to_basket(self, browser, open_start_page):
        start_page = StartPage(browser)
        with allure.step('Нажать на кнопку карточки "Добавить"'):
            start_page.click_to_visible_element(start_page.product_card.BUTTON_ADD_TO_CARD)
        with allure.step('Появляется allert'):
            assert start_page.is_element_present(start_page.alert.ALERT_SUCCESS), 'не появился allert'



