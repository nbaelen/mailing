# -*- coding: utf-8 -*-

print 'Starting mail script' 

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime
import time


startTime = datetime.now()

time.sleep(59)

SERVER = "smtp.live.com"
FROM = "n.baelen@hotmail.fr"
TO = "sg2019@edexpress.fr"
#TO = "margot.mantez@edhec.com"

print 'Server : ' + SERVER +'\nTO : ' + TO

# Prepare actual message
MSG = MIMEMultipart()
MSG['From'] = "n.baelen@hotmail.fr"
MSG['To'] = "sg2019@edexpress.fr"
MSG['Subject'] = "Shotgun EDX 2019"

# Prepare mail body
print 'Preparing Body'

BODY = "Bonjour,\n\nDe retour pour l'édition 2019 d'EDX avec Clément Evrard !\n\nBonne soirée, Nathan."


print 'Body is ' + BODY

MSG.attach(MIMEText(BODY, 'plain'))
TEXT = MSG.as_string()

# Send the mail
import smtplib

print 'Sending mail ..' 
try: 
	server = smtplib.SMTP(SERVER)
	server.starttls()
	server.login(FROM,'Nb040298')
	server.sendmail(FROM, TO, TEXT)
	server.quit()
        print 'Mail sent ...' 
except Exception as e: print(e)

print 'Durée totale du script : %s secondes' % (datetime.now() - startTime)
