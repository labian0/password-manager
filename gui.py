from tkinter import *
from manager import PwManager, Database

root = Tk() #create window

man = PwManager()
path_entry = Entry()
pw_entry = Entry()
path_entry.insert(0, "file")
pw_entry.insert(0, "password")
button1 = Button(text="create database", command=lambda:man.createdb(path_entry.get(), pw_entry.get()))
button2 = Button(text="open database", command=lambda:man.opendb(path_entry.get(), pw_entry.get()))
button3 = Button(text="get entries", command=lambda:label1.config(text=man.db.entries))
button4 = Button(text="exit", command=lambda:(man.savedb(pw_entry.get()), quit()))
label1 = Label()



path_entry.pack()
pw_entry.pack()
button1.pack()
button2.pack()
button3.pack()
label1.pack()
button4.pack()

root.mainloop() #run