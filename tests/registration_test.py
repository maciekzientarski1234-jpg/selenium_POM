from tests.base_test import BaseTest
from time import sleep

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email("jshjhd@gmail.com")

    def testNoSurname(self):
        sleep(3)