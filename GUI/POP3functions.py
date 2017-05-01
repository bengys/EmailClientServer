import sys
sys.path.insert(0, '../Client/')
from POP3client import *

conn = POP3manager()

def authenticatePOP3Username(username):
	return conn.USER(username)

def authenticatePOP3Password(password):
	return conn.PASS(password)

def getPOP3ReplyFromServer(comboboxItem, command):
	if (comboboxItem=="STAT" or comboboxItem=="RSET" or comboboxItem=="NOOP" or comboboxItem=="QUIT"):
		return conn.entercommand(comboboxItem)
	else:
		return conn.entercommand(comboboxItem + " " + command)


def interpretPOP3ComboboxItem(conboboxWord):
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

