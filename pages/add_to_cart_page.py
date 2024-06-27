from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddToCartPage(BasePage):
    CART_ICON = (By.CLASS_NAME, 'showcart')
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, 'strong.subtitle.empty')
    WATCHES_ITEM = (By.CLASS_NAME, 'product-item-link')

    HOME_PAGE_URL = 'https://magento.softwaretestingboard.com/what-is-new.html'

    def navigate_to_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)

    def get_cart_empty_text(self):
        return self.get_element_text(self.CART_EMPTY_TEXT)

    def get_watches_name(self):
        return self.get_element_text(self.WATCHES_ITEM)