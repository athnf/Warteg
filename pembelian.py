# pembelian.py
from .menu import menu, tampilkan_menu

def pesan_makanan():
    pesanan = {}
    while True:
        tampilkan_menu()
        pesanan_item = input("Masukkan nomor makanan yang ingin dipesan atau ketik 'selesai' untuk mengakhiri: ")

        if pesanan_item.lower() == 'selesai':
            break

        if pesanan_item.isdigit():
            nomor = int(pesanan_item)
            if nomor in menu:
                jumlah = int(input(f"Masukkan jumlah {menu[nomor]['nama']}: "))
                if jumlah > 0:
                    pesanan[menu[nomor]['nama']] = jumlah
                else:
                    print("Jumlah pesanan tidak valid.")
            else:
                print("Nomor menu tidak tersedia.")
        else:
            print("Masukkan nomor menu dengan benar.")

    return pesanan

def hitung_total(pesanan):
    total = 0
    for item, jumlah in pesanan.items():
        total += menu[item]['harga'] * jumlah
    return total

def tampilkan_struk(pesanan, total_harga):
    print("\n===== Struk Pembelian =====")
    for item, jumlah in pesanan.items():
        print(f"{item} x {jumlah}: Rp{menu[item]['harga'] * jumlah}")
    print(f"Total harga: Rp{total_harga}")
    print("===========================\n")
