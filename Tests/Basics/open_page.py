from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

# Auto install Chrome webdriver
d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open google.com
d.get("https://www.google.com")

d.maximize_window()

print(d.title)
print(d.current_url)

# d.get_screenshot_as_file("image1.png")
time.sleep(2)

d.get("https://www.freecodecamp.org/")
time.sleep(2)

d.back()
time.sleep(2)
d.refresh()
d.quit()

