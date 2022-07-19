from selenium.webdriver.common.by import By
from selenium.webdriver import Remote

from .base_page import BasePage
from .checkout_overview_page import CheckoutOverviewPage


class CheckoutPage(BasePage):

    FIRST_NAME_INPUT_LOCATOR = (By.ID, "first-name")
    LAST_NAME_INPUT_LOCATOR = (By.ID, "last-name")
    POSTAL_CODE_INPUT_LOCATOR = (By.ID, "postal-code")
    CONTINUE_BUTTON_LOCATOR = (By.ID, "continue")

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def fill_in_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME_INPUT_LOCATOR).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT_LOCATOR).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT_LOCATOR).send_keys(postal_code)

    def continue_purchase(self):
        self.driver.find_element(*self.CONTINUE_BUTTON_LOCATOR).click()
        return CheckoutOverviewPage(self.driver)
