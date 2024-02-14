import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#send an email to the email address in the variable email
#
# We need you to send a spoofed email.
# Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@ship-shape-security.com
# Recipient needs to be zultron@cyberdarkart.com
# Subject needs to be "I come in peace"
# Body needs to be "We come in peace, take us to your leader"
#

sender = "bob-roswell-1947@ship-shape-security.com"
receiver = "zultron@cyberdarkart.com"
subject = "I come in peace"
body = "We come in peace, take us to your leader"

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('127.0.0.1', 1025)
server.sendmail(sender, receiver, msg.as_string())
server.quit()


                      