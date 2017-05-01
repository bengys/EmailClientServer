class POP3server:
	def __init__(self):
		self.login = False
		self.mailBoxes = []
		#self.mailBoxes.append([])
		self.mailBoxes.append('from Harold - have a great day, my Japan!')
		self.mailBoxes.append('from Dan - I thought I saw you at the dry cleaners in September!!!')
	def interact(self,msg):
		if self.isUsername(msg):
			return self.handleUsername(msg)
		if self.isPass(msg):
			return self.handlePASS(msg)
		if self.isStat(msg):
			return self.handleStat(msg)
		if self.isList(msg):
			return self.handleList(msg)
		if self.isRetrieve(msg):
			return self.handleRetrieve(msg)
		if self.isDelete(msg):
			return self.handleDelete(msg)
		if self.isQuit(msg):
			return self.handleQuit()
		
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

	def messageNumberOutOfRange(self):
		return '-Err Message number out of range'
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
		mailBoxSize = len(self.mailBoxes)
		box = self.mailBoxes
		counter = 0
		for x in box:
			counter+=len(x)
		return '+OK ' + mailBoxSize + counter

#-----------------------------------------------------------------------
	
	def isList(self,msg):
		if self.getCommand(msg) == 'LIST':
			return True
		else:
			return False	
			
	def handleList(self,msg):
		mailBoxSize = len(self.mailBoxes)
		box = self.mailBoxes
		reply = ''
		counter = 1
		lengthCounter = 0
		for x in box:
			lengthCounter+=len(x)
			reply +=counter + len(x) + '\n'
			if(counter==msg.split()[1]):
				return '+OK ' + counter + len(x)
			counter++
		return '+OK ' + mailBoxSize + ' messages (' + lengthCounter ' bytes)\n' + reply

#-----------------------------------------------------------------------
	
	def isRetrieve(self,msg):
		if self.getCommand(msg) == 'RETR':
			return True
		else:
			return False	
			
	def handleRetrieve(self,msg):
		if(len(self.mailBoxes)>msg.split()[1])
			return messageNumberOutOfRange()
		box = self.mailBoxes
		counter = 1
		for x in box:
			if(counter==msg.split()[1]):
				return '+OK message follows \n' + x
			counter++
		
		
#-----------------------------------------------------------------------
	def isDelete(self,msg):
		if self.getCommand(msg) == 'DELE':
			return True
		else:
			return False	
			
	def handleDelete(self,msg):
		if(len(self.mailBoxes)>msg.split()[1])
			return messageNumberOutOfRange()
		box = self.mailBoxes
		counter = 1
		for x in box:
			if(counter==msg.split()[1]):
				tempVar = x
			counter++
		if(tempCounter<counter
		return '+OK marked for deletion'
			
#-----------------------------------------------------------------------
	def isQuit(self,msg):
		if self.getCommand(msg) == 'QUIT':
			return True
		else:
			return False
			
	def handleQuit(self):
		self.mailBoxes.remove(tempVar)
		return '+OK Farewell'

#-----------------------------------------------------------------------

tempVar = ''
