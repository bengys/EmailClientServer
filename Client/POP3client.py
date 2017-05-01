from client_sockets import *

#execfile("/home/ben/Desktop/EmailClientServer/GUI/GUI.py")


class POP3manager:
	def __init__(self):
		self.sock = clientPOP3Socket()
	
	def entercommand(self, message):
		return self.sock.sendMessageReceiveReply(message)
					
	#STAT
	def STAT(self):
		self.sock.sendMessageReceiveReply('STAT')
	#List
	def LIST(self, messageID):
		self.sock.sendMessageReceiveReply('LIST ' + messageID)
	#Retrieve
	def RETRIEVE(self, messageID):
		self.sock.sendMessageReceiveReply('RETR ' + messageID)
	#Delete
	def DELETE(self, messageID):
		self.sock.sendMessageReceiveReply('DELE ' + messageID)
	#NOOP
	def NOOP(self):
		self.sock.sendMessageReceiveReply('NOOP')
	#RSET
	def RESET(self):
		self.sock.sendMessageReceiveReply('RSET')
	#QUIT
	def QUIT(self):
		self.sock.sendMessageReceiveReply('QUIT')
	#TOP 
	def TOP(self, messageID, number):
		self.sock.sendMessageReceiveReply('TOP ' + messageID + " " + number)
	#Username 
	def USER(self, username):
		return self.sock.sendMessageReceiveReply('USER ' + username)
	#Password 
	def PASS(self, password):
		return self.sock.sendMessageReceiveReply('PASS ' + password)
	

	#RPOP
	#def RPOP(self, username):
		#self.sock.sendMessageReceiveReply('RPOP ' + username)

	#LAST
	#def LAST(self):
		#self.sock.sendMessageReceiveReply('LAST')

	#UIDL 
	#def UIDL(self):
		#self.sock.sendMessageReceiveReply('UIDL body[text]')
		
	#Replies are only +OK or -ERR
	#Authorization State - username and password
	#Transaction state - Recieve emails
	#Update State - Delete emails
		
conn = POP3manager()

#conn.USER("bobster1605@gmail.com")
#conn.PASS("BenSam4eva")
#conn.STAT()
#conn.LIST("400")
#conn.RETRIEVE("400")
#conn.DELETE("1")
#conn.NOOP()
#conn.RESET()
#conn.LIST("1")
#conn.TOP("1","10")
#conn.QUIT()

#conn.RPOP("networks4017tester")
#conn.LAST()
#conn.entercommand()
#hellosock.sendMessageReceiveReply('select inbox')
#hellosock.sendMessageReceiveReply('a003 fetch 12 full')
