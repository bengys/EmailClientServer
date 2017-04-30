# Run this file to demonstrate the working of the IMAPserver


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# NNNNB - TO TEST THE IMAP SERVER YOU MUST DO THE FOLLOWING:

# 1) EDIT serverClientDetails.py FOUND IN
# MAIN DIRECTORY AND MAKE SURE VALUE OF IMAP_SERVER is 'localhost'
# OTHERWISE IT WILL NOT DEMONSTATE the SMTP server
# 2) RUN IMAPserverDemo_1.py as Sudo in one terminal (Server)
# 3) RUN IMAPserverDemo_2.py in another terminal (Mock Client)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


import sys
sys.path.insert(0, '../Client')
sys.path.insert(0, '../Server')

from ServerHandler import *

IMAPhandler = IMAPsocketThreadHandler()
while 1:
	IMAPhandler.waitForConnection()
