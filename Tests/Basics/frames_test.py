from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import unittest
from time import sleep


class Test_frames_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome()
        cls.d.implicitly_wait(5)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://demoqa.com/frames"
        self.d.get(self.url)

    def test_find_frame(self):
        self.d.switch_to.frame("frame1")
        actual_text = self.d.find_element(By.ID, "sampleHeading").text
        self.d.switch_to.default_content()  # go back to main content page

        self.assertEquals(actual_text, "This is a sample page")

    def test_find_top_middle_frame(self):
        # Change url for better testing
        self.d.get("http://the-internet.herokuapp.com/nested_frames")

        self.d.switch_to.frame("frame-top")
        self.d.switch_to.frame("frame-middle")
        actual_text = self.d.find_element(By.TAG_NAME, "body").text
        self.d.switch_to.default_content()

        self.assertEquals(actual_text, "MIDDLE")

    @classmethod
    def tearDownClass(cls):
        cls.d.close()


if __name__ == '__main__':
    unittest.main()
