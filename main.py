'''import smtplib
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
    sender_password = "" 
    recipient_email = "c.njoroge@chem-labs.com"  
    smtp_server = "smtp.mailsafi.com"  
    smtp_port = 587  

    # Send the email notification
    send_email_notification(subject, notification_message,body, sender_email, sender_password, recipient_email, smtp_server, smtp_port)'''

'''import os
# Retrieving the value of the "PATH" environment variable
path = os.environ["PATH"]
print(path)

# Setting a new environment variable
os.environ["API_KEY"] = "YOUR_API_KEY"
'''
import socket
import datetime
log_filename = "Sample Packet Capture.txt"

# Generate timestamp for the log file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"{timestamp}_{log_filename}"

# Create or open the log file in append mode
log_file = open(log_filename, "a")
while True:
    # Get the list of network connections
    connections = socket.net_connections()

    # Write the connections to the log file
    log_file.write(f"Timestamp: {datetime.datetime.now()}\n")
    for connection in connections:
        log_file.write(f"{connection}\n")
    log_file.write("\n")

