from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from time import sleep

# import actions class
from selenium.webdriver.common.action_chains import ActionChains


class Test_drag_and_drop(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.url = "https://demoqa.com/droppable"
        self.d = webdriver.Chrome()
        self.d.implicitly_wait(5)
        self.d.get(self.url)
        self.d.maximize_window()

    def test_drag_and_drop(self):
        source = self.d.find_element(By.ID, "draggable")
        target = self.d.find_element(By.ID, "droppable")

        mouse = ActionChains(self.d).drag_and_drop(source, target)
        mouse.perform()

        text = target.text

        self.assertEquals(text, "Dropped!")

    # Closing the browser.
    def tearDown(self):
        self.d.close()


if __name__ == '__main__':
    unittest.main()
