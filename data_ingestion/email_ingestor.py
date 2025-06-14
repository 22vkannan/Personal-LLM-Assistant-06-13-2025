import imaplib, email, os
from memory.memory_store import store_memory

def fetch_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
    mail.select("inbox")
    _, data = mail.search(None, "ALL")
    for num in data[0].split()[-10:]:  # Last 10 emails
        _, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    store_memory(part.get_payload(decode=True).decode())
