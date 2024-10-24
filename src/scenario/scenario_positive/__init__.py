from src.utils.global_function import GlobalFunction
from success_increase_decrease_item_product import SuccessInCreaseDecreaseItemProduct
from success_add_one_product_in_bucket import SuccessAddOneProductInBucket
from success_add_more_than_one_product_in_bucket import SuccessAddMoreThanOneProductInBucket
from success_add_one_product_more_than_one_items_in_bucket import SuccessAddOneProductMoreThanOneItemInBucket
from success_add_more_than_one_product_more_than_one_items_in_bucket import SuccessAddMoreThanOneProductMoreThanOneItemsInBuckets
from success_add_one_product_until_checkout import SuccessAddOneProductUntilCheckout
from success_add_more_than_one_product_until_checkout import SuccessAddMoreThanOneProductUntilCheckout

if __name__ == '__main__':
    # Scenario 1
    print("Skenario 1: Sukses Menambah dan Mengurangi Item Pada Tiap Product di Keranjang. \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    scenario_positive_1 = SuccessInCreaseDecreaseItemProduct()
    print(f"Skenario 1: Sukses Menambah dan Mengurangi Item Pada Tiap Product di Keranjang. \t\t\t [HASIL: {scenario_positive_1.main(search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 2
    print("Skenario 2: Sukses Input Satu Product ke Keranjang. \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    scenario_positive_2 = SuccessAddOneProductInBucket()
    print(f"Skenario 2: Sukses Input Product ke Keranjang. \t\t\t [HASIL: {scenario_positive_2.main(search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 3
    print("Skenario 3: Sukses Input Lebih dari satu Product ke Keranjang. \t\t\t [PROSES TESTING]")
    list_search_product = {"Indomie", "Mie Sedap"}
    scenario_positive_3 = SuccessAddMoreThanOneProductInBucket()
    print(f"Skenario 3: Sukses Input Lebih dari satu Product ke Keranjang. \t\t\t [HASIL: {scenario_positive_3.main(list_search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 4
    print("Skenario 4: Sukses Input Satu Product dengan jumlah item lebih dari satu ke Keranjang. \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    total_item = 5
    scenario_positive_4 = SuccessAddOneProductMoreThanOneItemInBucket()
    print(f"Skenario 4: Sukses Input Satu Product dengan jumlah item lebih dari satu ke Keranjang. \t\t\t [HASIL: {scenario_positive_4.main(search_product, total_item)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 5
    print("Skenario 5: Sukses Input Lebih dari satu Product ke Keranjang yang dimana tiap product lebih dari satu item. \t\t\t [PROSES TESTING]")
    list_search_product = {"Indomie", "Kacang"}
    scenario_positive_5 = SuccessAddMoreThanOneProductMoreThanOneItemsInBuckets()
    print(f"Skenario 5: Sukses Input Lebih dari satu Product ke Keranjang yang dimana tiap product lebih dari satu item. \t\t\t [HASIL: {scenario_positive_5.main(list_search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 6
    print("Skenario 6: Sukses Melakukan Checkout dan Verifikasi bahwa Produk ada di Daftar Belanja (Satu Produk satu item) \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    scenario_positive_6 = SuccessAddOneProductUntilCheckout(1)
    print(f"Skenario 6: Sukses Melakukan Checkout dan Verifikasi bahwa Produk ada di Daftar Belanja (Satu Produk satu item) \t\t\t [HASIL: {scenario_positive_6.main_one_item(search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 7
    print("Skenario 7: Sukses Melakukan Checkout dan Verifikasi bahwa Produk ada di Daftar Belanja (Satu Produk lebih dari satu item) \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    total_item = 5
    scenario_positive_7 = SuccessAddOneProductUntilCheckout(2)
    print(f"Skenario 7: Sukses Melakukan Checkout dan Verifikasi bahwa Produk ada di Daftar Belanja (Satu Produk lebih dari satu item) \t\t\t [HASIL: {scenario_positive_7.main_more_than_one_product(search_product, total_item)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 8
    # print("Skenario 8: Sukses Melakukan Checkout dan Verifikasi bahwa Produk ada di Daftar Belanja (Lebih Dari Satu Produk satu item) \t\t\t [PROSES TESTING]")
    # list_search_product = {"Matras", "Indomie"}
    # scenario_positive_8 = SuccessAddMoreThanOneProductUntilCheckout(1)
    # print(f"Skenario 8: Sukses Melakukan Checkout dan Verifikasi bahwa Produk ada di Daftar Belanja (Lebih Dari Satu Produk satu item) \t\t\t [HASIL: {scenario_positive_8.main_one_items(list_search_product)}]")
    # GlobalFunction.delay(5)
