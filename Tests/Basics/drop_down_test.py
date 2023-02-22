
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import unittest
from time import sleep
""" Unit test template for Chrome """


class Test_drop_down_test(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.url = "https://ultimateqa.com/simple-html-elements-for-automation/"
        self.d = webdriver.Chrome()
        self.d.implicitly_wait(5)
        self.d.get(self.url)
        self.d.maximize_window()

    def test_A(self):
        # Scroll to bottom of page
        self.d.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Get dropdown element
        dd = Select(self.d.find_element(
            By.XPATH, '//*[@id="post-909"]/div/div[1]/div/div[3]/div/div[1]/div[9]/div/div/div/select'))

        # Select 'Audi', by text shown in DD
        dd.select_by_visible_text('Aud')

        # Get current showing value in DD
        dd_text = dd.first_selected_option.text
        sleep(2)
        self.assertEquals(dd_text, 'Audi')

    # Closing the browser.
    def tearDown(self):
        self.d.close()


if __name__ == '__main__':
    unittest.main()
