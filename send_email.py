import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
CREDENTIALS_FILE = "service_account.json"
FROM_EMAIL = "somakaushik98@gmail.com"
TO_EMAIL = "somasaikaushik@gmail.com"

def send_email(output):
    # Create the email message
    message = MIMEMultipart()
    message["From"] = FROM_EMAIL
    message["To"] = TO_EMAIL
    message["Subject"] = "GitHub Action - Python Output"
    body = f"The Python script completed. Here is the output:\n\n{output}"
    message.attach(MIMEText(body, "plain"))

    # Authenticate with Gmail using OAuth2
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)

    # Send the email using SMTP with OAuth2 credentials
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=creds)
        server.login(FROM_EMAIL, creds)

        server.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())

if __name__ == "__main__":
    output = "This is the default output message."
    send_email(output)
