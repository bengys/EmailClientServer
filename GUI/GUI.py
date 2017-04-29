from Tkinter import *

root = Tk()

def loggedIn(event, str):
	if (imapBool.get()):
		textArea.insert("end", "Logged In using imap \n")
		print("Logged In using imap")
	elif (pop3Bool.get()):
		textArea.insert("end", "Logged In using pop3 \n")
		print("Logged In using pop3")
	else:
		print("Error")

def sentMessage(event):
	textArea.insert("end", commandEnt.get() + "\n")
	commandEnt.delete(0, len(commandEnt.get()))
	print("Message sent")

def toggleIMAPBox(event):
	if (imapBool.get()):
		imapCheck.deselect()

def togglePOP3Box(event):
	if (pop3Bool.get()):
		pop3Check.deselect()

imapBool=IntVar()
imapCheck = Checkbutton(root, text = "IMAP", variable=imapBool)
pop3Bool=IntVar()
pop3Check = Checkbutton(root, text = "POP3", variable=pop3Bool)

userNameLbl = Label(root, text="Email ID")
userNameEnt = Entry(root)

passwordLbl = Label(root, text="Password")
passwordEnt = Entry(root)

userNameLbl.grid(row=0, column=0)
userNameEnt.grid(row=0, column=1, pady=5)
passwordLbl.grid(row=1, column=0)
passwordEnt.grid(row=1, column=1, pady=5)

loginBtn = Button(root, text="Login")
loginBtn.grid(row=1, column=3, padx=20)

pop3Check.grid(row=0, column=2, padx=15)
imapCheck.grid(row=1, column=2, padx=15)

placeHolderLbl = Label(root, text="")
placeHolderLbl.grid(row=2, column=1, padx=10, pady=10)

commandLbl = Label(root, text="Command")
commandEnt = Entry(root)
commandLbl.grid(row=4, column=3)
commandEnt.grid(row=4, column=4, columnspan=2)

sendBtn = Button(root, text="Send")
sendBtn.grid(row=4, column=6, padx=20)

textArea = Text(root)
textArea.grid(row=5, column=0, columnspan=7, pady=20)

loginBtn.bind("<Button-1>", lambda event: loggedIn(event, "Hi"))
sendBtn.bind("<Button-1>", sentMessage)
pop3Check.bind("<Button-1>", toggleIMAPBox)
imapCheck.bind("<Button-1>", togglePOP3Box)


root.mainloop()

