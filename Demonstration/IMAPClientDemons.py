

# NNNNB - TO TEST THE IMAP Client YOU MUST DO THE FOLLOWING:

# 1) OPEN serverClientDetails.py FOUND IN
# MAIN DIRECTORY AND MAKE SURE VALUE OF IMAP_SERVER is 'imap.gmail.com'


import sys
sys.path.insert(0, '../Client')
sys.path.insert(0, '../')
from serverClientDetails import *
from IMAPclient import *

print "================================================================"
# Establish imapclient
IMAPclient = IMAPclient()
print "================================================================"
IMAPclient.CAPABILITY()
print "================================================================"
IMAPclient.LOGIN(username,password)
print "================================================================"
IMAPclient.LIST()
print "================================================================"
IMAPclient.SELECT()
print "================================================================"
IMAPclient.FETCH()
print "================================================================"
IMAPclient.CLOSE()
print "================================================================"
