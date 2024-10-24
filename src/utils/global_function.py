import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GlobalFunction:
    @staticmethod
    def open_chrome(link):
        user_path_chrome = "user-data-dir=C:/Users/kelvi/AppData/Local/Google/Chrome/User Data"
        options = Options()
        options.add_argument(user_path_chrome)
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        return driver

    @staticmethod
    def delay(times):
        time.sleep(times)
