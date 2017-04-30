from socket import *
import struct
import time
import ssl
import sys
sys.path.insert(0, '../')
from serverClientDetails import *

class clientIMAPSocket:
	def __init__(self):
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.socket = ssl.wrap_socket(self.socket)
		self.socket.connect((IMAP_SERVER,IMAP_PORT))
		self.getServerReply()
		self.identifierNum = 0
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = self.generateAlphaNumeric() + ' ' + cmd + CLRF
		self.secureSocket.send(data)
		return self.getServerReply()
		
	def generateAlphaNumeric(self):
		alphNum = 'A00' + str(self.identifierNum)
		self.identifierNum+=1
		return alphNum
		
#-----------------------------------------------------------------------		
	def recvall(self,sock, n):
		# Helper function to recv n bytes or return None if EOF is hit
		data = ''
		while len(data) < n:
			packet = sock.recv(n - len(data))
			if not packet:
				return None
			data += packet
		return data
	
	def recv_msg(self,sock):
		# Read message length and unpack it into an integer
		raw_msglen = self.recvall(sock, 4)
		if not raw_msglen:
			return None
		msglen = struct.unpack('>I', raw_msglen)[0]
		# Read the message data
		return self.recvall(sock, msglen) 	
		
		
	def getServerReply(self):
		replyToSentence = self.recv_msg(self.socket)
		print replyToSentence
		return replyToSentence
		

#=======================================================================			
		
class clientPOP3Socket:
	def __init__(self):
		incomingEmailServer = 'pop.gmail.com'
		mailServerPort = 995
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.socket = ssl.wrap_socket(self.socket)
		self.socket.connect((incomingEmailServer,mailServerPort))
		self.getServerReply()
		self.identifierNum = 0
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = cmd + CLRF
		self.socket.send(data)
		print self.getServerReply()
		
	def generateAlphaNumeric(self):
		alphNum = 'A00' + str(self.identifierNum)
		self.identifierNum+=1
		return alphNum
		
	def getServerReply(self):
		replyToSentence = self.socket.recv(1024)
		return replyToSentence		

class clientSMTPSocket:
	def __init__(self):	
		self.socket = socket(AF_INET, SOCK_STREAM)	
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


