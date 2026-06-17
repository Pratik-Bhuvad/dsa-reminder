import smtplib
from email.message import EmailMessage

from ..config import GMAIL_SENDER_EMAIL as sender, GMAIL_APP_PASSWORD as password

def send_email(recipient: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    
    msg.set_content(body)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)