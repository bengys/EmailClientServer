from Tkinter import *
import ttk
import tkMessageBox
from IMAPfunctions import *
from POP3functions import *
from SMTPfunctions import *

root = Tk()


def loggedIn(event):
	authenticateSMTP(userNameEnt.get(), passwordEnt.get())

def sentMessage(event):
	selectedItem = box.get()
	if(selectedItem=="Stat" or selectedItem=="List" or selectedItem=="Retrieve" or selectedItem=="Delete" or selectedItem=="Reset" or selectedItem=="Quit" or selectedItem=="Noop" or selectedItem=="Top"):
		comboboxItem = interpretPOP3ComboboxItem(selectedItem)
		command = commandEnt.get()
		textArea.insert("end",  comboboxItem + " " + command + "\n")
		commandEnt.delete(0, len(commandEnt.get()))
		textArea.insert("end",  getPOP3ReplyFromServer(comboboxItem, command) + "\n")
	else:
		comboboxItem = interpretIMAPComboboxItem(selectedItem)
		command = commandEnt.get()
		textArea.insert("end",  comboboxItem + " " + command + "\n")
		commandEnt.delete(0, len(commandEnt.get()))
		textArea.insert("end",  getIMAPReplyFromServer(comboboxItem, command) + "\n")

def toggleIMAPBox(event):
	imapCheck.deselect()
	setComboBoxValues(loadComboBoxValues(True, False))
	textArea.delete('1.0', END)
	textArea.insert("end",  authenticatePOP3Username(userNameEnt.get()) + "\n")
	textArea.insert("end",  authenticatePOP3Password(passwordEnt.get()) + "\n")

def togglePOP3Box(event):
	pop3Check.deselect()
	setComboBoxValues(loadComboBoxValues(False, True))
	textArea.delete('1.0', END)
	textArea.insert("end",  authenticateIMAPUsernameAndPassword(userNameEnt.get(), passwordEnt.get()) + "\n")

def sendMessage(event):
	sendSMTPMessage(userNameEnt.get() + "@gmail.com", receiverEmailEnt.get(), textMessageArea.get("1.0", "end"))
	receiverEmailEnt.delete(0, len(receiverEmailEnt.get()))
	textMessageArea.delete('1.0', END)
	tkMessageBox.showinfo("Sending Message", 'Message Successfully Sent')

def loadComboBoxValues(pop3, imap):
	if(pop3):
		value=["Stat", "List", "Retrieve", "Delete", "Reset", "Quit", "Noop", "Top"]
	elif(imap):
		value=["Login", "Capability", "Select", "Delete", "List", "Fetch", "Subscribe", "Unsubscribe", "Close", 		"Copy", "Logout"]
	else:
		value=[]
	return value

def setComboBoxValues(val):
	box['values']=val


imapBool=IntVar()
imapCheck = Checkbutton(root, text = "IMAP", variable=imapBool)
pop3Bool=IntVar()
pop3Check = Checkbutton(root, text = "POP3", variable=pop3Bool)
#pop3Check.select()

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

box_value = []
box = ttk.Combobox(root, textvariable=box_value)
setComboBoxValues(loadComboBoxValues(False, False))
box.grid(row=4, column=1)

#senderEmailLbl = Label(root, text="Sender Email ID")
#senderEmailEnt = Entry(root)
#senderPassLbl = Label(root, text="Sender Password")
#senderPassEnt = Entry(root, show="*")

receiverEmailLbl = Label(root, text="Receiver Email ID")
receiverEmailEnt = Entry(root)

#senderEmailLbl.grid(row=2, column=8)
#senderEmailEnt.grid(row=2, column=9, pady=5, padx=5)
#senderPassLbl.grid(row=3, column=8)
#senderPassEnt.grid(row=3, column=9, pady=5, padx=5)
receiverEmailLbl.grid(row=4, column=8)
receiverEmailEnt.grid(row=4, column=9, pady=5, padx=5)

sendMessageBtn = Button(root, text="Send Message")
sendMessageBtn.grid(row=4, column=10)

textMessageArea = Text(root)
textMessageArea.grid(row=5, column=8, columnspan=3, pady=20, padx=10)

sendMessageBtn.bind("<Button-1>", sendMessage)


root.mainloop()

