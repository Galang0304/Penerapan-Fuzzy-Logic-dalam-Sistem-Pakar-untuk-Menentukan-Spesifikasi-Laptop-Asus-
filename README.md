# Sistem Pakar Rekomendasi Laptop menggunakan Logika Fuzzy

## Panduan Instalasi

### 1. Instalasi Python
1. Download Python dari website resmi: https://www.python.org/downloads/
2. Pilih "Download Python" (versi terbaru)
3. Buka file installer yang sudah didownload
4. **PENTING**: Centang opsi "Add Python to PATH" saat instalasi
5. Klik "Install Now"
6. Tunggu hingga proses instalasi selesai

### 2. Instalasi Library yang Diperlukan
1. Buka Command Prompt (CMD) atau PowerShell
2. Ketik perintah berikut satu per satu:
```
pip install numpy
pip install scikit-fuzzy
pip install matplotlib
```

## Cara Menjalankan Program
1. Download semua file program (fuzzy_laptop.py)
2. Buka Command Prompt (CMD) atau PowerShell
3. Arahkan ke folder tempat file program berada dengan perintah:
```
cd path/ke/folder/program
```
4. Jalankan program dengan perintah:
```
python fuzzy_laptop.py
```
5. Ikuti instruksi yang muncul di layar:
   - Masukkan harga laptop (dalam jutaan rupiah)
   - Masukkan RAM laptop (dalam GB)
   - Masukkan kapasitas penyimpanan/storage (dalam GB)

## Penjelasan Input
- Harga: Masukkan harga laptop dalam jutaan rupiah (contoh: untuk 8 juta, masukkan 8)
- RAM: Masukkan kapasitas RAM dalam GB (contoh: untuk 8GB, masukkan 8)
- Storage: Masukkan kapasitas penyimpanan dalam GB (contoh: untuk 512GB, masukkan 512)

## Troubleshooting
Jika terjadi error saat menjalankan program:
1. Pastikan Python sudah terinstall dengan benar (cek dengan perintah `python --version` di CMD)
2. Pastikan semua library sudah terinstall (cek dengan perintah `pip list`)
3. Pastikan berada di folder yang benar saat menjalankan program
4. Jika masih error, coba install ulang library dengan menambahkan `--user`:
```
pip install --user numpy scikit-fuzzy matplotlib
```

## Kontak
Jika ada pertanyaan atau kendala, silakan hubungi pembuat program. 