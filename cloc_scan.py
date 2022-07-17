# Python code to run cloc and sent results to given email address

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import sys
import subprocess

fromaddr = "mengani.premkanth@gmail.com"
toaddr = input('Please enter the email address to which the scan result need to be sent to:  \n')
ases_userid = os.environ.get('ases_uname')
ases_pass = os.environ.get('ases_pass')

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "cloc scan results"

# string to store the body of the mail
body = "Please find attached cloc scan results"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
restatus = subprocess.call(["./cloc", sys.argv[1], "--out", sys.argv[2]])
attachment = open(sys.argv[2], "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % sys.argv[2])

# attach the instance 'p' to instance 'msg'
msg.attach(p)



s = smtplib.SMTP('email-smtp.ap-south-1.amazonaws.com',587)
s.starttls()
s.login(ases_userid, ases_pass)

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()

