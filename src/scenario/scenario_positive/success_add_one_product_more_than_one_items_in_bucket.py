from selenium.webdriver.common.by import By

from src.utils.global_function import GlobalFunction


class SuccessAddOneProductMoreThanOneItemInBucket:
    def __init__(self):
        self.__name_product = ""
        self.__total_item_product = 0

        print("1. Open Web Chrome (Has been login)")
        self.__driver = GlobalFunction.open_chrome("https://www.tokopedia.com/")
        GlobalFunction.delay(5)

    def get_driver(self):
        return self.__driver

    def get_name_product(self):
        return self.__name_product

    def main(self, search_data, total_item):
        self.add_product(search_data)
        GlobalFunction.delay(5)

        self.go_to_detail_product()
        GlobalFunction.delay(5)

        self.set_item_product(total_item)
        GlobalFunction.delay(2)

        self.add_in_bucket()
        GlobalFunction.delay(5)

        self.list_product_in_bucket()
        GlobalFunction.delay(5)

        self.delete_all_product_in_bucket()
        GlobalFunction.delay(5)

        return self.close_web()

    def main_without_close_web(self, search_data, total_item):
        self.add_product(search_data)
        GlobalFunction.delay(5)

        self.go_to_detail_product()
        GlobalFunction.delay(5)

        self.set_item_product(total_item)
        GlobalFunction.delay(2)

        self.add_in_bucket()
        GlobalFunction.delay(5)

        self.list_product_in_bucket()
        GlobalFunction.delay(5)

    def add_product(self, search_data):
        print(f"2. Add Sample Product from Result Search '{search_data}'")
        input_search_product = self.__driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
        input_search_product.send_keys(search_data)
        GlobalFunction.delay(5)
        click_search_product = self.__driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
        click_search_product.click()

    def go_to_detail_product(self):
        print("3. Choose and Go to Details Product")
        element_name_product = self.__driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a/div[1]/div[2]/div[1]/span")
        self.__name_product = element_name_product.text
        click_detail_product = self.__driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a")
        click_detail_product.click()

    def set_item_product(self, total_item):
        print(f"4. Set 3 Item for Product {self.__name_product}")
        btn_adding_product = self.__driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[2]")
        for item in range(total_item - 1):
            btn_adding_product.click()

    def add_in_bucket(self):
        print(f"5. Add Product {self.__name_product} to Bucket")
        btn_add_to_bucket = self.__driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[4]/div[1]/button[1]")
        btn_add_to_bucket.click()

    def list_product_in_bucket(self):
        print("6. Check List Bucket")
        btn_check_in_bucket = self.__driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/article/div/section/div/button")
        btn_check_in_bucket.click()
        GlobalFunction.delay(2)
        element_name_product_in_bucket = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/section[1]/span[1]/a")
        name_product_in_bucket = element_name_product_in_bucket.text
        if name_product_in_bucket == self.__name_product:
            print(f">> Product '{self.__name_product}' in your bucket [MATCH]")
        element_total_item_product_in_bucket = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/input")
        total_item_product_in_bucket = element_total_item_product_in_bucket.get_attribute("value")
        if int(total_item_product_in_bucket) == self.__total_item_product:
            print(f">> Total Item: {total_item_product_in_bucket} [MATCH]")

    def delete_all_product_in_bucket(self):
        print("7. Delete All Product in Bucket")
        btn_delete_list_product = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/button")
        btn_delete_list_product.click()
        btn_ready_delete = self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/button[2]")
        btn_ready_delete.click()

    def close_web(self):
        print("8. Finish")
        self.__driver.close()
        return "VALID"
