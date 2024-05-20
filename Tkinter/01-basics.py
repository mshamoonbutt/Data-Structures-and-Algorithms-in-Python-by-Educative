import tkinter as tk

# Create the main window
root = tk.Tk()
# Set the title of the window
root.title("COMP111")
# Set the size of the window
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Welcome to tkinter")
# Add the label to the window
label.pack()

root.mainloop()