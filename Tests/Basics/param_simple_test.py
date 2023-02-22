from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import unittest
from time import sleep

# Import excel modules

import xlrd


class Param_simple_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Run Headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        cls.d = webdriver.Chrome(options=chrome_options)
        cls.d.implicitly_wait(5)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://demoqa.com/login"
        self.d.get(self.url)

    def test_multiple_logins(self):
        # Open workbook
        workbook = xlrd.open_workbook("Data\ToolQALogins.xls")

        # Open first sheet via index
        sheet = workbook.sheet_by_index(0)

        # Get the number of rows
        row_count = sheet.nrows

        expected_names = ["Billy", "Dave", "Bob", "Jill"]
        actual_names = []

        # Iterate over each row and print contents
        # Start at 1 to skip column titles
        for i in range(1, row_count):
            # Get respective username and password
            username = sheet.cell_value(i, 0)
            password = sheet.cell_value(i, 1)

            # Input current user and pass, then click login
            self.d.find_element(By.ID, "userName").send_keys(username)
            self.d.find_element(By.ID, "password").send_keys(password)
            self.d.find_element(By.ID, "login").click()

            # Get name of logged in user
            name = self.d.find_element(By.ID, "userName-value").text
            actual_names.append(name)

            # Logout
            self.d.find_element(By.ID, "submit").click()

        # Assert logged in names are accurate
        self.assertEquals(actual_names, expected_names)

    @classmethod
    def tearDownClass(cls):
        cls.d.close()


if __name__ == '__main__':
    unittest.main()
