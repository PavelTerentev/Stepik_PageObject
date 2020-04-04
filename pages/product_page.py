from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_button_add_to_basket()
        self.solve_quiz_and_get_code()
        self.check_for_matching_names()
        self.check_price_matches()

    def click_button_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def check_for_matching_names(self):
        name_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        name_book_alert = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ALERT)
        assert name_book.text == name_book_alert.text, "Product names do not match"

    def check_price_matches(self):
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        assert basket_cost.text == price_product.text, "Product prices do not match"

    def should_close_messages(self):
        close_messages = self.browser.find_element(*ProductPageLocators.CLOSE_MESSAGES_1)
        close_messages.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "There is no success message, although there should be"
