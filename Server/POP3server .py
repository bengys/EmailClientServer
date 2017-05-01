class POP3server:
	def __init__(self):
		self.login = False
		self.mailBoxes = []
		self.mailBoxes.append([])
		self.mailBoxes[0].append('from Harold - have a great day, my Japan!')
		self.mailBoxes[0].append('from Dan - I thought I saw you at the dry cleaners in September!!!')
	def interact(self,msg):
		if self.isUsername(msg):
			return self.handleUsername(msg)
		if self.isPass(msg):
			return self.handlePASS(msg)
		if self.isStat(msg):
			return self.handleStat(msg)	
		
	def getIdentifier(self,msg):
		identifier = msg.split()[0]
		return identifier	
				
	def getCommand(self,msg):
		cmd = msg.split()[0]
		return cmd

	def getNum1(self,msg):
		num1 = msg.split()[1]
		return cmd

	def getNum2(self,msg):
		num2 = msg.split()[2]
		return cmd

	def formReply(self,msg,str):
		reply = '+ ' + self.getIdentifier(msg) + ' ' + str
		return reply
#-----------------------------------------------------------------------
	
	def isUsername(self,msg):
		if self.getCommand(msg) == 'USER':
			return True
		else:
			return False	
			
	def handleUsername(self,msg):
		return '+OK send PASS'

#-----------------------------------------------------------------------
	
	def isPass(self,msg):
		if self.getCommand(msg) == 'PASS':
			return True
		else:
			return False	
			
	def handlePASS(self,msg):
		if (msg.split()[2] == 'networks4017'):
			self.login = True
			return '+OK Welcome'
		else:
			return "-ERR [AUTH] Username and Password not accepted."

#-----------------------------------------------------------------------
	
	def isStat(self,msg):
		if self.getCommand(msg) == 'STAT':
			return True
		else:
			return False	
			
	def handleStat(self,msg):
		reply = ''
		box = self.mailBoxes[0]
		for msg in box:
			reply += msg + '\n'
		return ('+OK ' + str(len(self.mailBoxes[0])))

#-----------------------------------------------------------------------
	
	def isList(self,msg):
		if msg.split()[1] == 'fetch':
			return True
		else:
			return False	
			
	def handleList(self,msg):
		reply = ''
		box = self.mailBoxes[0]
		for msg in box:
			reply += msg + '\n'
		return 'Messages : \n' + reply	

#-----------------------------------------------------------------------
	
	def isRetrieve(self,msg):
		if msg.split()[1] == 'fetch':
			return True
		else:
			return False	
			
	def handleRetrieve(self,msg):
		reply = ''
		box = self.mailBoxes[0]
		for msg in box:
			reply += msg + '\n'
		return 'Messages : \n' + reply	
		
		
#-----------------------------------------------------------------------
	def isDelete(self,msg):
		if msg.split()[1] == 'select':
			return True
		else:
			return False	
			
	def handleDelete(self,msg):
		if msg.split()[2] == 'inbox':
			reply = '* ' + str(len(self.mailBoxes[0])) + ' Exists'
			return reply
			
#-----------------------------------------------------------------------
	def isQuit(self,msg):
		if self.getCommand(msg) == 'login':
			return True
		else:
			return False
			
	def handleQuit(self,msg):
		if (msg.split()[2] == 'networks4017tester@gmail.com') & (msg.split()[3] == 'networks4017'):
			self.login = True
			reply = self.formReply(msg,'Ok LOGIN completed')
			return reply
		else:
			print msg
			reply = self.formReply(msg,'No login failure: username or password rejected') 
			return reply
