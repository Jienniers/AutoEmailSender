import os
from email.message import EmailMessage
import ssl
import smtplib
from email_validator import validate_email, EmailNotValidError


def is_valid_email(email):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        return False


def process_email(email):
    send_email(email=email)

def main():
    file_path = "emails.txt" 
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r') as file:
            for line in file:
                email = line.strip()

                if is_valid_email(email):
                    process_email(email)

    except Exception as e:
        print(f"An error occurred: {e}")


def send_email(email):
    with open("login.txt", "r") as f:
        login = [line.strip() for line in f]

    email_Sender = login[0]
    email_password = login[1]
    email_receiver = email

    with open("subject.txt", "r") as f:
        subj_text = [line.strip() for line in f]

    subject = subj_text[0]
    file = open('body.txt',mode='r')
    body_text = file.read()

    email = EmailMessage()

    email["From"] = email_Sender
    email["To"] = email_receiver
    email["Subject"] = subject

    email.set_content(body_text)

    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_Sender, email_password)
        smtp.sendmail(email_Sender, email_receiver, email.as_string())

if __name__ == "__main__":
    main()