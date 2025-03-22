import tkinter as tk

# Function to handle button click
def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "cant divide by zero")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

# Entry widget for the expression
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 18), command=evaluate_expression)
    elif text == "C":
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 18), command=clear_entry)
    else:
        button = tk.Button(window, text=text, width=5, height=3, font=("Arial", 18), command=lambda value=text: on_button_click(value))

    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
window.mainloop()
