# Muhammad Sholahuddin Sanjaya

# NIM 2609116048

# Kelas B

## Penjelasan Kode Program

---

<img width="311" height="97" alt="Screenshot 2026-10-06 200254" src="https://github.com/user-attachments/assets/2ccdd1b2-2cc7-4e1a-a02e-2cd0ee889325" />

Bagian ini mengimpor modul json untuk menangani file JSON dan modul os untuk berinteraksi dengan sistem operasi (dalam hal ini, untuk membersihkan layar terminal). Variabel file_json menyimpan nama file yang akan digunakan untuk menyimpan data inventaris.

---

<img width="550" height="83" alt="Screenshot 2026-10-06 200301" src="https://github.com/user-attachments/assets/48d49176-353e-4dcc-aaac-7eff6531f743" />

Fungsi ini menggunakan os.system untuk menjalankan perintah yang membersihkan layar terminal. Perintah yang dijalankan bergantung pada sistem operasi: cls untuk Windows (ditandai dengan os.name == 'nt') dan clear untuk sistem operasi lain (seperti macOS atau Linux).

---

<img width="420" height="134" alt="Screenshot 2026-10-06 200332" src="https://github.com/user-attachments/assets/417b8d2f-4dfa-4c26-a1ff-826a004107e7" />

Fungsi ini bertugas membuka file JSON ("inventaris.json") dalam mode baca ("r") dan memuat isinya ke dalam variabel data menggunakan json.load(). Fungsi ini mengasumsikan file tersebut sudah ada. Data yang dimuat kemudian dikembalikan (return data).

---

<img width="524" height="111" alt="Screenshot 2026-10-06 200339" src="https://github.com/user-attachments/assets/ae564f86-112b-4445-982b-eeaaa898195b" />

Fungsi ini menerima data (yang sudah berupa List of Dictionaries) dan menyimpannya kembali ke dalam file JSON. File dibuka dalam mode tulis ("w"), yang berarti isi file sebelumnya akan ditimpa. json.dump() digunakan untuk menulis data ke file, dan indent=4 memastikan struktur JSON dalam file diformat dengan rapi agar mudah dibaca.

---

<img width="1173" height="267" alt="Screenshot 2026-10-06 200346" src="https://github.com/user-attachments/assets/84d22b7d-2bb0-4167-b76a-b7a0f652107c" />

Fungsi ini pertama-tama membersihkan layar, lalu memanggil baca_data() untuk mendapatkan data inventaris. Jika data kosong (panjangnya 0), program akan memberitahu pengguna. Jika ada data, program akan melakukan perulangan for untuk mencetak detail setiap barang (ID, Nama, Stok, Harga) ke layar.

---

<img width="654" height="613" alt="Screenshot 2026-10-06 200355" src="https://github.com/user-attachments/assets/e7c8f969-ac06-4d24-a2f3-bc0420086f70" />

Fungsi ini menangani penambahan barang baru.Pertama, ia membaca data yang ada.Kemudian, ia meminta pengguna untuk memasukkan ID barang baru.  

Terdapat perulangan untuk memeriksa apakah ID tersebut sudah ada dalam data; jika ya, fungsi akan berhenti (return) dan menampilkan pesan error.   

Jika ID unik, program meminta input nama, stok (diubah menjadi integer), dan harga (diubah menjadi integer).   

Data baru ini dibungkus dalam bentuk Dictionary (barang_baru) dan ditambahkan ke List data menggunakan .append().   

Terakhir, ia memanggil simpan_data() untuk memperbarui file JSON secara permanen.

---

<img width="837" height="463" alt="Screenshot 2026-10-06 200405" src="https://github.com/user-attachments/assets/ff843058-c410-4aab-b743-a0bb9edf86ee" />

Fungsi ini memungkinkan pengguna mengubah stok dan harga barang.   

Setelah membaca data dan meminta ID barang yang ingin diubah, ia menggunakan variabel ditemukan = False sebagai penanda.   

Program mencari barang dengan ID yang sesuai menggunakan perulangan for.

Jika ditemukan, ditemukan diubah menjadi True, lalu program meminta input stok dan harga baru untuk menggantikan nilai yang lama.  

Perintah break menghentikan pencarian setelah barang ditemukan.   

Jika ditemukan bernilai True, file JSON akan diperbarui dengan data yang telah dimodifikasi. Jika tidak, pesan error akan ditampilkan.

---

<img width="686" height="431" alt="Screenshot 2026-10-06 200413" src="https://github.com/user-attachments/assets/3b5dcf6b-766a-44d4-8d1d-399122e460f0" />

