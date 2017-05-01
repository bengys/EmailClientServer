from socket import *
import struct
import time
import ssl
import sys
sys.path.insert(0, '../')
from serverClientDetails import *

# The Following 3 Classes allocates TCP soacket on clients side for
# varoius service - SMTP, POP3, IMAP. Responsible for sending
# and receiving messages to and from server through TCP stream
class clientIMAPSocket:
	def __init__(self):
		
		# Create socket
		self.socket = socket(AF_INET, SOCK_STREAM)
		
		# If port defind in ServerClientDetails config file is set to 993
		# Wrap as ssl socket
		if IMAP_PORT == 993:
			self.socket = ssl.wrap_socket(self.socket)
		
		# Connect to IMAP server configured in ServerClientDetails 
		self.socket.connect((IMAP_SERVER,IMAP_PORT))
		
		# Get initial greeting from IMAP server
		self.getServerReply()
		self.identifierNum = 0
		
	# Function used to send email to server and return reply from server	
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		
		# Append each message with unique alphanumeric identifier and
		# end with carriage rertun newline as defined by IMAP RFC
		data = self.generateAlphaNumeric() + ' ' + cmd + CLRF
		
		# Send client request in TCP stream
		self.socket.send(data)
		# Receive server response from TCP stream
		reply = self.getServerReply()
		print reply
		return reply
		
	# Generate unique alphanumerix identifier	
	def generateAlphaNumeric(self):
		alphNum = 'A00' + str(self.identifierNum)
		self.identifierNum+=1
		return alphNum		
		
	# receive data from TCP stream established with server	
	def getServerReply(self):
		replyToSentence = self.socket.recv(2048)
		return replyToSentence
		

#=======================================================================			
		
class clientPOP3Socket:
	def __init__(self):
		self.socket = socket(AF_INET, SOCK_STREAM)
		if POP_PORT == 995:
			self.socket = ssl.wrap_socket(self.socket)
		self.socket.connect((POP_SERVER,POP_PORT))
		self.getServerReply()
		self.identifierNum = 0
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = cmd + CLRF
		self.socket.send(data)
		reply = self.getServerReply()
		print reply
		return reply
		
	def generateAlphaNumeric(self):
		alphNum = 'A00' + str(self.identifierNum)
		self.identifierNum+=1
		return alphNum
		
	def getServerReply(self):
		replyToSentence = self.socket.recv(1024)
		return replyToSentence		


#=======================================================================

class clientSMTPSocket:
	def __init__(self):	
		self.socket = socket(AF_INET, SOCK_STREAM)	
		if SMTP_PORT == 465:
			self.socket = ssl.wrap_socket(self.socket)
		self.socket.connect((SMTP_SERVER,SMTP_PORT))	
		print 'Connected with Server'
	
		self.getServerReply()
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = cmd + CLRF
		self.socket.send(data)
		return self.getServerReply()		
		
	def getServerReply(self):
		replyToSentence = self.socket.recv(1024)
		print replyToSentence
		return replyToSentence


