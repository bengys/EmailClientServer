import sys
sys.path.insert(0, '../Client/')
from SMTPClient import *
sys.path.insert(0, '../')
from serverClientDetails import *

class SMTPserver:
	def __init__(self):
		self.ehloReceived = False
		self.MAIL_FROM = ''
		self. RCPT_TO = ''
		self.Header_and_Body = ''
		self.receiveMsg = False
	
	def interact(self,msg):
		
		if self.isEHLO(msg):
			return self.handleEHLO(msg)
		if self.isMAIL(msg):
			return self.handleMAIL(msg)
		if self.isRCPT(msg):
			return self.handleRCPT(msg)
		if self.isDATA(msg):
			return self.handleDATA(msg)
		if self.receiveMsg:
			return self.relayEmail()
		if self.isQUIT(msg):
			self.handleQUIT()			
	
	def formReply(self,code,string):
		CLRF = '\r\n'
		replyString =  str(code) + ' ' + string + CLRF
		return replyString
#-----------------------------------------------------------------------		
		
#-----------------------------------------------------------------------

	def isQUIT(self,msg):
		if msg.split()[0] == 'QUIT':
			return True
		else:
			return False
	
	def handleQUIT(self):
		return self.formReply(221,'Bye')		
#-----------------------------------------------------------------------
		
	def relayEmail(self):
		relayClient = SMTPclient()
		relayClient.authenticate(username,password)
		relayClient.sendMail(username,self.RCPT_TO,self.Header_and_Body)
		self.receiveMsg = False
		return self.formReply(250,'Ok')		
#-----------------------------------------------------------------------

	def isDATA(self,msg):
		if msg.split()[0] == 'DATA':
			return True
		else:
			return False
			
	def handleDATA(self,msg):
		self.receiveMsg = True
		return self.formReply(354,'End data with <CR><LF>.<CR><LF>')			
			
#-----------------------------------------------------------------------

	def isRCPT(self,msg):
		if msg.split(':')[0] == 'RCPT TO':
			return True
		else:
			return False
		
	def handleRCPT(self,msg):
		self.RCPT_TO = msg.split('<')[1].split('>')[0]
		return self.formReply(250,'Ok')	
#-----------------------------------------------------------------------

	def isMAIL(self,msg):
		if msg.split(':')[0] == 'MAIL FROM':
			return True
		else:
			return False
			
	def handleMAIL(self,msg):
		self.MAIL_FROM = msg.split('<')[1].split('>')[0]
		return self.formReply(250,'Ok')			

#-----------------------------------------------------------------------
	def isEHLO(self,msg):
		if (not self.ehloReceived) & (msg.split()[0] == 'EHLO'):
			return True
		else:
			return False		
	
	def handleEHLO(self,msg):
		self.ehloReceived = True;
		return self.formReply(250,"Hello, I am delighted to meet you.")
		
#-----------------------------------------------------------------------
