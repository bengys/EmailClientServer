from client_sockets import *

class POP3manager:
	def __init__(self):
		self.sock = clientPOP3Socket()
	
	def entercommand(self):
		msg = raw_input('--> ')
		self.sock.sendMessageReceiveReply(msg)
					
	#STAT
	def STAT(self):
		self.sock.sendMessageReceiveReply('STAT')
	#List
	def LIST(self):
		self.sock.sendMessageReceiveReply('LIST body[text]')
	#Retrieve
	def RETR(self):
		self.sock.sendMessageReceiveReply('RETR body[text]')
	#Delete
	def DELE(self):
		self.sock.sendMessageReceiveReply('DELETE  body[text]')
	#NOOP
	def NOOP(self):
		self.sock.sendMessageReceiveReply('NOOP')
	#RSET
	def RSET(self):
		self.sock.sendMessageReceiveReply('RSET')
	#QUIT
	def QUIT(self):
		self.sock.sendMessageReceiveReply('QUIT')
	#TOP 
	def TOP(self):
		self.sock.sendMessageReceiveReply('TOP 2 body[text]')
	#UIDL 
	def UIDL(self):
		self.sock.sendMessageReceiveReply('UIDL body[text]')
	#Username 
	def USER(self):
		self.sock.sendMessageReceiveReply('USER body[text]')
	#Password 
	def PASS(self):
		self.sock.sendMessageReceiveReply('PASS body[text]')
	#APOP
	def APOP(self):
		self.sock.sendMessageReceiveReply('APOP 2 body[text]')
		
	#Replies are only +OK or -ERR
	#Authorization State - username and password
	#Transaction state - Recieve emails
	#Update State - Delete emails
		
conn = POP3manager()
conn.USER()
conn.PASS()
conn.LIST()
conn.DELE()
conn.QUIT()
conn.entercommand()
#hellosock.sendMessageReceiveReply('select inbox')
#hellosock.sendMessageReceiveReply('a003 fetch 12 full')
