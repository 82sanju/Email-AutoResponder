from auth_gmail import get_gmail_service
import base64
from email.mime.text import MIMEText

def get_unread_emails():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', labelIds=['UNREAD'], maxResults=5).execute()
    messages = results.get('messages', [])

    email_data = []
    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = txt['payload']
        headers = payload.get("headers")
        subject = next(h['value'] for h in headers if h['name'] == 'Subject')
        sender = next(h['value'] for h in headers if h['name'] == 'From')
        body = base64.urlsafe_b64decode(payload['body'].get('data', '')).decode("utf-8", errors="ignore")
        email_data.append({'id': msg['id'], 'subject': subject, 'sender': sender, 'body': body})
    return email_data
