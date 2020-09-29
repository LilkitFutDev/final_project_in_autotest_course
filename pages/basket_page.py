from final_project_in_autotest_course.pages.base_page import BasePage
from final_project_in_autotest_course.pages.locators import Basket

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
       assert self.is_not_element_present(*Basket.BASKET_ITEMS), \
        "Items is presented, but should not be"

    def should_be_inscription_about_null_basket(self):
       assert self.is_element_present(*Basket.BASKET_NULL)