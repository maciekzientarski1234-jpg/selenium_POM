from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage

class Locators:
    """
    Authentication Page locators
    """
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")

class AuthenticationPage(BasePage):
    """
    Authentication Page Object
    """
    def enter_create_account_email(self, email):
        """
        Enter email for new user registration
        :param email:
        :return:
        """
        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)

    def click_create_account(self):
        """
        Clicks Create Account
        :return: CreateAccountPage Object
        """
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
        return CreateAccountPage(self.driver)