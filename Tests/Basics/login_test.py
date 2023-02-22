from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class login_test(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.url = "https://www.saucedemo.com/"
        self.d = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))

    def test_A(self):
        self.d.get(self.url)
        self.d.maximize_window()
        sleep(2)
        self.d.find_element(By.ID, "user-nam").send_keys("standard_user")
        sleep(2)

        self.d.find_element(By.ID, "password").send_keys("secret_sauce")
        sleep(2)

        self.d.find_element(By.ID, "login-button").click()

        page_text = self.d.find_element(
            By.XPATH, '//*[@id="header_container"]/div[2]/span').text

        self.assertEquals(page_text, "PRODUCTS")

        sleep(2)

    # Closing the browser.
    def tearDown(self):
        self.d.close()


if __name__ == '__main__':
    unittest.main()
