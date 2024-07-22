import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, body):
    smtp_server = "smtp-relay.brevo.com"
    smtp_port = 587
    smtp_username = "bizmgr.okekedc@gmail.com"
    smtp_password = "yVgTDK9nhfZRw4s3"
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Attach the message body
    msg.attach(MIMEText(body, 'plain'))
     
    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)  # Login to the SMTP server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
sender_email = "your_email@example.com"  # Replace with your email address
recipient_email = "recipient@example.com"  # Replace with recipient's email address
subject = "Test Email"
body = "This is a test email sent using Brevo SMTP server."

send_email(sender_email, recipient_email, subject, body)





# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_anonymous_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port):
#     # Create a multipart message
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = recipient_email
#     msg['Subject'] = subject
    
#     # Attach the message body
#     msg.attach(MIMEText(body, 'plain'))
    
#     try:
#         # Connect to the SMTP server
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.sendmail(sender_email, recipient_email, msg.as_string())
#             print("Email sent successfully")
#     except Exception as e:
#         print(f"Failed to send email: {e}")

# # Example usage
# send_anonymous_email(
#     sender_email="anonymous@example.com",
#     recipient_email="recipient@example.com",
#     subject="Test Anonymous Email",
#     body="This is a test message sent anonymously.",
#     smtp_server="smtp.example.com",  # Replace with a real SMTP server
#     smtp_port=587  # Common port for SMTP
# )
#                                                                                                                     