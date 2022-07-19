from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec

from .base_page import BasePage
from .shopping_cart_page import ShoppingCartPage
from .sorting_order import SortingOrder


class ProductsPage(BasePage):

    SORT_SELECT_LOCATOR = (By.CSS_SELECTOR, "select[data-test='product_sort_container']")
    ACTIVE_OPTION_LOCATOR = (By.CSS_SELECTOR, "span.active_option")
    PRICES_LOCATOR = (By.CSS_SELECTOR, "div.inventory_item_price")
    SHOPPING_CART_LINK_LOCATOR = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def __init__(self, driver: Remote, should_open=False):
        super().__init__(driver)
        if should_open:
            self.driver.get("https://www.saucedemo.com/inventory.html")

    def go_to_shopping_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK_LOCATOR).click()
        return ShoppingCartPage(self.driver)

    def sort(self, order: SortingOrder):
        Select(self.driver.find_element(*self.SORT_SELECT_LOCATOR)
               ).select_by_visible_text(order.value)
        self.ui_animation_wait.until(
            ec.text_to_be_present_in_element(self.ACTIVE_OPTION_LOCATOR, order.value.upper())
        )

    def get_prices(self):
        return list(map(lambda x: float(x.text[1:]), self.driver.find_elements(*self.PRICES_LOCATOR)))

    def add_to_cart(self, item):
        self.driver.find_element(By.ID, f"add-to-cart-{item.lower().replace(' ', '-')}").click()
