from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTER_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators:
    ADD_TO_BASKET = (By.ID, "add_to_basket_form")
    BOOK_NAME = (By.XPATH, "//h1")
    BOOK_NAME_ALERT = (By.XPATH, "//div[2]//div/div[1]/div/strong")
    BASKET_COST = (By.XPATH, "//div[3]/div/p[1]/strong")
    PRICE_PRODUCT = (By.XPATH, "//article/div[1]/div[2]/p[1]")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')
    CLOSE_MESSAGES_1 = (By.XPATH, '//*[@id="messages"]/div[1]/a')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "//div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_FORMSET = (By.ID, "basket_formset")
    BASKET_EMPTY = (By.XPATH, "//div[3]/div[2]/p")
    pass
