from read_emails import get_unread_emails
from generate_reply import generate_reply
from send_email import send_email

def main():
    emails = get_unread_emails()
    for email in emails:
        reply = generate_reply(email)
        send_email(email['sender'], email['subject'], reply)
        print(f"Replied to: {email['sender']}")

if __name__ == "__main__":
    main()
