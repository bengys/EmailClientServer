from client_sockets import *

class IMAPmanager:
	def __init__(self):
		self.sock = clientIMAPSocket()
	
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
