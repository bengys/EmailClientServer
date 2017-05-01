import sys
sys.path.insert(0, '../Client/')
from IMAPclient import *

manager = IMAPclient()

def authenticateIMAPUsernameAndPassword(username, password):
	return manager.LOGIN(username, password)

def getIMAPReplyFromServer(comboboxItem, command):
	if (comboboxItem=="STAT" or comboboxItem=="RSET" or comboboxItem=="NOOP" or comboboxItem=="QUIT"):
		return conn.entercommand(comboboxItem)
	else:
		return conn.entercommand(comboboxItem + " " + command)


def interpretIMAPComboboxItem(conboboxWord):
	return {
        'List': 'LIST',
        'Stat': 'STAT',
	'Retrieve': 'RETR',
        'Delete': 'DELE',
	'Reset': 'RSET',
        'Quit': 'QUIT',
	'Noop': 'NOOP',
        'Top': 'TOP',
    }[conboboxWord]

