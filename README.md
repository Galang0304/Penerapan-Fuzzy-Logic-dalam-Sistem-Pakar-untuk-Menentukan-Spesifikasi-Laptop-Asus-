# Sistem Pakar Rekomendasi Laptop ASUS menggunakan Logika Fuzzy

Sistem pakar untuk merekomendasikan laptop ASUS berdasarkan budget, kebutuhan performa, dan ukuran layar yang diinginkan menggunakan metode Fuzzy Logic.

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
pip install pandas
pip install openpyxl
```

## Dataset yang Digunakan
Program ini menggunakan dataset laptop ASUS yang berisi informasi:
- Model Laptop
- Prosesor
- RAM
- Penyimpanan
- Kartu Grafis
- Ukuran Layar
- Harga (IDR)
- Tujuan Penggunaan
- Portabilitas
- Baterai
- Tahun Rilis

Contoh beberapa laptop dalam dataset:
1. ASUS VivoBook 14 (Intel i3, 4GB RAM, 256GB SSD) - Rp 6.000.000
2. ASUS ZenBook 13 (Intel i5, 8GB RAM, 512GB SSD) - Rp 14.000.000
3. ASUS ROG Strix G15 (Intel i7, 16GB RAM, 1TB SSD) - Rp 18.500.000

## Cara Menjalankan Program
1. Download semua file program (fuzzy_laptop.py dan dataset laptop asus.xlsx)
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
   - Masukkan budget (dalam jutaan rupiah)
   - Masukkan kebutuhan performa (skala 0-10)
   - Masukkan ukuran layar yang diinginkan (11-17 inch)

## Penjelasan Input & Output
### Input:
1. Budget: Masukkan budget dalam JUTAAN rupiah (contoh: untuk 8 juta, masukkan 8)
   - Minimal: 0 juta
   - Maksimal: 50 juta
   - Kategori:
     * Rendah: 0-15 juta
     * Sedang: 10-30 juta
     * Tinggi: 25-50 juta
   - Format: Angka saja tanpa titik/koma (contoh: 8)

2. Performa: Masukkan nilai 0-10
   - 0-4: Performa dasar (basic)
   - 3-7: Performa menengah (medium)
   - 6-10: Performa tinggi
   - Format: Angka saja (contoh: 7)

3. Ukuran Layar: Masukkan ukuran dalam inch (11-17)
   - 11-14: Layar kecil
   - 13-15: Layar sedang
   - 14-17: Layar besar
   - Format: Angka dengan 1 desimal jika perlu (contoh: 14 atau 14.5)

### Aturan Rekomendasi
Program akan memberikan rekomendasi berdasarkan kombinasi berikut:

1. Budget Rendah (0-15 juta):
   - Performa basic + Layar kecil = Rekomendasi
   - Performa basic + Layar sedang = Pertimbangkan
   - Performa medium + Layar kecil = Pertimbangkan

2. Budget Sedang (10-30 juta):
   - Performa medium + Layar sedang = Rekomendasi
   - Performa tinggi + Layar sedang = Rekomendasi
   - Performa medium + Layar besar = Pertimbangkan

3. Budget Tinggi (25-50 juta):
   - Performa tinggi + Layar besar = Rekomendasi
   - Performa tinggi + Layar sedang = Rekomendasi
   - Performa medium + Layar besar = Pertimbangkan

Kombinasi input yang tidak sesuai dengan aturan di atas akan mendapatkan status "Tidak Direkomendasikan".

### Contoh Input yang Valid:
```
=== Sistem Pakar Rekomendasi Laptop ASUS ===
Masukkan budget (dalam jutaan rupiah): 8
Masukkan kebutuhan performa (0-10): 7
Masukkan ukuran layar yang diinginkan (11-17 inch): 14
```

### Contoh Input yang TIDAK Valid:
```
Masukkan budget (dalam jutaan rupiah): 8000000    ❌ (salah, harusnya 8)
Masukkan budget (dalam jutaan rupiah): 8.000.000  ❌ (salah, harusnya 8)
Masukkan kebutuhan performa (0-10): 15           ❌ (salah, maksimal 10)
Masukkan ukuran layar yang diinginkan: 20        ❌ (salah, maksimal 17)
```

### Output:
Program akan memberikan:
1. Nilai rekomendasi (0-100)
2. Status rekomendasi:
   - "Sangat Direkomendasikan" (nilai ≥ 60)
   - "Pertimbangkan" (nilai 40-59)
   - "Tidak Direkomendasikan" (nilai < 40)
3. Detail kriteria pencarian (jika sangat direkomendasikan)

### Contoh Output yang Berhasil:
```
Nilai rekomendasi: 75.50
Status: Sangat Direkomendasikan

Kriteria pencarian:
- Budget: Rp 8,000,000
- Performa: 7
- Ukuran Layar: 14 inch
```

## Troubleshooting
Jika nilai rekomendasi selalu 0.00:
1. Pastikan input budget dalam JUTAAN rupiah (misal: 8 untuk 8 juta)
2. Pastikan nilai performa antara 0-10
3. Pastikan ukuran layar antara 11-17 inch
4. Jangan gunakan tanda titik atau koma dalam input

Jika terjadi error saat menjalankan program:
1. Pastikan Python sudah terinstall dengan benar (cek dengan perintah `python --version` di CMD)
2. Pastikan semua library sudah terinstall (cek dengan perintah `pip list`)
3. Pastikan berada di folder yang benar saat menjalankan program
4. Pastikan file dataset (dataset laptop asus.xlsx) berada dalam folder yang sama
5. Jika masih error, coba install ulang library dengan menambahkan `--user`:
```
pip install --user numpy scikit-fuzzy matplotlib pandas openpyxl
```

## Kontak
Jika ada pertanyaan atau kendala, silakan hubungi pembuat program. 