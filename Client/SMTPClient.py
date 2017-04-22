from client_sockets import *
client = clientSMTPSocket()


def entercommand(sock):
	msg = raw_input('--> ')
	sock.sendMessageReceiveReply(msg)

entercommand(client)
