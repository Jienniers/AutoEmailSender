import os
from email.message import EmailMessage
import ssl
import smtplib
from email_validator import validate_email, EmailNotValidError
import json

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
                else:
                    print("One of a email is not valid.")
                    
    except Exception as e:
        print(f"An error occurred: {e}")


def send_email(email):
    with open('data.json', 'r') as file:
        data = json.load(file)

    email_Sender = data[0]["email-address"]
    email_password = data[0]['password']
    email_receiver = email

    subject = data[1]['subject']
    body_text = data[1]['body']

    email = EmailMessage()

    email["From"] = email_Sender
    email["To"] = email_receiver
    email["Subject"] = subject

    email.set_content(body_text)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_Sender, email_password)
            smtp.sendmail(email_Sender, email_receiver, email.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()