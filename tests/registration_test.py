from tests.base_test import BaseTest
from time import sleep
from test_data.registration_data_generator import RegistrationDataGenerator

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Obiekt data ma mieć w sobie dane testowe
        self.data = RegistrationDataGenerator()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email(self.data.EMAIL)
        self.create_account_page = self.authentication_page.click_create_account()


    def testNoLastname(self):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_first_name(self.data.FIRST_NAME)
        self.assertEqual(self.data.EMAIL, self.create_account_page.get_entered_email())
        self.create_account_page.enter_password(self.data.PASSWORD)
        self.create_account_page.select_date_of_birth(self.data.DATE_OF_BIRTH)
        self.create_account_page.click_register_button()
        visible_errors = self.create_account_page.get_visible_errors()
        expected_errors = ["lastname is required."]
        self.assertCountEqual(expected_errors, visible_errors)
        sleep(2)