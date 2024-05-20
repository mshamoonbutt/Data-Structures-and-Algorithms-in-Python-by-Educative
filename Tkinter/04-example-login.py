'''
   
'''
import tkinter as tk
from tkinter import ttk

from tkinter import messagebox


def login():
    # Fetch the username and password from the Entry widgets
    username = usernameEntry.get()
    password = passwordEntry.get()
    # Just a simple check to demonstrate functionality
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "You have successfully logged in!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = tk.Tk()
root.title("Simple Login Screen")
root.geometry("200x150")

# Create a label for username
usernameLabel = ttk.Label(root, text="Username:")
usernameLabel.pack()

# Create an entry widget for username
usernameEntry = ttk.Entry(root)
usernameEntry.pack()

# Create a label for password
passwordLabel = ttk.Label(root, text="Password:")
passwordLabel.pack()

# Create an entry widget for password
passwordEntry = ttk.Entry(root, show="*")
passwordEntry.pack()

# Create a login button
loginButton = ttk.Button(root, text="Login", command=login)
loginButton.pack()

root.mainloop()
