from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import unittest
from time import sleep


class Test_web_tables_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome()
        cls.d.implicitly_wait(5)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://www.techlistic.com/p/demo-selenium-practice.html"
        self.d.get(self.url)

    def test_table1(self):
        table = self.d.find_element(By.ID, "customers")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for i in range(1, len(rows)):
            cols = rows[i].find_elements(By.TAG_NAME, "td")

            print("Company: " + cols[0].text +
                  ", " + "Country: " + cols[2].text)

    @classmethod
    def tearDownClass(cls):
        cls.d.close()


if __name__ == '__main__':
    unittest.main()
