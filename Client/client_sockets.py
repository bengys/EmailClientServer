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
		
class clientPOP3Socket:
	def __init__(self):
		incomingEmailServer = 'pop.gmail.com'
		mailServerPort = 995
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.secureSocket = ssl.wrap_socket(self.socket)
		self.secureSocket.connect((incomingEmailServer,mailServerPort))
		self.getServerReply()
		self.identifierNum = 0
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = cmd + CLRF
		self.secureSocket.send(data)
		return self.getServerReply()
		
	def generateAlphaNumeric(self):
		alphNum = 'A00' + str(self.identifierNum)
		self.identifierNum+=1
		return alphNum
		
	def getServerReply(self):
		replyToSentence = self.secureSocket.recv(1024)
		return replyToSentence		

class clientSMTPSocket:
	def __init__(self):
		incomingEmailServer = '146.141.16.134'		
		mailServerPort = 25
		self.socket = socket(AF_INET, SOCK_STREAM)
#Uncomment/comment next lines depedning on if using school or gmail server
#'''	
		incomingEmailServer = 'localhost'#'smtp.gmail.com'		
		mailServerPort = 465	
		self.socket = ssl.wrap_socket(self.socket)
#'''		
		self.socket.connect((incomingEmailServer,mailServerPort))	
		print 'Connected with Server'
	
		self.getServerReply()
		
	def sendMessageReceiveReply(self,cmd):
		CLRF = '\r\n'
		data = cmd + CLRF
		self.socket.send(data)
		self.getServerReply()		
		
	def getServerReply(self):
		replyToSentence = self.socket.recv(1024)
		print replyToSentence


