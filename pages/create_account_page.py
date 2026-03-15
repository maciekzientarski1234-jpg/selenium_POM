from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from time import sleep
from utils.custom_types import Gender

class Locators:
    """
    CreateAccountPage locators
    """
    FIRST_NAME = (By.ID, "customer_firstname")
    GENDER_MALE = (By.XPATH, '//label[@for="id_gender1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="id_gender2"]')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    REGISTER_BTN = (By.ID, 'submitAccount')


class CreateAccountPage(BasePage):
    """
    Create Account Page Object
    """
    def choose_gender(self, gender):
        """
        Choose Mr or Mrs
        """
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.GENDER_MALE).click()
        else:
            self.driver.find_element(*Locators.GENDER_FEMALE).click()

    def enter_first_name(self, first_name):
        """
        Enter First Name
        """
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def enter_password(self, password):
        """
        Enter Password
        """
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def get_entered_email(self):
        """
        Get Email entered on previous page
        """
        return self.driver.find_element(*Locators.EMAIL).get_attribute("value")




    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.FIRST_NAME))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BTN))