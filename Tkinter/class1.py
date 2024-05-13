import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
root = tk.Tk()
root.title("COMP111")
root.geometry("400x300")
root.configure(bg='darkgrey')

labelfont = Font(family='Helvetica', size=12, weight='bold')
buttonfont = Font(family='Arial', size=18, weight='bold')
entryfont = Font(family='Courier', size=12)

def onSubmit():
    entryText = entry.get()
    textText = text.get('1.0','end-1c')
    messagebox.showinfo('Submitted Info', f'Entry: {entryText}\nText: {textText}')
    
label = tk.Label(root, text='Welcome to tkinter')
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

text = tk.Text(root, width=40, height=5)
text.pack()

button = tk.Button(root, text='Submit', command=onSubmit)
button.pack(pady=10)

root.mainloop()