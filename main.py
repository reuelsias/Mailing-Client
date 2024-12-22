import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

with open('password.txt', 'r') as passwd_file:
    password = passwd_file.read().strip()

server.login("sender@mail.com", password)

msg = MIMEMultipart()
msg['From'] = "Sender"
msg['To'] = 'receiver@mail.com'
msg['Subject'] = "Testing email from Mail Client"

with open('message.txt', 'r') as message_file:
    message = message_file.read()

msg.attach(MIMEText(message, "plain"))

text = msg.as_string()
server.sendmail("sender@mail.com", "receiver@mail.com", text)

server.quit()
