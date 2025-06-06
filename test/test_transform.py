import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransform(unittest.TestCase):

    # Test transform_data dengan data produk yang valid
    def test_transform_data(self):
        # Data dummy produk yang valid
        products = [
            {'title': 'Product 1', 'price': '10000', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product 2', 'price': '20000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Women'}
        ]
        
        # Transformasi data menggunakan fungsi yang diujikan
        df = transform_data(products)
        
        # Cek bahwa jumlah baris sesuai dengan jumlah produk
        self.assertEqual(len(df), 2)
        # Pastikan kolom penting ada dalam DataFrame hasil
        self.assertIn('price', df.columns)
        self.assertIn('rating', df.columns)
        self.assertIn('timestamp', df.columns)
        # Pastikan nilai price dan rating sudah dikonversi menjadi angka dan bernilai positif
        self.assertTrue(df['price'].iloc[0] > 0)
        self.assertTrue(df['rating'].iloc[0] > 0)

    # Test transform_data dengan data produk yang memiliki nilai price tidak valid
    def test_invalid_price(self):
        # Data dummy dengan price yang tidak bisa dikonversi menjadi angka
        products = [
            {'title': 'Product 1', 'price': 'invalid_price', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'}
        ]
        
        # Transformasi data
        df = transform_data(products)
        
        # Baris dengan price tidak valid harus dibuang, sehingga panjang DataFrame = 0
        self.assertEqual(len(df), 0)

# Menjalankan unit test jika file ini dijalankan secara langsung
if __name__ == '__main__':
    unittest.main()
