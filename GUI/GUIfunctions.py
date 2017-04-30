import sys
sys.path.insert(0, '../Client/')
from SMTPClient import *


def authenticateANDsendMessage(senderEmail, recipientEmail, password, message):
	manager = SMTPmanager()
	if not manager.authenticate(senderEmail,password):
		return False	
	manager.sendMail(username,recipientEmail,message)
	manager.terminateSession()
	return True
