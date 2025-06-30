from auth_gmail import get_gmail_service
from email.mime.text import MIMEText
import base64

def send_email(to, subject, message_text):
    service = get_gmail_service()
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = f"RE: {subject}"
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw}
    service.users().messages().send(userId='me', body=body).execute()
