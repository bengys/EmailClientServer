from Tkinter import *
import ttk
from GUIfunctions import *
sys.path.insert(0, '../Client')
from POP3client import *

conn = POP3manager()

#POP3manager.USER("networks4017tester")
#data=conn.recv(4096)
#textArea.insert("end", conn + " \n")
root = Tk()

def loggedIn(event):
	senderEmailEnt.insert(0, userNameEnt.get() + "@gmail.com")
	if (imapBool.get()):
		textArea.insert("end", "Logged In using imap \n")
		print("Logged In using imap")
	elif (pop3Bool.get()):
		userReply = conn.USER(userNameEnt.get())
		textArea.insert("end", userReply)
		passReply = conn.PASS(passwordEnt.get())
		textArea.insert("end", passReply)


def sentMessage(event):
	selectedItem = box.get()
	#hideWidget(selectedItem)
	comboboxItem = selectComboboxItem(selectedItem)
	command = commandEnt.get()
	
	if (selectedItem=="Stat" or selectedItem=="Reset" or selectedItem=="Noop" or selectedItem=="Quit"):
		textArea.insert("end",  comboboxItem + "\n")
		reply = conn.entercommand(comboboxItem)
	else:
		textArea.insert("end",  comboboxItem + " " + command + "\n")
		reply = conn.entercommand(comboboxItem + " " + command)
	#textArea.insert("end",  command + "\n")
	commandEnt.delete(0, len(commandEnt.get()))
	textArea.insert("end",  reply + "\n")
	print("Message sent")

def toggleIMAPBox(event):
	if (imapBool.get()):
		imapCheck.deselect()

def togglePOP3Box(event):
	if (pop3Bool.get()):
		pop3Check.deselect()

def selectComboboxItem(conboboxWord):
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

def sendMessage(event):
	print(senderEmailEnt.get())
	print(receiverEmailEnt.get())
	print(passwordEnt.get())
	print(textMessageArea.get("1.0", "end"))
	authenticateANDsendMessage(senderEmailEnt.get(), receiverEmailEnt.get(), passwordEnt.get(), textMessageArea.get("1.0", "end"))

imapBool=IntVar()
imapCheck = Checkbutton(root, text = "IMAP", variable=imapBool)
pop3Bool=IntVar()
pop3Check = Checkbutton(root, text = "POP3", variable=pop3Bool)
pop3Check.select()

userNameLbl = Label(root, text="Email ID")
userNameEnt = Entry(root)

passwordLbl = Label(root, text="Password")
passwordEnt = Entry(root, show="*")

userNameLbl.grid(row=0, column=0)
userNameEnt.grid(row=0, column=1, pady=5)
passwordLbl.grid(row=1, column=0)
passwordEnt.grid(row=1, column=1, pady=5)

loginBtn = Button(root, text="Login")
loginBtn.grid(row=1, column=2, padx=20)

pop3Check.grid(row=3, column=0, padx=15)
imapCheck.grid(row=4, column=0, padx=15)

#placeHolderLbl = Label(root, text="")
#placeHolderLbl.grid(row=2, column=1, padx=10, pady=10)

commandLbl = Label(root, text="Command")
commandEnt = Entry(root)
commandLbl.grid(row=4, column=2)
commandEnt.grid(row=4, column=3, columnspan=2)

sendBtn = Button(root, text="Send Command")
sendBtn.grid(row=4, column=5, padx=20)

textArea = Text(root)
textArea.grid(row=5, column=0, columnspan=7, pady=20)

loginBtn.bind("<Button-1>", loggedIn)
sendBtn.bind("<Button-1>", sentMessage)
pop3Check.bind("<Button-1>", toggleIMAPBox)
imapCheck.bind("<Button-1>", togglePOP3Box)

box_value=["Stat", "List", "Retrieve", "Delete", "Reset", "Quit", "Noop", "Top"]
box = ttk.Combobox(root, textvariable=box_value)
box['values']=box_value
box.grid(row=4, column=1)


senderEmailLbl = Label(root, text="Sender Email ID")
senderEmailEnt = Entry(root)

receiverEmailLbl = Label(root, text="Receiver Email ID")
receiverEmailEnt = Entry(root)

senderEmailLbl.grid(row=3, column=8)
senderEmailEnt.grid(row=3, column=9, pady=5, padx=5)
receiverEmailLbl.grid(row=4, column=8)
receiverEmailEnt.grid(row=4, column=9, pady=5, padx=5)

sendMessageBtn = Button(root, text="Send Message")
sendMessageBtn.grid(row=4, column=10)

textMessageArea = Text(root)
textMessageArea.grid(row=5, column=8, columnspan=3, pady=20, padx=10)

sendMessageBtn.bind("<Button-1>", sendMessage)


root.mainloop()

