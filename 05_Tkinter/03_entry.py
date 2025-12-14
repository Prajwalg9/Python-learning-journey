import tkinter as tk
from tkinter import ttk
root=tk.Tk()


#ttk is newer of tk you can say themed version of tk
root.geometry("500x500")
def welcome():
    user=entry.get()
    label.config(text=f"Welcome {user}!")
label = ttk.Label(root,text="Welcome!",font=("Times New Roman",20))
label.pack()
entry = ttk.Entry(root,font=("Arial",15))
entry.pack()
button=ttk.Button(root,text="Click me!",command=welcome)
button.pack()


#to close app with button
quit = ttk.Button(root,text="Quit",command=root.quit)
quit.pack()
root.mainloop()