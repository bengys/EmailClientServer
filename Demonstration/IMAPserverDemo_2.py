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
