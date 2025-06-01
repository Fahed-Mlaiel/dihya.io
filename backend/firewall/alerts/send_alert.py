# send_alert.py – Script d’envoi d’alerte sécurité (Dihya)
import smtplib, json, os
from email.message import EmailMessage

def send_security_alert(subject, message, to_email):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = os.getenv('ALERT_EMAIL_FROM', 'alert@dihya.app')
    msg['To'] = to_email
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)

if __name__ == '__main__':
    send_security_alert('Alerte Sécurité Dihya', 'Test d’alerte critique.', 'admin@dihya.app')
