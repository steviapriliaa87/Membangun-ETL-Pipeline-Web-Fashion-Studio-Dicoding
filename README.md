# Proyek ETL Pipeline

## Ringkasan Proyek

Proyek ini bertujuan untuk membangun pipeline ETL (Extract, Transform, Load) yang mengolah data produk dari situs **Fashion Studio Dicoding**. Data yang dikumpulkan akan diproses dan disimpan ke dalam berbagai media seperti file CSV, Google Sheets, serta database PostgreSQL. Proyek ini juga dilengkapi dengan pengujian unit untuk memastikan setiap proses berjalan dengan benar.

### Fitur Utama

- **Ekstraksi Data:** Mengambil informasi produk dari situs https://fashion-studio.dicoding.dev/.
- **Transformasi Data:** Melakukan pembersihan data, konversi harga ke dalam satuan Rupiah, menghapus data tidak valid, serta memastikan kesesuaian tipe data.
- **Pemuatan Data:** Menyimpan hasil akhir ke file CSV, spreadsheet Google Sheets, dan basis data PostgreSQL.
- **Pengujian Unit:** Menguji setiap komponen ETL secara terpisah untuk validasi fungsionalitas.

## Struktur Berkas

- `tests/test_extract.py` – Skrip pengujian unit untuk proses ekstraksi.
- `tests/test_transform.py` – Pengujian unit untuk proses transformasi data.
- `tests/test_load.py` – Unit test untuk tahap pemuatan data.
- `utils/extract.py` – Fungsi-fungsi untuk scraping data dari situs web.
- `utils/transform.py` – Modul yang menangani transformasi data termasuk konversi harga dan validasi.
- `utils/load.py` – Berisi fungsi untuk menyimpan data ke berbagai format/output.
- `main.py` – Skrip utama yang mengeksekusi seluruh pipeline ETL.
- `requirements.txt` – Daftar pustaka Python yang dibutuhkan.
- `google-sheets-api.json` – File akun layanan untuk mengakses Google Sheets (tidak disertakan karena alasan keamanan).
- `products.csv` – File CSV yang berisi hasil akhir data yang telah dibersihkan.

## Instalasi Dependensi

Sebelum menjalankan proyek, pastikan semua dependensi telah terpasang. Gunakan perintah berikut untuk menginstalnya:

```bash
pip install -r requirements.txt

## Cara Menjalankan

1. Pastikan Anda sudah mengaktifkan virtual environment.
2. Jalankan `main.py` untuk mengeksekusi pipeline ETL:

```bash
python main.py
```

3. Data yang telah diproses akan disimpan dalam file `products.csv` dan juga akan dimuat ke dalam Google Sheets.

## Unit Testing

Unit testing dilakukan untuk memastikan setiap fungsi dalam pipeline ETL berjalan sesuai dengan yang diharapkan. 

### Hasil Test Coverage

Berikut adalah hasil test coverage dari proyek ini:

```
Name                      Stmts   Miss  Cover
---------------------------------------------
tests\test_extract.py        28      2    93%
tests\test_load.py           21      1    95%
tests\test_transform.py      19      1    95%
utils\extract.py             30      3    90%
utils\load.py                27     11    59%
utils\transform.py           28      0   100%
---------------------------------------------
TOTAL                       153     18    88%
```