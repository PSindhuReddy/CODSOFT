import tkinter as tk
from tkinter import messagebox
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))  # Evaluates expression
            screen.set(result)
        except:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "C":
        screen.set("")  # Clear screen
    else:
        screen.set(screen.get() + text)  # Append text to the current input
root = tk.Tk()
root.title("Calculator")
#  screen setup
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", bd=8, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
# Create buttons
r_val = 1
c_val = 0
for button in buttons:
    btn = tk.Button(root, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=r_val, column=c_val)
    btn.bind("<Button-1>", click)  
    c_val += 1
    if c_val == 4:
        c_val = 0
        r_val += 1
root.mainloop()
