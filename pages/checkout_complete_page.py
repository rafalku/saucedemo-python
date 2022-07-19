from selenium.webdriver.common.by import By
from selenium.webdriver import Remote

from .base_page import BasePage


class CheckoutCompletePage(BasePage):

    COMPLETE_HEADER_LOCATOR = (By.CSS_SELECTOR, "h2.complete-header")

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def get_complete_message(self):
        return self.driver.find_element(*self.COMPLETE_HEADER_LOCATOR).text
