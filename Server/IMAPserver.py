class IMAPserver:
	def __init__(self):
		self.login = False
		self.mailBoxes = []
		self.mailBoxes.append([])
		self.mailBoxes[0].append('from Harold - have a great day, my Japan!')
		self.mailBoxes[0].append('from Dan - I thought I saw you at the dry cleaners in September!!!')
	def interact(self,msg):
		if self.isLogin(msg):
			return self.handleLogin(msg)
		if self.isSelect(msg):
			return self.handleSelect(msg)
		if self.isFetch(msg):
			return self.handleFetch(msg)	
		
	def getIdentifier(self,msg):
		identifier = msg.split()[0]
		return identifier	
				
	def getCommand(self,msg):
		cmd = msg.split()[1]
		return cmd

	def formReply(self,msg,str):
		reply = '* ' + self.getIdentifier(msg) + ' ' + str
		return reply
#-----------------------------------------------------------------------
	
	def isFetch(self,msg):
		if msg.split()[1] == 'fetch':
			return True
			print 'ssssssssssss'
		else:
			return False	
			
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
		if msg.split()[2] == 'inbox':
			reply = '* ' + str(len(self.mailBoxes[0])) + ' Exists'
			return reply
			
#-----------------------------------------------------------------------
	def isLogin(self,msg):
		if self.getCommand(msg) == 'login':
			return True
		else:
			return False
			
	def handleLogin(self,msg):
		if (msg.split()[2] == 'networks4017tester@gmail.com') & (msg.split()[3] == 'networks4017'):
			self.login = True
			reply = self.formReply(msg,'Ok LOGIN completed')
			return reply
		else:
			print msg
			reply = self.formReply(msg,'No login failure: username or password rejected') 
			return reply
