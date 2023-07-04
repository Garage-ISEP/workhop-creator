from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://wwww.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE= 'garage-gpt-bf4b42e4da2e.json'
FOLDER_ID='1hQg0NptvMcv1_cmmEn2OrY7ZRuPYMre8'

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    return creds

def upload_photo(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': "Hello",
        "parents": [FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

upload_photo("output/️Cyber_3 JUL_post.png")
