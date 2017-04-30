from client_sockets import *
import sys
sys.path.insert(0, '../')
from serverClientDetails import *
from base64 import b64encode

def entercommand(sock):
	while 1:
		msg = raw_input('--> ')
		sock.sendMessageReceiveReply(msg)

class SMTPclient:
	def __init__(self):
		self.sock = clientSMTPSocket()
		self.sock.sendMessageReceiveReply('EHLO localhost')
		
		
	def authenticate(self,user,password):
		userb64 = b64encode(bytes(user))
		passb64 = b64encode(bytes(password))
		self.sock.sendMessageReceiveReply('AUTH LOGIN')
		self.sock.sendMessageReceiveReply(userb64)
		authOutcome = self.sock.sendMessageReceiveReply(passb64)
		print authOutcome.split(' ')[0]
		if authOutcome.split(' ')[0] == str(235):
			return True
		else:
			return False
	
	def sendMail(self,FROM,TO,body):
		self.sock.sendMessageReceiveReply('MAIL FROM:<' + FROM + '>')
		self.sock.sendMessageReceiveReply('RCPT TO:<' + TO + '>')
		self.sock.sendMessageReceiveReply('DATA')
		self.sock.sendMessageReceiveReply(body + '\n' + '\r\n' '.' + '\r\n')
	
	def abortCurrentMailTransaction(self):
		self.sock.sendMessageReceiveReply('RSET')
		
	def doNothingJustGet250_OK(self):
		self.sock.sendMessageReceiveReply('NOOP')	
	def terminateSession(self):
		self.sock.sendMessageReceiveReply('QUIT')

	def verifyAddress(self,user):
		self.sock.sendMessageReceiveReply('VRFY ' + user)		
			
		
	def entercommand(self):
		while 1:
			msg = raw_input('--> ')
			self.sock.sendMessageReceiveReply(msg)	
					


