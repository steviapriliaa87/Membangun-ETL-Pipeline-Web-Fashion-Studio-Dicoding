import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_to_csv, save_to_google_sheets

class TestLoad(unittest.TestCase):
    # Unit test untuk fungsi save_to_csv
    # Menggunakan patch untuk memalsukan method to_csv dari pandas
    @patch('utils.load.pd.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        # Membuat dummy DataFrame untuk diuji
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Memanggil fungsi yang ingin diuji
        save_to_csv(df, 'test.csv')
        
        # Memastikan to_csv dipanggil sekali dengan argumen yang benar
        mock_to_csv.assert_called_once_with('test.csv', index=False)

    # Unit test untuk fungsi save_to_google_sheets
    # Patch digunakan untuk menggantikan dependencies eksternal (Google Sheets API)
    @patch('utils.load.build')  # Mock fungsi build dari Google API client
    @patch('utils.load.Credentials.from_service_account_file')  # Mock kredensial
    def test_save_to_google_sheets(self, mock_creds, mock_build):
        # Membuat dummy DataFrame untuk diuji
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Set mock return value untuk kredensial dan service build
        mock_creds.return_value = MagicMock()
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        
        # Memanggil fungsi yang ingin diuji
        save_to_google_sheets(df, 'spreadsheet_id', 'Sheet1!A2')
        
        # Memastikan bahwa update ke spreadsheet dipanggil sekali
        mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()

# Menjalankan unit test jika file ini dieksekusi langsung
if __name__ == '__main__':
    unittest.main()
