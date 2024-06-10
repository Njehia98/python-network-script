import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
recipient_email = os.getenv('RECIPIENT_EMAIL')

try:
    smtp_port = int(smtp_port)
except ValueError:
    print("Error: SMTP_PORT must be an integer")

input_file = 'Sample Packet Capture.txt'  

def filter_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    udp_tcp_lines = [line for line in lines if 'UDP' in line or 'TCP' in line]
    return udp_tcp_lines

def send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, subject, body):
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(sender_email, sender_password)  
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)

subject = 'Filtered Log File'
body = 'Please find the attached filtered log file.'
send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, subject, body)
