'''
    Widget is a GUI element that can be added to a window.
      - They include buttons, labels, textboxes, etc.
      - They can me much more complex than this. Nesting widgets within widgets is common.
'''

import tkinter as tk
from tkinter import messagebox

def on_submit():
    # Retrieve data from Entry and Text widgets
    entry_text = entry.get()
    # Here 1.0 means the first line, 0th character.
    # end means the last line, last character.
    # end-1c means the last line, last character minus 1 character, which is typically \n.
    text_widget_content = text.get("1.0", "end-1c")
    # Display a message box with the content
    messagebox.showinfo("Submitted Info", f"Entry: {entry_text}\nText: {text_widget_content}")

    # Deleting and inserting text
    #entry.delete(0)
    #entry.delete(0, 4)
    #entry.insert(0, "Python")

root = tk.Tk()
root.title("Tkinter Widget Showcase")
root.geometry("400x300")  # Set initial size of the window

# Label widget
label = tk.Label(root, text="Enter some text:")
label.pack(pady=10)  # Add some vertical padding

# Entry widget
entry = tk.Entry(root, width=50)
entry.pack(pady=10)  # Add some vertical padding

# Text widget
text = tk.Text(root, height=5, width=40)
text.pack(pady=10)  # Add some vertical padding

# Button widget
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()
