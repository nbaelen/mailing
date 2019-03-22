# -*- coding: utf-8 -*-

print 'Starting mail script' 

import config
import sys

print 'Argument List:', str(sys.argv)

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime

startTime = datetime.now()

SERVER = "smtp.live.com"
FROM = "n.baelen@hotmail.fr"
TO = "n.baelen@gmail.com"

print 'Server : ' + SERVER +'\nTO : ' + TO

# Prepare actual MIME message
MSG = MIMEMultipart()
MSG['From'] = "n.baelen@hotmail.fr"
MSG['To'] = "n.baelen@gmail.com"
MSG['Subject'] = "Shotgun EDX 2019"

# Prepare mail body
print 'Preparing Body'

BODY = "?"

print 'Body is ' + BODY

MSG.attach(MIMEText(BODY, 'plain'))
TEXT = MSG.as_string()

# Send the mail
import smtplib

print 'Sending mail ..' 
try: 
	server = smtplib.SMTP(SERVER)
	server.starttls()
	server.login(FROM,config.PASSWORD)
	server.sendmail(FROM, TO, TEXT)
	server.quit()
        print 'Mail sent ...' 
except Exception as e: print(e)

print 'Durée totale du script : %s secondes' % (datetime.now() - startTime)
