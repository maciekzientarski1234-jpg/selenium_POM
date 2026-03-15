from tests.base_test import BaseTest
from time import sleep

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email("jshjhd@gmail.com")
        self.create_account_page = self.authentication_page.click_create_account()

    def testNoLastname(self):
        self.create_account_page.enter_first_name("Marcin")
        sleep(3)