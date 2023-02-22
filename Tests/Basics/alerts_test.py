
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# import explicit wait modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import unittest
from time import sleep


class Test_alerts_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome()
        cls.d.implicitly_wait(5)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://demoqa.com/alerts"  # site goes down sometimes
        self.d.get(self.url)

    def test_Regular_alert(self):
        self.d.find_element(By.ID, "alertButton").click()  # Click Alert button
        alert_msg = self.d.switch_to.alert.text  # Get alert text
        self.d.switch_to.alert.accept()  # Accept alert

        # assert alert text
        self.assertEqual(alert_msg, "You clicked a button")

    def test_Timer_alert(self):
        self.d.find_element(By.ID, "timerAlertButton").click()

        # Explicit wait for alert to appear
        WebDriverWait(self.d, 10).until(ec.alert_is_present())

        alert_msg = self.d.switch_to.alert.text
        self.d.switch_to.alert.accept()

        self.assertEqual(alert_msg, "This alert appeared after 5 seconds")

    def test_Accept_alert_message(self):
        # Click Alert button
        self.d.find_element(By.ID, "confirmButton").click()
        self.d.switch_to.alert.accept()  # Accept alert

        confirmMessage = self.d.find_element(By.ID, "confirmResult").text

        # assert alert text
        self.assertEqual(confirmMessage, "You selected Ok")

    def test_Dismiss_alert_message(self):
        self.d.find_element(By.ID, "confirmButton").click()
        self.d.switch_to.alert.dismiss()  # Dismiss alert

        confirmMessage = self.d.find_element(By.ID, "confirmResult").text

        # assert alert text
        self.assertEqual(confirmMessage, "You selected Cancel")

    def test_Prompt_alert(self):
        self.d.find_element(By.ID, "promtButton").click()
        send_message = "Spencer"
        self.d.switch_to.alert.send_keys(send_message)  # Send text to alert
        self.d.switch_to.alert.accept()

        confirmMessage = self.d.find_element(By.ID, "promptResult").text

        # assert alert text
        self.assertEqual(confirmMessage, "You entered " + send_message)

    @classmethod
    def tearDownClass(cls):
        cls.d.close()


if __name__ == '__main__':
    unittest.main()
