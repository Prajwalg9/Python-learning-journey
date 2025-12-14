import tkinter as tk

# 1) Create main window
root = tk.Tk()
root.title("Label & Button Example")
root.geometry("400x200")

# 2) Create a Label widget
label = tk.Label(
    root,                     # parent window
    text="Original Text",     # text to display
    font=("Arial", 16)        # font family and size
)

# 3) Place the label on the window using pack()
label.pack(pady=20)           # pady adds vertical space

# 4) Define a function that will run when button is clicked
counter=0
def change_text():
    global counter
    counter+=1
    label.config(text=f"Button Clicked {counter} times!")  # change label text

# 5) Create a Button widget and link it to the function
button = tk.Button(
    root,
    text="Click Me",
    font=("Arial", 14),
    command=change_text       # note: NO parentheses here
)

# 6) Place the button
button.pack()

# 7) Start event loop
root.mainloop()
