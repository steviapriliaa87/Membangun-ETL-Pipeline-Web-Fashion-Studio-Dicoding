import requests  # Library untuk melakukan HTTP request
from bs4 import BeautifulSoup  # Library untuk parsing HTML
from datetime import datetime  # Library untuk mendapatkan waktu saat ini

# Fungsi utama untuk melakukan scraping data produk dari suatu URL
def scrape_main(url):
    try:
        # Mengirimkan permintaan GET ke URL dengan batas waktu 10 detik
        response = requests.get(url, timeout=10)
        # Memunculkan exception jika status kode HTTP bukan 200
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Menampilkan pesan error jika URL tidak dapat diakses
        raise Exception(f"Failed to access URL: {url}. Details: {e}")

    try:
        # Parsing isi HTML dari halaman menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []  # List kosong untuk menampung semua data produk

        # Loop untuk mencari setiap elemen kartu produk berdasarkan class 'collection-card'
        for card in soup.find_all('div', class_='collection-card'):
            # Mengambil judul produk jika tersedia, jika tidak beri nilai default
            title_tag = card.find('h3', class_='product-title')
            title = title_tag.text.strip() if title_tag else 'Unknown Title'

            # Mengambil harga produk jika tersedia, jika tidak beri nilai default
            price_tag = card.find('div', class_='price-container')
            price = price_tag.text.strip() if price_tag else 'Price Unavailable'

            # Mengambil rating produk berdasarkan teks yang mengandung 'Rating'
            rating_tag = card.find('p', string=lambda text: text and 'Rating' in text)
            rating = rating_tag.text.strip() if rating_tag else 'No Rating'

            # Mengambil informasi warna berdasarkan teks yang mengandung 'Colors'
            colors_tag = card.find('p', string=lambda text: text and 'Colors' in text)
            colors = colors_tag.text.strip() if colors_tag else 'No Color Info'

            # Mengambil ukuran produk berdasarkan teks yang mengandung 'Size'
            size_tag = card.find('p', string=lambda text: text and 'Size' in text)
            size = size_tag.text.strip() if size_tag else 'No Size Info'

            # Mengambil informasi gender produk berdasarkan teks yang mengandung 'Gender'
            gender_tag = card.find('p', string=lambda text: text and 'Gender' in text)
            gender = gender_tag.text.strip() if gender_tag else 'No Gender Info'

            # Menambahkan data produk ke dalam list 'products' sebagai dictionary
            products.append({
                'title': title,
                'price': price,
                'rating': rating,
                'colors': colors,
                'size': size,
                'gender': gender,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Menyimpan waktu scraping
            })

        # Menampilkan jumlah produk yang berhasil diambil dari halaman
        print(f"Data scraping completed: {len(products)} products retrieved from {url}") 
        return products

    except Exception as e:
        # Menampilkan pesan error jika proses parsing HTML gagal
        raise Exception(f"Unable to parse HTML from {url}. Details: {e}")
