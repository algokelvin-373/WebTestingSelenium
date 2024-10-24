from src.utils.global_function import GlobalFunction
from failed_add_product_if_the_product_is_empty import FailedAddProductIfTheProductIsEmpty
from failed_checkout_if_the_product_in_bucket_is_empty import FailedCheckoutIfTheProductInBucketIsEmpty
from failed_get_product_and_show_err_msg import FailedGetProductAndShowErrMsg

if __name__ == '__main__':
    # Scenario 1
    print("Skenario 1: Gagal Menambah Produk ke Keranjang Jika Item Produk Habis. \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    scenario_negative_1 = FailedAddProductIfTheProductIsEmpty()
    print(f"Skenario 1: Gagal Menambah Produk ke Keranjang Jika Item Produk Habis. \t\t\t [HASIL: {scenario_negative_1.main(search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 2
    print("Skenario 2: Gagal Checkout dengan Kondisi Awal Ada Produk di Keranjang lalu Hapus Semua Produk di Keranjang. \t\t\t [PROSES TESTING]")
    list_search_product = {"keyboard", "mouse"}
    scenario_negative_2 = FailedCheckoutIfTheProductInBucketIsEmpty()
    print(f"Skenario 2: Gagal Checkout dengan Kondisi Awal Ada Produk di Keranjang lalu Hapus Semua Produk di Keranjang. \t\t\t [HASIL: {scenario_negative_2.main(list_search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 3
    print("Skenario 3: Gagal Dapat List Produk dan Menampilkan Pesan 'Produk tidak ditemukan'. \t\t\t [PROSES TESTING]")
    search_product = "1234567890abcde"
    scenario_negative_3 = FailedGetProductAndShowErrMsg()
    print(f"Skenario 3: Gagal Dapat List Produk dan Menampilkan Pesan 'Produk tidak ditemukan'. \t\t\t [HASIL: {scenario_negative_3.main(search_product)}]")
    GlobalFunction.delay(5)
