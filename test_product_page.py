import time
import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import CartPage


@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  ])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = CartPage(browser, link)
    page.open()
    page.can_click_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = CartPage(browser, link)
    page.open()
    page.can_click_product_to_basket()
    page.should_not_be_success_message_with_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page() #тест тут падает, потому что в одном из заданий біло разместить invalid локатор

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_busket()
    assert_on_busket = BasketPage(browser, link)
    assert_on_busket.should_not_be_items_in_basket()
    assert_on_busket.should_be_inscription_about_null_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = CartPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = CartPage(browser, link)
    page.open()
    page.can_click_product_to_basket_without_solve()
    page.assert_on_true_that_book_in_cart()
    page.assert_value_cart()


@pytest.mark.basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        password = "AM7zewrhffewfi7we"
        page.register_new_user(email, password)

        base_page = BasePage(browser, link)
        base_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = CartPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = CartPage(browser, link)
        page.open()

        page.can_click_product_to_basket_without_solve()
        page.assert_on_true_that_book_in_cart()
        page.assert_value_cart()
