import sys
sys.path.insert(0, '../Client/')
from SMTPClient import *

manager = SMTPclient()

def sendSMTPMessage(senderEmail, recipientEmail, message):
	manager.sendMail(senderEmail,recipientEmail,message)
	#manager.terminateSession()

def authenticateSMTP(emailID, password):
	if(manager.authenticate(emailID, password)):
		print 'OK'
	else:
		print 'ERR'

