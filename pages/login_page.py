from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, 'email')
    PASS_INPUT = (By.ID, 'pass')
    SIGNIN_BUTTON = (By.XPATH, '//*[@id="send2"]/span')
    ERROR_MESSAGE_MAIN = (By.CSS_SELECTOR, 'div#email-error')
    ERROR_MESSAGE_EMAIL = (By.ID, 'Email-error')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@id="login-form"]/fieldset/div[4]/div[2]/a/span')

    LOGIN_PAGE_URL = 'https://magento.softwaretestingboard.com/customer/account/login'

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    # Funtie pentru seta o adresa de email neinregistrata folosind metoda set_email() de mai sus
    def set_unregistered_email(self):
        self.set_email('wrong_email@host.com')

    def set_password(self, password):
        self.type(self.PASS_INPUT, password)

    # Functie pentru a seta o parola folosind functia set_password() de mai sus
    def set_wrong_password(self):
        self.set_password('parolaoarecare')

    def click_login_button(self):
        self.click(self.SIGNIN_BUTTON)

    def is_main_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE_MAIN)

    def get_main_error_message_text(self):
        return self.get_element_text(self.ERROR_MESSAGE_MAIN)

    def is_email_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE_EMAIL)

    def get_email_error_message_text(self):
        return self.get_element_text(self.ERROR_MESSAGE_EMAIL)

    def click_forgot_password_link(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def the_account_signin_was_incorrect_message_displayed(self):
        return 'The account signin was incorrect' in self.get_main_error_message_text()