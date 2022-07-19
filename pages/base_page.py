from abc import ABC

from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(ABC):

    UI_ANIMATION_TIMEOUT = 10
    MENU_BUTTON_LOCATOR = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK_LOCATOR = (By.ID, "logout_sidebar_link")
    HEADER_CONTAINER_LOCATOR = (By.CSS_SELECTOR, "#header_container span.title")

    def __init__(self, driver: Remote):
        self.driver = driver
        self.driver.maximize_window()
        self.ui_animation_wait = WebDriverWait(self.driver, self.UI_ANIMATION_TIMEOUT)

    def get_header(self):
        return self.driver.find_element(*self.HEADER_CONTAINER_LOCATOR).text

    def logout(self):
        self.driver.find_element(*self.MENU_BUTTON_LOCATOR).click()
        self.ui_animation_wait.until(
            ec.element_to_be_clickable(self.LOGOUT_LINK_LOCATOR)
        ).click()
        from .main_page import MainPage
        return MainPage(self.driver)