Logika fungsi ini mirip dengan ubah_barang, namun alih-alih mengubah nilai, ia menghapus seluruh dictionary barang dari list. Jika ID barang ditemukan, 

ia menggunakan fungsi data.remove(barang) untuk menghapusnya. File JSON kemudian diperbarui.

---

<img width="730" height="596" alt="Screenshot 2026-10-06 200420" src="https://github.com/user-attachments/assets/cc3dbb9a-c2aa-414e-89a8-b30cbecdb618" />

Ini adalah bagian utama program yang mengatur interaksi dengan pengguna.

while True menciptakan loop tak terbatas yang akan terus menampilkan menu pilihan hingga pengguna memilih untuk keluar.  

Berdasarkan input angka yang dipilih pengguna, program akan memanggil fungsi yang sesuai (tampilkan_barang, tambah_barang, dll.) 

menggunakan struktur percabangan if-elif-else.Jika pengguna memilih opsi "5", perintah break akan menghentikan loop while dan program pun selesai. 

---

<img width="548" height="72" alt="Screenshot 2026-10-06 200425" src="https://github.com/user-attachments/assets/d64b467b-3197-4252-9b61-e6bb83ab1396" />

perintah main() digunakan untuk memicu jalannya seluruh program.

---

## Hasil Output

### MENU Utama

<img width="279" height="161" alt="Screenshot 2026-10-06 201834" src="https://github.com/user-attachments/assets/f0dc0291-cb69-40c2-8fe1-24728ed59a0a" />

---

### Tampilkan Data

<img width="635" height="282" alt="Screenshot 2026-10-06 201850" src="https://github.com/user-attachments/assets/62489b16-f555-4c50-87f6-808fb90d56cd" />

---

### Ubah Data

<img width="656" height="519" alt="Screenshot 2026-10-06 201923" src="https://github.com/user-attachments/assets/bbe9831f-9efd-4d33-9651-300110abc366" />

Jika Data Sudah Ada

<img width="367" height="435" alt="Screenshot 2026-10-06 202112" src="https://github.com/user-attachments/assets/3dc7184c-f8d8-4701-9416-6f71657fc7d0" />

Jika Data Baru Ingin Ditambahkan

<img width="589" height="309" alt="Screenshot 2026-10-06 202121" src="https://github.com/user-attachments/assets/2b397f23-2f46-4eec-8fcf-fe103d27a690" />

Data Baru Muncul Di Menu Tampilan

<img width="801" height="647" alt="Screenshot 2026-10-06 202208" src="https://github.com/user-attachments/assets/5389b355-5b5f-410b-aaf5-f7e3934e7c7d" />

Data Baru Muncul Di File json

---

### Ubah Data

<img width="628" height="384" alt="Screenshot 2026-10-06 202330" src="https://github.com/user-attachments/assets/58f18449-cd54-4690-a01f-0cf15ec54d5f" />

Ubah data yang Akan mau diubah

<img width="1095" height="621" alt="Screenshot 2026-10-06 202343" src="https://github.com/user-attachments/assets/b74868c6-4aa3-460f-bbe1-4ba5d9bff015" />

Data Dalam File json Udah Berubah

---

<img width="480" height="209" alt="Screenshot 2026-10-06 202423" src="https://github.com/user-attachments/assets/71f4064b-c9d4-4f4a-a88b-abc6a807f482" />

Hapus data Yang Akan dihapus

<img width="1245" height="531" alt="Screenshot 2026-10-06 202436" src="https://github.com/user-attachments/assets/d70e65c8-4ce3-4f84-8a7d-57b8c304f8a3" />

Data pada file json Udah Diupdate dan data yang dihapus telah terhapus

---

<img width="506" height="170" alt="Screenshot 2026-10-06 202454" src="https://github.com/user-attachments/assets/19d3e0a5-ca1e-4891-a068-5dd51a65be13" />

Keluar Dari Program

---

<img width="596" height="256" alt="Screenshot 2026-10-06 202659" src="https://github.com/user-attachments/assets/2e92cd95-62bf-4db4-bea5-77d71ce511a3" />

tampilan data tetap sama meskipun program dirunning ulang

<img width="808" height="543" alt="Screenshot 2026-10-06 202707" src="https://github.com/user-attachments/assets/7ea955ef-0eb6-4055-ba78-60b17a6e4546" />

meskipun dirunning ulang Data pada file json tidak berubah sama sekali


