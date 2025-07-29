import json
import os

DATA_FILE = "data_inventori.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def tambah_barang(data):
    nama = input("Nama Barang: ")
    stok = int(input("Stok: "))
    harga = float(input("Harga: "))
    data.append({"nama": nama, "stok": stok, "harga": harga})
    print("Barang berhasil ditambahkan.")

def tampilkan_barang(data):
    print("\nDaftar Barang:")
    for i, item in enumerate(data):
        print(f"{i+1}. {item['nama']} | Stok: {item['stok']} | Harga: {item['harga']}")

def edit_barang(data):
    tampilkan_barang(data)
    idx = int(input("Pilih nomor barang yang akan diedit: ")) - 1
    if 0 <= idx < len(data):
        data[idx]['nama'] = input("Nama baru: ")
        data[idx]['stok'] = int(input("Stok baru: "))
        data[idx]['harga'] = float(input("Harga baru: "))
        print("Barang berhasil diedit.")
    else:
        print("Nomor tidak valid.")

def hapus_barang(data):
    tampilkan_barang(data)
    idx = int(input("Pilih nomor barang yang akan dihapus: ")) - 1
    if 0 <= idx < len(data):
        del data[idx]
        print("Barang berhasil dihapus.")
    else:
        print("Nomor tidak valid.")

def cari_barang(data):
    keyword = input("Masukkan kata kunci nama barang: ").lower()
    hasil = [item for item in data if keyword in item['nama'].lower()]
    if hasil:
        for item in hasil:
            print(f"{item['nama']} | Stok: {item['stok']} | Harga: {item['harga']}")
    else:
        print("Barang tidak ditemukan.")

def laporan_ringkas(data):
    total_barang = len(data)
    total_nilai = sum(item['stok'] * item['harga'] for item in data)
    print(f"\nTotal Jenis Barang: {total_barang}")
    print(f"Total Nilai Inventori: Rp{total_nilai:,.2f}")

def menu():
    data = load_data()
    while True:
        print("\n--- Menu Inventori ---")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Cari Barang")
        print("6. Laporan Ringkas")
        print("7. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == '1':
            tambah_barang(data)
        elif pilih == '2':
            tampilkan_barang(data)
        elif pilih == '3':
            edit_barang(data)
        elif pilih == '4':
            hapus_barang(data)
        elif pilih == '5':
            cari_barang(data)
        elif pilih == '6':
            laporan_ringkas(data)
        elif pilih == '7':
            save_data(data)
            print("Data disimpan. Keluar.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
