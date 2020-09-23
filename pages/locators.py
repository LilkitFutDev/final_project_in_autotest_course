from selenium.webdriver.common.by import By


from final_project_in_autotest_course.pages.base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(BasePage):
      LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
      REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
      URL = "login"


