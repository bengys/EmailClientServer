import sys
sys.path.insert(0, '../Client')
sys.path.insert(0, '../Server')
sys.path.insert(0, '../')
from serverClientDetails import *
from IMAPclient import *


conn = IMAPclient()
conn.LOGIN()
conn.SELECT()
conn.FETCH()
conn.SUBSCRIBE()
conn.UNSUBSCRIBE()
conn.CLOSE()
conn.COPY()
conn.entercommand()
