import test_data.registration_data
from tests.base_test import BaseTest
from time import sleep
from test_data.registration_data import RegistrationDataGenerator
from ddt import ddt, data, unpack
import datetime

from utils.custom_types import Gender


@ddt
class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Obiekt data ma mieć w sobie dane testowe
        self.data = RegistrationDataGenerator()
        self.authentication_page = self.home_page.click_sign_in()

    @data(*test_data.registration_data.get_csv_data("test_data/registration.csv"))
    @unpack
    def testNoLastname(self, gender, firstname, _, email, password, day, month, year):
        self.authentication_page.enter_create_account_email(email)
        self.create_account_page = self.authentication_page.click_create_account()
        self.create_account_page.choose_gender(gender)
        self.create_account_page.enter_first_name(firstname)
        self.assertEqual(email, self.create_account_page.get_entered_email())
        self.create_account_page.enter_password(password)
        self.create_account_page.select_date_of_birth(datetime.date(int(year), int(month), int(day)))
        self.create_account_page.click_register_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.create_account_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.create_account_page.get_visible_errors()
        expected_errors = ["lastname is required."]
        self.assertCountEqual(expected_errors, visible_errors)

    def testNoFirstname(self):
        self.authentication_page.enter_create_account_email(self.data.EMAIL)
        self.create_account_page = self.authentication_page.click_create_account()
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_last_name(self.data.LAST_NAME)
        self.assertEqual(self.data.EMAIL, self.create_account_page.get_entered_email())
        self.create_account_page.enter_password(self.data.PASSWORD)
        self.create_account_page.select_date_of_birth(self.data.DATE_OF_BIRTH)
        self.create_account_page.click_register_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.create_account_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.create_account_page.get_visible_errors()
        expected_errors = ["firstname is required."]
        self.assertCountEqual(expected_errors, visible_errors)