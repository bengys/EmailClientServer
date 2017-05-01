import sys
sys.path.insert(0, '../Client/')
from SMTPClient import *
sys.path.insert(0, '../')
from serverClientDetails import *

# SMTP server. Each thread for each individual client connection will
# have its own instance of SMTPserver object

class SMTPserver:
	def __init__(self):
		self.ehloReceived = False
		self.MAIL_FROM = ''
		self. RCPT_TO = ''
		self.Header_and_Body = ''
		self.receiveMsg = False
	
	# Main interaction loop. Messages from client processed, validated and
	# responded to by this function
	def interact(self,msg):
		
		if self.isEHLO(msg):
			return self.handleEHLO(msg)
		if self.isMAIL(msg):
			return self.handleMAIL(msg)
		if self.isRCPT(msg):
			return self.handleRCPT(msg)
		if self.isDATA(msg):
			return self.handleDATA(msg)
		
		# If a message has been sent by client (MAIL FROM, RCPT TO, DATA etc)
		if self.receiveMsg:
			# Relay the message to another SMTP server. In this case -
			# smtp.gmail.com
			return self.relayEmail(msg)
		if self.isQUIT(msg):
			self.handleQUIT()			
	
	# Form reply based on a response code and informative string
	def formReply(self,code,string):
		CLRF = '\r\n'
		replyString =  str(code) + ' ' + string + CLRF
		return replyString
#-----------------------------------------------------------------------		
		
#-----------------------------------------------------------------------
	# Did client send quit command?
	def isQUIT(self,msg):
		if msg.split()[0] == 'QUIT':
			return True
		else:
			return False
	
	def handleQUIT(self):
		return self.formReply(221,'Bye')		
#-----------------------------------------------------------------------
	
	#	Function to relay message received from client to another SMTP
	# server
	def relayEmail(self,msg):
		# SMTP server now becomes a client in regards to next SMTP server
		relayClient = SMTPclient()
			
		# Store contents of body of email from client	
		self.Header_and_Body = msg
		
		# Authenticate to next SMTP server - in this case all received
		# messages get relayed in the name of the current SMTP server
		relayClient.authenticate(username,password)
		
		# Send mail. Get destination email address from message client
		# originally send with RCPT TO. Also get contents of the message sent
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
		
		# Indicates that a message has been received and it must be relayed
		self.receiveMsg = True
		return self.formReply(354,'End data with <CR><LF>.<CR><LF>')			
			
#-----------------------------------------------------------------------

	# Check for RCPT TO command
	def isRCPT(self,msg):
		if msg.split(':')[0] == 'RCPT TO':
			return True
		else:
			return False
		
	def handleRCPT(self,msg):
		# Store RCPT TO value for address to which SMTP server must forward
		# email
		self.RCPT_TO = msg.split('<')[1].split('>')[0]
		return self.formReply(250,'Ok')	
#-----------------------------------------------------------------------

	# check for MAIL FROM command
	def isMAIL(self,msg):
		if msg.split(':')[0] == 'MAIL FROM':
			return True
		else:
			return False
					
	def handleMAIL(self,msg):
		self.MAIL_FROM = msg.split('<')[1].split('>')[0]
		return self.formReply(250,'Ok')			

#-----------------------------------------------------------------------
	# Check for EHLO account
	def isEHLO(self,msg):
		if (not self.ehloReceived) & (msg.split()[0] == 'EHLO'):
			return True
		else:
			return False		
	
	def handleEHLO(self,msg):
		self.ehloReceived = True;
		return self.formReply(250,"Hello, I am delighted to meet you.")
		
#-----------------------------------------------------------------------
