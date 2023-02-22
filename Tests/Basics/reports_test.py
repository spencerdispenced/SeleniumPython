from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest

# Import html reports modules
# import HtmlTestRunner
# #from HtmlTestRunner import runner
from HtmlTestRunner.runner import HTMLTestRunner


class Test_Reports(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome()
        cls.d.implicitly_wait(5)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://demoqa.com/alerts"
        self.d.get(self.url)

    def test_Regular_alert(self):
        self.d.find_element(By.ID, "alertButton").click()
        alert_msg = self.d.switch_to.alert.text
        self.d.switch_to.alert.accept()
        self.assertEqual(alert_msg, "You clicked a button")

    def test_Timer_alert(self):
        self.d.find_element(By.ID, "timerAlertButton").click()
        WebDriverWait(self.d, 10).until(ec.alert_is_present())
        alert_msg = self.d.switch_to.alert.text
        self.d.switch_to.alert.accept()
        self.assertEqual(alert_msg, "This alert appeared after 5 seconds")

    def test_Accept_alert_message(self):
        self.d.find_element(By.ID, "confirmButton").click()
        self.d.switch_to.alert.accept()
        confirmMessage = self.d.find_element(By.ID, "confirmResult").text
        self.assertEqual(confirmMessage, "You selected Ok")

    def test_Dismiss_alert_message(self):
        self.d.find_element(By.ID, "confirmButton").click()
        self.d.switch_to.alert.dismiss()
        confirmMessage = self.d.find_element(By.ID, "confirmResult").text
        self.assertEqual(confirmMessage, "You selected Cancel")

    def test_Prompt_alert(self):
        self.d.find_element(By.ID, "promtButton").click()
        send_message = "Spencer"
        self.d.switch_to.alert.send_keys(send_message)
        self.d.switch_to.alert.accept()
        confirmMessage = self.d.find_element(By.ID, "promptResult").text
        self.assertEqual(confirmMessage, "You entered " + send_message)

    @classmethod
    def tearDownClass(cls):
        cls.d.close()


if __name__ == '__main__':
    # Create HTML test runner instance and pass to arg in main function, only work in terminal
    runner = HTMLTestRunner(
        output="../Reports", report_title="Alerts Tests", report_name="Alerts_Tests")
    unittest.main(testRunner=runner)
