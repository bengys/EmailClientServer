from socket import *
import time
import ssl

#serverName = '146.141.16.134'

class clientSocket:
	def __init__(self):
		incomingEmailServer = 'Babbage.ug.eie.wits.ac.za'
		mailServerPort = 993
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.secureSocket = ssl.wrap_socket(self.socket)#, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
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
		
class IMAPmanager:
	def __init__(self):
		self.sock = clientSocket()
	
	def entercommand(self):
		msg = raw_input('--> ')
		self.sock.sendMessageReceiveReply(msg)
			
								
	def LOGIN(self):
		self.sock.sendMessageReceiveReply('login group1 T6YzvQ89Z')
	def CAPABILITY(self):
		self.sock.sendMessageReceiveReply('CAPABILITY')
	def LOGOUT(self):
		self.sock.sendMessageReceiveReply('LOGOUT')
	def SELECT(self):
		self.sock.sendMessageReceiveReply('SELECT inbox')
	def LIST(self):
		self.sock.sendMessageReceiveReply('LIST INBOX *')
	def DELETE(self):
		self.sock.sendMessageReceiveReply('DELETE inbox')
	def FETCH(self):
		self.sock.sendMessageReceiveReply('FETCH 2 body[text]')			
		
		
#Not working 
#---------------------------------------------		
	def CREATE(self):
		self.sock.sendMessageReceiveReply('CREATE /testfolder')		
		
				


conn = IMAPmanager()
conn.LOGIN()
conn.SELECT()
conn.FETCH()
conn.entercommand()
#hellosock.sendMessageReceiveReply('select inbox')
#hellosock.sendMessageReceiveReply('a003 fetch 12 full')
