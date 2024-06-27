from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WatchesPage(BasePage):

    LUMA_ANALOG_WATCH_CART_BUTTON = (
        By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[4]/div/div/div[3]/div/div[1]/form/button/span')
    CART_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')

    WATCHES_PAGE_URL = 'https://magento.softwaretestingboard.com/gear/watches.html'

    def navigate_to_watches_page(self):
        self.driver.get(self.WATCHES_PAGE_URL)

    def add_the_luma_analog_watch_to_cart(self):
        self.click(self.LUMA_ANALOG_WATCH_CART_BUTTON)

    def is_successful_added_to_cart(self):
        return self.is_element_displayed(self.CART_MESSAGE)

    def get_successful_added_to_cart_message(self):
        return self.get_element_text(self.CART_MESSAGE)