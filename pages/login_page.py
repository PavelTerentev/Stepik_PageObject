from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "word \"login\" not in url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME), "No login username"
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD), "No login password"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL), "No register email"
        assert self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1), "No register password 1"
        assert self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2), "No register password 2"


    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        register_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        register_password1.send_keys(password)
        register_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        register_password2.send_keys(password)
        register_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        register_submit.click()