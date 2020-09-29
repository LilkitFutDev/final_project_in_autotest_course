import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import CartPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  ])
def test_guest_can_add_product_to_basket(browser,link):

        page = CartPage(browser,link)
        page.open()
        page.can_click_product_to_basket()
        page.assert_on_true_that_book_in_cart()
        page.assert_value_cart()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = CartPage(browser, link)
        page.open()
        page.can_click_product_to_basket()
        page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = CartPage(browser, link)
        page.open()
        page.should_not_be_success_message()

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

def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasePage(browser,link)
        page.open()
        page.go_to_busket()
        assert_on_busket = BasketPage(browser, link)
        assert_on_busket.should_not_be_items_in_basket()
        assert_on_busket.should_be_inscription_about_null_basket()










