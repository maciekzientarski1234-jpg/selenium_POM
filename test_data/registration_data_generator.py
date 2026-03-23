from faker import Faker
from utils.custom_types import Gender
import random
import csv

def get_csv_data(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        # Pomiń pierwszy wiersz
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows


class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER= random.choice([Gender.MALE, Gender.FEMALE])
        self.__fake = Faker("pl_PL")
        if self.GENDER == Gender.FEMALE:
            self.FIRST_NAME = self.__fake.first_name_female()
            self.LAST_NAME = self.__fake.last_name_female()
        else:
            self.FIRST_NAME = self.__fake.first_name_male()
            self.LAST_NAME = self.__fake.last_name_male()
        self.EMAIL = self.__fake.email()
        self.PASSWORD = self.__fake.password()
        self.DATE_OF_BIRTH = self.__fake.date_of_birth()