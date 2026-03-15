from faker import Faker
from utils.custom_types import Gender
import random

class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER= random.choice([Gender.MALE, Gender.FEMALE])
        self.__fake = Faker("pl_PL")
        if self.GENDER == Gender.FEMALE:
            self.FIRST_NAME = self.__fake.first_name_female()
        else:
            self.FIRST_NAME = self.__fake.first_name_male()
        self.EMAIL = self.__fake.email()
        self.PASSWORD = self.__fake.password()