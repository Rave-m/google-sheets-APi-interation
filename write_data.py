from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = './client_secret.json' # api key spreadsheet

SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # mendefinisikan “izin” untuk membaca dan memodifikasi spreadsheets

credential = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1VTjrSr2cTfmeVg1wUnLeX2BE_8Aya6wG4QNr4NxaPHY' # id spreadsheet yang ingin diakses
RANGE_NAME = 'testing!A2:F11' # range yang ingin diakses

def main():
    try:
        service = build('sheets', 'v4', credentials=credential)
        sheet = service.spreadsheets()
        values = [
            ['Evans', 'Jl.Batik Kumeli, Kota Bandung', 'evansaja@gmail.com', 'Monitor Samsung 4K', '2', '9000000']
        ]
        body = {
            'values': values
        }

        result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption='RAW',
            body=body
        ).execute()

        print("Berhasil menambahkan data!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()