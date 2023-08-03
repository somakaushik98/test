import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.environ.get("GMAIL_USERNAME")
SMTP_PASSWORD = os.environ.get("GMAIL_PASSWORD")
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

    # Send the email using SMTP
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
    server.quit()

if __name__ == "__main__":
    output = "This is the default output message."
    send_email(output)
