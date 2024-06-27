from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser


class BasePage(Browser):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.action.search')
    CART_BUTTON = (By.CSS_SELECTOR, '.action.showcart')

    BASE_URL = 'https://magento.softwaretestingboard.com/'

    # Functie pentru a astepta ca un element sa fie prezent
    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(expected_conditions.presence_of_element_located(element_locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def is_url_correct(self, expected_url):
        return expected_url == self.driver.current_url

    def type_text_on_search_input(self, text):
        self.type(self.SEARCH_INPUT, text)

    def click_on_wishlist_button(self):
        self.click(self.CART_BUTTON)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    # Functie pentru a selecta o valoare din Dropdown list
    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    # Functie pentru a bifa un checkbox
    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if not checkbox_element.is_selected():
            self.click(checkbox_element)

    # Functie pentru a debifa un checkbox
    def uncheck_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if checkbox_element.is_selected():
            self.click(checkbox_element)