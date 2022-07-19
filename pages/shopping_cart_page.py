from selenium.webdriver.common.by import By
from selenium.webdriver import Remote

from .base_page import BasePage
from .checkout_page import CheckoutPage


class ShoppingCartPage(BasePage):

    ITEMS_LOCATOR = (By.CSS_SELECTOR, "div.inventory_item_name")
    CHECKOUT_BUTTON_LOCATOR = (By.ID, "checkout")

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def get_items(self):
        return list(map(lambda x: x.text, self.driver.find_elements(*self.ITEMS_LOCATOR)))

    def go_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON_LOCATOR).click()
        return CheckoutPage(self.driver)
