import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, recipient):
    sender = "your_email@gmail.com"
    password = "your_app_password"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

print("Email service ready!")
