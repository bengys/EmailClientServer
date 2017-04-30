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
		if IMAP_PORT == 993:
			self.socket = ssl.wrap_socket(self.socket)
		self.socket.connect((IMAP_SERVER,IMAP_PORT))
		self.getServerReply()
		self.identifierNum = 0
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = self.generateAlphaNumeric() + ' ' + cmd + CLRF
		self.secureSocket.send(data)
		repy = self.getServerReply()
		print reply
		return reply
		
	def generateAlphaNumeric(self):
		alphNum = 'A00' + str(self.identifierNum)
		self.identifierNum+=1
		return alphNum		
		
	def getServerReply(self):
		replyToSentence = self.recv_msg(self.socket)
		print replyToSentence
		return replyToSentence
		

#=======================================================================			
		
class clientPOP3Socket:
	def __init__(self):
		self.socket = socket(AF_INET, SOCK_STREAM)
		if POP_PORT = 995:
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

#ddddd

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


