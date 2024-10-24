from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.utils.global_function import GlobalFunction


class FailedGetProductAndShowErrMsg:
    def __init__(self):
        self.__name_product = ""

        print("1. Open Web Chrome (Has been login)")
        self.__driver = GlobalFunction.open_chrome("https://www.tokopedia.com/")
        GlobalFunction.delay(5)

    def main(self, search_data):
        self.add_product(search_data)
        GlobalFunction.delay(5)

        self.show_err_msg()
        GlobalFunction.delay(5)

        return self.close_web()

    def add_product(self, search_data):
        print(f"2. Add Sample Product '{search_data}'")
        input_search_product = self.__driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
        input_search_product.send_keys(search_data)
        GlobalFunction.delay(5)
        input_search_product.send_keys(Keys.ENTER)

    def show_err_msg(self):
        element_txt_err_msg = self.__driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]")
        if element_txt_err_msg.is_displayed():
            print(f">>> Error Message is Showing - {element_txt_err_msg.text}")

    def close_web(self):
        print("3. Finish")
        self.__driver.close()
        return "VALID"
