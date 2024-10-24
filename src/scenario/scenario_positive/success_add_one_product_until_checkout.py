from selenium.webdriver.common.by import By
from src.utils.global_function import GlobalFunction
from success_add_one_product_in_bucket import SuccessAddOneProductInBucket
from success_add_one_product_more_than_one_items_in_bucket import SuccessAddOneProductMoreThanOneItemInBucket


class SuccessAddOneProductUntilCheckout:
    def __init__(self, types):
        self.__name_product = ""
        self.__total_item = 0
        self.__types_data = 0
        self.__status_checkout_product = "VALID"
        self.__driver = None
        self.__flow_add_product_in_bucket = None
        if types == 1:
            self.__flow_add_product_in_bucket = SuccessAddOneProductInBucket()
            self.__driver = self.__flow_add_product_in_bucket.get_driver()
        elif types == 2:
            self.__flow_add_product_in_bucket = SuccessAddOneProductMoreThanOneItemInBucket()
            self.__driver = self.__flow_add_product_in_bucket.get_driver()
            self.__types_data = types

    def main_one_item(self, search_data):
        self.__flow_add_product_in_bucket.main_without_close_web(search_data)
        GlobalFunction.delay(5)

        self.__name_product = self.__flow_add_product_in_bucket.get_name_product()

        self.checkout()
        GlobalFunction.delay(5)

        self.validate_checkout()
        self.delete_all_and_refresh()
        GlobalFunction.delay(5)

        return self.close_web()

    def main_more_than_one_product(self, list_search_data, total_item):
        self.__total_item = total_item
        self.__flow_add_product_in_bucket.main_without_close_web(list_search_data, total_item)
        GlobalFunction.delay(5)

        self.__name_product = self.__flow_add_product_in_bucket.get_name_product()

        self.checkout()
        GlobalFunction.delay(5)

        self.validate_checkout()
        self.delete_all_and_refresh()
        GlobalFunction.delay(5)

        return self.close_web()

    def checkout(self):
        print("6. Checkout")
        btn_checkout = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[2]/div/button")
        if btn_checkout.is_enabled():
            btn_checkout.click()
        else:
            print(">>> Tidak bisa checkout karena di keranjang kosong")

    def validate_checkout(self):
        print("7. Validate Checkout")
        element_checkout_name_product = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/p[1]")
        checkout_name_product = element_checkout_name_product.text
        if self.__name_product == checkout_name_product:
            print(f"Produk {checkout_name_product} ada di Halaman Checkout --> [VALID]")
        else:
            print(f"Produk {checkout_name_product} tidak ada di Halaman Checkout --> [NOT VALID]")
            self.__status_checkout_product = "NOT VALID"
        if self.__types_data == 2:
            element_checkout_total_items = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/span[1]")
            total_items = element_checkout_total_items.text
            if self.__total_item == int(total_items):
                print(f"Total Items Produk {checkout_name_product} sesuai di Halaman Checkout = {total_items} --> [VALID]")
            else:
                print(f"Total Items Produk {checkout_name_product} tidak sesuai di Halaman Checkout --> [NOT VALID]")
                self.__status_checkout_product = "NOT VALID"

    def delete_all_and_refresh(self):
        print("8. Back to Cart Page - Delete All")
        self.__driver.get("https://www.tokopedia.com/cart")
        self.__driver.refresh()
        GlobalFunction.delay(5)
        btn_delete_list_product = self.__driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/button")
        btn_delete_list_product.click()
        btn_ready_delete = self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/button[2]")
        btn_ready_delete.click()

    def close_web(self):
        print("8. Finish")
        self.__driver.close()
        return self.__status_checkout_product
