from selenium.webdriver.common.by import By

from src.utils.global_function import GlobalFunction


class SuccessAddMoreThanOneProductMoreThanOneItemsInBuckets:
    def __init__(self):
        self.__name_product = ""
        self.__count_product = 0

        print("1. Open Web Chrome (Has been login)")
        self.__driver = GlobalFunction.open_chrome("https://www.tokopedia.com/")
        GlobalFunction.delay(5)

    def get_driver(self):
        return self.__driver

    def main(self, list_search_data):
        count = len(list_search_data)
        self.__count_product = count
        index = 1
        for data in list_search_data:
            self.add_product(data)
            GlobalFunction.delay(5)

            self.go_to_detail_product()
            GlobalFunction.delay(5)

            self.set_item_product(3)  # Set 3 items every product
            GlobalFunction.delay(5)

            self.add_in_bucket()
            GlobalFunction.delay(5)

            self.close_frame()
            GlobalFunction.delay(5)

            # if index < count:
            #     index += 1
            #     self.close_frame()
            #     GlobalFunction.delay(5)
            # else:
            #     self.checklist_product_in_bucket()
            #     GlobalFunction.delay(5)

        self.checklist_product_in_bucket()
        GlobalFunction.delay(5)

        self.list_product_in_bucket()
        GlobalFunction.delay(5)

        self.delete_all_product_in_bucket()
        GlobalFunction.delay(5)

        return self.close_web()

    def main_without_close_web(self, list_search_data):
        count = len(list_search_data)
        self.__count_product = count
        index = 1
        for data in list_search_data:
            self.add_product(data)
            GlobalFunction.delay(5)

            self.go_to_detail_product()
            GlobalFunction.delay(5)

            self.set_item_product(3)  # Set 3 items every product
            GlobalFunction.delay(5)

            self.add_in_bucket()
            GlobalFunction.delay(5)

            self.close_frame()
            GlobalFunction.delay(5)

            # if index < count:
            #     index += 1
            #     self.close_frame()
            #     GlobalFunction.delay(5)
            # else:
            #     self.checklist_product_in_bucket()
            #     GlobalFunction.delay(5)

        self.checklist_product_in_bucket()
        GlobalFunction.delay(5)

        self.list_product_in_bucket()
        GlobalFunction.delay(5)

    def add_product(self, search_data):
        print(f"2. Add Sample Product from Result Search '{search_data}'")
        input_search_product = self.__driver.find_element(By.XPATH,"//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
        input_search_product.send_keys(search_data)
        GlobalFunction.delay(5)
        click_search_product = self.__driver.find_element(By.XPATH,"//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
        click_search_product.click()

    def go_to_detail_product(self):
        print("3. Choose and Go to Details Product")
        element_name_product = self.__driver.find_element(By.XPATH,"//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[3]/a/div[1]/div[2]/div[1]/span")
        self.__name_product = element_name_product.text
        click_detail_product = self.__driver.find_element(By.XPATH,"//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[3]/a")
        click_detail_product.click()

    def set_item_product(self, total_item):
        print(f"4. Set 3 Item for Product {self.__name_product}")
        btn_adding_product = self.__driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[2]")
        for item in range(total_item - 1):
            btn_adding_product.click()

    def add_in_bucket(self):
        print(f"4. Add Product {self.__name_product} to Bucket")
        btn_add_to_bucket = self.__driver.find_element(By.XPATH,"//*[@id='pdpFloatingActions']/div[4]/div[1]/button[1]")
        btn_add_to_bucket.click()

    def close_frame(self):
        print("5. Close Frame")
        btn_close_frame = self.__driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/article/header/button")
        btn_close_frame.click()

    def checklist_product_in_bucket(self):
        print("6. Check List Product in Bucket")
        btn_check_in_bucket = self.__driver.find_element(By.XPATH,"//*[@id='header-main-wrapper']/div[2]/div[3]/div[1]")
        btn_check_in_bucket.click()

    def list_product_in_bucket(self):
        print("7. Check List Bucket")

        for index in range(self.__count_product):
            # xpath_element_store = "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div"
            # element_store
            xpath_element = "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div[" + str(
                index + 1) + "]/div/div[2]/div/div[2]/div/div/div/div[1]/section[1]/span[1]"
            element_name_product_in_bucket = self.__driver.find_element(By.XPATH, xpath_element)
            name_product_in_bucket = element_name_product_in_bucket.get_attribute("title")
            print(f">>> Ada Produk '{name_product_in_bucket}' di Keranjang")

        # element_name_product_in_bucket_1 = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/section[1]/span[1]")
        # name_product_in_bucket_1 = element_name_product_in_bucket_1.get_attribute("title")
        # print(name_product_in_bucket_1)
        # # if name_product_in_bucket_1 == name_product_1:
        # #     print(f">> Product 1 - {name_product_1} in your bucket")
        # # else:
        # #     print(">> No product in your bucket")
        # element_name_product_in_bucket_2 = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div/div[1]/section[1]/span[1]")
        # name_product_in_bucket_2 = element_name_product_in_bucket_2.get_attribute("title")
        # print(name_product_in_bucket_2)
        # # if name_product_in_bucket_2 == name_product_2:
        # #     print(f">> Product 2 - {name_product_2} in your bucket")
        # # else:
        # #     print(">> No product in your bucket")

    def delete_all_product_in_bucket(self):
        print("8. Delete All Product in Bucket")
        btn_delete_list_product = self.__driver.find_element(By.XPATH,"//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/button")
        btn_delete_list_product.click()
        btn_ready_delete = self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/button[2]")
        btn_ready_delete.click()

    def close_web(self):
        print("9. Finish")
        self.__driver.close()
        return "VALID"
