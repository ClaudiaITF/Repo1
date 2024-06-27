from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):

    FIRST_NAME_INPUT = (By.ID, 'firstName')
    LAST_NAME_INPUT = (By.ID, 'lastName')
    EMAIL_INPUT = (By.ID, 'email_address')
    PASSWORD_INPUT = (By.ID, 'password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'password_confirmation')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button/span')

    FIRST_NAME_ERROR = (By.ID, 'firstName-error')
    LAST_NAME_ERROR = (By.ID, 'lastName-error')
    EMAIL_ERROR = (By.ID, 'email_address-error')
    PASSWORD_ERROR = (By.ID, 'password-error')
    CONFIRM_PASSWORD_ERROR = (By.ID, 'password_confirmation-error')
    SUCCESSFUL_REGISTRATION_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div')

    REGISTER_PAGE_URL = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def navigate_to_register_page(self):
        self.driver.get(self.REGISTER_PAGE_URL)

    def set_first_name(self, first_name):
        self.type(self.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)

    def set_email_input(self, email):
        self.type(self.EMAIL_INPUT, email)


    def set_password_input(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def set_confirm_password_input(self, confirm_password):
        self.type(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    def click_register_button(self):
        self.click(self.REGISTER_BUTTON)

    def is_first_name_error_displayed(self):
        return self.is_element_displayed(self.FIRST_NAME_ERROR)

    def is_last_name_error_displayed(self):
        return self.is_element_displayed(self.LAST_NAME_ERROR)

    def is_email_name_error_displayed(self):
        return self.is_element_displayed(self.EMAIL_ERROR)

    def is_password_error_displayed(self):
        return self.is_element_displayed(self.PASSWORD_ERROR)

    def is_confirm_password_error_displayed(self):
        return self.is_element_displayed(self.CONFIRM_PASSWORD_ERROR)

    def is_successful_registration_message_displayed(self):
        return self.is_element_displayed(self.SUCCESSFUL_REGISTRATION_MESSAGE)

    def get_successful_registration_message_text(self):
        return self.get_element_text(self.SUCCESSFUL_REGISTRATION_MESSAGE)

