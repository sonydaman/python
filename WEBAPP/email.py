#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import smtplib

sender = 'sonydaman@gmail.com'
receivers = ['sonydaman1985@gmail.com']

message = """From: From sonydaman <sonydaman@gmail.com>
To: To sonydaman1985 <sonydaman1985@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('http://127.0.0.1:8089/')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
