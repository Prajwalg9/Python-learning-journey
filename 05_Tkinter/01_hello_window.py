import tkinter as tk  # import the tkinter module and give it a short name

# 1) Create the main application window (root window)
root = tk.Tk()

# 2) Set basic properties of the window
root.title("My First Tkinter App")   # window title text
root.geometry("400x300")             # width x height in pixels

# 3) Start the event loop so the window appears and stays open
root.mainloop()
