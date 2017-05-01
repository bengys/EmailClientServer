from client_sockets import *

class IMAPclient:
	def __init__(self):
		self.sock = clientIMAPSocket()
		self.numMsgs = 0
	def entercommand(self):
		msg = raw_input('--> ')
		return self.sock.sendMessageReceiveReply(msg)
			
	def sendOwnText(self,msg):
		self.sock.sendMessageReceiveReply(msg)
								
	def LOGIN(self, username, password):
		return self.sock.sendMessageReceiveReply('login ' + username + ' ' + password)
	def CAPABILITY(self):
		self.sock.sendMessageReceiveReply('CAPABILITY')
	def LOGOUT(self):
		self.sock.sendMessageReceiveReply('LOGOUT')
	def SELECT(self):
		reply = self.sock.sendMessageReceiveReply('SELECT INBOX')
		self.numMsgs = int(reply.split(' EXISTS')[0].split('* ')[-1])
	def LIST(self):
		self.sock.sendMessageReceiveReply('LIST INBOX *')
	def DELETE(self):
		self.sock.sendMessageReceiveReply('DELETE inbox')
	def FETCH(self):
		for i in range(1,self.numMsgs+1):
			print 'Message: ' + str(i)
			self.sock.sendMessageReceiveReply('FETCH ' + str(i) + ' body[header]')
			self.sock.sendMessageReceiveReply('FETCH ' + str(i) + ' body[text]')			
	
	def SUBSCRIBE(self,listname):
		self.sock.sendMessageReceiveReply('SUBSCRIBE ' + listname)
	def UNSUBSCRIBE(self,listname):
		self.sock.sendMessageReceiveReply('UNSUBSCRIBE ' + listname)	
	
	def CLOSE(self):
		self.sock.sendMessageReceiveReply('CLOSE')	
		
	def COPY(self):
		self.sock.sendMessageReceiveReply('COPY 1:10 Inbox')	
#---------------------------------------------		
	def CREATE(self):
		self.sock.sendMessageReceiveReply('CREATE /testfolder')		
		


