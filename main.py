# main.py
from warteg.menu import tampilkan_menu
from warteg.pembelian import pesan_makanan, hitung_total, tampilkan_struk

def main():
    print("Selamat datang di Warteg ABC")
    pesanan = pesan_makanan()
    total_harga = hitung_total(pesanan)
    tampilkan_struk(pesanan, total_harga)

if __name__ == "__main__":
    main()
