from tkinter import *
import message_automation

def result_display(message):
	user_name_label.destroy()
	pass_word_label.destroy()
	message_label.destroy()
	user_name_entry.destroy()
	password_entry.destroy()
	message_text.destroy()

	result_label = Label(root, text = message, height = 30, width = 50)
	result_label.grid(row = 0, column = 0)
	
	root.update()

def execute():
	username, pass_word = user_name.get(), password.get()
	message = message_text.get("1.0", "end-1c")
	
	result = message_automation.start_messaging(user_name.get(), password.get(), message)
	
	if bool(result):
		result_display("Success")

	else:
		result_display("Failed")


root = Tk()
root.title("Instagram Message automation")
root.minsize(height = 300, width = 500)

user_name_label = Label(root, text = "Username :")
user_name_label.grid(row = 0, column = 0, pady = 10)
pass_word_label = Label(root, text = "Password :")
pass_word_label.grid(row = 1, column = 0, pady = 10)
message_label = Label(root, text = "Message :")
message_label.grid(row = 3, column = 0, pady = 10)

user_name, password = StringVar(), StringVar()

user_name_entry = Entry(root, textvariable = user_name, width = 50)
user_name_entry.grid(row = 0, column = 1)
password_entry = Entry(root, textvariable = password, width = 50, show = "*")
password_entry.grid(row = 1, column = 1, )
message_text = Text(root, height = 7, width = 38)
message_text.grid(row = 3, column = 1)

button_send = Button(root, text = "Send", command = lambda: execute()).grid(row = 5 ,column =  3, rowspan = 2, pady = 20, ipadx = 5, ipady = 5)
buttton_exit = Button(root, text = "Exit", command = root.destroy).grid(row = 5 ,column =  5, rowspan = 2, columnspan = 2, pady = 20, ipadx = 5, ipady = 5)

root.mainloop()
