
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from time import sleep




class Test_radio_button_test(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.url = "https://ultimateqa.com/simple-html-elements-for-automation/"
        self.d = webdriver.Chrome()
        self.d.implicitly_wait(5)
        self.d.get(self.url)
        self.d.maximize_window()

    def test_A(self):
        #button = self.d.find_element(By.XPATH, '//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[7]/div/div/div/form/input[1]')
        button_male = self.d.find_element(By.CSS_SELECTOR, "input[value='male']")
        button_female = self.d.find_element(By.CSS_SELECTOR, "input[value='female']")
        button_other = self.d.find_elements(By.NAME, "gender")[2]
        sleep(3)
        button_other.click()
        sleep(3)
        button_male.click()
        self.assertTrue(button_male.is_selected())

    # Closing the browser.
    def tearDown(self):
        self.d.close()


if __name__ == '__main__':
    unittest.main()