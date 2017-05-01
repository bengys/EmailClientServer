from client_sockets import *

# IMAP client class that provides various IMAP functionality commands
#	 and their formatiing
class IMAPclient:
	def __init__(self):
		self.sock = clientIMAPSocket()
		self.numMsgs = 0
	
	# Prompts for user input that will be send to server - formatted
	# as per IMAP	
	def entercommand(self):
		msg = raw_input('--> ')
		return self.sock.sendMessageReceiveReply(msg)
			
	# Send own string to IMAP server		
	def sendOwnText(self,msg):
		self.sock.sendMessageReceiveReply(msg)
	
	# Login command to server							
	def LOGIN(self, username, password):
		return self.sock.sendMessageReceiveReply('login ' + username + ' ' + password)
	
	def CAPABILITY(self):
		self.sock.sendMessageReceiveReply('CAPABILITY')
	
	
	def LOGOUT(self):
		self.sock.sendMessageReceiveReply('LOGOUT')
	
	# Display messages in mailbox 'inbox'
	def SELECT(self):
		reply = self.sock.sendMessageReceiveReply('SELECT INBOX')
		self.numMsgs = int(reply.split(' EXISTS')[0].split('* ')[-1])
	
	# List folders in mailbox (inbox in this case)
	def LIST(self):
		self.sock.sendMessageReceiveReply('LIST INBOX *')
		
	# Delete folder/inbox	
	def DELETE(self):
		self.sock.sendMessageReceiveReply('DELETE inbox')
	
	# Fetch all emails on IMAP server and display to client headers and body
	def FETCH(self):
		for i in range(1,self.numMsgs+1):
			print 'Message: ' + str(i)
			self.sock.sendMessageReceiveReply('FETCH ' + str(i) + ' body[header]')
			self.sock.sendMessageReceiveReply('FETCH ' + str(i) + ' body[text]')			
	
	# subscribe/unsubscribe to mailing list
	def SUBSCRIBE(self,listname):
		self.sock.sendMessageReceiveReply('SUBSCRIBE ' + listname)
	def UNSUBSCRIBE(self,listname):
		self.sock.sendMessageReceiveReply('UNSUBSCRIBE ' + listname)	
	
	# Close session
	def CLOSE(self):
		self.sock.sendMessageReceiveReply('CLOSE')	
		
	# Copies spcified emails to destination inbox (in this case a folder
	# called arbFolder	
	def COPY(self):
		self.sock.sendMessageReceiveReply('COPY 1:10 arbFolder')	
#---------------------------------------------		
	
	# Create new inbox
	def CREATE(self):
		self.sock.sendMessageReceiveReply('CREATE /testfolder')		
		


