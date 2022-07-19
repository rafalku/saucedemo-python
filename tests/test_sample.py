import pytest
from hamcrest import *

from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.sorting_order import SortingOrder


def test_login_successful(driver):
    products_page = MainPage(driver).login("standard_user", "secret_sauce")
    assert_that(products_page.get_header(), equal_to_ignoring_case("products"))


def test_login_invalid(driver):
    error = MainPage(driver).login_expecting_error("non-existing", "password")
    assert_that(error, equal_to("Epic sadface: Username and password do not match any user in this service"))


@pytest.fixture
def products_page(driver):
    MainPage(driver)
    driver.add_cookie({"name": "session-username", "value": "standard_user"})
    return ProductsPage(driver, True)


def test_logout(products_page: ProductsPage):
    main_page = products_page.logout()
    assert main_page.is_login_form_visible()


def test_sort_by_price(products_page: ProductsPage):
    products_page.sort(SortingOrder.PRICE_ASC)
    prices = products_page.get_prices()
    sorted_prices = prices.copy()
    sorted_prices.sort()
    assert_that(prices, contains_exactly(*sorted_prices))


@pytest.mark.parametrize("shopping_list", [
    ["Sauce Labs Bike Light",
     "Sauce Labs Backpack",
     "Sauce Labs Fleece Jacket"],
    ["Sauce Labs Onesie"]
])
def test_add_items_to_cart(products_page: ProductsPage, shopping_list):
    for item in shopping_list:
        products_page.add_to_cart(item)
    shopping_cart_page = products_page.go_to_shopping_cart()
    assert_that(shopping_cart_page.get_items(), contains_inanyorder(*shopping_list))


def test_complete_purchase(products_page: ProductsPage):
    products_page.add_to_cart("Sauce Labs Bike Light")
    checkout_page = products_page.go_to_shopping_cart().go_to_checkout()
    checkout_page.fill_in_form("John", "Doe", "123456")
    checkout_overview_page = checkout_page.continue_purchase()
    assert_that(checkout_overview_page.get_total_amount(), equal_to(10.79))
    checkout_complete_page = checkout_overview_page.finish()
    assert_that(checkout_complete_page.get_complete_message(), equal_to_ignoring_case("thank you for your order"))
