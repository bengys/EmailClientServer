# IMAP server - handles IMAP requests, processses and responds according
# to IMAP protocol. Each connection will have its own IMAPserver object running
# in its own server thread.

class IMAPserver:
	def __init__(self):
		self.login = False
		self.mailBoxes = []
		self.mailBoxes.append([])
		# Mock Mailbox
		# Mock messages to populate Mailbox
		self.mailBoxes[0].append('from Harold - have a great day, my Japan!')
		self.mailBoxes[0].append('from Dan - I thought I saw you at the dry cleaners in September!!!')
	
	#Takes in received message from client and interpretes it, and responds
	def interact(self,msg):
		
		# If message was a login message:
		if self.isLogin(msg):
			# handle it as a login message and validate
			return self.handleLogin(msg)
			
		# If message was select command	
		if self.isSelect(msg):
			return self.handleSelect(msg)
			
		# If message was fetch command	
		if self.isFetch(msg):
			return self.handleFetch(msg)	
	
	# Get alphanumeric identifier sent by client	
	def getIdentifier(self,msg):
		identifier = msg.split()[0]
		return identifier	
	
	# Extract command from clients message			
	def getCommand(self,msg):
		cmd = msg.split()[1]
		return cmd

	# Form a reply to send to client. Consists of client's identifier
	# and a response string
	def formReply(self,msg,str):
		reply = '* ' + self.getIdentifier(msg) + ' ' + str
		return reply
#-----------------------------------------------------------------------
	
	def isFetch(self,msg):
		if msg.split()[1] == 'fetch':
			return True
		else:
			return False	
	
	# Get all mail in mailbox, and form it into one long string for
	# transmission		
	def handleFetch(self,msg):
		reply = ''
		box = self.mailBoxes[0]
		for msg in box:
			reply += msg + '\n'
		return 'Messages : \n' + reply	
		
		
#-----------------------------------------------------------------------
	def isSelect(self,msg):
		if msg.split()[1] == 'select':
			return True
		else:
			return False	
			
	def handleSelect(self,msg):
		# See if selected mailbox exists and indicate so to client 
		if msg.split()[2] == 'inbox':
			reply = '* ' + str(len(self.mailBoxes[0])) + ' Exists'
			return reply
			
#-----------------------------------------------------------------------
	def isLogin(self,msg):
		if self.getCommand(msg) == 'login':
			return True
		else:
			return False
	
	# For this server there is only one valid 'mock' user on the system
	# login only works if credentials correspond to them		
	def handleLogin(self,msg):
		if (msg.split()[2] == 'networks4017tester@gmail.com') & (msg.split()[3] == 'networks4017'):
			self.login = True
			reply = self.formReply(msg,'Ok LOGIN completed')
			return reply
		else:
			print msg
			reply = self.formReply(msg,'No login failure: username or password rejected') 
			return reply
