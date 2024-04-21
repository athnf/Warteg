# menu.py

menu = {
    1: {"nama": "Nasi Rames", "harga": 15000},
    2: {"nama": "Ayam Goreng", "harga": 12000},
    3: {"nama": "Tempe Goreng", "harga": 5000},
    4: {"nama": "Tahu Goreng", "harga": 5000},
    5: {"nama": "Sayur Asem", "harga": 10000},
    6: {"nama": "Sambal Terasi", "harga": 2000}
}

def tampilkan_menu():
    print("Menu Warteg:")
    print("===============")
    for nomor, item in menu.items():
        print(f"{nomor}. {item['nama']}: Rp{item['harga']}")
    print("===============")
