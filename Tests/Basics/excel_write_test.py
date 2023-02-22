from selenium.webdriver.common.by import By
from selenium import webdriver

# For Headless
from selenium.webdriver.chrome.options import Options

import unittest
from time import sleep

import xlwt


class Excel_write_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Run Headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        # Other optional headless options
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-gpu")
        cls.d = webdriver.Chrome(options=chrome_options)
        cls.d.implicitly_wait(5)
        cls.d.maximize_window()

    def setUp(self):
        self.url = "https://www.techlistic.com/p/demo-selenium-practice.html"
        self.d.get(self.url)

    def test_write_to_excel(self):
        table = self.d.find_element(By.ID, "customers")
        rows = table.find_elements(By.TAG_NAME, "tr")

        book = xlwt.Workbook()
        sheet = book.add_sheet("Customers", cell_overwrite_ok=True)

        # Write headers to excel
        headers = rows[0].find_elements(By.TAG_NAME, "th")
        for i in range(len(headers)):
            sheet.write(0, i, headers[i].text)

        # iterate over entire webtable
        for i in range(1, len(rows)):
            cols = rows[i].find_elements(By.TAG_NAME, "td")

            # Write data to excel
            for j in range(len(cols)):
                sheet.write(i, j, cols[j].text)

        # Save the excel file
        book.save("Data\Customers.xls")

    @classmethod
    def tearDownClass(cls):
        cls.d.close()


if __name__ == '__main__':
    unittest.main()
