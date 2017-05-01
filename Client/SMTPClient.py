

from client_sockets import *
import sys
sys.path.insert(0, '../')
from serverClientDetails import *
from base64 import b64encode

# SMTP client class to interact with SMTP server
class SMTPclient:
	def __init__(self):
		# creare client Socekt object. Establish connection with SMTP
		# server socket
		self.sock = clientSMTPSocket()
		
		# Send EHLO command as per SMTP protocol
		self.sock.sendMessageReceiveReply('EHLO localhost')
		
	# Authenticate user on SMTP server	
	def authenticate(self,user,password):
		
		# Base64 encodes credentials
		userb64 = b64encode(bytes(user))
		passb64 = b64encode(bytes(password))
		
		# Send request to login
		self.sock.sendMessageReceiveReply('AUTH LOGIN')
		
		# Server responds, requesting client to send username and password
		self.sock.sendMessageReceiveReply(userb64)
		authOutcome = self.sock.sendMessageReceiveReply(passb64)
		print authOutcome.split(' ')[0]
		if authOutcome.split(' ')[0] == str(235):
			return True
		else:
			return False
	
	# Wrapper function to send email. Sends MAIL FROM, RCPT TO and DATA
	# commands in sequence as per SMTP protocol
	def sendMail(self,FROM,TO,body):
		self.sock.sendMessageReceiveReply('MAIL FROM:<' + FROM + '>')
		self.sock.sendMessageReceiveReply('RCPT TO:<' + TO + '>')
		self.sock.sendMessageReceiveReply('DATA')
		
		# Terminate message with CLRF a fullstop and another CLRF to indicate
		# to server end of message
		self.sock.sendMessageReceiveReply(body + '\n' + '\r\n' '.' + '\r\n')
	
	
	def abortCurrentMailTransaction(self):
		self.sock.sendMessageReceiveReply('RSET')
		
	def doNothingJustGet250_OK(self):
		self.sock.sendMessageReceiveReply('NOOP')	
	
	def terminateSession(self):
		self.sock.sendMessageReceiveReply('QUIT')

	# Verify if a user exists on the server
	def verifyAddress(self,user):
		self.sock.sendMessageReceiveReply('VRFY ' + user)		
			
	# Continuos loop to interact with server with own commands and get reply	
	def entercommand(self):
		while 1:
			msg = raw_input('--> ')
			self.sock.sendMessageReceiveReply(msg)	
					


