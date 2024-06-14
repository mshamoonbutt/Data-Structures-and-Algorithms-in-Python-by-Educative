'''import tkinter as tk
import tkinter as ttk

root = tk.Tk()
root.title("")
root.geometry("100x100")

label = tk.Label(text="Python rocks!")
label.pack()

root.mainloop()'''
'''
import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()'''

'''import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(frame, text=relief_name)
    label.pack()

window.mainloop()'''

'''import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()'''

'''import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()'''

'''import tkinter as tk

def on_radio_button_selected():
    print(f"Selected option: {radio_var.get()}")

root = tk.Tk()
radio_var = tk.StringVar()

radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="1", command=on_radio_button_selected)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="2", command=on_radio_button_selected)
radio_button3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="3", command=on_radio_button_selected)

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

root.mainloop()'''

import tkinter as tk

def on_check_button_toggled():
    selected_options = []
    if check_var1.get():
        selected_options.append("Option 1")
    if check_var2.get():
        selected_options.append("Option 2")
    if check_var3.get():
        selected_options.append("Option 3")
    print(f"Selected options: {', '.join(selected_options)}")

root = tk.Tk()
check_var1 = tk.IntVar()
check_var2 = tk.IntVar()
check_var3 = tk.IntVar()

check_button1 = tk.Checkbutton(root, text="Option 1", variable=check_var1, command=on_check_button_toggled)
check_button2 = tk.Checkbutton(root, text="Option 2", variable=check_var2, command=on_check_button_toggled)
check_button3 = tk.Checkbutton(root, text="Option 3", variable=check_var3, command=on_check_button_toggled)

check_button1.pack()
check_button2.pack()
check_button3.pack()

root.mainloop()
