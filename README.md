import json
import os
from datetime import datetime

class InventoryApp:
    def __init__(self):
        self.inventory = []
        self.load_data()
    
    def load_data(self):
        if os.path.exists('inventory.json'):
            with open('inventory.json', 'r') as file:
                self.inventory = json.load(file)
    
    def save_data(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.inventory, file, indent=4)
    
    def add_item(self):
        print("\nTambah Barang Baru")
        name = input("Nama barang: ")
        
        # Cek apakah barang sudah ada
        for item in self.inventory:
            if item['nama'].lower() == name.lower():
                print("Barang sudah ada dalam inventori. Gunakan edit untuk mengubah.")
                return
        
        try:
            stock = int(input("Stok: "))
            price = float(input("Harga: "))
            
            new_item = {
                'nama': name,
                'stok': stock,
                'harga': price
            }
            
            self.inventory.append(new_item)
            self.save_data()
            print(f"Barang '{name}' berhasil ditambahkan!")
        except ValueError:
            print("Input tidak valid. Stok harus angka dan harga harus angka (gunakan titik untuk desimal).")
    
    def display_items(self):
        if not self.inventory:
            print("\nInventori kosong.")
            return
        
        print("\nDaftar Barang:")
        print("-" * 60)
        print(f"{'No.':<5} {'Nama':<20} {'Stok':<10} {'Harga':<15} {'Total Nilai':<15}")
        print("-" * 60)
        
        for idx, item in enumerate(self.inventory, 1):
            total_value = item['stok'] * item['harga']
            print(f"{idx:<5} {item['nama']:<20} {item['stok']:<10} {item['harga']:<15.2f} {total_value:<15.2f}")
        
        self.display_summary()
    
    def display_summary(self):
        total_items = len(self.inventory)
        total_stock = sum(item['stok'] for item in self.inventory)
        total_value = sum(item['stok'] * item['harga'] for item in self.inventory)
        
        print("\nRingkasan Inventori:")
        print(f"Jumlah barang unik: {total_items}")
        print(f"Total stok semua barang: {total_stock}")
        print(f"Total nilai inventori: {total_value:.2f}")
    
    def edit_item(self):
        self.display_items()
        if not self.inventory:
            return
        
        try:
            item_no = int(input("\nNomor barang yang akan diedit (0 untuk batal): "))
            if item_no == 0:
                return
            if item_no < 1 or item_no > len(self.inventory):
                print("Nomor tidak valid.")
                return
            
            item = self.inventory[item_no - 1]
            print(f"\nMengedit barang: {item['nama']}")
            
            name = input(f"Nama baru ({item['nama']}): ") or item['nama']
            stock = input(f"Stok baru ({item['stok']}): ")
            price = input(f"Harga baru ({item['harga']}): ")
            
            if stock:
                item['stok'] = int(stock)
            if price:
                item['harga'] = float(price)
            item['nama'] = name
            
            self.save_data()
            print("Barang berhasil diperbarui!")
        except ValueError:
            print("Input tidak valid. Stok harus angka dan harga harus angka.")
    
    def delete_item(self):
        self.display_items()
        if not self.inventory:
            return
        
        try:
            item_no = int(input("\nNomor barang yang akan dihapus (0 untuk batal): "))
            if item_no == 0:
                return
            if item_no < 1 or item_no > len(self.inventory):
                print("Nomor tidak valid.")
                return
            
            deleted_item = self.inventory.pop(item_no - 1)
            self.save_data()
            print(f"Barang '{deleted_item['nama']}' berhasil dihapus!")
        except ValueError:
            print("Input tidak valid. Masukkan nomor barang.")
    
    def search_item(self):
        if not self.inventory:
            print("\nInventori kosong.")
            return
        
        search_term = input("\nCari barang (nama atau sebagian nama): ").lower()
        found_items = [item for item in self.inventory if search_term in item['nama'].lower()]
        
        if not found_items:
            print("Tidak ditemukan barang yang sesuai.")
            return
        
        print("\nHasil Pencarian:")
        print("-" * 60)
        print(f"{'No.':<5} {'Nama':<20} {'Stok':<10} {'Harga':<15} {'Total Nilai':<15}")
        print("-" * 60)
        
        for idx, item in enumerate(found_items, 1):
            total_value = item['stok'] * item['harga']
            print(f"{idx:<5} {item['nama']:<20} {item['stok']:<10} {item['harga']:<15.2f} {total_value:<15.2f}")
    
    def export_to_file(self):
        if not self.inventory:
            print("\nInventori kosong. Tidak ada data untuk diexport.")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"inventory_export_{timestamp}.txt"
        
        with open(filename, 'w') as file:
            file.write("Daftar Barang\n")
            file.write("-" * 60 + "\n")
            file.write(f"{'No.':<5} {'Nama':<20} {'Stok':<10} {'Harga':<15} {'Total Nilai':<15}\n")
            file.write("-" * 60 + "\n")
            
            for idx, item in enumerate(self.inventory, 1):
                total_value = item['stok'] * item['harga']
                file.write(f"{idx:<5} {item['nama']:<20} {item['stok']:<10} {item['harga']:<15.2f} {total_value:<15.2f}\n")
            
            # Tambahkan ringkasan
            total_items = len(self.inventory)
            total_stock = sum(item['stok'] for item in self.inventory)
            total_value = sum(item['stok'] * item['harga'] for item in self.inventory)
            
            file.write("\nRingkasan Inventori:\n")
            file.write(f"Jumlah barang unik: {total_items}\n")
            file.write(f"Total stok semua barang: {total_stock}\n")
            file.write(f"Total nilai inventori: {total_value:.2f}\n")
        
        print(f"Data berhasil diexport ke file: {filename}")
    
    def menu(self):
        while True:
            print("\n=== APLIKASI INVENTORI ===")
            print("1. Tambah Barang")
            print("2. Tampilkan Daftar Barang")
            print("3. Edit Barang")
            print("4. Hapus Barang")
            print("5. Cari Barang")
            print("6. Export ke File")
            print("0. Keluar")
            
            choice = input("Pilihan: ")
            
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.display_items()
            elif choice == '3':
                self.edit_item()
            elif choice == '4':
                self.delete_item()
            elif choice == '5':
                self.search_item()
            elif choice == '6':
                self.export_to_file()
            elif choice == '0':
                print("Keluar dari aplikasi. Data disimpan.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    app = InventoryApp()
    app.menu()
