import pandas as pd
import numpy as np
import warnings

# Nonaktifkan peringatan FutureWarning agar output lebih bersih
warnings.simplefilter(action='ignore', category=FutureWarning)
# Aktifkan peringatan eksplisit jika terjadi silent downcasting pada pandas
pd.set_option('future.no_silent_downcasting', True)

def transform_data(products):
    # Tampilkan jumlah total data hasil scraping sebelum transformasi
    print(f"\nTotal items scraped: {len(products)}")
    
    # Konversi data list of dict menjadi DataFrame
    df = pd.DataFrame(products)

    # Hapus baris yang mengandung 'unknown' pada kolom title
    df = df[~df['title'].str.lower().str.contains('unknown')]

    # Bersihkan kolom harga dari karakter selain angka dan titik
    df['price'] = df['price'].replace(r'[^\d.]', '', regex=True)
    df['price'] = df['price'].replace('', np.nan)  # Ganti string kosong jadi NaN
    df.dropna(subset=['price'], inplace=True)      # Hapus baris tanpa harga
    df['price'] = df['price'].astype(float) * 16000  # Konversi harga ke IDR

    # Bersihkan dan ubah kolom rating ke tipe float
    df['rating'] = df['rating'].replace(r'[^0-9.]', '', regex=True)
    df['rating'] = df['rating'].replace('', np.nan)
    df.dropna(subset=['rating'], inplace=True)
    df['rating'] = df['rating'].astype(float)

    # Ambil jumlah warna sebagai angka (contoh: "Colors: 3" jadi 3)
    df['colors'] = df['colors'].replace(r'\D', '', regex=True)
    df['colors'] = df['colors'].replace('', np.nan)
    df.dropna(subset=['colors'], inplace=True)
    df['colors'] = df['colors'].astype(int)

    # Hapus label 'Size:' dari data size
    df['size'] = df['size'].replace(r'Size:\s*', '', regex=True)

    # Hapus label 'Gender:' dari data gender
    df['gender'] = df['gender'].replace(r'Gender:\s*', '', regex=True)

    # Hapus data duplikat dan data kosong
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Tambahkan kolom timestamp dengan waktu saat transformasi dilakukan
    df['timestamp'] = pd.Timestamp.now().isoformat() 

    # Tampilkan jumlah data valid setelah transformasi
    print(f"Valid data count after transformation: {len(df)}")
    return df
