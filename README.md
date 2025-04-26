## Getting Started

### Prerequisites

- Python 3.6+
- Google Cloud account

### Obtaining client_secret.json

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing project
3. Enable the Google Sheets API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Sheets API" and enable it
4. Create service account credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Fill in the service account details and click "Create"
   - Grant the service account the "Editor" role for Google Sheets
   - Click "Done"
5. Create a key for the service account:
   - Go to the service account you just created
   - Under the "Keys" tab, click "Add Key" > "Create new key"
   - Choose JSON format and click "Create"
   - The key file will be automatically downloaded as client_secret.json
6. Place the downloaded client_secret.json in the project root directory

### Directory Structure

```
GoogleSheetsAPI/
├── client_secret.json  # Service account credentials (not committed to repository)
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── write_data.py       # Main script to write data to Google Sheets
```

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: activate
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Place your client_secret.json in the project root
2. Open write_data.py and update:
   - `SPREADSHEET_ID` with your Google Sheet ID
   - `RANGE_NAME` with your target sheet and cell range
   - `values` with the data you want to write

## Usage

Run the script to write data to your Google Sheet:

```bash
python write_data.py
```

### Sharing Your Spreadsheet

Make sure to share your Google Sheet with the service account email found in client_secret.json (`client_email` field). In your case, this is:
`googleseets-exercise@fifth-bonito-458003-a4.iam.gserviceaccount.com`

## Security Note

- Never commit your client_secret.json to public repositories
- Consider adding this file to your .gitignore
- If you accidentally expose your credentials, regenerate them immediately in the Google Cloud Console

## Dependencies

- [google-auth](https://pypi.org/project/google-auth/) ~=2.36
- [google-api-python-client](https://pypi.org/project/google-api-python-client/) ~=2.152
- [google-sheets-guide](https://developers.google.com/sheets/api/guides/values#methods.)
