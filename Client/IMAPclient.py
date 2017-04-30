from client_sockets import *
sys.path.insert(0, '../')
from serverClientDetails import *

class IMAPmanager:
	def __init__(self):
		self.sock = clientIMAPSocket()
		self.numMsgs = 0
	def entercommand(self):
		msg = raw_input('--> ')
		self.sock.sendMessageReceiveReply(msg)
			
								
	def LOGIN(self):
		self.sock.sendMessageReceiveReply('login ' + username + ' ' + password)
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
