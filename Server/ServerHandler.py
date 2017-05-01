	# This file contains classes for handling server interactions at the TCP level. 
#The classes manage setting up listening sockets hnsling of threads assoicatied with each process.

from socket import *
from SMTPserver import *
from IMAPserver import *
#from POP3server import *
import threading
import ssl
import sys
sys.path.insert(0, '../')
from serverClientDetails import *


# Thread class that runs when a TCP connection has been accepted by the SMTP server socket.
# The below three classes all follow a similair structure.

class SMTPserver_thread(threading.Thread):
    def __init__(self, acceptedConnection):
        threading.Thread.__init__(self)
        
        # Get socket and its address of TCP socket assigned for this
        # Clients process
        self.socket, self.addr = acceptedConnection
	
		# Instantiate instance of SMTP server. Each connection has its own instance of the server.
        self.manager = SMTPserver()	
	
	# Main thread loop
    def run(self):
		print("Allocating a new thread for the connection that was just recieved")
		print '-------------------------------------------------------'
		# Welcome line sent to client
		self.socket.send('220 localhost ESMTP \r\n')
		try:
			
			# Loop runs till timeout or till client terminates connection
			while 1:	
				
				# Receive data from client			
				incomingData = self.socket.recv(1024)
				if not incomingData:	
					break	
				
				# Interpret data of client and respond to client	
				outgoingData = self.manager.interact(incomingData)
				if not outgoingData:
					break
					
				self.socket.send(outgoingData)				
		except KeyboardInterrupt:			
			self.socket.shutdown(SHUT_RDWR)
			self.socket.close()	
	

#=======================================================================

# Thread that runs when TCP connection received from IMAP client
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

# Thread that runs when TCP connection received from POP3 Client
class POP3server_thread(threading.Thread):
	def __init__(self, acceptedConnection):
		threading.Thread.__init__(self)
		self.socket, self.addr = acceptedConnection
		self.manager = POP3server()
	def run(self):
		print("Allocating a new thread for the connection that was just recieved")
		print '-------------------------------------------------------'
		self.socket.send('* OK POP Service is ready ')
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

# The following classes set up the sockets listening for the services - SMTP, POP3
# and IMAP

class SMTPsocketThreadHandler:
	def __init__(self):
		SMTPport = 465
		# Create socket
		self.socket = socket(AF_INET,SOCK_STREAM)
		# Make socket secure socket layer socket
		# Certificate and keyfile found in same folder as Server
		self.SMTPwelcomeSocket = ssl.wrap_socket(self.socket,server_side=True,certfile='cacert.pem',keyfile='private.pem')
		#Bind socket to port 465
		self.SMTPwelcomeSocket.bind(('',SMTPport))
		# Listen for incoming connections
		self.SMTPwelcomeSocket.listen(1)
		print 'SMTP Server is now taking requests'
		print "=============================================="
			
	def waitForConnection(self):
		# Wait for incoming TCP connection to the socket
		SMTPserver_thread(self.SMTPwelcomeSocket.accept()).start()

#=======================================================================

# Following three classes establish listening socket for three respective services
# - IMAP, POP3 and SMTP

class IMAPsocketThreadHandler:
	def __init__(self):
		IMAPport = 993
		# Create socket
		self.socket = socket(AF_INET,SOCK_STREAM)
		# Make socket SSL socket
		self.IMAPwelcomeSocket = ssl.wrap_socket(self.socket,server_side=True,certfile='cacert.pem',keyfile='private.pem')
		# Bind socket to port 993
		self.IMAPwelcomeSocket.bind(('',IMAPport))
		# Socket now listens for incoming connections
		self.IMAPwelcomeSocket.listen(1)
		print 'IMAP Server is now taking requests'
		print "=============================================="
		
	def waitForConnection(self):
		IMAPserver_thread(self.IMAPwelcomeSocket.accept()).start()

#=======================================================================

class POP3socketThreadHandler:
	def __init__(self):
		POP3port = 995
		self.socket = socket(AF_INET,SOCK_STREAM)
		self.POP3welcomeSocket = ssl.wrap_socket(self.socket,server_side=True,certfile='cacert.pem',keyfile='private.pem')
		self.POP3welcomeSocket.bind(('',POP3port))
		self.POP3welcomeSocket.listen(1)
		print 'POP3 Server is now taking requests'
		print "=============================================="
		
	def waitForConnection(self):
		POP3server_thread(self.POP3welcomeSocket.accept()).start()


#Swaks SMTP client test	for CLI
#swaks --to bshear13@gmail.com  --from networks4017tester@gmail.com --server localhost:465 --tlsc	

