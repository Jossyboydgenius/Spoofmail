import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_spoofed_email(smtp_server, smtp_port, smtp_username, smtp_password, sender_email, recipient_email, subject, body, is_html=False):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Attach the message body
    content_type = 'html' if is_html else 'plain'
    msg.attach(MIMEText(body, content_type))
    
    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)  # Login to the SMTP server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    # Prompt user for SMTP server details
    smtp_server = input("Enter the SMTP server address: ")
    smtp_port = int(input("Enter the SMTP server port: "))
    smtp_username = input("Enter the SMTP username: ")
    smtp_password = input("Enter the SMTP password: ")
    
    # Prompt user for email details
    sender_email = input("Enter the sender email address: ")
    recipient_email = input("Enter the recipient email address: ")
    subject = input("Enter the email subject: ")
    
    # Prompt for body format
    use_html = input("Do you want to use HTML content? (yes/no): ").strip().lower() == 'yes'
    
    if use_html:
        # Ask for HTML file path
        file_path = input("Enter the path to the HTML file: ").strip()
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                body = file.read()
        else:
            print(f"File {file_path} does not exist. Using empty body.")
            body = ""
    else:
        # Prompt user for plain text body
        body = input("Enter the email body: ")
    
    # Send the spoofed email
    send_spoofed_email(smtp_server, smtp_port, smtp_username, smtp_password, sender_email, recipient_email, subject, body, is_html=use_html)

if __name__ == "__main__":
    main()
