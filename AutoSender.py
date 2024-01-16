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
                else:
                    #sends error for invalid email
                    print(f"Invalid email: {email}")

    except Exception as e:
        #sends error for any error in try method
        print(f"An error occurred: {e}")


def send_email(email):
    #specify the email from which the email would be sent
    email_Sender = ""
    #Specify the email password makesure to get the password from app passwords in google
    #link: myaccount.google.com/u/1/apppasswords
    email_password = ""
    #leave it as it is because you will specify the email in the text file
    email_receiver = email
    #Write the subject of the email
    subject = "For Testing Purpose"
    #Write the message body for the email
    body =  """
        Its to inform you that this is a test body.
    """
    #initialize the EmailMessage from the module
    email = EmailMessage()
    email["From"] = email_Sender
    email["To"] = email_receiver
    email["Subject"] = subject
    email.set_content(body)

    context = ssl.create_default_context()
    #Specify the smtp for example for gmail: smtp.gmail.com
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        #login with smptp
        smtp.login(email_Sender, email_password)
        #send the email
        smtp.sendmail(email_Sender, email_receiver, email.as_string())

if __name__ == "__main__":
    main()