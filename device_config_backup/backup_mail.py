#!/usr/bin/python3
import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

send_from = "sender@mail.com"
send_to = ['receiver@mail.com']
subject = 'Router Backup'
message = 'All route backup in attachment'
files=['/home/backup_config.tar']
server="smtp.office365.com"
port=587
username='sender@mail.com'
password='Par17974'
use_tls=True

msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = COMMASPACE.join(send_to)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject

msg.attach(MIMEText(message))
for path in files:
    part = MIMEBase('application', "octet-stream")
    with open(path, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename={}'.format('backup_config.tar'))
    msg.attach(part)

smtp = smtplib.SMTP(server, port)
if use_tls:
    smtp.starttls()
smtp.login(username, password)
smtp.sendmail(send_from, send_to, msg.as_string())
smtp.quit()

