import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine

# Fungsi untuk menyimpan DataFrame ke file CSV
def save_to_csv(df, filename="products.csv"):
    df.to_csv(filename, index=False)  # Simpan DataFrame ke CSV tanpa index
    print(f"Data successfully saved to CSV: {filename}")

# Fungsi untuk menyimpan DataFrame ke Google Sheets
def save_to_google_sheets(df, spreadsheet_id, range_name):
    # Autentikasi menggunakan file service account JSON
    creds = Credentials.from_service_account_file('google-sheets-api.json')
    service = build('sheets', 'v4', credentials=creds)  # Bangun service Google Sheets API
    sheet = service.spreadsheets()

    # Siapkan data: baris pertama adalah nama kolom, diikuti oleh isi datanya
    values = [df.columns.tolist()] + df.values.tolist()
    body = {'values': values}

    # Update data ke Google Sheets pada range yang ditentukan
    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

    print(f"Data successfully saved to Google Sheets: {spreadsheet_id}")

# Fungsi untuk memuat DataFrame ke tabel PostgreSQL
def load_to_postgresql(df, table_name='products'):
    try:
        # Konfigurasi koneksi database
        username = 'postgres'
        password = 'STEVISUKSESS887'  # Ganti password sesuai milikmu
        host = 'localhost'
        port = '5432'
        database = 'db_etl_pipeline'

        # Buat koneksi ke PostgreSQL menggunakan SQLAlchemy
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
        
        # Simpan DataFrame ke tabel PostgreSQL, timpa jika tabel sudah ada
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully saved to PostgreSQL table '{table_name}'")

    except Exception as e:
        # Tampilkan pesan error jika gagal menyimpan ke database
        print(f"Failed to save to PostgreSQL: {e}")
