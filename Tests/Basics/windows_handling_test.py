from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import unittest
from time import sleep


class Test_window_handling_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome()
        cls.d.implicitly_wait(5)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://demoqa.com/browser-windows"
        self.d.get(self.url)

    def test_A(self):
        expected_list = ["This is a sample page", "https://demoqa.com/sample",
                         "https://demoqa.com/browser-windows"]
        actual_list = []

        # click to open new tab
        self.d.find_element(By.ID, "tabButton").click()

        # Get all open window handles
        #handles = self.d.window_handles

        # Switch to newly opened tab
        # self.d.switch_to.window(handles[1])

        self.switch_tab("https://demoqa.com/sample")

        # Append new page text and new tab url
        actual_list.append(self.d.find_element(By.ID, "sampleHeading").text)
        actual_list.append(self.d.current_url)

        # Close current tab
        self.d.close()

        # Switch control back to first tab
        # self.d.switch_to.window(handles[0])
        self.switch_tab("https://demoqa.com/browser-windows")

        # Append current url to expected list to prove we moved back
        actual_list.append(self.d.current_url)

        # Assert expected and actual match
        self.assertEquals(actual_list, expected_list)

    def switch_tab(self, target):
        """ Helper method to switch tabs via url"""
        handles = self.d.window_handles
        for tab in handles:
            self.d.switch_to.window(tab)
            if self.d.current_url == target:
                break

    @classmethod
    def tearDownClass(cls):
        cls.d.quit()


if __name__ == '__main__':
    unittest.main()
