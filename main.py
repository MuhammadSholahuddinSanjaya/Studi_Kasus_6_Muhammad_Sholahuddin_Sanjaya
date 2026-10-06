import json
import os

file_json = "inventaris.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Fungsi untuk membaca data dari file JSON
def baca_data():
    with open(file_json, "r") as file:
        data = json.load(file)
        return data

# 2. Fungsi untuk menyimpan data ke file JSON
def simpan_data(data):
    with open(file_json, "w") as file:
        json.dump(data, file, indent=4)

# 3. Fungsi untuk melihat barang (Read)
def tampilkan_barang():
    clear_screen()
    data = baca_data()
    print("DAFTAR BARANG")
    if len(data) == 0:
        print("Belum ada data barang di dalam gudang.")
    else:
        for barang in data:
            print("ID:", barang['id'], ", Nama:", barang['nama'], ", Stok:", barang['stok'], ", Harga: Rp", barang['harga'])

# 4. Fungsi untuk menambah barang (Create)
def tambah_barang():
    data = baca_data()
    
    id_baru = input("\nMasukkan ID Barang (contoh: B001): ")
    
    for barang in data:
        if barang["id"] == id_baru:
            print("Maaf, ID barang tersebut sudah ada!")
            return
            
    nama = input("Masukkan Nama Barang: ")
    stok = int(input("Masukkan Stok: "))
    harga = int(input("Masukkan Harga (Rp): "))
    
    barang_baru = {
        "id": id_baru,
        "nama": nama,
        "stok": stok,
        "harga": harga
    }
    
    data.append(barang_baru)
    
    simpan_data(data)
    print("Barang berhasil ditambahkan!")

# 5. Fungsi untuk mengubah stok dan harga barang (Update)
def ubah_barang():
    data = baca_data()
    
    id_ubah = input("\nMasukkan ID Barang yang mau diubah: ")
    
    ditemukan = False
    for barang in data:
        if barang["id"] == id_ubah:
            ditemukan = True
            print("Data saat ini:", barang['nama'], "(Stok:", barang['stok'], ")")
            barang["stok"] = int(input("Masukkan Stok Baru: "))
            barang["harga"] = int(input("Masukkan Harga Baru (Rp): "))
            break
            
    if ditemukan == True:
        simpan_data(data)
        print("Data barang berhasil diubah!")
    else:
        print("ID barang tidak ditemukan.")

# 6. Fungsi untuk menghapus barang (Delete)
def hapus_barang():
    data = baca_data()
    
    id_hapus = input("\nMasukkan ID Barang yang mau dihapus: ")
    
    ditemukan = False
    for barang in data:
        if barang["id"] == id_hapus:
            ditemukan = True
            data.remove(barang) # Menghapus item Dictionary dari List
            break
            
    if ditemukan == True:
        simpan_data(data)
        print("Data barang berhasil dihapus!")
    else:
        print("ID barang tidak ditemukan.")

# BAGIAN UTAMA PROGRAM (MENU)
def main():
    while True:
        print(" SISTEM INVENTARIS TOKO")
        print("1. Lihat Data Barang")
        print("2. Tambah Data Barang")
        print("3. Ubah Stok/Harga Barang")
        print("4. Hapus Data Barang")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            ubah_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break # Memecah perulangan while agar program berhenti
        else:
            print("Pilihan salah, silakan pilih angka 1 sampai 5.")

# Memanggil fungsi utama untuk menjalankan program
main()