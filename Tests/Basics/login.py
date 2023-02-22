from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

# Auto install Chrome webdriver
d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.saucedemo.com/"
d.get(url)

d.maximize_window()

d.find_element(By.ID, "user-name").send_keys("standard_user")
d.find_element(By.ID, "password").send_keys("secret_sauce")
d.find_element(By.ID, "login-button").click()

sleep(2)

d.close()
