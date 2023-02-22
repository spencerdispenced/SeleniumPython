from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expcon
from selenium.common.exceptions import NoSuchElementException

import unittest
from time import sleep

# Import excel modules

import xlrd
import xlwt
from xlutils.copy import copy


class Exceptions_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome()
        cls.d.implicitly_wait(2)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://www.saucedemo.com/"
        self.d.get(self.url)
        self.path = "data\SwagLogins.xls"

    def test_multiple_logins(self):
        try:
            # Open workbook, copy to writebook
            workbook = xlrd.open_workbook("data\SwagLogins.xls")
            writebook = copy(workbook)

            # Open first sheet via name, copy to writesheet
            sheet = workbook.sheet_by_name('logins')
            writesheet = writebook.get_sheet('logins')
            row_count = sheet.nrows  # Get the number of rows

        except Exception as e:
            print("FAIL: " + e)

        # Iterate over each row and print contents
        # Start at 1 to skip column titles
        for i in range(1, row_count):

            # Get respective username and password
            username = sheet.cell_value(i, 0)
            password = sheet.cell_value(i, 1)

            # Input current user and pass, then click login
            self.d.find_element(By.ID, "user-name").send_keys(username)
            self.d.find_element(By.ID, "password").send_keys(password)
            self.d.find_element(By.ID, "login-button").click()

            if self.check_exists_by_xpath("//*[@id=\"login_button_container\"]/div/form/div[3]"):
                # If login error message appears
                writesheet.write(i, 3, "FAIL")
                self.capture_error("login")
                self.d.refresh()
                continue

            else:
                # Logut
                self.d.find_element(By.ID, "react-burger-menu-btn").click()
                self.d.find_element(By.ID, "logout_sidebar_link").click()

                writesheet.write(i, 3, "PASS")  # Write pass to excel

        writebook.save(self.path)

    def check_exists_by_xpath(self, xpath):
        try:
            self.d.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def capture_error(self, msg):
        self.d.get_screenshot_as_file(f"Screenshots\SwagLogins_{msg}.png")

    @classmethod
    def tearDownClass(cls):
        cls.d.close()


if __name__ == '__main__':
    unittest.main()
