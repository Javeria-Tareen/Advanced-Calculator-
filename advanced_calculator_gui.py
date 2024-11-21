import tkinter as tk
from tkinter import messagebox
import math

# Functions for calculator operations
def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "Error"

def click_button(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = evaluate_expression(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "√":
        try:
            num = float(entry.get())
            result = math.sqrt(num)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value in ["sin", "cos", "tan"]:
        try:
            num = float(entry.get())
            radians = math.radians(num)
            if value == "sin":
                result = math.sin(radians)
            elif value == "cos":
                result = math.cos(radians)
            elif value == "tan":
                result = math.tan(radians)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "log":
        try:
            num = float(entry.get())
            result = math.log10(num)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "!":
        try:
            num = int(entry.get())
            result = math.factorial(num)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

# Create the main application window
app = tk.Tk()
app.title("Advanced Calculator")
app.geometry("400x600")

# Entry widget to display and enter expressions
entry = tk.Entry(app, font=("Arial", 24), borderwidth=2, relief="solid")
entry.pack(pady=10, fill=tk.BOTH)

# Button layout
buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "!"],
    ["1", "2", "3", "-", "log"],
    ["0", ".", "C", "+", "="],
    ["sin", "cos", "tan",]
]

# Frame for buttons
button_frame = tk.Frame(app)
button_frame.pack()

# Create buttons dynamically
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(fill=tk.BOTH, expand=True)
    for button in row:
        btn = tk.Button(
            row_frame, 
            text=button, 
            font=("Arial", 18), 
            command=lambda b=button: click_button(b), 
            height=2, 
            width=5
        )
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Run the application
app.mainloop()
