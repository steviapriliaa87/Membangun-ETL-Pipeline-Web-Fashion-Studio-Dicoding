import unittest
from unittest.mock import patch, MagicMock
from utils.extract import scrape_main

class TestExtract(unittest.TestCase):

    # Unit test untuk memastikan scrape_main berhasil saat response valid
    @patch('utils.extract.requests.get')  # Mock permintaan HTTP
    def test_scrape_main_success(self, mock_get):
        url = "https://fashion-studio.dicoding.dev/"

        # Mock response yang dikembalikan oleh requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Test Product</h3>
                    <div class="price-container">$10</div>
                    <p>Rating: 5 stars</p>
                    <p>Colors: Red, Blue</p>
                    <p>Size: M, L</p>
                    <p>Gender: Unisex</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response  # Gunakan mock response saat requests.get dipanggil

        # Panggil fungsi yang diuji
        result = scrape_main(url)

        # Verifikasi hasil scrape
        self.assertIsInstance(result, list)               # Hasil harus berupa list
        self.assertGreater(len(result), 0)                # List tidak boleh kosong
        self.assertIn('title', result[0])                 # Harus ada key 'title' di dictionary produk
        self.assertEqual(result[0]['title'], 'Test Product')  # Nilai title harus sesuai dengan HTML mock

    # Unit test untuk memastikan scrape_main gagal saat terjadi error HTTP
    @patch('utils.extract.requests.get')
    def test_scrape_main_failure(self, mock_get):
        url = "https://fashion-studio.dicoding.dev/"

        # Mock response untuk error 404
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404 Client Error")  # Simulasikan exception
        mock_get.return_value = mock_response

        # Uji bahwa exception dilempar ketika scrape_main dipanggil
        with self.assertRaises(Exception) as context:
            scrape_main(url)
            # (Opsional) Cek pesan error-nya mengandung informasi yang sesuai
            self.assertIn('Failed to access URL', str(context.exception))

# Jalankan semua unit test saat file ini dieksekusi langsung
if __name__ == '__main__':
    unittest.main()
