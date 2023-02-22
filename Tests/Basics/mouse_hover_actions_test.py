from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from time import sleep

# import actions class
from selenium.webdriver.common.action_chains import ActionChains


class Test_mouse_hover_actions_test(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.url = "https://magento.softwaretestingboard.com/"
        self.d = webdriver.Chrome()
        self.d.implicitly_wait(5)
        self.d.get(self.url)
        self.d.maximize_window()

    def test_actions(self):
        # Create actions object
        actions = ActionChains(self.d)
        # find respective element locations
        first = self.d.find_element(By.XPATH, "//*[@id=\"ui-id-5\"]/span[2]")
        second = self.d.find_element(By.XPATH, "//*[@id=\"ui-id-17\"]/span[2]")
        third = self.d.find_element(By.XPATH, "//*[@id=\"ui-id-20\"]/span")

        # create actions queue
        actions.move_to_element(first).move_to_element(
            second).move_to_element(third).click()

        # Execute actions
        actions.perform()

        expected = self.d.find_element(
            By.XPATH, "//*[@id=\"page-title-heading\"]/span").text

        self.assertEquals(expected, "Hoodies & Sweatshirts")

    def tearDown(self):
        self.d.close()


if __name__ == '__main__':
    unittest.main()
