import unittest
from selenium import webdriver
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class Test(unittest.TestCase):
    def testTitle1(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertEqual("Google", titleOfWebPage, "Webpage Title is not same ")  # True

    def testTitle2(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertEqual("Google123", titleOfWebPage, "Webpage Title is not same ")  # False


if __name__ == "__main__":
    unittest.main()
