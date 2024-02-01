import os
from email.message import EmailMessage
import ssl
import smtplib
from email_validator import validate_email, EmailNotValidError

#validation function which validates if the email is valid to be used
def is_valid_email(email):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        return False
#processes the email after retrieving and validating
def process_email(email):
    #runs send_email in which it emails to all the emails in the text file
    send_email(email=email)

def main():
    #name of the text file with file extension
    file_path = "emails.txt" 
    try:
        #checks if file exists in the current directory
        if not os.path.exists(file_path):
            #if file doesnt exist raise the error
            raise FileNotFoundError(f"File not found: {file_path}")
        #opens the file to read lines from it
        with open(file_path, 'r') as file:
            #looping through the emails in text file
            for line in file:
                email = line.strip()
                #checks if the email is valid
                if is_valid_email(email):
                    #runs the function
                    process_email(email)

    except Exception as e:
        #sends error for any error in try method
        print(f"An error occurred: {e}")


def send_email(email):
    #getting login detials from the text file
    with open("login.txt", "r") as f:
        login = [line.strip() for line in f]

    email_Sender = login[0]
    #Specify the email password maksure to get the password from app passwords in google
    #link: myaccount.google.com/u/1/apppasswords
    email_password = login[1]
    #leave it as it is because u will specify the email in the text file
    email_receiver = email
    #Get the subject from the text file
    with open("subject.txt", "r") as f:
        subj_text = [line.strip() for line in f]
    subject = subj_text[0]
    #Get the message from text file
    file = open('body.txt',mode='r')
    body_text = file.read()
    #initialize the EmailMessage from the module
    email = EmailMessage()
    email["From"] = email_Sender
    email["To"] = email_receiver
    email["Subject"] = subject
    email.set_content(body_text)

    context = ssl.create_default_context()
    #Specify the smtp for example for gmail: smtp.gmail.com
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        #login with smptp
        smtp.login(email_Sender, email_password)
        #send the email
        smtp.sendmail(email_Sender, email_receiver, email.as_string())

if __name__ == "__main__":
    main()