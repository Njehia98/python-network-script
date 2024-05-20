import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_notification(subject, message, body, sender_email, sender_password, recipient_email, smtp_server, smtp_port):
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg['Body'] = body
        # Attach the email body
        msg.attach(MIMEText(message, ''))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email notification sent successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Email details
    subject = "Notification from Python Script"
    notification_message = "You have been hacked!!!"
    body= "This is a body"
    sender_email = "s.njehia@chem-labs.com"  
    sender_password = "k7%45AenhS" 
    recipient_email = "c.njoroge@chem-labs.com"  
    smtp_server = "smtp.mailsafi.com"  
    smtp_port = 587  

    # Send the email notification
    send_email_notification(subject, notification_message,body, sender_email, sender_password, recipient_email, smtp_server, smtp_port)
