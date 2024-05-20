'''
    
'''

import tkinter as tk
from tkinter import messagebox

def addTask():
    task = taskEntry.get()
    if task:
        tasksListbox.insert(tk.END, task)
        taskEntry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "The task cannot be empty.")

def removeTask():
    try:
        # Remove the selected task
        selectedTaskIndex = tasksListbox.curselection()[0]
        tasksListbox.delete(selectedTaskIndex)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove.")

root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("300x350")

# Entry widget for entering new tasks
taskEntry = tk.Entry(root, width=25)
taskEntry.pack(pady=10)

# Button to add a new task
addTaskButton = tk.Button(root, text="Add Task", command=addTask)
addTaskButton.pack(pady=5)

# Listbox to display tasks
tasksListbox = tk.Listbox(root, width=25, height=10)
tasksListbox.pack(pady=10)

# Button to remove a selected task
removeTaskButton = tk.Button(root, text="Remove Task", command=removeTask)
removeTaskButton.pack(pady=5)

root.mainloop()
