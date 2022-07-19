from selenium.webdriver.common.by import By
from selenium.webdriver import Remote

from .base_page import BasePage
from .products_page import ProductsPage


class MainPage(BasePage):

    USERNAME_INPUT_LOCATOR = (By.ID, "user-name")
    PASSWORD_INPUT_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    ERROR_HEADER_LOCATOR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT_LOCATOR).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()
        return ProductsPage(self.driver)

    def login_expecting_error(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT_LOCATOR).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()
        return self.driver.find_element(*self.ERROR_HEADER_LOCATOR).text

    def is_login_form_visible(self):
        return self.driver.find_element(*self.USERNAME_INPUT_LOCATOR).is_displayed()\
               and self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR).is_displayed()\
               and self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).is_displayed()
