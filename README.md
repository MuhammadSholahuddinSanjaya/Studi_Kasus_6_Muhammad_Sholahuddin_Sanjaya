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
