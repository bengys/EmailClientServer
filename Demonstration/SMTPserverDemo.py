#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Instructions to test SMTP server: 
# 1) First run SMTPserverDemo.py as sudo (Start SMTP server)
# 2)

# OPTION A
# Open new terminal
# Install swaks in command line - tool which has basic SMTP client to test SMTP server
#sudo apt-get update
#sudo apt-get install swaks

#Run the following line in terminal - replace destination_email with valid email
# swaks --to destination_email  --from networks4017tester@gmail.com --server localhost:465 --tlsc

# OPTION B
#Point your own email client to this SMTP server ('localhost' if run off
# same machine).


import sys
sys.path.insert(0, '../Server')
from ServerHandler import *

# Set up listeing SMTP server
SMTPhandler = SMTPsocketThreadHandler()
while 1:
	# Wait for connection from clients to SMTP server
	SMTPhandler.waitForConnection()
