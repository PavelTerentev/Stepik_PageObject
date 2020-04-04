from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_that_basket_empty(self):
        self.should_not_be_goods_in_the_basket()
        self.should_be_text_that_the_basket_is_empty()

    def should_not_be_goods_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "Success message is presented, but should not be"

    def should_be_text_that_the_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"



