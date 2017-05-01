# Run this file to demonstrate working of SMTP client
# Will send email to imap server specified in Serverclientdetails.py
# config file

import sys
sys.path.insert(0, '../Client')
sys.path.insert(0, '../')
from serverClientDetails import *
from SMTPClient import *

print 'Enter EMAIL to WHICH you want to send the email'
destination = raw_input('--> ')
print 'enter message'
msg = raw_input('--> ')
SMTPclient = SMTPclient()
SMTPclient.authenticate(username,password)		
SMTPclient.sendMail(username,destination,msg)
SMTPclient.terminateSession()	
