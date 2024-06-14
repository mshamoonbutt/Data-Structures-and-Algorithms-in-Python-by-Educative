'''
   
'''

import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def on_submit():
    # Retrieve data from Entry and Text widgets
    entry_text = entry.get()
    text_widget_content = text.get("1.0", "end-1c")
    # Display a message box with the content
    messagebox.showinfo("Submitted Info", f"Entry: {entry_text}\nText: {text_widget_content}")

root = tk.Tk()
root.title("Customized Widgets Example")
root.geometry("400x300")  # Set initial size of the window

root.configure(bg='lightgreen')  # Using a named color
# root.configure(bg='#ADD8E6')  # Using a hexadecimal color code

# Custom fonts
label_font = Font(family="Helvetica", size=12, weight="bold")
button_font = Font(family="Arial", size=18, weight="bold")
entry_font = Font(family="Courier", size=12)

# Label widget with custom font and foreground color
label = tk.Label(root, text="Enter some text:", font=label_font, fg="blue")
label.pack(pady=(10, 0))  # Add some vertical padding

# Entry widget with custom background, foreground color, and font
entry = tk.Entry(root, font=entry_font, bg="lightgray", fg="black", width=50)
entry.insert(0,"Hello")
entry.insert(0, "ok ")
entry.delete(0, tk.END)
entry.pack(pady=10)  # Add some vertical padding

# Text widget with custom font, background, and foreground color
text = tk.Text(root, height=5, width=38, font=entry_font, bg="black", fg="white")
text.insert(tk.END, "Put me at the end!")
text.insert(tk.END, "\nPut me at the end!")
text.pack(pady=10)  # Add some vertical padding

# Button widget with custom background, foreground color, and font
submit_button = tk.Button(root, text="Submit", command=on_submit, font=button_font, bg="green", fg="red")
submit_button.pack(pady=10)



root.mainloop()


