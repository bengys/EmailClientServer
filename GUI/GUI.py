from Tkinter import *

class Class1:
	def __init__(self, master):
		frame = Frame(master, width=800, height=250)
		frame.pack()

		self.printButton = Button(frame, text = "Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text = "Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)
	
	def printMessage(self):
		print("Wow, this actually worked")

class MenuClass:
	def __init__(self, master):
		frame = Frame(master, width=800, height=250)
		frame.grid(row=0)
		
		mainMenu = Menu(master)
		master.config(menu=mainMenu)

		subMenu = Menu(mainMenu)
		mainMenu.add_cascade(label="IMAP or POP3", menu=subMenu)
		subMenu.add_command(label="IMAP", command=self.IMAPselected)
		subMenu.add_command(label="POP3", command=self.POP3selected)
		subMenu.add_separator()
		subMenu.add_command(label="Exit", command=frame.quit)

		editMenu = Menu(mainMenu)
		mainMenu.add_cascade(label="Edit", menu=editMenu)

		imapCheck = Checkbutton(master, text = "IMAP")
		imapCheck.grid(row=0, column=1)

		pop3Check = Checkbutton(master, text = "POP3")
		pop3Check.grid(row=1, column=1)
	
	def IMAPselected(self):
		print("User selected IMAP")

	def POP3selected(self):
		print("User selected POP3")

class mainGrid:
	def __init__(self, master):
		#frame = Frame(master, width=400, height=250)
		#frame.grid()

		imapCheck = Checkbutton(master, text = "IMAP")
		#imapCheck.grid(row=0, column=0)

		pop3Check = Checkbutton(master, text = "POP3")
		#pop3Check.grid(row=1, column=0)

		userNameLbl = Label(master, text="Username")
		userNameEnt = Entry(master)
		
		passwordLbl = Label(master, text="Password")
		passwordEnt = Entry(master)

		userNameLbl.grid(row=0, column=0)
		userNameEnt.grid(row=0, column=1, pady=5)
		passwordLbl.grid(row=1, column=0)
		passwordEnt.grid(row=1, column=1, pady=5)

		loginBtn = Button(master, text="Login")
		loginBtn.grid(row=1, column=2, padx=20)

		placeHolderLbl = Label(master, text="")
		placeHolderLbl.grid(row=2, column=1, padx=10, pady=20)
		
		pop3Check.grid(row=3, column=1)
		imapCheck.grid(row=4, column=1)

		commandLbl = Label(master, text="Command")
		commandEnt = Entry(master)
		commandLbl.grid(row=3, column=3)
		commandEnt.grid(row=3, column=4, columnspan=2)

		serverLbl = Label(master, text="Reply")
		serverReplyEnt = Entry(master)
		serverLbl.grid(row=4, column=3)
		serverReplyEnt.grid(row=4, column=4, columnspan=2)
		
		sendBtn = Button(master, text="Send")
		sendBtn.grid(row=4, column=6, padx=20)
		

root = Tk()

#c1 = Class1(root)
#m1 = MenuClass(root)
#mg = mainGrid(root)


imapCheck = Checkbutton(root, text = "IMAP")

pop3Check = Checkbutton(root, text = "POP3")

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

#serverLbl = Label(root, text="Reply")
#serverReplyEnt = Entry(root)
#serverLbl.grid(row=4, column=3)
#serverReplyEnt.grid(row=4, column=4, columnspan=2)

sendBtn = Button(root, text="Send")
sendBtn.grid(row=4, column=6, padx=20)

textArea = Text(root)
textArea.grid(row=5, column=0, columnspan=7, pady=20)

root.mainloop()



#def leftClick(event):
#	print("Left")

#def middleClick(event):
	#print("Middle")

#def rightClick(event):
	#print("Right")

#frame = Frame(root, width=800, height=250)
#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)

#frame.pack()
