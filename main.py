# Mengimpor fungsi-fungsi utama dari modul utils
from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, load_to_postgresql

def main():
    try:
        # URL utama dari website yang akan di-scrape
        base_url = 'https://fashion-studio.dicoding.dev/'
        all_products = []

        # Scrape halaman utama
        print(f"Scraping main page: {base_url}")
        try:
            products = scrape_main(base_url)
            all_products.extend(products)  # Tambahkan hasil scrape ke daftar produk
        except Exception as e:
            print(f"Failed to scrape main page! {e}")

        # Loop untuk scrape halaman 2 sampai 50
        for page in range(2, 51):
            url = f"{base_url}page{page}"
            print(f"Scraping page {page}: {url}")
            try:
                products = scrape_main(url)
                all_products.extend(products)
            except Exception as e:
                # Tangani error scrape per halaman agar proses tetap lanjut
                print(f"Failed to scrape page {page}: {e}")

        # Tampilkan total produk yang berhasil diambil
        print(f"\nSuccessfully scraped {len(all_products)} products")

        # Transformasi data mentah menjadi format yang siap dimuat
        transformed_data = transform_data(all_products)

        # Simpan data ke file CSV
        save_to_csv(transformed_data)

        # Load data ke database PostgreSQL
        load_to_postgresql(transformed_data)

        # Simpan data ke Google Sheets
        save_to_google_sheets(
            transformed_data,
            spreadsheet_id='1HT8ijac-WcgrmMqBey86JYyyR897WMeS8sjmB0',
            range_name='Sheet1!A1'
        )

    except Exception as e:
        # Tangani error fatal pada keseluruhan proses ETL
        print(f"ETL pipeline failed due to a fatal error! {e}")

# Menjalankan fungsi main jika script ini dieksekusi langsung
if __name__ == '__main__':
    main()
