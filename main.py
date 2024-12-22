# Imported libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create a connection to the SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()

# Start TLS encryption to secure the connection
server.starttls()

# Read the password from a password file for security reasons
with open('password.txt', 'r') as passwd_file:
    password = passwd_file.read().strip()

# Login to the SMTP server with username and password
server.login("sender@mail.com", password)

# Set headers for message
msg = MIMEMultipart()
msg['From'] = "Sender"
msg['To'] = 'receiver@mail.com'
msg['Subject'] = "Testing email from Mail Client"

# Read the message content from a message file
with open('message.txt', 'r') as message_file:
    message = message_file.read()

# Attach message and convert to string
msg.attach(MIMEText(message, "plain"))
text = msg.as_string()

# Send mail and close server connection
server.sendmail("sender@mail.com", "receiver@mail.com", text)
server.quit()
