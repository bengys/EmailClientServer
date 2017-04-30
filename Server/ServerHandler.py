from socket import *
from SMTPserver import *
from IMAPserver import *
import threading
import ssl


class SMTPserver_thread(threading.Thread):
    def __init__(self, acceptedConnection):
        threading.Thread.__init__(self)
        self.socket, self.addr = acceptedConnection
        self.manager = SMTPserver()
    def run(self):
		print("Allocating a new thread for the connection that was just recieved")
		print '-------------------------------------------------------'
		self.socket.send('220 localhost ESMTP \r\n')
		try:
			while 1:				
				incomingData = self.socket.recv(1024)
				if not incomingData:	
					break	
				outgoingData = self.manager.interact(incomingData)
				if not outgoingData:
					break
					
				self.socket.send(outgoingData)				
		except KeyboardInterrupt:			
			self.socket.shutdown(SHUT_RDWR)
			self.socket.close()	
	

#=======================================================================


class IMAPserver_thread(threading.Thread):
	def __init__(self, acceptedConnection):
		threading.Thread.__init__(self)
		self.socket, self.addr = acceptedConnection
		self.manager = IMAPserver()
	def run(self):
		print("Allocating a new thread for the connection that was just recieved")
		print '-------------------------------------------------------'
		self.socket.send('* OK IMAP Service is ready ')
		try:
			while 1:				
				incomingData = self.socket.recv(1024)
				if not incomingData:	
					break	
				outgoingData = self.manager.interact(incomingData)
				if not outgoingData:
					break
				self.socket.send(outgoingData)				
		except KeyboardInterrupt:			
			self.socket.shutdown(SHUT_RDWR)
			self.socket.close()	
		

#=======================================================================

class SMTPsocketThreadHandler:
	def __init__(self):
		SMTPport = 465
		self.socket = socket(AF_INET,SOCK_STREAM)
		self.SMTPwelcomeSocket = ssl.wrap_socket(self.socket,server_side=True,certfile='cacert.pem',keyfile='private.pem')
		self.SMTPwelcomeSocket.bind(('',SMTPport))
		self.SMTPwelcomeSocket.listen(1)
		print 'SMTP Server is now taking requests'
		print "=============================================="
			
	def waitForConnection(self):
		SMTPserver_thread(self.SMTPwelcomeSocket.accept()).start()

#=======================================================================


class IMAPsocketThreadHandler:
	def __init__(self):
		IMAPport = 993
		self.socket = socket(AF_INET,SOCK_STREAM)
		self.IMAPwelcomeSocket = ssl.wrap_socket(self.socket,server_side=True,certfile='cacert.pem',keyfile='private.pem')
		self.IMAPwelcomeSocket.bind(('',IMAPport))
		self.IMAPwelcomeSocket.listen(1)
		print 'IMAP Server is now taking requests'
		print "=============================================="
		
	def waitForConnection(self):
		IMAPserver_thread(self.IMAPwelcomeSocket.accept()).start()

#=======================================================================

SMTPhandler = SMTPsocketThreadHandler()
IMAPhandler = IMAPsocketThreadHandler()

while 1:
#	SMTPhandler.waitForConnection()
	IMAPhandler.waitForConnection()

#Swaks SMTP client test	for CLI
#swaks --to bshear13@gmail.com  --from networks4017tester@gmail.com --server localhost:465 --tlsc	
