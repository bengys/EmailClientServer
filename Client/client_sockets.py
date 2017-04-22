from socket import *
import time
import ssl

#serverName = '146.141.16.134'

class clientIMAPSocket:
	def __init__(self):
		incomingEmailServer = 'Babbage.ug.eie.wits.ac.za'
		mailServerPort = 993
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.secureSocket = ssl.wrap_socket(self.socket)
		self.secureSocket.connect((incomingEmailServer,mailServerPort))
		self.getServerReply()
		self.identifierNum = 0
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = self.generateAlphaNumeric() + ' ' + cmd + CLRF
		self.secureSocket.send(data)
		self.getServerReply()
		
	def generateAlphaNumeric(self):
		alphNum = 'A00' + str(self.identifierNum)
		self.identifierNum+=1
		return alphNum
		
	def getServerReply(self):
		replyToSentence = self.secureSocket.recv(1024)
		print replyToSentence
		

class clientSMTPSocket:
	def __init__(self):
		incomingEmailServer = '146.141.16.134'
		mailServerPort = 25
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.socket.connect((incomingEmailServer,mailServerPort))
		self.getServerReply()
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = cmd + CLRF
		self.socket.send(data)
		self.getServerReply()		
		
	def getServerReply(self):
		replyToSentence = self.socket.recv(1024)
		print replyToSentence
