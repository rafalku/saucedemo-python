from selenium.webdriver.common.by import By
from selenium.webdriver import Remote

from .base_page import BasePage
from .checkout_complete_page import CheckoutCompletePage


class CheckoutOverviewPage(BasePage):

    TOTAL_AMOUNT_LOCATOR = (By.CSS_SELECTOR, "div.summary_total_label")
    FINISH_BUTTON_LOCATOR = (By.ID, "finish")

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def get_total_amount(self):
        total = self.driver.find_element(*self.TOTAL_AMOUNT_LOCATOR)
        return float(total.text.split("$")[1])

    def finish(self):
        self.driver.find_element(*self.FINISH_BUTTON_LOCATOR).click()
        return CheckoutCompletePage(self.driver)
