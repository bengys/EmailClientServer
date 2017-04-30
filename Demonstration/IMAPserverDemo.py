# Run this file to demonstrate the working of the IMAPserver


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# NNNNB - TO TEST THE IMAP SERVER YOU MUST DO THE FOLLOWING:

# 1) EDIT serverClientDetails.py FOUND IN
# MAIN DIRECTORY AND MAKE SURE VALUE OF IMAP_SERVER is 'localhost'
# OTHERWISE IT WILL NOT DEMONSTATE
# 2) RUN ServerHandler.py found in Server folder. This will start the
# the SMTP server

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import sys
sys.path.insert(0, '../Client')
sys.path.insert(0, '../Server')
sys.path.insert(0, '../')
from serverClientDetails import *
from IMAPclient import *
#import ServerHandler

IMAPclient = IMAPclient()
IMAPclient.sendOwnText('login networks4017tester@gmail.com networks4017')
IMAPclient.sendOwnText('select inbox')
IMAPclient.sendOwnText('fetch 1:10 full')
