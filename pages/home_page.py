from pages.base_page import BasePage
from pages.authentication_page import AuthenticationPage
from selenium.webdriver.common.by import By

class Locators:
    """
    Home Page elements locators
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

class HomePage(BasePage):
    """
    Home Page Object
    """
    def click_sign_in(self):
        """
        Clicks Sign In and goes to Authentication Page
        :return: AuthenticationPage Object
        """
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()
        return AuthenticationPage(self.driver)